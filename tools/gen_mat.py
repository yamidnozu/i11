"""Generador del banco de Matemáticas (42 preguntas originales) con hojas, marcas, guiones y enfoques."""
import json
import re

def parse_num(t):
    pass

def make_q(id, evidencia, nivel, enunciado, opciones, correcta, explicacion, distractores,
           afirmacion, competencia, marcas, pasos, tema, que, pistas, clave, no_list, plan,
           g1, g2, g3, bloque=None, figuras=None):
    # Validations before assembling
    assert 0 <= correcta < len(opciones)
    assert len(distractores) == len(opciones)
    assert distractores[correcta] == ""
    for i, d in enumerate(distractores):
        if i != correcta:
            assert d != "", f"Distractor {i} vacío en {id}"
    assert len(no_list) >= 2
    for item in no_list:
        assert "Pero" in item["p"], f"Falta 'Pero' en enfoque.no de {id}: {item['p']}"
        bad = re.search(r"armo la regla|casos favorables|despejo|reemplazo en", item["p"], re.I)
        assert not bad, f"Frase prohibida en enfoque.no de {id}"
    assert len(pistas) >= 2
    assert len(plan) >= 3
    assert len(que) > 40, f"enfoque.que muy corto en {id}: {len(que)} chars"
    assert any(p.get("k") == "check" for p in pasos), f"Falta paso check en {id}"
    assert len(pasos) >= 2

    # Check non-overlapping marcas
    ranges = []
    for m in marcas:
        idx = enunciado.find(m["frag"])
        assert idx >= 0, f"Marca '{m['frag']}' no encontrada en enunciado de {id}"
        end = idx + len(m["frag"])
        ranges.append((idx, end, m["frag"]))
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            a, b, f1 = ranges[i]
            c, d, f2 = ranges[j]
            assert not (a < d and c < b), f"Marcas solapadas en {id}: '{f1}' y '{f2}'"

    # Check guion level 2 option elimination
    incorrectas = [chr(65 + i) for i in range(len(opciones)) if i != correcta]
    g2_actions = " ".join([b.get("a", "") for b in g2])
    for inc in incorrectas:
        assert f"o:{inc}:no" in g2_actions, f"Falta descarte o:{inc}:no en guion 2 de {id}"

    hoja = {
        "modo": "calculo",
        "marcas": marcas,
        "pasos": pasos,
        "enfoque": {
            "tema": tema,
            "que": que,
            "pistas": pistas,
            "clave": clave,
            "no": no_list,
            "plan": plan
        },
        "guion": {
            "1": g1,
            "2": g2,
            "3": g3
        }
    }

    q = {
        "id": id,
        "area": "matematicas",
        "evidencia": evidencia,
        "nivel": nivel,
        "enunciado": enunciado,
        "opciones": opciones,
        "correcta": correcta,
        "explicacion": explicacion,
        "distractores": distractores,
        "origen": "original",
        "afirmacion": afirmacion,
        "competencia": competencia,
        "hoja": hoja
    }
    if bloque:
        q["bloque"] = bloque
    if figuras:
        q["figuras"] = figuras
    return q

print("Helper cargado correctamente")
