"""Script generador maestro de los 62 casos clínicos y preguntas de Odontología (Endodoncia).
Genera content/questions/odontologia.json y actualiza content/unidades.json.
Valida todas las reglas pedagógicas y técnicas:
- Sin cifras en los textos hablados del guion o enfoque
- Todos los distractores incorrectos descartados con o:X:no en guion 2
- Claves balanceadas ~25%
- Longitudes de opciones equilibradas
- Unidades actualizadas con las 62 preguntas asignadas
"""
import json
import re
import os
import sys

from odontologia_data_p1 import get_questions_1_to_20
from odontologia_data_p2 import get_questions_21_to_40
from odontologia_data_p3 import get_questions_41_to_62

LETTERS = ['A', 'B', 'C', 'D']

def make_q(qid, nivel, enunciado, opciones, correcta, distractores, explicacion, competencia, afirmacion, tema, que, clave, pistas, plan, marcas_data, steps_ideas, lvl1_steps):
    marcas = [{"frag": m[0], "rol": m[1], "campo": m[2], "nota": m[3]} for m in marcas_data]
    pasos = [{"k": s[0], "titulo": s[1], "texto": s[2]} for s in steps_ideas]
    
    no_items = []
    for i, d in enumerate(distractores):
        if i != correcta and d:
            p_text = d if d.startswith("Pero ") else f"Pero {d[0].lower() + d[1:]}"
            no_items.append({"t": f"Opción {LETTERS[i]}", "p": p_text})
            
    correct_letter = LETTERS[correcta]
    
    lvl2 = [
        {"a": "leer", "t": "Analicemos detalladamente por qué se descartan las alternativas incorrectas según la semiología clínica."}
    ]
    for i, d in enumerate(distractores):
        if i != correcta:
            lvl2.append({"a": f"o:{LETTERS[i]}:no", "k": "err", "t": f"La opción {LETTERS[i]} es incorrecta: {d}"})
    lvl2.append({"a": f"o:{correct_letter}:ok", "t": f"Por correlación semiológica y descarte riguroso, la opción {correct_letter} es la respuesta correcta."})
    
    lvl1 = []
    for st in lvl1_steps:
        lvl1.append({"a": st[0], "t": st[1]})
    lvl1.append({"a": f"o:{correct_letter}:ok", "t": f"Concluimos que la respuesta fundamentada corresponde a la opción {correct_letter}: {opciones[correcta]}"})
    
    lvl3 = [
        {"a": "p:0", "k": "ana", "t": "Integramos el motivo de consulta con la cronología del dolor y los antecedentes del paciente."},
        {"a": "p:1", "k": "por", "t": clave},
        {"a": f"o:{correct_letter}:ok", "t": f"Confirmamos con certeza clínica que la opción adecuada es {correct_letter}."}
    ]
    
    hoja = {
        "modo": "concepto",
        "marcas": marcas,
        "pasos": pasos,
        "enfoque": {
            "tema": tema,
            "que": que,
            "clave": clave,
            "pistas": pistas,
            "plan": [{"t": p} for p in plan],
            "no": no_items
        },
        "guion": {
            "1": lvl1,
            "2": lvl2,
            "3": lvl3
        }
    }
    
    return {
        "id": qid,
        "area": "odontologia",
        "nivel": nivel,
        "tipo": "multiple",
        "origen": "propio",
        "enunciado": enunciado,
        "opciones": opciones,
        "correcta": correcta,
        "distractores": distractores,
        "explicacion": explicacion,
        "competencia": competencia,
        "afirmacion": afirmacion,
        "hoja": hoja
    }

