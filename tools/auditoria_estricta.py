#!/usr/bin/env python3
"""Revisor estricto del contenido ICFES y del banco propio.

Falla (exit 1) si encuentra: "Pendiente", campos vacios, razones con la misma
estructura, razones que repiten la explicacion, preguntas sin pistas/pasos/profe,
LaTeX roto, letras de opcion que contradicen la clave, sesgo de posicion o de largo.

Uso: python3 tools/auditoria_estricta.py [--json salida.json] [--max-fallas N]
"""
import collections
import difflib
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = "ABCDEFGH"
CLAIM = [
    re.compile(r"respuesta(?: correcta)? (?:es|ser[aá]) (?:la )?(?:opci[oó]n )?([A-H])\b"),
    re.compile(r"opci[oó]n ([A-H]) (?:se sostiene|satisface|es la correcta|es correcta|es la clave)"),
    re.compile(r"por qu[eé] la opci[oó]n ([A-H]) satisface"),
    re.compile(r"\(opci[oó]n ([A-H])\)"),
]
MULETILLAS = [
    "Pendiente",
    "Parece razonable si se omite",
    "Parece posible al mirar un dato aislado",
    "No coincide con la resoluci",
    "Explica comprender que",
    "No corresponde al fen",
    "Pero no responde al criterio central",
]


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def esqueleto(s):
    s = norm(s).lower()
    s = re.sub(r"[«\"“].*?[»\"”]", "#", s)
    s = re.sub(r"\b[a-e]\b", "#", s)
    s = re.sub(r"\d+([.,]\d+)?", "#", s)
    return s


