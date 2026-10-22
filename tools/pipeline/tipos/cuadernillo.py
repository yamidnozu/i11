import json,re,shutil,subprocess
from pathlib import Path
import fitz

def detectar(ctx):
    d=fitz.open(ctx['source']); text='\n'.join(p.get_text(sort=True) for p in d)
    return {'pages':len(d),'title':d.metadata.get('title'),'text_markers':len(re.findall(r'(?im)^\s*(?:Pregunta|Question)\s+\d+\s*$',text)),'has_answer_key':bool(re.search(r'(?i)(?:Tabla de respuestas(?: correctas)?|TABLA DE RESPUESTAS|answer key)',text))}

def extraer(ctx):
    target=ctx['dirs']['texto']/'documento.txt'; cmd=shutil.which('pdftotext')
    if cmd:
        subprocess.run([cmd,'-layout',str(ctx['source']),str(target)],check=True)
        method='pdftotext -layout'
    else:
        # PyMuPDF fallback preserves text order when Poppler is not installed.
        d=fitz.open(ctx['source']); target.write_text('\n\n'.join(p.get_text(sort=True) for p in d),encoding='utf-8'); method='PyMuPDF page.get_text(sort=True) fallback; pdftotext unavailable'
    return {'path':str(target.relative_to(ctx['root'])),'metodo':method,'sha256':__import__('hashlib').sha256(target.read_bytes()).hexdigest()}