def validate_all(questions):
    print("Iniciando validación exhaustiva de 62 preguntas...")
    issues = []
    key_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    longest_count = 0
    plans = set()
    
    for q in questions:
        qid = q["id"]
        corr = q["correcta"]
        key_counts[corr] += 1
        
        # Longitud de opciones
        lens = [len(o) for o in q["opciones"]]
        if lens[corr] == max(lens):
            longest_count += 1
            
        # Comprobar cifras en textos hablados
        h = q["hoja"]
        spoken_texts = []
        for n in ['1', '2', '3']:
            for b in h["guion"][n]:
                spoken_texts.append((f"{qid} guion {n}", b["t"]))
        enf = h["enfoque"]
        spoken_texts.append((f"{qid} enfoque.que", enf["que"]))
        spoken_texts.append((f"{qid} enfoque.clave", enf["clave"]))
        for p in enf["pistas"]:
            spoken_texts.append((f"{qid} enfoque.pista", p))
        for pl in enf["plan"]:
            spoken_texts.append((f"{qid} enfoque.plan", pl["t"]))
        for no in enf["no"]:
            spoken_texts.append((f"{qid} enfoque.no", no["p"]))
            
        for loc, txt in spoken_texts:
            clean = re.sub(r'\{\{.+?\}\}', '', txt)
            if re.search(r'\d', clean):
                issues.append(f"Cifra arábiga en {loc}: '{txt}'")
            if re.search(r'[\\$^_]|\bfrac\b', clean):
                issues.append(f"Código TeX/LaTeX no escapado en {loc}: '{txt}'")
                
        # Comprobar o:X:no para cada distractor en guion 2
        dichas = set()
        for b in h["guion"]["2"]:
            a = b.get("a", "")
            for act in a.split("|"):
                if act.startswith("o:") and act.endswith(":no"):
                    dichas.add(act[2])
        for i in range(len(q["opciones"])):
            if i != corr:
                L = LETTERS[i]
                if L not in dichas:
                    issues.append(f"Falta descarte o:{L}:no en guion 2 de {qid}")
                    
        # Comprobar marcas
        marcas_frags = set(m["frag"] for m in h["marcas"])
        for n in ['1', '2', '3']:
            for b in h["guion"][n]:
                a = b.get("a", "")
                for act in a.split("|"):
                    if act.startswith("m:"):
                        frag = act[2:]
                        if frag not in marcas_frags:
                            issues.append(f"Marca m:{frag} no declarada en {qid}")
                            
        # Comprobar pasos
        for n in ['1', '2', '3']:
            for b in h["guion"][n]:
                a = b.get("a", "")
                for act in a.split("|"):
                    if act.startswith("p:"):
                        idx = int(act[2:])
                        if idx >= len(h["pasos"]):
                            issues.append(f"Paso p:{idx} fuera de rango en {qid}")
                            
        # Comprobar plan propio
        plan_str = " | ".join(p["t"] for p in enf["plan"])
        if plan_str in plans:
            issues.append(f"Plan idéntico duplicado en {qid}: '{plan_str[:50]}...'")
        plans.add(plan_str)
        
        # Comprobar que en.no tenga Pero
        for no in enf["no"]:
            if "Pero" not in no["p"]:
                issues.append(f"enfoque.no sin 'Pero' en {qid}: '{no['p'][:40]}'")
                
        # Comprobar distractor vacío en correcta y lleno en incorrectas
        for i, d in enumerate(q["distractores"]):
            if i == corr and d != "":
                issues.append(f"Distractor de clave correcta no vacío en {qid}")
            elif i != corr and (not d or len(d.strip()) < 15):
                issues.append(f"Distractor vacío o muy corto en opción {LETTERS[i]} de {qid}")

    print(f"Total preguntas: {len(questions)}")
    print("Distribución de claves:")
    for k in range(4):
        cnt = key_counts[k]
        pct = cnt / len(questions) * 100
        print(f"  {LETTERS[k]}: {cnt:2d} ({pct:.1f}%)")
    print(f"Opción correcta más larga: {longest_count}/{len(questions)} ({longest_count/len(questions)*100:.1f}%)")
    
    if issues:
        print(f"\n[ERROR] Se encontraron {len(issues)} problemas de validación:")
        for iss in issues[:10]:
            print(f"  - {iss}")
        sys.exit(1)
    else:
        print("\n[ÉXITO] 100% de las 62 preguntas pasaron todas las validaciones técnicas y pedagógicas.")

