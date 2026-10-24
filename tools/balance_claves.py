"""Reparte la posición de la clave (A-D) en las ICFES permutando (intercambiando) la opción
correcta con otra, y remapea letras en explicación, hoja, guion y distractores.
No toca preguntas cuyas opciones se refieren entre sí, tienen figuras por opción o usan letras
sueltas ambiguas en la explicación (puntos, modelos, etc.).
Uso: python3 tools/balance_claves.py [prefijo ...]"""
import json, re, sys, glob, collections
sys.path.insert(0, 'tools')
from ronda_fix import rd, wr, ROOT
L = 'ABCDEFGH'
REF = re.compile(r'(?i)\b(anterior|ambas|ambos|todas|todos|ninguna|ningun|cualquiera|opciones? [A-D]|[A-D] y [A-D]|\bI y II|solo I|solo II|I, II)')
PAT2 = re.compile(r'(?<![\w{])((?:\b[Ll]a |\b[Ee]l |\bde |\bpor |; |: |\by |\bo |, ))([A-D])(?= y [A-D]\b| (?:no|sí|si|es|son|se|afirma|expresa|usa|ignora|cambia|altera|suma|calcula|identifica|omite|invierte|confunde|incorpora|deja|refleja|aplica|equivale|equivalen|respeta|representa|presenta|plantea|propone|describe|mantiene|conserva|restringe|resume|mezcla|corresponde|justifica|concluye|solo)\b)|(?<![\w{])([A-D]) y ([A-D])\b')
PAT = re.compile(r'(?<![\w{])((?:[Oo]pci[oó]n|[Aa]lternativa|respuesta(?: correcta)? es|clave es|correcta es|correcta:)\s*)([A-H])\b')

def strings(x):
    if isinstance(x, dict):
        for v in x.values(): yield from strings(v)
    elif isinstance(x, list):
        for v in x: yield from strings(v)
    elif isinstance(x, str): yield x

def residual(q):
    for t in strings({k: q.get(k) for k in ('explicacion', 'hoja', 'distractores')}):
        u = PAT2.sub('', PAT.sub('', t)); u = re.sub(r'\{\{.*?\}\}|$.*?$|o:[A-H]:\w+', '', u)
        if re.search(r'(?<![\w])[B-D](?![\w])', u): return True
    return False

def movible(q):
    n = len(q['opciones'])
    if n > 4 or n < 3 or q.get('opcionesFig') or q.get('figuras') and any('opci' in json.dumps(f).lower() for f in q['figuras']): return False
    if any(REF.search(o) for o in q['opciones']) or REF.search(q['enunciado']): return False
    if q.get('revisar'): return False
    if any(re.fullmatch(r'[\d\s.,$\\%/-]+', o) for o in q['opciones']) and False: return False
    return not residual(q)

def remap(t, m):
    t = PAT.sub(lambda g: g.group(1) + m.get(g.group(2), g.group(2)), t)
    t = PAT2.sub(lambda g: (g.group(1) + m.get(g.group(2), g.group(2))) if g.group(2) else m.get(g.group(3), g.group(3)) + ' y ' + m.get(g.group(4), g.group(4)), t)
    return re.sub(r'\bo:([A-H]):(\w+)', lambda g: f'o:{m.get(g.group(1), g.group(1))}:{g.group(2)}', t)

def walk(x, m):
    if isinstance(x, dict):
        for k, v in list(x.items()):
            if k == 'a' and isinstance(v, str): x[k] = remap(v, m)
            elif k == 't' and isinstance(v, str) and re.fullmatch(r'Opci[oó]n [A-H]', v): x[k] = 'Opción ' + m.get(v[-1], v[-1])
            else: x[k] = walk(v, m)
        return x
    if isinstance(x, list): return [walk(v, m) for v in x]
    if isinstance(x, str): return remap(x, m)
    return x

def swap(q, t):
    k = q['correcta']; m = {L[k]: L[t], L[t]: L[k]}
    for f in ('opciones', 'distractores'): q[f][k], q[f][t] = q[f][t], q[f][k]
    q['correcta'] = t
    q['explicacion'] = remap(q['explicacion'], m)
    q['distractores'] = [remap(d, m) for d in q['distractores']]
    if q.get('hoja'):
        q['hoja'] = walk(q['hoja'], m)
        no = q['hoja'].get('enfoque', {}).get('no')
        if no: no.sort(key=lambda e: e['t'])
    return m

def balancear(p):
    d = rd(f'{ROOT}/{p}/preguntas.json'); qs = d['preguntas']
    cnt = collections.Counter(q['correcta'] for q in qs if q['correcta'] < 4)
    mov = {q['id']: movible(q) for q in qs}
    hechos = {}
    while True:
        hi = max(range(4), key=lambda i: cnt[i]); lo = min(range(4), key=lambda i: cnt[i])
        if cnt[hi] - cnt[lo] <= 2: break
        cand = [q for q in qs if q['correcta'] == hi and mov[q['id']] and q['id'] not in hechos and len(q['opciones']) > lo]
        if not cand: break
        q = cand[0]; hechos[q['id']] = swap(q, lo); cnt[hi] -= 1; cnt[lo] += 1
    if not hechos: return {}, cnt
    wr(f'{ROOT}/{p}/preguntas.json', d)
    ov = rd(f'{ROOT}/{p}/overrides.json')
    for q in qs:
        if q['id'] in hechos:
            if q['id'] in ov:
                for k in ('opciones', 'distractores', 'explicacion', 'correcta'): ov[q['id']][k] = q[k]
            hp = f"{ROOT}/{p}/hojas/{q['id']}.json"
            try: hs = rd(hp); hs['hoja'] = q['hoja']; wr(hp, hs)
            except FileNotFoundError: pass
    wr(f'{ROOT}/{p}/overrides.json', ov)
    return hechos, cnt

if __name__ == '__main__':
    for p in (sys.argv[1:] or [x.split('/')[2] for x in sorted(glob.glob(f'{ROOT}/*/preguntas.json'))]):
        h, c = balancear(p)
        print(p, 'permutadas', len(h), 'claves', sorted(c.items()))
