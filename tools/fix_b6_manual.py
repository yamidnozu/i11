#!/usr/bin/env python3
"""Bloque 6: ajustes manuales finales (mth-i008, cfi-i104)."""
import re, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from icfes_io import procesar
import fix_b1_guion_letras as b1
import fix_b2_basura_ingles as b2
from fix_b3_propagar import reemplazar

MAN = {"mth-i008": {
    0: "El 1 % de hombres con bajo peso corresponde a un IMC menor de 18,5; con 33,3 la persona está muy por encima de ese rango.",
    1: "El 50 % de hombres está en sobrepeso (25,0 a 29,9), pero un IMC de 33,3 ya superó ese intervalo.",
    2: "El 1 % con obesidad alta exige un IMC de 40 o más; 33,3 todavía no alcanza ese valor.",
}}

def fix(q, c):
    ch = False
    if q["id"] in MAN:
        old = list(q["distractores"])
        for k, r in MAN[q["id"]].items():
            q["distractores"][k] = r
        reemplazar(q["hoja"], [(a, b) for a, b in zip(old, q["distractores"]) if a != b])
        b2.resync_nivel2(q); b1.fix(q, c); ch = True
    if q["id"] == "cfi-i104":
        def rec(o):
            nonlocal ch
            it = o.items() if isinstance(o, dict) else enumerate(o)
            for k, v in list(it):
                if isinstance(v, str) and v.startswith("La opción G no encaja"):
                    o[k] = "La opción H no encaja: " + q["distractores"][7]; ch = True
                elif isinstance(v, (dict, list)): rec(v)
        rec(q["hoja"])
    return ch

if __name__ == "__main__":
    print(procesar(fix))
