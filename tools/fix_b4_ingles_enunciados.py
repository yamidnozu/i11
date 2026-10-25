#!/usr/bin/env python3
"""Bloque 4: enunciado con texto de otra pregunta, frases 'no encaja' en la hoja y mas variedad
de plantillas en razones de vocabulario."""
import re
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from icfes_io import L, procesar
from fix_b2_basura_ingles import VOC
import fix_b1_guion_letras as b1

CONECT = ["no tiene relación con ", "la pista habla de ", "no responde a ", "apunta a "]
PL8 = [
    "{{{{{w}}}}} significa {g} y {f}; no tiene relación con {t}.",
    "Con {{{{{w}}}}} ({g}) piensas en algo que {f}, pero la pista habla de {t}.",
    "{G} ({{{{{w}}}}}) {f}; por eso no responde a {t}.",
    "Confunde la pista: {{{{{w}}}}} {f}, mientras que la descripción apunta a {t}.",
    "Quien elige {{{{{w}}}}} recuerda que {f}, dato que no sirve para {t}.",
    "La palabra {{{{{w}}}}} ({g}) existe y {f}, pero la frase pide {t}.",
    "{{{{{w}}}}}: {g}. Eso {f}, lo cual no coincide con {t}.",
    "Descarta {{{{{w}}}}} porque {f}; el enunciado se refiere a {t}.",
]
VIEJA = re.compile(r"\{\{(\w+)\}\}")


def tail(d):
    for c in CONECT:
        if c in d:
            return d.rsplit(c, 1)[1].rstrip(".")
    return None


def fix(q, c):
    ch = False
    e = q["enunciado"]
    m = re.search(r"\?\s*\n\s*(Altitud|[A-D]\.)", e)
    if "Cuadernillo de preguntas" in e and q["id"] == "mat-i008":
        q["enunciado"] = e[: e.index("?") + 1]
        ch = True
    ds = q["distractores"]
    if q["id"][:3] in ("ing", "ena", "eng") or q["id"] in ("cfi-i104", "cfi-i106"):
        for k, d in enumerate(ds):
            if k == q["correcta"] or not d:
                continue
            w = VIEJA.search(d)
            t = tail(d)
            if w and t and w.group(1) in VOC and any(x in d for x in CONECT):
                g, f = VOC[w.group(1)]
                n = PL8[k % 8].format(w=w.group(1), g=g, G=g.capitalize(), f=f, t=t)
                if n != d:
                    ds[k] = n
                    ch = True
    # frases 'no encaja' en la hoja -> razon actual
    cor = q["correcta"]
    razon = {i: d for i, d in enumerate(ds) if i != cor and d}

    def rec(o):
        nonlocal ch
        items = o.items() if isinstance(o, dict) else enumerate(o)
        for k, v in list(items):
            if isinstance(v, str):
                m = re.match(r"^La opción ([A-H]) no encaja: ", v)
                if m and L.index(m.group(1)) in razon:
                    n = f"La opción {m.group(1)} no encaja: {razon[L.index(m.group(1))]}"
                    if n != v:
                        o[k] = n
                        ch = True
            elif isinstance(v, (dict, list)):
                rec(v)

    rec(q["hoja"])
    if ch:
        enf = q["hoja"].get("enfoque") or {}
        if enf.get("no") and len(razon) == len(q["opciones"]) - 1:
            enf["no"] = [{"t": f"Opción {L[i]}", "p": "Pero " + b1.minus(r)} for i, r in razon.items()]
        for st in q["hoja"].get("guion", {}).get("3", []):
            if st.get("t", "").startswith("Descarta las trampas"):
                st["t"] = "Descarta las trampas: " + " ".join(f"{L[i]}) {r}" for i, r in razon.items())
        for st in q["hoja"].get("guion", {}).get("2", []):
            mm = re.match(r"o:([A-H]):no$", st.get("a", ""))
            if mm and L.index(mm.group(1)) in razon and st.get("t", "").startswith("La opción"):
                st["t"] = f"La opción {mm.group(1)} es incorrecta: {razon[L.index(mm.group(1))]}"
    return ch


if __name__ == "__main__":
    print("preguntas modificadas:", procesar(fix))