def textos(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from textos(v)
    elif isinstance(o, list):
        for v in o:
            yield from textos(v)


def acciones(o):
    if isinstance(o, dict):
        a = o.get("a")
        if isinstance(a, str):
            yield a
        for v in o.values():
            yield from acciones(v)
    elif isinstance(o, list):
        for v in o:
            yield from acciones(v)


def latex_roto(s):
    f = []
    if re.search(r"\$[\\]?(rac|imes|heta|ext|au|ho|eq|ge|le)\b", s) and "\\" not in s:
        f.append("latex sin escapar")
    if re.search(r"[\t\x08\x0c\r\x07\x0b]", s):
        f.append("caracter de control (escape roto)")
    if s.count("$") % 2:
        f.append("$ sin cerrar")
    if re.search(r"\$rac|\$\s?imes|\bheta\b", s):
        f.append("comando LaTeX mutilado")
    return f


def cargar():
    out = []
    for f in sorted(glob.glob(RAIZ + "/content/icfes/*/preguntas.json")):
        c = os.path.basename(os.path.dirname(f))
        for q in json.load(open(f))["preguntas"]:
            out.append((c, q))
    return out


def cargar_propias():
    out = []
    for f in sorted(glob.glob(RAIZ + "/content/questions/*.json")):
        d = json.load(open(f))
        qs = d if isinstance(d, list) else d.get("preguntas", d.get("questions", []))
        for q in qs:
            out.append((os.path.basename(f)[:-5], q))
    return out


def revisar(c, q):
    fallas = []
    op = q.get("opciones", [])
    cor = q.get("correcta")
    ds = q.get("distractores", [])
    ex = norm(q.get("explicacion"))
    h = q.get("hoja") or {}
    enf = h.get("enfoque") or {}
    if not ex:
        fallas.append("explicacion vacia")
    for t in textos(q):
        for m in MULETILLAS:
            if m in t:
                fallas.append("muletilla: " + m)
                break
    razones = [norm(d) for i, d in enumerate(ds) if i != cor]
    if any(not r for r in razones):
        fallas.append("razon vacia")
    if len(ds) != len(op):
        fallas.append("distractores != opciones")
    # misma estructura entre razones propias
    sk = [esqueleto(r) for r in razones if r]
    for i in range(len(sk)):
        for j in range(i + 1, len(sk)):
            if difflib.SequenceMatcher(None, sk[i], sk[j]).ratio() > 0.82:
                fallas.append("razones casi iguales entre si")
                break
        else:
            continue
        break
    pref = collections.Counter(" ".join(r.split()[:3]).lower() for r in razones if r)
    if pref and max(pref.values()) >= 3 and len(razones) >= 3:
        fallas.append("razones con el mismo arranque")
    for r in razones:
        if r and ex and len(r) > 40 and difflib.SequenceMatcher(None, r, ex).ratio() > 0.8:
            fallas.append("razon repite la explicacion")
            break
    # flujo completo
    if not enf.get("pistas") or len(enf["pistas"]) < 2:
        fallas.append("sin pistas")
    if not h.get("pasos") or len(h["pasos"]) < 2:
        fallas.append("sin pasos")
    g = h.get("guion") or {}
    if not all(g.get(k) for k in ("1", "2", "3")):
        fallas.append("sin 3 niveles del profe")
    if not enf.get("no"):
        fallas.append("sin trampas")
    # latex
    for t in textos(q):
        fl = latex_roto(t)
        if fl:
            fallas.append("latex: " + fl[0])
            break
    # letras vs clave
    if isinstance(cor, int) and 0 <= cor < len(op):
        letra = L[cor]
        for t in textos({"e": q.get("explicacion"), "h": h}):
            bad = False
            for p in CLAIM:
                for m in p.finditer(t):
                    if m.group(1) != letra:
                        bad = True
            if bad:
                fallas.append("texto nombra opcion distinta a la clave")
                break
        for a in acciones(h):
            for part in a.split("|"):
                m = re.match(r"o:([A-H]):(ok|no)$", part)
                if m and ((m.group(2) == "ok") != (m.group(1) == letra)):
                    fallas.append("accion ok/no contradice la clave")
                    break
            else:
                continue
            break
    # trampas con letra: "Opcion X" debe ser distractor
    for n in enf.get("no") or []:
        m = re.match(r"Opci[oó]n ([A-H])$", n.get("t", ""))
        if m and isinstance(cor, int) and m.group(1) == L[cor]:
            fallas.append("trampa asignada a la opcion correcta")
            break
    if q.get("revisar"):
        fallas.append("marcada por revisar")
    return fallas


def sesgo(items, nombre):
    """Sesgo de posicion y de largo por grupo."""
    res = []
    items = [q for q in items if isinstance(q.get("correcta"), int) and 0 <= q["correcta"] < len(q.get("opciones", []))]
    n = len(items)
    if n < 12:
        return res
    cnt = collections.Counter(q["correcta"] for q in items)
    k = len(items[0]["opciones"])
    for i in range(k):
        p = cnt.get(i, 0) / n
        if p > 0.40 or p < 0.10:
            res.append(f"{nombre}: clave {L[i]} = {p:.0%}")
    larga = sum(
        1
        for q in items
        if len(q["opciones"][q["correcta"]]) == max(len(o) for o in q["opciones"])
    )
    if larga / n > 0.45:
        res.append(f"{nombre}: la clave es la mas larga en {larga}/{n}")
    return res


def main():
    salida = None
    maxf = 25
    if "--json" in sys.argv:
        salida = sys.argv[sys.argv.index("--json") + 1]
    if "--max-fallas" in sys.argv:
        maxf = int(sys.argv[sys.argv.index("--max-fallas") + 1])
    todas = cargar()
    malas = {}
    porc = collections.defaultdict(lambda: [0, 0])
    for c, q in todas:
        f = revisar(c, q)
        porc[c][1] += 1
        if f:
            malas[(c, q["id"])] = f
        else:
            porc[c][0] += 1
    print("=" * 70)
    print("REVISOR ESTRICTO ICFES")
    for c in sorted(porc):
        ok, t = porc[c]
        print(f"[{c:4}] {ok:3}/{t:3} limpias")
    print("-" * 70)
    tot = len(todas)
    print(f"TOTAL: {tot - len(malas)}/{tot} limpias | con fallas: {len(malas)}")
    tipos = collections.Counter(x for f in malas.values() for x in set(f))
    for t, v in tipos.most_common():
        print(f"  {v:4}  {t}")
    sesgos = []
    por_c = collections.defaultdict(list)
    for c, q in todas:
        por_c[c].append(q)
    for c, qs in por_c.items():
        sesgos += sesgo(qs, c)
    propias = collections.defaultdict(list)
    for c, q in cargar_propias():
        if "opciones" in q and isinstance(q.get("correcta"), int):
            propias[c].append(q)
    for c, qs in propias.items():
        sesgos += sesgo(qs, "propio/" + c)
    print("SESGOS:", len(sesgos))
    for s in sesgos:
        print("  ", s)
    for k, f in list(malas.items())[:maxf]:
        print("  ", k, "|", "; ".join(f))
    if salida:
        json.dump({"%s/%s" % k: v for k, v in malas.items()}, open(salida, "w"), ensure_ascii=False, indent=1)
    sys.exit(1 if malas or sesgos else 0)


if __name__ == "__main__":
    main()
