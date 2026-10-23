#!/usr/bin/env python3
"""Reanudable, disk-backed pipeline for source documents."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, re, shutil, subprocess, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STAGES=['detectar','texto','figuras','estructurar','enriquecer','validar','empaquetar']
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def write(p,obj):
    p.parent.mkdir(parents=True,exist_ok=True); data=json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    if not p.exists() or p.read_text(encoding='utf-8')!=data: p.write_text(data,encoding='utf-8',newline='\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def image_refs(obj):
    if isinstance(obj,dict):
        if obj.get('tipo')=='img' and isinstance(obj.get('src'),str): yield obj['src']
        for value in obj.values(): yield from image_refs(value)
    elif isinstance(obj,list):
        for value in obj: yield from image_refs(value)
def load_plugin(name):
    f=ROOT/'tools'/'pipeline'/'tipos'/f'{name}.py'
    sys.path.insert(0,str(f.parent))
    spec=importlib.util.spec_from_file_location('pipeline_tipo_'+name,f); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--doc'); ap.add_argument('--desde',choices=STAGES); ap.add_argument('--forzar',action='store_true'); ap.add_argument('--solo',choices=STAGES); args=ap.parse_args()
    cfg=read(ROOT/'tools/pipeline/config.json'); droot=ROOT/cfg['docus']; wroot=ROOT/cfg['work']; mpath=droot/'manifest.json'; manifest=read(mpath) if mpath.exists() else {'version':1,'documents':{}}
    docs=cfg['documents']; selected=[(k,v) for k,v in docs.items() if not args.doc or args.doc in (k,v['file'])]
    if not selected: raise SystemExit(f"Documento no configurado: {args.doc}")
    for doc_id,spec in selected:
        src=droot/spec['file']
        if not src.is_file(): raise SystemExit(f"No existe PDF: {src}")
        digest=sha(src); old=manifest['documents'].get(doc_id,{})
        if old.get('sha256')!=digest: args.forzar=True
        work=wroot/doc_id; dirs={s:work/s for s in STAGES}
        for p in dirs.values(): p.mkdir(parents=True,exist_ok=True)
        plugin=load_plugin(spec['tipo']); ctx={'root':ROOT,'doc':doc_id,'source':src,'spec':spec,'config':cfg,'dirs':dirs,'work':work}
        meta={'sha256':digest,'tipo':spec['tipo'],'prefijo':spec['prefijo'],'area':spec['area'],'archivo':spec['file'],'etapas':old.get('etapas',{})}
        start=STAGES.index(args.solo or args.desde or STAGES[0]); end=STAGES.index(args.solo) if args.solo else len(STAGES)-1
        if args.solo and start and not all((dirs[s]/'result.json').exists() for s in STAGES[:start]): raise SystemExit(f"--solo {args.solo} requiere etapas previas en disco")
        failed=False
        for i in range(start,end+1):
            stage=STAGES[i]; out=dirs[stage]/'result.json'; upstream=[sha(dirs[s]/'result.json') for s in STAGES[:i] if (dirs[s]/'result.json').exists()]
            # A plugin may import a helper from another type (e.g. the English
            # and mixed-booklet plugins reuse the cuadernillo extractor).
            # Hash every type so dependency edits invalidate the stage cache.
            implementation=[ROOT/'tools/pipeline/run.py',*sorted((ROOT/'tools/pipeline/tipos').glob('*.py'))]
            code_hash=''.join(sha(p) for p in implementation if p.exists())
            text_tool=shutil.which('pdftotext') if stage=='texto' else ''
            signature=hashlib.sha256((digest+json.dumps(upstream)+json.dumps(cfg,sort_keys=True)+stage+code_hash+(text_tool or 'pymupdf-fallback')).encode()).hexdigest()
            if stage == 'figuras' or stage in STAGES[4:]:
                outdir=ROOT/'content'/'icfes'/spec['prefijo']
                manual=[outdir/'overrides.json']
                if stage=='figuras' and (outdir/'overrides.json').exists():
                    for src_ref in image_refs(read(outdir/'overrides.json')):
                        if src_ref.startswith(f"/icfes/{spec['prefijo']}/"):
                            asset=outdir/'imagenes'/Path(src_ref).name
                            if asset.exists(): manual.append(asset)
                if stage in STAGES[4:]: manual += sorted((outdir/'hojas').glob('*.json'))
                manual_hash=''.join(f'{p.name}:{sha(p)}' for p in manual if p.exists())
                signature=hashlib.sha256((signature+manual_hash).encode()).hexdigest()
            cached=meta['etapas'].get(stage,{}).get('estado')=='completa' and meta['etapas'].get(stage,{}).get('firma')==signature and out.exists()
            if cached and not args.forzar: print(doc_id,stage,'cache'); continue
            try:
                if stage=='detectar': result=plugin.detectar(ctx)
                elif stage=='texto': result=plugin.extraer(ctx)
                elif stage=='figuras': result=extract_figures(ctx)
                elif stage=='estructurar': result=plugin.estructurar(ctx)
                elif stage=='enriquecer': result=enrich(ctx)
                elif stage=='validar': result=validate(ctx)
                else: result=package(ctx)
            except (Exception,SystemExit) as exc:
                meta['etapas'][stage]={'estado':'error','fecha':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'firma':signature,'error':str(exc)}
                manifest['documents'][doc_id]=meta; write(mpath,manifest)
                print(doc_id,stage,'ERROR',str(exc),file=sys.stderr)
                failed=True; break
            write(out,result); meta['etapas'][stage]={'estado':'completa','fecha':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'firma':signature,'salida_sha256':sha(out)}
            for later in STAGES[i+1:]: meta['etapas'].pop(later,None)
            manifest['documents'][doc_id]=meta; write(mpath,manifest); print(doc_id,stage,'ok')
        if failed: continue
        manifest['documents'][doc_id]=meta; write(mpath,manifest)
def extract_figures(c):
    import fitz
    d=fitz.open(c['source']); dest=c['dirs']['figuras']; full=c['work']/'paginas'; full.mkdir(exist_ok=True)
    cfg=c['config']; items=[]; dpi=int(cfg['dpi']); threshold=float(cfg['stroke_grouping_pt'])
    for pi,page in enumerate(d,1):
        page.get_pixmap(matrix=fitz.Matrix(dpi/72,dpi/72),alpha=False).save(full/f'page-{pi:03}.png')
        drawings=page.get_drawings(); boxes=[]
        for dr in drawings:
            r=fitz.Rect(dr['rect']);
            if r.width>=8 and r.height>=8: boxes.append(r)
        clusters=[]
        for r in boxes:
            for j,old in enumerate(clusters):
                near=fitz.Rect(old); near.x0-=threshold;near.y0-=threshold;near.x1+=threshold;near.y1+=threshold
                if near.intersects(r): clusters[j]=old|r; break
            else: clusters.append(r)
        for ci,r in enumerate(clusters,1):
            r &= page.rect
            if r.width<18 or r.height<18: continue
            path=dest/f'p{pi:03}-f{ci:02}.png'; page.get_pixmap(matrix=fitz.Matrix(dpi/72,dpi/72),clip=r,alpha=False).save(path)
            labels=[]
            for b in page.get_text('dict')['blocks']:
                if 'lines' not in b: continue
                br=fitz.Rect(b['bbox']); expanded=fitz.Rect(r);expanded.x0-=threshold;expanded.y0-=threshold;expanded.x1+=threshold;expanded.y1+=threshold
                if expanded.intersects(br): labels += [s['text'] for line in b['lines'] for s in line['spans']]
            items.append({'pagina':pi,'id':path.name,'bbox':[round(x,1) for x in r],'archivo':str(path.relative_to(c['root'])),'etiquetas':labels})
    # Recortes asociados manualmente: el ID estable determina la pregunta y
    # la posición del encabezado en la fuente. Se guardan bajo content/icfes
    # y Vite solo los copia al build cuando VITE_ICFES=1.
    pref=c['spec']['prefijo']; content=c['root']/'content'/'icfes'/pref
    ov_path=content/'overrides.json'; overrides=read(ov_path) if ov_path.exists() else {}
    image_dir=content/'imagenes'; image_dir.mkdir(parents=True,exist_ok=True); linked=[]
    figures=[(qid,fig) for qid,changes in sorted(overrides.items()) if qid!='__paquete__' and isinstance(changes,dict) for fig in (list(changes.get('figuras',[]))+[f for f in (changes.get('opcionesFig') or []) if isinstance(f,dict)])]
    figures += [('__paquete__',fig) for block in overrides.get('__paquete__',{}).get('bloques_agregar',[]) for fig in block.get('figuras',[])]
    for qid,fig in figures:
        if not isinstance(fig,dict) or fig.get('tipo')!='img': continue
        src=str(fig.get('src',''))
        if not src.startswith(f'/icfes/{pref}/'): continue
        name=Path(src).name; recorte=fig.get('recorteFuente')
        # Las figuras seleccionadas o recortadas manualmente también son una
        # entrada persistente del pipeline. Si no tienen receta geométrica,
        # conservar el PNG versionado en `imagenes/` en vez de intentar
        # reconstruirlo buscando un encabezado (que no existe en todos los
        # formatos, por ejemplo en el cuadernillo mixto numerado `n.`).
        manual_asset=image_dir/name
        if not recorte and manual_asset.is_file():
            linked.append({'pregunta_o_bloque':qid,'archivo':str(manual_asset.relative_to(c['root'])),'src':src,'reutilizado':True})
            continue
        if recorte:
            pi=int(recorte['pagina'])
            if pi<1 or pi>len(d): raise SystemExit(f'Página de recorte fuente inválida: {src}')
            rect=fitz.Rect(*recorte['rect']) & d[pi-1].rect
            if rect.is_empty: raise SystemExit(f'Recorte fuente inválido: {src}')
            d[pi-1].get_pixmap(matrix=fitz.Matrix(dpi/72,dpi/72),clip=rect,alpha=False).save(image_dir/name)
            linked.append({'pregunta_o_bloque':qid,'pagina':pi,'archivo':str((image_dir/name).relative_to(c['root'])),'src':src,'bbox':[round(v,1) for v in rect]}); continue
        num_match=re.search(r'(\d{3,4})$',qid)
        if not num_match: continue
        number=int(num_match.group(1)); found=False
        for pi,page in enumerate(d,1):
            hits=page.search_for(f'Pregunta {number}')
            if not hits: continue
            title=hits[0]; below=[]
            for other in range(1,61):
                if other==number: continue
                below.extend(r for r in page.search_for(f'Pregunta {other}') if r.y0>title.y0)
            end=min((r.y0 for r in below),default=page.rect.height-24)
            clip=fitz.Rect(28,title.y0-4,page.rect.width-28,max(title.y1+8,end-5)) & page.rect
            if clip.height<30: continue
            page.get_pixmap(matrix=fitz.Matrix(dpi/72,dpi/72),clip=clip,alpha=False).save(image_dir/name)
            linked.append({'pregunta_o_bloque':qid,'pagina':pi,'archivo':str((image_dir/name).relative_to(c['root'])),'src':src,'bbox':[round(v,1) for v in clip]}); found=True; break
        if not found: raise SystemExit(f'No se encontró encabezado de fuente para {qid} al generar {name}')
    write(dest/'figuras.json',{'candidatas':items,'recortes_asociados':linked,'nota':'Candidatos vectoriales y recortes solicitados explícitamente por overrides.json.'}); return {'paginas':len(d),'figuras_candidatas':len(items),'recortes_asociados':len(linked),'indice':'figuras.json'}
def enrich(c):
    pkg=read(c['dirs']['estructurar']/'result.json')
    if 'preguntas' not in pkg:
        write(c['dirs']['enriquecer']/'package.json',pkg)
        return {'preguntas':0,'documento_tipo':pkg.get('tipo')}
    ov_path=c['root']/'content/icfes'/c['spec']['prefijo']/'overrides.json'
    overrides=read(ov_path) if ov_path.exists() else {}
    dest=c['root']/'content/icfes'/c['spec']['prefijo']/'hojas'; dest.mkdir(parents=True,exist_ok=True)
    batch_size=max(1,int(c['config'].get('batch_size',10))); created_sheets=0
    for q in pkg['preguntas']:
        for key,val in overrides.get(q['id'],{}).items(): q[key]=val
        if q.get('correcta') is None: continue
        p=dest/(q['id']+'.json')
        # Una hoja existente puede contener corrección humana aunque siga en
        # borrador. Solo crearla cuando falta; nunca borrar trabajo al reanudar.
        if p.exists(): continue
        if created_sheets >= batch_size: continue
        wrong=[chr(65+i) for i in range(len(q['opciones'])) if i!=q['correcta']]
        blank=''.join(ch for ch in q['enunciado'][:40].split()[:5] if ch.isalpha())
        marca=[]
        if blank:
            frag=' '.join(q['enunciado'].split()[:2]).strip(' ¿?.,:;')
            if frag and frag in q['enunciado']: marca=[{'frag':frag,'rol':'pide','nota':'Fragmento automático; revisar su función.','campo':'Fragmento por revisar'}]
        def descartes():
            return [{'t':f'La opción {l} queda señalada por la clave, pero falta verificar en el original por qué no responde la pregunta.', 'a':f'o:{l}:no','k':'err'} for l in wrong]
        intro={'t':'Este guion es una plantilla de revisión; todavía no explica la solución.'}
        cierre={'t':'La clave indica una respuesta; falta comprobar el razonamiento en el cuadernillo.','a':f"o:{chr(65+q['correcta'])}:ok"}
        area=q.get('area')
        modo='calculo' if area=='matematicas' else 'concepto' if area=='ciencias' else 'lectura'
        sheet={'estado':'borrador','hoja':{'modo':modo,'marcas':marca,'pasos':[{'k':'idea','texto':'Revisa el enunciado, los datos y los apoyos gráficos en la página fuente.'},{'k':'check','texto':'Confirma la respuesta y el procedimiento contra el cuadernillo original.'}],'enfoque':{'tema':'Lectura del cuadernillo pendiente de revisión','que':'Identificar qué pide el enunciado y cotejar cada dato con la página fuente antes de justificar una respuesta.','pistas':['leer el enunciado completo','contrastar los apoyos gráficos con la página'],'clave':'La clave oficial orienta la revisión, pero no reemplaza una solución razonada.','no':[{'t':f'Opción {l}','p':'Parece una alternativa posible. Pero falta cotejarla con el original; no se debe concluir todavía.'} for l in wrong[:2]],'plan':[{'t':'Leer el enunciado y reconocer qué pide.'},{'t':'Revisar datos, opciones y figuras en la página original.'},{'t':'Escribir una solución comprobable y justificar cada descarte.'}]},'guion':{'1':[intro,{'t':'Primero revisemos qué pide la pregunta.'},cierre],'2':[intro,{'t':'Cotejemos los datos y las figuras con el cuadernillo.'},*descartes(),cierre],'3':[intro,{'t':'La explicación debe mostrar el procedimiento y las pistas relevantes.'},{'t':'Revisemos la clave y confirmemos el razonamiento antes de aprobarla.'},cierre]}}}
        write(p,sheet); created_sheets+=1; q['hoja']=sheet['hoja']; q['estadoHoja']=sheet['estado']
    write(c['dirs']['enriquecer']/'package.json',pkg); return {'preguntas':len(pkg['preguntas']),'hojas_creadas':created_sheets,'hojas_borrador':sum(1 for q in pkg['preguntas'] if q.get('estadoHoja')=='borrador')}
def validate(c):
    p=read(c['dirs']['enriquecer']/'package.json'); errors=[]
    if 'preguntas' not in p:
        write(c['dirs']['validar']/'validated.json',p)
        return {'preguntas':0,'errores':0,'tipo':p.get('tipo'),'paginas':len(p.get('paginas',[]))}
    ov_path=c['root']/'content/icfes'/c['spec']['prefijo']/'overrides.json'
    overrides=read(ov_path) if ov_path.exists() else {}
    for q in p['preguntas']:
        for key,val in overrides.get(q['id'],{}).items(): q[key]=val
    pending=[]
    for q in p['preguntas']:
        if q.get('correcta') is None:
            pending.append(q)
            continue
        if not isinstance(q.get('correcta'),int) or not 0 <= q['correcta'] < len(q.get('opciones',[])):
            errors.append(q['id']+':clave fuera de rango'); continue
        if q.get('origen') in ('icfes','licenciado') and not q.get('fuente'): errors.append(q['id']+':sin fuente')
        if not q.get('opciones') or len(q['opciones'])<2: errors.append(q['id']+':opciones')
        if len(q.get('distractores',[])) != len(q['opciones']): errors.append(q['id']+':distractores')
        elif any((i == q['correcta']) != (d == '') for i,d in enumerate(q['distractores'])): errors.append(q['id']+':distractor correcto/inactivo')
    if errors: raise SystemExit('\n'.join(errors))
    p['pendientes_clave']=pending
    p['preguntas']=[q for q in p['preguntas'] if q.get('correcta') is not None]
    # Una clave manual documentada en overrides.json también completa las
    # listas del simulacro y de la unidad, que se construyeron en estructurar.
    resolved_ids=[q['id'] for q in p['preguntas']]
    units=p.get('unidades',[])
    for unit in units:
        if len(units)<=1:
            unit['preguntas']=resolved_ids
        else:
            area=unit.get('area')
            scoped=[q['id'] for q in p['preguntas'] if q.get('area')==area]
            if scoped: unit['preguntas']=scoped
    for sim in p.get('simulacros',[]):
        sections=sim.get('secciones',[])
        if len(sections)<=1:
            for section in sections: section['preguntas']=resolved_ids
        else:
            # Mantener la partición editorial (p. ej. Examen 1 / Examen 2).
            # Solo completar IDs aprobados cuyo `parte` corresponde al título.
            assigned=set()
            for section in sections:
                title=str(section.get('titulo','')).strip()
                scoped=[q['id'] for q in p['preguntas'] if q.get('parte','').startswith(title+',')]
                if scoped:
                    section['preguntas']=scoped
                else:
                    section['preguntas']=[qid for qid in section.get('preguntas',[]) if qid in resolved_ids]
                assigned.update(section['preguntas'])
            # Completar claves por override sin aplanar secciones. El área
            # identifica el destino cuando solo hay una sección de esa área.
            missing=[q for q in p['preguntas'] if q['id'] not in assigned]
            for q in missing:
                candidates=[s for s in sections if s.get('area')==q.get('area')]
                if len(candidates)==1:
                    candidates[0].setdefault('preguntas',[]).append(q['id'])
    write(c['dirs']['validar']/'validated.json',p); return {'preguntas':len(p['preguntas']),'pendientes_clave':len(pending),'errores':0,'por_revisar':sum(bool(q.get('revisar')) for q in p['preguntas'])}
def package(c):
    src=read(c['dirs']['validar']/'validated.json'); out=c['root']/'content/icfes'/c['spec']['prefijo']; out.mkdir(parents=True,exist_ok=True)
    if 'preguntas' not in src:
        write(out/'documento.json',src)
        for stale in (out/'preguntas.json',out/'pendientes_clave.json'):
            if stale.exists(): stale.unlink()
        return {'archivo':str((out/'documento.json').relative_to(c['root'])),'preguntas':0,'paginas':len(src.get('paginas',[]))}
    # Conservar la transcripción íntegra ya generada como artefacto de trabajo;
    # el build gateado importa el paquete de preguntas, no este sidecar.
    pending=src.get('pendientes_clave',[])
    if pending: write(out/'pendientes_clave.json',{'preguntas':pending})
    else:
        stale_pending=out/'pendientes_clave.json'
        if stale_pending.exists(): stale_pending.unlink()
    overrides=out/'overrides.json'; ov=read(overrides) if overrides.exists() else {}
    if not isinstance(ov,dict): raise SystemExit('overrides.json debe ser un objeto por id')
    by_id={q['id']:q for q in src['preguntas']}
    package_override=ov.get('__paquete__',{})
    if not isinstance(package_override,dict): raise SystemExit('Override __paquete__ debe ser un objeto')
    unknown=set(ov)-set(by_id)-{'__paquete__'}
    if unknown: raise SystemExit('Overrides para IDs inexistentes: '+', '.join(sorted(unknown)))
    for q in src['preguntas']:
        changes=ov.get(q['id'],{})
        if not isinstance(changes,dict): raise SystemExit(f"Override de {q['id']} debe ser un objeto de campos")
        if 'id' in changes: raise SystemExit(f"No se permite cambiar el ID estable de {q['id']}")
        for key,val in changes.items(): q[key]=val
        sheet=out/'hojas'/(q['id']+'.json')
        if sheet.exists(): q['hoja']=read(sheet)['hoja']; q['estadoHoja']=read(sheet)['estado']
    for key,val in package_override.items():
        if key == 'bloques_agregar':
            if not isinstance(val,list): raise SystemExit('bloques_agregar debe ser una lista')
            current=src.setdefault('bloques',[])
            current.extend(b for b in val if b.get('id') not in {x.get('id') for x in current})
            continue
        if key not in ('bloques','unidades','simulacros','nombre','version'):
            raise SystemExit(f'Campo de paquete no permitido en override: {key}')
        src[key]=val
    for q in src['preguntas']:
        if q.get('origen') in ('icfes','licenciado') and not q.get('fuente'): raise SystemExit(q['id']+':sin fuente tras override')
        if not q.get('opciones') or not 0 <= q.get('correcta',-1) < len(q['opciones']): raise SystemExit(q['id']+':opciones/clave inválida tras override')
    write(out/'preguntas.json',src); return {'archivo':str((out/'preguntas.json').relative_to(c['root'])),'preguntas':len(src['preguntas'])}
if __name__=='__main__': main()
