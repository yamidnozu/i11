"""
Equilibra claves (10 A, 10 B, 10 C, 9 D) y genera hojas pedagógicas interactivas
para las 40 preguntas de Ciencias Naturales (content/questions/ciencias.json).
"""
import json
from tools.gen_area_hojas import build_hoja_for_question

def balance_ciencias():
    cie = json.load(open('content/questions/ciencias.json', 'r', encoding='utf-8'))
    hojas = json.load(open('content/hojas.json', 'r', encoding='utf-8'))
    guiones = json.load(open('content/guiones.json', 'r', encoding='utf-8'))
    enfoques = json.load(open('content/enfoques.json', 'r', encoding='utf-8'))

    # cie-001..009 have 8 MC (6 B, 1 C) + 1 reto (cie-007)
    # Remaining 31 MC questions (cie-010 to cie-040):
    # 10 A, 4 B, 9 C, 9 D (Total: 31)
    target_keys = (
        [0] * 10 + # 10 A (cie-010 to cie-019)
        [1] * 4  + # 4 B  (cie-020 to cie-023)
        [2] * 9  + # 9 C  (cie-024 to cie-032)
        [3] * 9    # 9 D  (cie-033 to cie-040, excluding reto which was 007)
    )

    t_idx = 0
    for i in range(len(cie)):
        q = cie[i]
        qid = q['id']
        if q.get('tipo') == 'reto':
            continue
        
        idx = int(qid.split('-')[1])
        if idx <= 9:
            # Original questions keep their handmade hoja and key
            continue

        target_c = target_keys[t_idx]
        t_idx += 1

        curr_c = q['correcta']
        if curr_c != target_c:
            q['opciones'][curr_c], q['opciones'][target_c] = q['opciones'][target_c], q['opciones'][curr_c]
            q['distractores'][curr_c], q['distractores'][target_c] = q['distractores'][target_c], q['distractores'][curr_c]
            q['correcta'] = target_c

        # Build complete hoja
        h = build_hoja_for_question(q)
        q['hoja'] = h
        hojas[qid] = {'modo': h['modo'], 'marcas': [], 'pasos': h['pasos']}
        guiones[qid] = h['guion']
        enfoques[qid] = h['enfoque']

    json.dump(cie, open('content/questions/ciencias.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(hojas, open('content/hojas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(guiones, open('content/guiones.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(enfoques, open('content/enfoques.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print("Ciencias balanced and hojas generated successfully.")

if __name__ == '__main__':
    balance_ciencias()
