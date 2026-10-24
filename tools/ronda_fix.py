"""Ronda de corrección: aplica razones/opciones específicas a preguntas ICFES concretas
y las propaga de forma coherente a preguntas.json, overrides.json y hojas/<id>.json
(enfoque.no y las líneas 'err' del guion en los niveles 2 y 3)."""
import json, re, sys
ROOT = 'content/icfes'
def rd(p): return json.load(open(p, encoding='utf-8'))
def wr(p, d): json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
MULET = re.compile(r'^(Parece[^.]*\.\s*Pero,?\s*|Pero,\s*)', re.I)
def limpia(t):
    t = MULET.sub('', t).strip()
    return t[:1].upper() + t[1:] if t and not t.startswith('{{') else t

def _nums(t):
    """Envuelve cifras sueltas en {{…}} para que el profe las lea en palabras."""
    partes = re.split(r'(\{\{.*?\}\}|\$.*?\$)', t)
    return ''.join(x if x.startswith(('{{', '$')) else re.sub(r'\d[\d.,]*(?: ?%)?', lambda m: '{{' + m.group(0).rstrip('.,') + '}}' + m.group(0)[len(m.group(0).rstrip('.,')):], x) for x in partes)

def _pero(t):
    return 'Pero, ' + (t if t.startswith('{{') else t[:1].lower() + t[1:])

def sync_hoja(h, q):
    L = 'ABCDEFGH'
    enf = h.get('enfoque')
    if enf is not None:
        enf['no'] = [{'t': f'Opción {L[i]}', 'p': _nums(_pero(q['distractores'][i]))} for i in range(len(q['opciones'])) if i != q['correcta'] and q['distractores'][i]]
    for nivel, g in (h.get('guion') or {}).items():
        for s in g:
            m = re.fullmatch(r'o:([A-H]):no', s.get('a', ''))
            if not m: continue
            i = L.index(m.group(1))
            if i >= len(q['distractores']) or not q['distractores'][i]: continue
            pref = re.match(r'^(La opción [A-H] [^:]+: )', s.get('t', ''))
            s['t'] = (pref.group(1) if pref else f'La opción {m.group(1)} no corresponde: ') + _nums(q['distractores'][i])

def aplicar(cambios):
    por = {}
    for i, c in cambios.items(): por.setdefault(i.split('-')[0], {})[i] = c
    for p, items in por.items():
        pq = f'{ROOT}/{p}/preguntas.json'; po = f'{ROOT}/{p}/overrides.json'
        d = rd(pq); ov = rd(po)
        for q in d['preguntas']:
            c = items.get(q['id'])
            if not c: continue
            for k in ('opciones', 'distractores', 'explicacion'):
                if k in c:
                    q[k] = c[k]
                    if q['id'] in ov: ov[q['id']][k] = c[k]
            assert len(q['distractores']) == len(q['opciones']) and q['distractores'][q['correcta']] == ''
            if q.get('hoja'): sync_hoja(q['hoja'], q)
            hp = f"{ROOT}/{p}/hojas/{q['id']}.json"
            try:
                hs = rd(hp); sync_hoja(hs['hoja'], q); wr(hp, hs)
            except FileNotFoundError: pass
        wr(pq, d); wr(po, ov)

def limpiar_muletillas():
    """Quita la muletilla 'Parece … Pero' / 'Pero,' del inicio de las razones en hoja.no y guion (sin tocar el fondo)."""
    import glob
    PRE = re.compile(r'^(Parece[^.]*\.\s*Pero,?\s+|Pero,\s+)')
    def fx(t):
        if not t.startswith('Parece'): return t
        return _pero(PRE.sub('', t))
    def hoja(h):
        c = 0
        for a in (h.get('enfoque') or {}).get('no', []):
            n = fx(a['p']); c += n != a['p']; a['p'] = n
        for g in (h.get('guion') or {}).values():
            for s in g:
                m = re.match(r'^(La opción [A-H] [^:]+: )(.*)$', s.get('t', ''), re.S)
                if m:
                    n = m.group(1) + fx(m.group(2)); c += n != s['t']; s['t'] = n
        return c
    n = 0
    for pq in glob.glob(f'{ROOT}/*/preguntas.json'):
        p = pq.split('/')[2]; d = rd(pq); ch = False
        for q in d['preguntas']:
            h = q.get('hoja')
            if h and hoja(h):
                ch = True; n += 1
                hp = f"{ROOT}/{p}/hojas/{q['id']}.json"
                try: hs = rd(hp); hoja(hs['hoja']); wr(hp, hs)
                except FileNotFoundError: pass
        if ch: wr(pq, d)
    return n
