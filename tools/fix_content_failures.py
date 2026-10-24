import json, re

# 1. cfi-i042
cfi_f = 'content/icfes/cfi/preguntas.json'
cfi_data = json.load(open(cfi_f, 'r', encoding='utf-8'))
for q in cfi_data['preguntas']:
    if q['id'] == 'cfi-i042':
        frag = "cumple la función de"
        q['hoja']['marcas'] = [{'campo': 'Pista de lectura', 'frag': frag, 'nota': 'Indica qué pide interpretar.', 'rol': 'pide'}]
        for s in q['hoja']['guion']['1']:
            if s.get('a', '').startswith('m:'):
                s['a'] = f'm:{frag}'
    elif q['id'] == 'cfi-i078':
        frag = "mide su temperatura cada minuto"
        q['hoja']['marcas'] = [{'campo': 'Pista central', 'frag': frag, 'nota': 'Registro de datos.', 'rol': 'pide'}]
        for s in q['hoja']['guion']['1']:
            if s.get('a', '').startswith('m:'):
                s['a'] = f'm:{frag}'
    elif q['id'] == 'cfi-i079':
        frag = "velocidad de formación de W"
        q['hoja']['marcas'] = [{'campo': 'Tarea de la pregunta', 'frag': frag, 'nota': 'Objeto de análisis.', 'rol': 'pide'}]
        for s in q['hoja']['guion']['1']:
            if s.get('a', '').startswith('m:'):
                s['a'] = f'm:{frag}'
    elif q['id'] == 'cfi-i082':
        frag = "se espera que después de la oxidación se haya formado una mezcla de"
        q['hoja']['marcas'] = [{'campo': 'Tarea de la pregunta', 'frag': frag, 'nota': 'Objeto de análisis.', 'rol': 'pide'}]
        for s in q['hoja']['guion']['1']:
            if s.get('a', '').startswith('m:'):
                s['a'] = f'm:{frag}'
    elif q['id'] == 'cfi-i085':
        # clean any double-bracing
        for fld in ['explicacion']:
            q[fld] = re.sub(r'\{\{+', '{{', re.sub(r'\}\}+', '}}', q[fld]))
        for i in range(len(q['distractores'])):
            q['distractores'][i] = re.sub(r'\{\{+', '{{', re.sub(r'\}\}+', '}}', q['distractores'][i]))
        if q.get('hoja'):
            s = json.dumps(q['hoja'], ensure_ascii=False)
            s = re.sub(r'\{\{+', '{{', re.sub(r'\}\}+', '}}', s)
            q['hoja'] = json.loads(s)
    elif q['id'] == 'cfi-i001':
        for i in range(len(q['distractores'])):
            if q['distractores'][i] and not re.search(r'\bpero\b', q['distractores'][i], re.I):
                q['distractores'][i] = 'Pero ' + q['distractores'][i][:1].lower() + q['distractores'][i][1:]
        if q.get('hoja') and 'enfoque' in q['hoja'] and 'no' in q['hoja']['enfoque']:
            for no in q['hoja']['enfoque']['no']:
                if not re.search(r'\bpero\b', no['p'], re.I):
                    no['p'] = 'Pero ' + no['p'][:1].lower() + no['p'][1:]

json.dump(cfi_data, open(cfi_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 2. mat-i017 clean double-bracing
mat_f = 'content/icfes/mat/preguntas.json'
mat_data = json.load(open(mat_f, 'r', encoding='utf-8'))
for q in mat_data['preguntas']:
    if q['id'] == 'mat-i017':
        for i in range(len(q['distractores'])):
            q['distractores'][i] = re.sub(r'\{\{+', '{{', re.sub(r'\}\}+', '}}', q['distractores'][i]))
        if q.get('hoja'):
            s = json.dumps(q['hoja'], ensure_ascii=False)
            s = re.sub(r'\{\{+', '{{', re.sub(r'\}\}+', '}}', s)
            q['hoja'] = json.loads(s)
json.dump(mat_data, open(mat_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 3. cie-i018: replace Cl2 with Cl₂
cie_f = 'content/icfes/cie/preguntas.json'
cie_data = json.load(open(cie_f, 'r', encoding='utf-8'))
for q in cie_data['preguntas']:
    if q['id'] == 'cie-i018':
        s = json.dumps(q, ensure_ascii=False).replace('Cl2', 'Cl₂')
        q.clear()
        q.update(json.loads(s))
json.dump(cie_data, open(cie_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

cna_f = 'content/icfes/cna/preguntas.json'
cna_data = json.load(open(cna_f, 'r', encoding='utf-8'))
for q in cna_data['preguntas']:
    if q['id'] == 'cna-i018':
        s = json.dumps(q, ensure_ascii=False).replace('Cl2', 'Cl₂')
        q.clear()
        q.update(json.loads(s))
json.dump(cna_data, open(cna_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# Sync hojas files
for p, f in [('cfi', cfi_f), ('mat', mat_f), ('cie', cie_f), ('cna', cna_f)]:
    d = json.load(open(f, 'r', encoding='utf-8'))
    for q in d['preguntas']:
        hp = f'content/icfes/{p}/hojas/{q["id"]}.json'
        if os.path.exists(hp) and q.get('hoja'):
            try:
                hs = json.load(open(hp, 'r', encoding='utf-8'))
                hs['hoja'] = q['hoja']
                json.dump(hs, open(hp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
            except: pass

print("Content failures fixed.")
