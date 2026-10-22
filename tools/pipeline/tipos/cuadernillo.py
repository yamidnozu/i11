import json,re,shutil,subprocess
from pathlib import Path
import fitz

def detectar(ctx):
    d=fitz.open(ctx['source']); text='\n'.join(p.get_text(sort=True) for p in d)
    return {'pages':len(d),'title':d.metadata.get('title'),'text_markers':len(re.findall(r'(?m)^\s*Pregunta\s+\d+\s*$',text)),'has_answer_key':'Tabla de respuestas correctas' in text}

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
    cuts=re.split(r'Tabla de respuestas correctas',text); key={int(n):L for n,L in re.findall(r'(?m)^\s*(\d{1,3})\s+([A-H])\s*$',cuts[1])} if len(cuts)>1 else {}
    body=re.sub(r'(?m)^\s*\d{1,2}\s*$','',cuts[0]); chunks=re.split(r'(?m)^\s*Pregunta\s+(\d+)\s*$',body)
    qs=[]; blocks=[]; pending=None
    def clean(s): return re.sub(r'[ \t]+',' ',re.sub(r'\n(?!\n)',' ',s.strip())).strip()
    for i in range(1,len(chunks),2):
        n=int(chunks[i]); raw=chunks[i+1]; ctxm=re.search(r'RESPONDE LAS PREGUNTAS\s+(\d+)\s+A\s+(\d+)\s+(DE ACUERDO CON[^\n]*)\n(.*)$',raw,re.I|re.S)
        new=None
        if ctxm: raw=raw[:ctxm.start()]; new=(int(ctxm[1]),int(ctxm[2]),ctxm[3].strip(),ctxm[4])
        opt=re.search(r'(?m)^\s*A\.\s',raw); stem=clean(raw[:opt.start()] if opt else raw); choices=[]
        if opt:
            choices=[clean(x) for x in re.findall(r'(?ms)^\s*[A-H]\.\s*(.*?)(?=^\s*[A-H]\.\s|\Z)',raw[opt.start():])]
        rev=[]
        answer_index='ABCDEFGH'.index(key[n]) if n in key else -1
        bad_choices=(len(choices)!=4 or len(set(choices))!=len(choices) or any(not x.strip() or 'Cuadernillo de preguntas' in x for x in choices) or (answer_index>=len(choices)))
        graphical_options=bad_choices
        if graphical_options:
            rev.append('Opciones gráficas detectadas en el área de respuesta; se requiere cotejo visual.')
            choices=list('ABCD')
        if n not in key: rev.append('No se detectó clave de respuesta.')
        if re.search(r'figura|gráfica|grafica|tabla|imagen|diagrama|mapa|esquema',stem,re.I): rev.append('Referencia visual: asociar figura extraída tras cotejo visual.')
        if re.search(r'[=√∑]|\b(sen|cos|tan)\b',raw,re.I): rev.append('Fórmulas/símbolos: cotejar transcripción con PDF.')
        if not stem: stem=f'(Pregunta {n}: enunciado en figura)'; rev.append('Enunciado posiblemente gráfico; cotejar PDF.')
        correct=answer_index
        q={'id':f'{pref}-i{n:03d}','area':cfg['area'],'evidencia':'Pendiente de marco de referencia','nivel':2,'enunciado':stem,'opciones':choices or ['A','B','C','D'],'correcta':correct if correct>=0 else 0,'explicacion':'Pendiente de solución verificada.','distractores':['' if j==correct else 'Pendiente de análisis; no inferido automáticamente.' for j in range(len(choices or ['A','B','C','D']))],'origen':cfg['origen'],'fuente':f"Icfes ({cfg['anio']}). {cfg['prueba']}, Cuadernillo de preguntas. Saber 11.º. Bogotá D. C.: Instituto Colombiano para la Evaluación de la Educación (Icfes). Pregunta {n}.",'parte':f'Pregunta {n}'}
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
    unit={'id':f'u-icfes-{pref}','area':cfg['area'],'titulo':cfg['prueba'],'resumen':'Cuadernillo oficial; revisar preguntas y soluciones antes de uso.','preguntas':[q['id'] for q in qs],'sim':None,'leccion':None,'min':max(10,len(qs))}
    pack={'id':f'icfes-{pref}','nombre':cfg['prueba'],'version':1,'preguntas':qs,'bloques':blocks,'unidades':[unit],'simulacros':[]}
    return pack
