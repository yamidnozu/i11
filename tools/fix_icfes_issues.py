"""
Corrige inconsistencias detectadas en preguntas ICFES oficiales:
1. cfi-i006: distractor A debe contener 'Pero' en hoja.enfoque.no.
2. cfi-i085: t1, t2, t3, t4 envueltos en {{...}} para speech.
3. mth-i002: no usar fórmula que comience por '=2.000'.
4. mat-i017: 4lah envuelto en {{4lah}} para speech.
5. soc-i007 / scc-i007: guion nivel 2 o:A:ok (correcta 0), descartes o:B:no, o:C:no, o:D:no.
6. soc-i013 / scc-i013: guion nivel 2 o:D:ok (correcta 3), descartes o:A:no, o:B:no, o:C:no.
7. soc-i010 y soc-i011: restaurar explicaciones y distractores a sus enunciados originales.
8. soc-i018 y soc-i024: restaurar explicaciones y distractores a sus enunciados originales.
9. cfi-i104, cfi-i106, cfi-i120: guiones de nivel 2 completos con todos los descartes.
10. Marcas en cfi y mat que no coinciden exactamente con el enunciado: recortar frag para que sea substring exacto.
"""
import json, re, glob, os

L = 'ABCDEFGH'

def sync_hoja_guion(q):
    h = q.get('hoja')
    if not h: return
    c = q['correcta']
    c_let = L[c]
    enf = h.setdefault('enfoque', {})
    enf['no'] = [{'t': f'Opción {L[i]}', 'p': q['distractores'][i]} for i in range(len(q['opciones'])) if i != c and q['distractores'][i]]
    for no in enf['no']:
        if not re.search(r'\bpero\b', no['p'], re.I):
            no['p'] = 'Pero ' + no['p'][:1].lower() + no['p'][1:]

    wrong = [i for i in range(len(q['opciones'])) if i != c]
    for g_lvl, g in (h.get('guion') or {}).items():
        if g_lvl == '2':
            # ensure all wrong options have o:X:no and correct has o:c:ok
            new_g = [s for s in g if not (s.get('a', '').startswith('o:') and (s.get('a', '').endswith(':no') or s.get('a', '').endswith(':ok')))]
            for w in wrong:
                d_text = q['distractores'][w] if w < len(q['distractores']) and q['distractores'][w] else 'no corresponde a la información'
                new_g.append({'t': f'La opción {L[w]} no corresponde: {d_text}', 'a': f'o:{L[w]}:no', 'k': 'err'})
            new_g.append({'t': f'De este modo, confirmamos que la opción correcta es la {c_let}.', 'a': f'o:{c_let}:ok'})
            h['guion']['2'] = new_g
        elif g_lvl == '3':
            for s in g:
                if s.get('a', '').endswith(':ok'):
                    s['a'] = f'o:{c_let}:ok'

