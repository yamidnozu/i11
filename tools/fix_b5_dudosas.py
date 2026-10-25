#!/usr/bin/env python3
"""Bloque 5: resuelve las dudosas verificables; las demas quedan marcadas y se informan."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from icfes_io import procesar

def fix(q, c):
    if q["id"] == "mat-i038":
        q["revisar"] = None
        if "Esto supone" not in q["explicacion"]:
            q["explicacion"] += " Esto supone que cada cliente pidió al menos un producto, como indica el registro de pedidos de los 110 clientes. Las otras opciones dependen de cuántos clientes combinaron pizza con bebida caliente o fría, dato que la tabla no separa: por eso no se pueden calcular."
        return True
    if q["id"] == "cfi-i101":
        q["revisar"] = None
        if "road" not in q["explicacion"]:
            q["explicacion"] += " Un avión (plane) y un barco (boat) no circulan por una vía donde otros conductores puedan leer el letrero; solo un autobús (bus) lo hace."
        return True
    return False

if __name__ == "__main__":
    print(procesar(fix))
