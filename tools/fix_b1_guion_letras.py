#!/usr/bin/env python3
"""Bloque 1: coherencia letra/clave en hojas + reescritura del nivel 2/3 del profe y de las
trampas usando las razones reales de q['distractores'] (en vez de plantillas)."""
import re
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from icfes_io import L, procesar

CLAIM = [
    re.compile(r"(respuesta(?: correcta)? (?:es|ser[aá]) (?:la )?(?:opci[oó]n )?)([A-H])\b"),
    re.compile(r"(opci[oó]n )([A-H])( (?:se sostiene|satisface|es la correcta|es correcta|es la clave))"),
    re.compile(r"(por qu[eé] la opci[oó]n )([A-H])( satisface)"),
    re.compile(r"(\(opci[oó]n )([A-H])(\))"),
]
PLANT = ("criterio central", "Parece razonable si se", "plantea «")


def fix_text(t, letra):
    for p in CLAIM:
        if p.groups == 2:
            t = p.sub(lambda m: m.group(1) + letra, t)
        else:
            t = p.sub(lambda m: m.group(1) + letra + m.group(3), t)
    return t


def fix_action(a, letra):
    out = []
    for part in a.split("|"):
        m = re.match(r"o:([A-H]):(ok|no)$", part)
        if m:
            if m.group(2) == "ok":
                part = f"o:{letra}:ok"
            elif m.group(1) == letra:
                continue
        if part not in out:
            out.append(part)
    return "|".join(out)


def walk(o, letra):
    ch = False
    if isinstance(o, dict):
        for k, v in list(o.items()):
            if isinstance(v, str):
                n = fix_action(v, letra) if k == "a" else fix_text(v, letra)
                if n != v:
                    o[k] = n
                    ch = True
            else:
                ch |= walk(v, letra)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str):
                n = fix_text(v, letra)
                if n != v:
                    o[i] = n
                    ch = True
            else:
                ch |= walk(v, letra)
    return ch


def minus(s):
    s = s.strip()
    return s[:1].lower() + s[1:] if s else s


def fix(q, c):
    cor = q.get("correcta")
    if not isinstance(cor, int) or cor >= len(q["opciones"]):
        return False
    letra = L[cor]
    h = q.get("hoja") or {}
    ch = walk(h, letra)
    if isinstance(q.get("explicacion"), str):
        n = fix_text(q["explicacion"], letra)
        if n != q["explicacion"]:
            q["explicacion"] = n
            ch = True
    ds = q.get("distractores", [])
    razon = {i: d.strip() for i, d in enumerate(ds) if i != cor and d and d.strip()}
    enf = h.get("enfoque") or {}
    # trampas alineadas con las razones reales
    if enf.get("no") and len(razon) == len(q["opciones"]) - 1:
        nuevo = [{"t": f"Opción {L[i]}", "p": "Pero " + minus(r)} for i, r in razon.items()]
        if nuevo != enf["no"]:
            enf["no"] = nuevo
            ch = True
    g = h.get("guion") or {}
    # nivel 2: razon por opcion
    for st in g.get("2", []):
        m = re.match(r"o:([A-H]):no$", st.get("a", ""))
        if m and any(p in st.get("t", "") for p in PLANT):
            i = L.index(m.group(1))
            if i in razon:
                st["t"] = f"La opción {m.group(1)} es incorrecta: {razon[i]}"
                ch = True
    # nivel 3: descarte especifico
    for st in g.get("3", []):
        if st.get("t", "").startswith("Revisa las otras alternativas") and len(razon) >= 2:
            st["t"] = "Descarta las trampas: " + " ".join(
                f"{L[i]}) {r}" for i, r in razon.items()
            )
            ch = True
    return ch


if __name__ == "__main__":
    print("preguntas modificadas:", procesar(fix))