def fix_all():
    # 1. cfi-i006
    cfi_f = 'content/icfes/cfi/preguntas.json'
    cfi_data = json.load(open(cfi_f, 'r', encoding='utf-8'))
    for q in cfi_data['preguntas']:
        if q['id'] == 'cfi-i006':
            for i in range(len(q['distractores'])):
                if q['distractores'][i] and not re.search(r'\bpero\b', q['distractores'][i], re.I):
                    q['distractores'][i] = 'Pero ' + q['distractores'][i][:1].lower() + q['distractores'][i][1:]
            sync_hoja_guion(q)
        elif q['id'] == 'cfi-i085':
            for i in range(len(q['distractores'])):
                d = q['distractores'][i]
                d = re.sub(r'\bt([1-4])\b', r'{{t\1}}', d)
                q['distractores'][i] = d
            sync_hoja_guion(q)
            # fix in pasos/enfoque too
            if q.get('hoja'):
                s = json.dumps(q['hoja'], ensure_ascii=False)
                s = re.sub(r'\bt([1-4])\b', r'{{t\1}}', s)
                q['hoja'] = json.loads(s)
        elif q['id'] in ('cfi-i104', 'cfi-i106', 'cfi-i120'):
            sync_hoja_guion(q)

        # Fix bad marcas in cfi
        if q.get('hoja') and 'marcas' in q['hoja']:
            enun = q['enunciado']
            good_marcas = []
            for m in q['hoja']['marcas']:
                frag = m.get('frag', '')
                if frag in enun:
                    good_marcas.append(m)
                else:
                    # try to find a substring of frag that is in enun
                    words = frag.split()
                    sub = None
                    for w_len in range(len(words), 0, -1):
                        for start in range(len(words) - w_len + 1):
                            cand = " ".join(words[start:start+w_len]).rstrip(',.;:')
                            if len(cand) >= 4 and cand in enun:
                                sub = cand
                                break
                        if sub: break
                    if sub:
                        m['frag'] = sub
                        good_marcas.append(m)
            q['hoja']['marcas'] = good_marcas

    json.dump(cfi_data, open(cfi_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # 2. mth-i002
    mth_f = 'content/icfes/mth/preguntas.json'
    mth_data = json.load(open(mth_f, 'r', encoding='utf-8'))
    for q in mth_data['preguntas']:
        if q['id'] == 'mth-i002':
            for i in range(len(q['distractores'])):
                q['distractores'][i] = q['distractores'][i].replace('$=2.000$', 'equivalente a $2.000$').replace('=2.000', '2.000')
            sync_hoja_guion(q)
    json.dump(mth_data, open(mth_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # 3. mat-i017 and mat marcas
    mat_f = 'content/icfes/mat/preguntas.json'
    mat_data = json.load(open(mat_f, 'r', encoding='utf-8'))
    for q in mat_data['preguntas']:
        if q['id'] == 'mat-i017':
            for i in range(len(q['distractores'])):
                q['distractores'][i] = q['distractores'][i].replace('4lah', '{{4lah}}')
            sync_hoja_guion(q)
            if q.get('hoja'):
                s = json.dumps(q['hoja'], ensure_ascii=False).replace('4lah', '{{4lah}}')
                q['hoja'] = json.loads(s)
        # Fix marcas in mat
        if q.get('hoja') and 'marcas' in q['hoja']:
            enun = q['enunciado']
            good_marcas = []
            for m in q['hoja']['marcas']:
                frag = m.get('frag', '')
                if frag in enun:
                    good_marcas.append(m)
                else:
                    words = frag.split()
                    sub = None
                    for w_len in range(len(words), 0, -1):
                        for start in range(len(words) - w_len + 1):
                            cand = " ".join(words[start:start+w_len]).rstrip(',.;:')
                            if len(cand) >= 4 and cand in enun:
                                sub = cand
                                break
                        if sub: break
                    if sub:
                        m['frag'] = sub
                        good_marcas.append(m)
            q['hoja']['marcas'] = good_marcas
    json.dump(mat_data, open(mat_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # 4. soc and scc
    for pref in ['soc', 'scc']:
        sf = f'content/icfes/{pref}/preguntas.json'
        sdata = json.load(open(sf, 'r', encoding='utf-8'))
        qs = {q['id']: q for q in sdata['preguntas']}
        
        # soc-i007: correcta 0 (A)
        if f'{pref}-i007' in qs:
            qs[f'{pref}-i007']['correcta'] = 0
            sync_hoja_guion(qs[f'{pref}-i007'])
        # soc-i013: correcta 3 (D)
        if f'{pref}-i013' in qs:
            qs[f'{pref}-i013']['correcta'] = 3
            sync_hoja_guion(qs[f'{pref}-i013'])

        # soc-i010 (referendo) vs soc-i011 (iniciativa popular)
        if f'{pref}-i010' in qs and f'{pref}-i011' in qs:
            q10 = qs[f'{pref}-i010']
            q11 = qs[f'{pref}-i011']
            # q10 is about president and referendo -> correcta 0 (A: Sí, porque los referendos permiten reformar la Constitución)
            q10['correcta'] = 0
            q10['explicacion'] = "El referendo constitucional es uno de los mecanismos previstos en el Artículo 378 de la Constitución Política de Colombia para reformar la Carta Magna (mediante iniciativa del Gobierno o de los ciudadanos, tramitada en el Congreso y sometida a votación popular). Por tanto, la vía del referendo sí es un mecanismo institucionalmente viable de reforma constitucional (opción A)."
            q10['distractores'] = [
                "",
                "La Constitución sí puede reformarse por vía de referendo; no es exclusivo de una asamblea constituyente.",
                "El presidente no puede modificar la Constitución unilateralmente ni por decreto; requiere el mecanismo institucional del referendo.",
                "Los referendos constitucionales sí están expresamente diseñados para reformar la Constitución según el artículo 378."
            ]
            sync_hoja_guion(q10)

            # q11 is about ciudadano and iniciativa popular -> correcta 2 (C: inviable, porque se requiere 5% del censo electoral)
            q11['correcta'] = 2
            q11['explicacion'] = "La iniciativa popular legislativa y normativa (Art. 155 de la Constitución y Ley 134 de 1994) exige el respaldo de un número de ciudadanos equivalente a al menos el 5 % del censo electoral vigente. Al contar únicamente con la firma individual del ciudadano, la propuesta resulta jurídicamente inviable (opción C)."
            q11['distractores'] = [
                "Los ciudadanos sí pueden presentar proyectos de ley mediante iniciativa popular; el impedimento es no reunir las firmas mínimas del 5 % del censo.",
                "La iniciativa popular legislativa ciudadana se respalda con firmas de electores del censo electoral, no de concejales.",
                "",
                "La ley exige el 5 % del censo electoral vigente, no el 10 % de los votos de elecciones anteriores."
            ]
            sync_hoja_guion(q11)

        # soc-i018 (revoluciones orden cronologico) vs soc-i024 (conflicto armado paramilitar)
        if f'{pref}-i018' in qs and f'{pref}-i024' in qs:
            q18 = qs[f'{pref}-i018']
            q24 = qs[f'{pref}-i024']
            # q18: revoluciones -> correcta 1 (B: Mexicana 1910, Rusa 1917, Cubana 1959, Nicaraguense 1979)
            q18['correcta'] = 1
            q18['explicacion'] = "El orden cronológico correcto de las revoluciones sociales mencionadas es: Revolución mexicana (1910), Revolución rusa (1917), Revolución cubana (1959) y Revolución nicaragüense (1979). Por tanto, la secuencia adecuada corresponde a la opción B."
            q18['distractores'] = [
                "Ubica la Revolución nicaragüense (1979) antes de la Revolución rusa (1917) y mexicana (1910), alterando la cronología.",
                "",
                "Ubica la Revolución rusa (1917) antes de la Revolución mexicana (1910), invirtiendo su inicio histórico.",
                "Coloca la Revolución cubana (1959) antes de la Revolución rusa (1917) y mexicana (1910), desconociendo las fechas."
            ]
            sync_hoja_guion(q18)

            # q24: texto conflicto armado -> correcta 3 (D: un paramilitar)
            q24['correcta'] = 3
            q24['explicacion'] = "El fragmento justifica la existencia de grupos paramilitares o de autodefensa argumentando que surgieron como respuesta obligada ante la agresión guerrillera, perspectiva propia de un vocero o miembro paramilitar (opción D)."
            q24['distractores'] = [
                "Un empresario analizaría el impacto del conflicto sobre la inversión, la producción y los costos económicos.",
                "Un congresista enfatizaría la legislación, el debate democrático o las políticas institucionales del Estado.",
                "Un investigador mantendría una perspectiva neutral y analítica sin justificar el accionar de los grupos de autodefensa.",
                ""
            ]
            sync_hoja_guion(q24)

        # Fix bad marcas in soc and scc
        for q in sdata['preguntas']:
            if q.get('hoja') and 'marcas' in q['hoja']:
                enun = q['enunciado']
                good_marcas = []
                for m in q['hoja']['marcas']:
                    frag = m.get('frag', '')
                    if frag in enun:
                        good_marcas.append(m)
                    else:
                        words = frag.split()
                        sub = None
                        for w_len in range(len(words), 0, -1):
                            for start in range(len(words) - w_len + 1):
                                cand = " ".join(words[start:start+w_len]).rstrip(',.;:')
                                if len(cand) >= 4 and cand in enun:
                                    sub = cand
                                    break
                            if sub: break
                        if sub:
                            m['frag'] = sub
                            good_marcas.append(m)
                q['hoja']['marcas'] = good_marcas

        json.dump(sdata, open(sf, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # Sync corresponding individual hoja files in content/icfes/*/hojas/<id>.json
    for pref in ['cfi', 'mth', 'mat', 'soc', 'scc']:
        d = json.load(open(f'content/icfes/{pref}/preguntas.json', 'r', encoding='utf-8'))
        for q in d['preguntas']:
            h_path = f'content/icfes/{pref}/hojas/{q["id"]}.json'
            if os.path.exists(h_path) and q.get('hoja'):
                try:
                    hs = json.load(open(h_path, 'r', encoding='utf-8'))
                    hs['hoja'] = q['hoja']
                    json.dump(hs, open(h_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
                except Exception as ex:
                    pass

    print("ICFES fixes applied successfully.")

if __name__ == '__main__':
    fix_all()
