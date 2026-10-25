#!/usr/bin/env python3
"""Bloque 8: razones alineadas con su opcion en scc-i010, cfi-i008 (comparado con f84265f)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from icfes_io import procesar
import fix_b1_guion_letras as b1
import fix_b2_basura_ingles as b2
from fix_b3_propagar import reemplazar, minus

MAN = {
 "scc-i010": {
  0: "Acierta en que es inviable, pero se equivoca en el motivo: el ciudadano sí tiene la facultad de la iniciativa popular; lo que no puede es presentarla solo, necesita el respaldo del 5 % del censo electoral.",
  1: "Dice que es viable porque basta un ciudadano; sin el 5 % del censo electoral que respalde la propuesta no se puede radicar.",
 },
 "cfi-i008": {
  0: "Intercambia las coordenadas de los puntos correctos: pone la altura donde va la abscisa y rompe la simetría del trapecio respecto al eje Y.",
  2: "Intercambia x e y de los vértices dados y cambia el signo de x; confunde los ejes en lugar de reflejar solo la abscisa.",
 },
}

def fix(q, c):
    m = MAN.get(q["id"])
    if not m:
        return False
    old = list(q["distractores"])
    for k, r in m.items():
        q["distractores"][k] = r
    pares = []
    for a, b in zip(old, q["distractores"]):
        if a != b:
            pares += [(a, b), (minus(a), minus(b))]
    reemplazar(q["hoja"], pares)
    b2.resync_nivel2(q); b1.fix(q, c)
    # frases tipo 'La opcion X: razon' del paso por opcion
    import re
    from icfes_io import L
    razon = {i: d for i, d in enumerate(q["distractores"]) if i != q["correcta"] and d}
    def rec(o):
        it = o.items() if isinstance(o, dict) else enumerate(o)
        for k, v in list(it):
            if isinstance(v, str):
                mm = re.match(r"^La opción ([A-H]): ", v)
                if mm and L.index(mm.group(1)) in razon:
                    o[k] = f"La opción {mm.group(1)}: {razon[L.index(mm.group(1))]}"
            elif isinstance(v, (dict, list)): rec(v)
    rec(q["hoja"])
    return True

if __name__ == "__main__":
    print(procesar(fix))
