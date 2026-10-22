#!/usr/bin/env python3
"""Convierte el texto de un cuadernillo ICFES (pdftotext o texto del conector) en un pack JSON.
Uso: python3 tools/importar_icfes.py texto.txt --area matematicas --pref mat --prueba "Prueba Matemáticas" --anio 2026 [--figuras figuras.json] [--imagenes dir]
Salida: content/icfes/<pref>/preguntas.json (solo entra al build con VITE_ICFES=1).
figuras.json (opcional): {"b:bq-mat-i4-6":[{"tipo":"tabla",...}] (figuras de un contexto compartido), "7":[{"tipo":"img","src":"/icfes/mat/p07.png","alt":"..."}], "12":{"opciones":[{...},{...},{...},{...}]}}
Texto copiado tal cual; lo dudoso queda en "revisar" para corregir a mano. Figuras sin archivo -> tipo "pendiente"."""
import re, json, sys, argparse, os
ap = argparse.ArgumentParser()
ap.add_argument('txt'); ap.add_argument('--area', required=True); ap.add_argument('--pref', required=True)
ap.add_argument('--prueba', required=True); ap.add_argument('--anio', default='2026'); ap.add_argument('--figuras')
a = ap.parse_args()
t = open(a.txt, encoding='utf-8').read().replace('\r', '')
fig = json.load(open(a.figuras)) if a.figuras else {}
fuente = f'Icfes ({a.anio}). {a.prueba}, Cuadernillo de preguntas. Saber 11.º. Bogotá D. C.: Dirección de Evaluación, Icfes.'

# 1) clave de respuestas (al final)
cut = re.split(r'Tabla de respuestas correctas', t)
clave = {int(n): L for n, L in re.findall(r'(?m)^\s*(\d{1,3})\s+([A-H])\s*$', cut[1])} if len(cut) > 1 else {}
cuerpo = cut[0]
# 2) limpiar encabezados y números de página sueltos
cuerpo = re.sub(r'(?m)^\s*Cuadernillo\s*(de preguntas)?\s*\.?\s*$', '', cuerpo)
cuerpo = re.sub(r'(?m)^\s*(de preguntas\s*)?Prueba [^\n]*$', '', cuerpo)
cuerpo = re.sub(r'(?m)^\s*\d{1,2}\s*$', '', cuerpo)
cuerpo = re.sub(r'\n{3,}', '\n\n', cuerpo)
# 3) partir en preguntas y contextos
partes = re.split(r'(?m)^\s*Pregunta\s+(\d+)\s*$', cuerpo)
bloques, preguntas, ctx = [], [], None
def limpia(s): return re.sub(r'[ \t]+', ' ', re.sub(r'\n(?!\n)', ' ', s.strip())).strip()
# texto antes de la primera pregunta = portada: se ignora salvo contexto "RESPONDE..."
def buscar_ctx(texto, n_sig):
    m = re.search(r'RESPONDE LAS PREGUNTAS\s+(\d+)\s+A\s+(\d+)\s+(DE ACUERDO CON [^\n]*)\n(.*)$', texto, re.S)
    return m
revisar_glob = []
for i in range(1, len(partes), 2):
    n = int(partes[i]); txt = partes[i + 1]
    # contexto compartido que aparece al final de la pregunta anterior
    m = buscar_ctx(txt, n)
    nuevo = None
    if m:
        txt = txt[:m.start()]
        nuevo = (int(m.group(1)), int(m.group(2)), m.group(3).strip(), m.group(4))
    mo = re.search(r'(?m)^\s*A\.\s', txt)
    enun = limpia(txt[:mo.start()] if mo else txt)
    ops, rev = [], []
    if mo:
        for L, o in re.findall(r'(?ms)^\s*([A-H])\.\s(.*?)(?=^\s*[A-H]\.\s|\Z)', txt[mo.start():]):
            ops.append(limpia(o))
    solo = re.fullmatch(r'(?:\s*[A-H]\.)+\s*', txt[mo.start():]) if mo else None
    if solo: ops = list(re.findall(r'[A-H](?=\.)', txt[mo.start():]))
    gr = len(ops) == 0 or bool(solo)
    hint = bool(re.search(r'\b(figura|gráfica|grafica|tabla|ilustraci|imagen|diagrama|mapa|esquema)', enun, re.I))
    f = fig.get(str(n)); figuras = []; opfig = None
    if isinstance(f, list): figuras = f
    elif hint: figuras = [{'tipo': 'pendiente', 'alt': f'Figura de la pregunta {n}'}]; rev.append('figura')
    if gr:
        ops = ops if len(ops) >= 2 else list('ABCD')
        og = (f or {}).get('opciones') if isinstance(f, dict) else None
        opfig = og or [{'tipo': 'pendiente', 'alt': f'Opción {L} de la pregunta {n}'} for L in ops]
        rev.append('opciones gráficas')
    if re.search(r'[=√∑]|\b(sen|cos|tan)\b|\d\s*\n', txt) and not gr: rev.append('fórmulas: comparar con el PDF')
    L = clave.get(n); cor = 'ABCDEFGH'.index(L) if L else 0
    if not L: rev.append('sin clave')
    q = {'id': f'{a.pref}-i{n:03d}', 'area': a.area, 'evidencia': 'ICFES', 'nivel': 2, 'enunciado': enun or f'(Pregunta {n}: enunciado en la figura)',
         'opciones': ops, 'correcta': cor, 'explicacion': 'Pendiente: explicación del profe.',
         'distractores': ['' if k == cor else 'Pendiente: por qué no es.' for k in range(len(ops))], 'origen': 'icfes', 'fuente': f'{fuente} Pregunta {n}.', 'parte': f'p{n}'}
    if figuras: q['figuras'] = figuras
    if opfig: q['opcionesFig'] = opfig
    if rev: q['revisar'] = rev
    preguntas.append(q)
    if nuevo: ctx = nuevo; bloques.append({'id': f'bq-{a.pref}-i{nuevo[0]}-{nuevo[1]}', 'area': a.area, 'encabezado': nuevo[2], 'texto': limpia(nuevo[3]), '_r': (nuevo[0], nuevo[1])})
# 4) enlazar bloques; el texto que antecede al primer "RESPONDE" también puede quedar dentro de la pregunta anterior
for b in bloques:
    lo, hi = b.pop('_r')
    for q in preguntas:
        n = int(q['parte'][1:])
        if lo <= n <= hi: q['bloque'] = b['id']
    b['fuente'] = fuente
    if fig.get('b:' + b['id']): b['figuras'] = fig['b:' + b['id']]
uni = {'id': f'u-icfes-{a.pref}', 'area': a.area, 'titulo': a.prueba + ' (Icfes)', 'resumen': 'Preguntas oficiales del Icfes, tal cual.', 'preguntas': [q['id'] for q in preguntas], 'sim': None, 'leccion': None, 'min': max(10, len(preguntas))}
pack = {'unidades': [uni], 'id': f'icfes-{a.pref}', 'nombre': a.prueba + ' (Icfes)', 'version': 1, 'bloques': bloques, 'preguntas': preguntas}
os.makedirs(f'content/icfes/{a.pref}', exist_ok=True)
json.dump(pack, open(f'content/icfes/{a.pref}/preguntas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(preguntas)} preguntas, {len(bloques)} bloques, clave para {len(clave)}; por revisar: {sum(1 for q in preguntas if q.get("revisar"))}')
