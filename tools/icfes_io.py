"""E/S compartida para scripts por lotes sobre content/icfes (preguntas + hojas sincronizadas)."""
import glob
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = "ABCDEFGH"


def dump(obj, path):
    with open(path, "w", encoding="utf8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def cuadernillos():
    return sorted(glob.glob(RAIZ + "/content/icfes/*/preguntas.json"))


def procesar(fn, solo=None):
    """fn(q, cuadernillo) -> True si modifico q. Guarda preguntas.json y hojas/<id>.json."""
    cambios = 0
    for f in cuadernillos():
        c = os.path.basename(os.path.dirname(f))
        d = json.load(open(f, encoding="utf8"))
        tocado = False
        for q in d["preguntas"]:
            if solo and q["id"] not in solo:
                continue
            if fn(q, c):
                tocado = True
                cambios += 1
                hp = os.path.join(os.path.dirname(f), "hojas", q["id"] + ".json")
                if os.path.exists(hp):
                    h = json.load(open(hp, encoding="utf8"))
                    h["hoja"] = q["hoja"]
                    if "estadoHoja" in q:
                        h["estado"] = q["estadoHoja"]
                    dump(h, hp)
        if tocado:
            dump(d, f)
    return cambios
