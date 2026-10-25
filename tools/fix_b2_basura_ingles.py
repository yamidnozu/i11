#!/usr/bin/env python3
"""Bloque 2: limpieza de texto basura del PDF, razones especificas de ingles/vocabulario y
reescrituras manuales, campo 'que' generico de las explicaciones de catalogo."""
import re
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from icfes_io import L, procesar
import fix_b1_guion_letras as b1

BASURA = re.compile(r"\s*\n+\s*RESPOND[AE]\b.*$", re.S)

VOC = {
    "glasses": ("gafas", "se llevan sobre los ojos"),
    "handbags": ("bolsos", "sirven para guardar y cargar objetos"),
    "hat": ("sombrero", "se pone en la cabeza"),
    "pajamas": ("pijama", "es la ropa con la que se duerme"),
    "scarf": ("bufanda", "se enrolla alrededor del cuello"),
    "skirt": ("falda", "es una prenda que cubre desde la cintura hacia abajo"),
    "socks": ("medias", "se ponen dentro del zapato"),
    "watch": ("reloj", "se lleva en la muñeca para ver la hora"),
    "ambulance": ("ambulancia", "lleva pacientes al hospital"),
    "boat": ("bote", "se desplaza sobre el agua"),
    "bike": ("bicicleta", "se mueve pedaleando"),
    "bus": ("bus", "lleva pasajeros por carretera"),
    "motorbike": ("moto", "se conduce con motor por carretera"),
    "plane": ("avión", "vuela por el aire"),
    "train": ("tren", "circula sobre rieles"),
    "truck": ("camión", "carga mercancía pesada por carretera"),
}
R1 = re.compile(r"^\{\{(\w+)\}\} significa [^;]+; esa palabra no corresponde a (.+)\.$")
R2 = re.compile(r"^\{\{(\w+)\}\} .+?, pero esa característica no corresponde a (.+)\.$")
PLANTILLAS = [
    "{{{w}}} significa {g} y {f}; no tiene relación con {t}.",
    "Con {{{w}}} ({g}) piensas en algo que {f}, pero la pista habla de {t}.",
    "{G} ({{{w}}}) {f}; por eso no responde a {t}.",
    "Confunde la pista: {{{w}}} {f}, mientras que la descripción apunta a {t}.",
]

MANUAL = {
    "cfi-i044": {
        0: "Los peatones son el 22 %, un grupo grande, pero queda por debajo del 50 % que reúnen los ocupantes de otros vehículos.",
        1: "Los motociclistas (23 %) son la segunda categoría, aun así quedan lejos de la mitad que corresponde a otro vehículo.",
        2: "Los ciclistas apenas aportan el 5 %: son el grupo menos probable de los cuatro.",
    },
    "cfi-i122": {
        0: "«Where» pregunta por un lugar; la oración habla de la razón por la que se intercambian regalos, no de un sitio.",
        2: "«When» pregunta por el momento; el texto ya dice que es en el día de San Valentín, así que no es lo que se cuestiona.",
        3: "«What» pediría el objeto de la acción, pero «do this» ya nombra la acción; lo que falta es preguntar el motivo.",
    },
    "cfi-i123": {
        0: "«Essays» son ensayos argumentativos; la frase presenta una leyenda tradicional sobre San Valentín, no un ensayo.",
        2: "«Reports» son informes con datos verificados; la historia de un sacerdote es una narración, no un informe.",
        3: "«Letters» son cartas; nada en el texto indica que el relato provenga de cartas.",
    },
    "cfi-i124": {
        0: "«Find off» no existe como verbo compuesto en inglés; descubrir un secreto exige «find out».",
        1: "«Find in» sugiere hallar algo dentro de un lugar, pero aquí el rey descubre un secreto: «find out».",
        2: "«Find at» no forma un phrasal verb con el sentido de descubrir.",
    },
    "cfi-i125": {
        1: "«Only» (solamente) resta importancia a la cifra, pero el 90 % es una proporción muy alta.",
        2: "«Hardly» significa casi nada: diría que las mujeres compran muy pocas tarjetas, lo contrario de un 90 %.",
        3: "«Just 90 %» expresa exactitud o poca cantidad; la idea de la frase es una cifra cercana al 90 %, que pide «almost».",
    },
    "mat-i006": {
        0: "Dos cursos del módulo I cuestan $2.800.000, más del triple de los $900.000 que pagó la empresa.",
        1: "En el módulo II dos cursos suman $1.800.000, el doble de lo pagado.",
        2: "El módulo III costaría $3.200.000 con dos cursos, una cifra muy superior al pago.",
    },
    "mth-i006": {
        0: "Dos cursos del módulo I cuestan $2.800.000, más del triple de los $900.000 que pagó la empresa.",
        1: "En el módulo II dos cursos suman $1.800.000, el doble de lo pagado.",
        2: "El módulo III costaría $3.200.000 con dos cursos, una cifra muy superior al pago.",
    },
}


def ultima_pregunta(enun):
    fr = [s.strip() for s in re.split(r"(?<=[?])\s+", enun.strip()) if s.strip().endswith("?")]
    if fr:
        return fr[-1][-220:]
    return enun.strip().split("\n")[-1][-200:]


def resync_nivel2(q):
    cor = q["correcta"]
    razon = {i: d.strip() for i, d in enumerate(q["distractores"]) if i != cor and d and d.strip()}
    g = (q.get("hoja") or {}).get("guion", {})
    for st in g.get("2", []):
        m = re.match(r"o:([A-H]):no$", st.get("a", ""))
        if m and L.index(m.group(1)) in razon:
            st["t"] = f"La opción {m.group(1)} es incorrecta: {razon[L.index(m.group(1))]}"


def fix(q, c):
    ch = False
    # basura del PDF
    for k, o in enumerate(q["opciones"]):
        n = BASURA.sub("", o)
        if n != o:
            q["opciones"][k] = n
            ch = True
    # ingles
    ds = q["distractores"]
    cor = q["correcta"]
    nuevos = list(ds)
    for k, d in enumerate(ds):
        if k == cor or not d:
            continue
        m = R1.match(d) or R2.match(d)
        if m and m.group(1) in VOC:
            w, t = m.group(1), m.group(2)
            g, f = VOC[w]
            nuevos[k] = PLANTILLAS[k % 4].format(w=w, g=g, G=g.capitalize(), f=f, t=t)
    for k, r in MANUAL.get(q["id"], {}).items():
        nuevos[k] = r
    if nuevos != ds:
        q["distractores"] = nuevos
        resync_nivel2(q)
        b1.fix(q, c)
        ch = True
    # campo 'que' de catalogo
    enf = (q.get("hoja") or {}).get("enfoque") or {}
    if str(enf.get("que", "")).startswith("Explica comprender"):
        enf["que"] = "Responde: " + ultima_pregunta(q["enunciado"])
        ch = True
    return ch


if __name__ == "__main__":
    print("preguntas modificadas:", procesar(fix))
