from pathlib import Path
import json,re
from cuadernillo import extraer

def detectar(ctx,tipo):
    import fitz
    doc=fitz.open(ctx['source']); text='\n'.join(p.get_text(sort=True) for p in doc)
    q=len(re.findall(r'(?im)^\s*(?:Pregunta|Question)\s+\d+\s*$',text))
    return {'tipo':tipo,'pages':len(doc),'title':doc.metadata.get('title'),'pregunta_markers':q,'has_answer_key':bool(re.search(r'(?i)(tabla de respuestas|clave de respuestas|answer key)',text))}

def estructurar_documento(ctx,tipo,incluir_figuras=False):
    path=ctx['dirs']['texto']/'documento.txt'
    text=path.read_text(encoding='utf-8') if path.exists() else ''
    pages=[{'pagina':i,'texto':s.strip()} for i,s in enumerate(text.split('\f'),1) if s.strip()]
    result={'tipo':tipo,'archivo':ctx['spec']['file'],'origen':ctx['spec']['origen'],'cita':ctx['spec'].get('cita'),'area':ctx['spec']['area'],'paginas':pages,'revisar':['Texto literal preservado por página; estructuración semántica pendiente de cotejo.']}
    if incluir_figuras:
        f=ctx['dirs']['figuras']/'figuras.json'
        result['figurasCandidatas']=json.loads(f.read_text(encoding='utf-8')).get('candidatas',[]) if f.exists() else []
        result['revisar'].append('Las figuras candidatas no están asociadas automáticamente con una página/afirmación validada.')
    return result