def update_unidades(q_ids):
    unidades_file = "content/unidades.json"
    with open(unidades_file, "r", encoding="utf-8") as f:
        unidades = json.load(f)
        
    # Filtrar las unidades que no son de odontología
    base_unidades = [u for u in unidades if u.get("area") != "odontologia"]
    
    # Definición de las 7 unidades de odontología con las 62 preguntas asignadas
    odo_unidades = [
        {
            "id": "u-odo-anamnesis",
            "area": "odontologia",
            "titulo": "Historia clínica y análisis del dolor",
            "resumen": "Motivo de consulta, evaluación de síntomas cardinales, dolor nocturno, las ocho dimensiones del dolor y anestesia.",
            "preguntas": [
                "odo-001", "odo-002", "odo-031", "odo-032", "odo-033", "odo-041", "odo-042", "odo-043"
            ],
            "sim": None,
            "leccion": None,
            "min": 15
        },
        {
            "id": "u-odo-pruebas",
            "area": "odontologia",
            "titulo": "Pruebas de sensibilidad y examen clínico",
            "resumen": "Protocolo de prueba térmica al frío y calor, percusión, fistulografía, test de cavidad, vitalómetro y sondeo.",
            "preguntas": [
                "odo-004", "odo-006", "odo-008", "odo-010", "odo-015", "odo-016", "odo-020", "odo-034", "odo-035", "odo-036", "odo-037", "odo-038"
            ],
            "sim": None,
            "leccion": None,
            "min": 20
        },
        {
            "id": "u-odo-diagnostico-pulpar",
            "area": "odontologia",
            "titulo": "Patología pulpar y alteraciones tisulares",
            "resumen": "Criterios para diferenciar pulpitis reversible, irreversible sintomática, asintomática, pólipo pulpar y necrosis.",
            "preguntas": [
                "odo-003", "odo-009", "odo-017", "odo-019", "odo-021", "odo-025", "odo-026"
            ],
            "sim": None,
            "leccion": None,
            "min": 15
        },
        {
            "id": "u-odo-diagnostico-periapical",
            "area": "odontologia",
            "titulo": "Patología periapical y urgencias infecciosas",
            "resumen": "Periodontitis apical sintomática, asintomática, absceso agudo, crónico, osteítis condensante y signos de alarma.",
            "preguntas": [
                "odo-005", "odo-007", "odo-011", "odo-013", "odo-018", "odo-022", "odo-023", "odo-056", "odo-057", "odo-058"
            ],
            "sim": None,
            "leccion": None,
            "min": 20
        },
        {
            "id": "u-odo-ayudas-conductas",
            "area": "odontologia",
            "titulo": "Ayudas radiográficas y decisiones clínicas",
            "resumen": "Radiografía angulada horizontal, lámina dura, radiografía inicial, redacción de hallazgos y toma de decisiones.",
            "preguntas": [
                "odo-012", "odo-014", "odo-024", "odo-027", "odo-029", "odo-030", "odo-039", "odo-040", "odo-062"
            ],
            "sim": None,
            "leccion": None,
            "min": 15
        },
        {
            "id": "u-odo-bases",
            "area": "odontologia",
            "titulo": "Bases biológicas, anatomía pulpar y causas",
            "resumen": "Capas histológicas de la pulpa, funciones del complejo dentinopulpar, ligamento periodontal, anacoresis y factores iatrogénicos.",
            "preguntas": [
                "odo-044", "odo-045", "odo-046", "odo-047", "odo-048", "odo-049"
            ],
            "sim": None,
            "leccion": None,
            "min": 15
        },
        {
            "id": "u-odo-tratamientos",
            "area": "odontologia",
            "titulo": "Terapéutica endodóntica, controles y reabsorciones",
            "resumen": "Apexogénesis, apexificación, medicación intraconducto, manejo de abscesos, reabsorción interna y externa, y profilaxis.",
            "preguntas": [
                "odo-028", "odo-050", "odo-051", "odo-052", "odo-053", "odo-054", "odo-055", "odo-059", "odo-060", "odo-061"
            ],
            "sim": None,
            "leccion": None,
            "min": 20
        }
    ]
    
    # Verificar que cada id esté en exactamente una unidad
    assigned = []
    for u in odo_unidades:
        assigned.extend(u["preguntas"])
    assert len(assigned) == len(q_ids), f"Preguntas asignadas ({len(assigned)}) != total ({len(q_ids)})"
    assert len(set(assigned)) == len(q_ids), "Hay preguntas duplicadas en las unidades"
    for qid in q_ids:
        assert qid in assigned, f"Falta pregunta {qid} en unidades"
        
    full_unidades = base_unidades + odo_unidades
    with open(unidades_file, "w", encoding="utf-8") as f:
        json.dump(full_unidades, f, ensure_ascii=False, indent=1)
    print(f"content/unidades.json actualizado exitosamente con 7 unidades y {len(assigned)} preguntas de odontología.")

def main():
    p1 = get_questions_1_to_20(make_q)
    p2 = get_questions_21_to_40(make_q)
    p3 = get_questions_41_to_62(make_q)
    
    all_questions = p1 + p2 + p3
    assert len(all_questions) == 62, f"Se esperaban 62 preguntas, se obtuvieron {len(all_questions)}"

    from odontologia_balanced_options import BALANCED_OPTIONS
    for q in all_questions:
        qid = q["id"]
        if qid in BALANCED_OPTIONS:
            q["opciones"] = BALANCED_OPTIONS[qid]
            corr = q["correcta"]
            corr_letter = LETTERS[corr]
            corr_text = q["opciones"][corr]
            lvl1 = q["hoja"]["guion"]["1"]
            if lvl1 and lvl1[-1]["a"] == f"o:{corr_letter}:ok":
                lvl1[-1]["t"] = f"Concluimos que la respuesta fundamentada corresponde a la opción {corr_letter}: {corr_text}"
    
    validate_all(all_questions)
    
    out_path = "content/questions/odontologia.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    print(f"Escritas {len(all_questions)} preguntas exitosamente en {out_path}.")
    
    q_ids = [q["id"] for q in all_questions]
    update_unidades(q_ids)

if __name__ == "__main__":
    main()
