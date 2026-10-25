#!/usr/bin/env python3
"""Bloque 3: corrige llaves {{palabra}}, quita la muletilla 'Pero revisa el dato...' de las razones
y propaga a toda la hoja (trampas, profe, pasos) cualquier razon cambiada respecto a HEAD."""
import json
import re
import subprocess
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from icfes_io import procesar, RAIZ

LLAVE = re.compile(r"(?<![\\\w{])\{(\w+)\}(?!\})")
COLA = re.compile(r"\s*Pero revisa el dato que exige el enunciado\.?")


def minus(s):
    return s[:1].lower() + s[1:] if s else s


def cargar_head():
    old = {}
    ls = subprocess.run(["git", "ls-files", "content/icfes/*/preguntas.json"], cwd=RAIZ, capture_output=True, text=True).stdout.split()
    for f in ls:
        s = subprocess.run(["git", "show", "HEAD:" + f], cwd=RAIZ, capture_output=True, text=True).stdout
        for q in json.loads(s)["preguntas"]:
            old[q["id"]] = q["distractores"]
    return old


def reemplazar(o, pares):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str):
                for a, b in pares:
                    if a in v:
                        v = v.replace(a, b)
                o[k] = v
            else:
                reemplazar(v, pares)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str):
                for a, b in pares:
                    if a in v:
                        v = v.replace(a, b)
                o[i] = v
            else:
                reemplazar(v, pares)


OLD = cargar_head()


def fix(q, c):
    ds = q["distractores"]
    nd = [COLA.sub("", LLAVE.sub(r"{{\1}}", d)).strip() if d else d for d in ds]
    od = OLD.get(q["id"], ds)
    if nd == od:
        return False
    q["distractores"] = nd
    pares = []
    for a, b in zip(od, nd):
        if a and b and a != b:
            pares.append((a, b))
            pares.append((minus(a), minus(b)))
            # variante con llaves simples ya escrita en hoja por el bloque 2
            pares.append((LLAVE.sub(r"{{\1}}", a), b))
    pares.sort(key=lambda p: -len(p[0]))
    reemplazar(q["hoja"], pares)
    return True


if __name__ == "__main__":
    print("preguntas modificadas:", procesar(fix))
