#!/usr/bin/env python3
"""Bloque 7: repara \\comando{{x}} (llaves duplicadas por error) y el campo 'que' sin cifras."""
import re, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from icfes_io import procesar

ROTO = re.compile(r"(\\[A-Za-z]+)\{\{([^{}]*)\}\}")
def arreglar(s):
    return ROTO.sub(lambda m: m.group(1) + "{" + m.group(2) + "}", s)

def rec(o):
    ch = False
    it = o.items() if isinstance(o, dict) else enumerate(o)
    for k, v in list(it):
        if isinstance(v, str):
            n = arreglar(v)
            if n != v: o[k] = n; ch = True
        elif isinstance(v, (dict, list)):
            ch |= rec(v)
    return ch

def fix(q, c):
    ch = rec(q)
    enf = (q.get("hoja") or {}).get("enfoque") or {}
    qq = enf.get("que", "")
    if qq.startswith("Responde: ") and re.search(r"[\d$\\]", qq):
        enf["que"] = "Responde la pregunta final del enunciado usando solo lo que muestran los datos y las observaciones."
        ch = True
    return ch

if __name__ == "__main__":
    print(procesar(fix))
