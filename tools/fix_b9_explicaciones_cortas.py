#!/usr/bin/env python3
"""Bloque 9: explicaciones de ing/eng/ena i038 e i039 ampliadas a 2 frases en espanol sencillo."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from icfes_io import procesar
from fix_b3_propagar import reemplazar

E38 = "«{{largest}}» es el superlativo de «large» y se usa para decir que este grupo es el más grande de todos. Como la frase empieza con «The» y no compara con otro grupo usando «than», no sirven «{{larger}}» ni «{{large}}»."
E39 = "«{{in}}» se usa para decir que algo está dentro de un lugar o de un área, como un parque nacional. «{{along}}» significa a lo largo de una línea y «{{on}}» significa encima de una superficie, por eso no encajan aquí."

def fix(q, c):
    if q["id"][:3] not in ("ing", "eng", "ena") or q["id"][3:] not in ("-i038", "-i039"):
        return False
    nuevo = E38 if q["id"].endswith("038") else E39
    old = q["explicacion"]
    q["explicacion"] = nuevo
    reemplazar(q["hoja"], [(old, nuevo)])
    return True

if __name__ == "__main__":
    print(procesar(fix))