def estructurar(ctx):
    text=(ctx['dirs']['texto']/'documento.txt').read_text(encoding='utf-8'); cfg=ctx['spec']; pref=cfg['prefijo']
    # Quita solo numeración aislada al borde de cada página; los números dentro
    # del procedimiento pueden quedar solos en su línea y deben conservarse.
    pages=[]
    for page in text.split('\f'):
        lines=page.splitlines()
        nonblank=[i for i,line in enumerate(lines) if line.strip()]
        for i in reversed(nonblank[-1:] + nonblank[:1]):
            if re.fullmatch(r'\s*\d{1,2}\s*',lines[i]): lines[i]=''
        pages.append('\n'.join(lines))
    text='\f'.join(pages)
    # ICFES ha usado varios encabezados para la misma tabla de claves.
    # Mantener las variantes en el plugin evita tratar documentos antiguos
    # como si no tuvieran clave y dejar preguntas válidas fuera del paquete.
    cuts=re.split(r'(?:Tabla de respuestas(?: correctas)?|TABLA DE RESPUESTAS)',text,flags=re.I)
    key={int(n):L for n,L in re.findall(r'(?<!\d)(\d{1,3})\s+([A-H])(?=\s|$)',cuts[1])} if len(cuts)>1 else {}
    body=cuts[0]; chunks=re.split(r'(?im)^\s*(?:Pregunta|Question)\s+(\d+)\s*$',body)
    records=[]
    if len(chunks)>1:
        records=[(int(chunks[i]),chunks[i+1]) for i in range(1,len(chunks),2)]
    elif key:
        # Cuadernillos antiguos imprimen el número junto al enunciado ("1.").
        # Creamos un registro por cada posición de la clave y dejamos explícita
        # la revisión cuando el OCR no permite delimitar ese reactivo con certeza.
        marks=list(re.finditer(r'(?m)^\s*(\d{1,3})\.\s+',body))
        found={}
        for j,m in enumerate(marks):
            n=int(m.group(1))
            if n not in key: continue
            end=marks[j+1].start() if j+1<len(marks) else len(body)
            raw=body[m.end():end]
            choices=re.findall(r'(?m)^\s*[A-D]\.\s+',raw)
            if n not in found or len(choices)>=4: found[n]=raw
        records=[(n,found.get(n,'')) for n in sorted(key)]
    qs=[]; blocks=[]; pending=None
    def clean(s): return re.sub(r'[ \t]+',' ',re.sub(r'\n(?!\n)',' ',s.strip())).strip()
    for n,raw in records:
        ctxm=re.search(r'RESPONDE LAS PREGUNTAS\s+(\d+)\s+A\s+(\d+)\s+(DE ACUERDO CON[^\n]*)\n(.*)$',raw,re.I|re.S)
        new=None
        if ctxm: raw=raw[:ctxm.start()]; new=(int(ctxm[1]),int(ctxm[2]),ctxm[3].strip(),ctxm[4])
        opt=re.search(r'(?m)^[ \t]*A\.[ \t]+',raw); stem=clean(raw[:opt.start()] if opt else raw); choices=[]
        if opt:
            options_text=raw[opt.start():].split('Cuadernillo de preguntas',1)[0]
            raw_choices=re.findall(r'(?ms)^[ \t]*[A-H]\.[ \t]*(.*?)(?=^[ \t]*[A-H]\.[ \t]+|\Z)',options_text)
            if raw_choices:
                # Poppler includes the printed page footer after the final
                # option. Remove only a standalone number on the last lines;
                # a numeric answer such as "10" on its own is preserved.
                raw_choices[-1]=re.sub(r'\n(?:[ \t]*\n)*[ \t]*\d{1,2}[ \t]*(?:\n[ \t]*)*$', '', raw_choices[-1])
            choices=[clean(x) for x in raw_choices]
        rev=[]
        answer_index='ABCDEFGH'.index(key[n]) if n in key else -1
        bad_choices=(len(choices)!=4 or len(set(choices))!=len(choices) or any(not x.strip() or 'Cuadernillo de preguntas' in x for x in choices) or (answer_index>=len(choices)))
        graphical_options=bad_choices
        if graphical_options:
            rev.append('Opciones gráficas detectadas en el área de respuesta; se requiere cotejo visual.')
            choices=list('ABCD')
        if n not in key: rev.append('No se detectó clave de respuesta; pregunta apartada para evitar inventar una opción correcta.')
        if re.search(r'figura|gráfica|grafica|tabla|imagen|diagrama|mapa|esquema',stem,re.I): rev.append('Referencia visual: asociar figura extraída tras cotejo visual.')
        # Do not flag ordinary Spanish words such as "tan"/"tanto"; these
        # function names count only as notation when followed by an argument.
        if re.search(r'[=√∑]|\b(?:sen|cos|tan)\s*(?:\(|[a-z]\s*(?=[=+*/-]))',raw,re.I): rev.append('Fórmulas/símbolos: cotejar transcripción con PDF.')
        if not stem: stem=f'(Pregunta {n}: enunciado no delimitado en la extracción)'; rev.append('Enunciado no delimitado con certeza; cotejar página fuente antes de usar.')
        if len(chunks)==1: rev.append('Formato numerado antiguo: cotejar enunciado, opciones, figuras y contexto compartido en PDF.')
        correct=answer_index
        citation=cfg.get('cita') if cfg['origen']!='icfes' else f"Icfes ({cfg['anio']}). {cfg['prueba']}, Cuadernillo de preguntas. Saber 11.º. Bogotá D. C.: Instituto Colombiano para la Evaluación de la Educación (Icfes). Pregunta {n}."
        if cfg['origen']!='icfes': rev.append('Completar y cotejar la cita editorial del documento fuente.')
        q={'id':f'{pref}-i{n:03d}','area':cfg['area'],'evidencia':'Pendiente de marco de referencia','nivel':2,'enunciado':stem,'opciones':choices or ['A','B','C','D'],'correcta':correct if correct>=0 else None,'explicacion':'Pendiente de solución verificada.','distractores':['' if j==correct else 'Pendiente de análisis; no inferido automáticamente.' for j in range(len(choices or ['A','B','C','D']))],'origen':cfg['origen'],'fuente':citation,'parte':f'Pregunta {n}'}
        if rev: q['revisar']=rev
        if graphical_options:
            q['opcionesFig']=[{'tipo':'pendiente','alt':f'Opción {letter} de la pregunta {n}'} for letter in choices]
        qs.append(q)
        if new:
            lo,hi,header,txt=new; bid=f'bq-{pref}-i{lo}-{hi}'; blocks.append({'id':bid,'area':cfg['area'],'encabezado':header,'texto':clean(txt),'fuente':q['fuente'],'_range':[lo,hi]})
    for b in blocks:
        lo,hi=b.pop('_range')
        for q in qs:
            n=int(q['parte'].split()[-1])
            if lo<=n<=hi: q['bloque']=b['id']
    if not qs:
        from documento import estructurar_documento
        return estructurar_documento(ctx,'cuadernillo_sin_marcadores',True)
    valid_ids=[q['id'] for q in qs if q.get('correcta') is not None]
    sim_id=f'sim-icfes-{pref}'
    unit={'id':f'u-icfes-{pref}','area':cfg['area'],'titulo':cfg['prueba'],'resumen':'Cuadernillo fuente; reactivos y explicaciones en revisión.','preguntas':valid_ids,'sim':None,'leccion':None,'min':max(10,len(valid_ids))}
    simulacros=[{'id':sim_id,'nombre':f"Simulacro: {cfg['prueba']}",'descripcion':'Reactivos con clave detectada; verificar transcripción, figuras y explicaciones antes de uso.','nivel':'En revisión','barajar':False,'modo':'secciones','secciones':[{'titulo':cfg['prueba'],'area':cfg['area'],'minutos':max(10,len(valid_ids)),'preguntas':valid_ids}]}] if valid_ids else []
    pack={'id':f'icfes-{pref}','nombre':cfg['prueba'],'version':1,'preguntas':qs,'bloques':blocks,'unidades':[unit],'simulacros':simulacros}
    return pack
