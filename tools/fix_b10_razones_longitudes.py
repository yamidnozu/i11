#!/usr/bin/env python3
"""Alinea razones y hojas; equilibra distractores sin cambiar las claves.

Uso: python3 tools/fix_b10_razones_longitudes.py
Longitud llamativa: clave >= 1.25 veces el distractor mas largo y >= 15
caracteres adicionales. Se revisan ICFES, banco propio y packs.
"""
import copy
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LETTERS = "ABCDEFGH"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, data):
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")


def questions(data):
    return data["preguntas"] if isinstance(data, dict) else data


def length_stats(items):
    valid = [q for q in items if isinstance(q.get("correcta"), int)
             and len(q.get("opciones", [])) > 1]
    longest, obvious = [], []
    for q in valid:
        sizes = [len(o) for o in q["opciones"]]
        right = sizes[q["correcta"]]
        other = max(n for i, n in enumerate(sizes) if i != q["correcta"])
        if right > other:
            longest.append(q["id"])
        if right >= other * 1.25 and right - other >= 15:
            obvious.append(q["id"])
    return len(valid), len(longest), obvious


def replace_text(obj, pairs):
    if isinstance(obj, str):
        for old, new in pairs:
            obj = obj.replace(old, new)
        return obj
    if isinstance(obj, list):
        return [replace_text(v, pairs) for v in obj]
    if isinstance(obj, dict):
        return {k: replace_text(v, pairs) for k, v in obj.items()}
    return obj


def sync_reasons(q, old):
    """Actualiza tambien citas, trampas, tabla y voz de cada alternativa."""
    pairs = []
    for field in ("opciones", "distractores"):
        for before, after in zip(old[field], q[field]):
            if before and before != after:
                pairs.append((before, after))
                pairs.append((before[0].lower() + before[1:], after[0].lower() + after[1:]))
    h = replace_text(q["hoja"], sorted(pairs, key=lambda p: -len(p[0])))
    q["hoja"] = h
    h["enfoque"]["no"] = [
        {"t": "Opci\u00f3n " + LETTERS[i], "p": reason}
        for i, reason in enumerate(q["distractores"]) if i != q["correcta"]
    ]
    for step in h["pasos"]:
        if step.get("k") == "tabla" and step.get("cols") == ["Opci\u00f3n", "Estado", "An\u00e1lisis pedag\u00f3gico"]:
            for row in step["filas"]:
                i = LETTERS.index(row[0])
                if i != q["correcta"]:
                    row[2] = q["distractores"][i]
    for entry in h["guion"]["2"]:
        match = re.fullmatch(r"o:([A-H]):no", entry.get("a", ""))
        if match:
            i = LETTERS.index(match[1])
            entry["t"] = q["distractores"][i]


def core(q):
    qid = q["id"]
    if qid == "mth-i002":
        q["distractores"] = [
            "A afirma que el rendimiento se conserva sin importar las variaciones del cambio. Pero esa generalizaci\u00f3n es falsa: si el d\u00f3lar bajara, la ganancia en pesos podr\u00eda ser menor o convertirse en p\u00e9rdida; aqu\u00ed solo se conserva porque la tasa es constante.",
            "B exige el capital exacto para hallar cu\u00e1nto dinero se gana. Pero se pregunta por un porcentaje, no por una cantidad: cualquier capital y su ganancia se convierten con el mismo factor, que se cancela al dividirlos.",
            "",
            "D confunde una cantidad monetaria mayor con un porcentaje mayor. Pero los dos mil multiplican tanto la ganancia como la inversi\u00f3n inicial: su cociente sigue siendo tres por ciento, no un rendimiento dos mil veces mayor."
        ]
        q["explicacion"] = "La opci\u00f3n C es correcta porque la tasa permanece constante. Si se invierten $P$ d\u00f3lares, la ganancia es $0,03P$ d\u00f3lares. En pesos, el capital es $2.000P$ y la ganancia es $2.000(0,03P)$; al dividir ganancia entre capital, el factor $2.000$ se cancela y queda $0,03=3\\%$. Se conserva el porcentaje, aunque cambie la cantidad expresada en cada moneda."
        h = q["hoja"]
        h["enfoque"]["clave"] = "Con cambio constante, capital y ganancia se multiplican por dos mil; el cociente ganancia sobre capital sigue siendo tres por ciento."
        h["guion"]["1"] = [
            {"t": "Compara la ganancia con el capital inicial, ambos en la misma moneda."},
            {"t": "La tasa fija multiplica los dos valores por dos mil, por lo que su cociente no cambia."},
            {"a": "o:C:ok", "t": "C usa la condici\u00f3n de tasa constante y conserva el tres por ciento. La respuesta es C."}
        ]
        h["guion"]["2"] = [
            {"t": "Con mil d\u00f3lares se ganan treinta d\u00f3lares. En pesos son dos millones de capital y sesenta mil de ganancia."},
            {"t": "Sesenta mil dividido entre dos millones es tres por ciento; el monto absoluto cambia, el rendimiento no."},
            *[{"a": f"o:{LETTERS[i]}:no", "k": "err", "t": r} for i, r in enumerate(q["distractores"]) if r],
            {"a": "o:C:ok", "t": "La conversi\u00f3n mantiene la proporci\u00f3n porque usa la misma tasa al principio y al final. La respuesta es C."}
        ]
        h["guion"]["3"] = [
            {"a": "p:0", "k": "ana", "t": "Distingue rendimiento porcentual de ganancia en dinero."},
            {"a": "p:1", "t": "Al convertir ganancia y capital con una tasa fija, el factor com\u00fan desaparece del cociente."},
            {"a": "o:A:no|o:B:no|o:D:no", "k": "err", "t": "A extiende la conclusi\u00f3n a tasas variables; B pide un capital innecesario para hallar el porcentaje; D confunde pesos con rendimiento."},
            {"a": "p:2|o:C:ok", "t": "C justifica el tres por ciento con la tasa constante indicada. La respuesta correcta es C."}
        ]
    elif qid == "cfi-i008":
        q["distractores"] = [
            "A propone $(8,2)$ y $(2,4)$. Pero el reflejo de $(-4,2)$ debe ser $(4,2)$, no $(8,2)$, y el de $(-2,8)$ debe conservar la altura ocho, no cambiarla a cuatro.",
            "",
            "C da $(-2,-4)$ y $(-8,-2)$ al transformar $(x,y)$ en $(-y,x)$, una rotaci\u00f3n de noventa grados en sentido antihorario. Pero reflejar sobre el eje vertical solo cambia el signo de la abscisa y conserva las alturas positivas.",
            "D mantiene las abscisas negativas y cambia las alturas a $-2$ y $-8$, como en una reflexi\u00f3n sobre el eje horizontal. Pero la simetr\u00eda pedida es respecto al eje vertical: deben cambiar los signos de las abscisas."
        ]
        q["explicacion"] = "La simetr\u00eda respecto al eje $Y$ aplica $(x,y)\\to(-x,y)$: $(-4,2)$ se refleja en $(4,2)$ y $(-2,8)$ en $(2,8)$. La opci\u00f3n B contiene exactamente esos dos puntos, escritos en el orden inverso; las alturas se conservan y los puntos quedan a igual distancia del eje vertical."
        h = q["hoja"]
        h["guion"]["2"] = [
            {"t": "El reflejo conserva la altura y cambia el signo de la primera coordenada."},
            {"t": "Resultan los puntos cuatro coma dos y dos coma ocho."},
            *[{"a": f"o:{LETTERS[i]}:no", "k": "err", "t": r} for i, r in enumerate(q["distractores"]) if r],
            {"a": "o:B:ok", "t": "B enumera los dos reflejos en orden inverso. La respuesta es B."}
        ]
        h["guion"]["3"][3]["t"] = "A altera la abscisa del primer reflejo y la altura del segundo; C aplica una rotaci\u00f3n de noventa grados; D refleja sobre el eje horizontal."
    elif qid == "cfi-i105":
        q["distractores"] = [
            "{{Bike}} puede significar bicicleta y tambi\u00e9n usarse para motocicleta; una bicicleta permite viajar por carretera y puede llevar uno o dos ocupantes. Pero la clave oficial elige {{motorbike}}: el enunciado no menciona motor y, por s\u00ed solo, no permite excluir A con certeza.",
            "{{Boat}} significa barco o bote y permite viajar por agua. Pero {{by road}} exige desplazamiento por carretera, no navegaci\u00f3n.",
            "{{Bus}} es un autob\u00fas destinado al transporte colectivo por carretera. Pero {{only one or two people}} describe un transporte para uno o dos ocupantes, no la cantidad ocasional de pasajeros de un autob\u00fas.",
            "{{Helicopter}} es un helic\u00f3ptero; puede transportar pocas personas. Pero se desplaza por el aire y no cumple {{by road}}.",
            "",
            "{{Plane}} significa avi\u00f3n, incluso si es peque\u00f1o y lleva solo dos personas. Pero su medio de desplazamiento es el aire, no la carretera.",
            "{{Truck}} designa un cami\u00f3n destinado a transportar carga, no principalmente a llevar una o dos personas. Pero su cabina s\u00ed puede tener dos plazas: se descarta por el uso que destaca la definici\u00f3n, no porque sea imposible viajar dos en \u00e9l.",
            "{{Train}} es un tren que circula sobre rieles. Pero {{by road}} se refiere a carretera y no a una v\u00eda f\u00e9rrea, independientemente de cu\u00e1ntas personas viajen."
        ]
        q["explicacion"] = "La clave oficial es E, motorbike (motocicleta): es un veh\u00edculo para viajar por carretera que suele admitir conductor y pasajero, de modo que cumple las dos pistas del enunciado. Sin embargo, la frase no dice que tenga motor ni dos ruedas: bike tambi\u00e9n puede ajustarse, y la cabina de un truck puede llevar dos personas. Se conserva E como respuesta oficial y se mantiene la marca de revisi\u00f3n; el texto disponible no demuestra una respuesta \u00fanica."
        h = q["hoja"]
        h["enfoque"].update({
            "que": "Relaciona una definici\u00f3n breve con medios de transporte y reconoce el l\u00edmite de sus pistas.",
            "clave": "La clave oficial E, motorbike, cumple carretera y uno o dos ocupantes; el enunciado no menciona motor y no excluye de manera inequ\u00edvoca bike.",
            "pistas": [
                "{{By road}} identifica el desplazamiento por carretera; excluye agua, aire y rieles.",
                "{{Only one or two people}} destaca la capacidad reducida; no a\u00f1ade una exigencia de motor."
            ],
            "plan": [
                {"t": "Localiza las pistas de medio de desplazamiento y n\u00famero de ocupantes."},
                {"t": "Compara cada palabra con esas dos pistas, sin inventar requisitos."},
                {"t": "Reconoce motorbike como clave oficial y conserva la advertencia sobre bike."}
            ]
        })
        h["marcas"] = [
            {"campo": "Capacidad", "frag": "only one or two people", "nota": "Uno o dos ocupantes.", "rol": "dato"},
            {"campo": "Medio de desplazamiento", "frag": "by road", "nota": "Viaje por carretera.", "rol": "dato"}
        ]
        h["pasos"] = [
            {"k": "idea", "titulo": "Lee las dos pistas", "texto": "Se describe transporte por carretera para uno o dos ocupantes. No se menciona motor."},
            {"k": "check", "titulo": "Clave oficial y l\u00edmite", "texto": q["explicacion"]}
        ]
        h["guion"] = {
            "1": [
                {"a": "leer", "t": "Busca transporte por carretera para una o dos personas."},
                {"a": "p:0", "t": "{{Motorbike}} cumple ambas pistas, pero la frase no dice que se requiera motor."},
                {"a": "o:E:ok", "t": "La respuesta oficial es E. Se mantiene la advertencia porque {{bike}} tambi\u00e9n puede ajustarse."}
            ],
            "2": [
                {"a": "leer", "t": "Analicemos cada alternativa con sus propias caracter\u00edsticas."},
                *[{"a": f"o:{LETTERS[i]}:no", "k": "err", "t": r} for i, r in enumerate(q["distractores"]) if r],
                {"a": "o:E:ok", "t": "{{Motorbike}} permite viajar por carretera con conductor y pasajero. La clave oficial es E, aunque el texto no garantiza unicidad."}
            ],
            "3": [
                {"a": "p:0", "k": "ana", "t": "Agua, aire y rieles no satisfacen {{by road}}; un autob\u00fas es de transporte colectivo."},
                {"a": "p:1", "t": "La motocicleta cumple las pistas; una bicicleta y una cabina de cami\u00f3n muestran por qu\u00e9 la definici\u00f3n no es inequ\u00edvoca."},
                {"a": "o:E:ok", "t": "Se conserva la respuesta oficial E y la marca de revisi\u00f3n, sin atribuir al enunciado una exigencia de motor."}
            ]
        }


# Cada entrada modifica solo alternativas incorrectas y su razon particular.
# Se conserva el texto correcto y su indice, incluso en las copias oficiales.
BALANCE = {
    "cfi-i045": {
        0: ("qu\u00e9 pa\u00edses de cada regi\u00f3n utilizan una menor cantidad de veh\u00edculos automotores.", "Relaciona la mortalidad regional con el uso de automotores. Pero una tasa de muertes no informa cu\u00e1ntos veh\u00edculos utiliza cada pa\u00eds."),
        1: ("que Asia y el Pac\u00edfico registran el mismo n\u00famero total de muertes por tr\u00e1nsito.", "Confunde una tasa de mortalidad con un total de fallecidos. Pero comparar muertes por habitante no demuestra que dos regiones tengan el mismo n\u00famero absoluto de muertes."),
        3: ("qu\u00e9 regiones necesitan mejorar sus v\u00edas para reducir los accidentes de tr\u00e1nsito.", "Propone decidir obras viales a partir de las muertes. Pero el gr\u00e1fico no muestra el estado de las v\u00edas ni identifica las causas de los accidentes.")
    },
    "mat-i013": {
        0: ("La ganancia total obtenida por los productores de mango y banano.", "Usa las toneladas vendidas para calcular ganancias de productores. Pero faltan sus costos de producci\u00f3n; las cantidades vendidas no determinan esa ganancia."),
        1: ("El pago total que recibir\u00e1 cada trabajador al terminar enero.", "Toma el n\u00famero de trabajadores como dato suficiente para hallar sus pagos. Pero se desconoce qu\u00e9 cantidad transport\u00f3 cada uno y a qu\u00e9 ciudad."),
        2: ("Los costos totales de transporte y personal del comerciante.", "Pretende sumar todos los costos a partir del volumen vendido. Pero sin conocer el reparto de env\u00edos entre ciudades no se determinan transporte y pagos al personal.")
    },
    "soc-i003": {
        0: ("En muchos pa\u00edses hay personas homosexuales tanto entre la poblaci\u00f3n masculina como entre la femenina, y representan una parte importante de ambas.", "Describe la presencia de personas homosexuales en la poblaci\u00f3n. Pero esa afirmaci\u00f3n demogr\u00e1fica no condiciona su capacidad de ense\u00f1ar ni supone que transmitan su orientaci\u00f3n."),
        1: ("Las personas con inclinaciones homosexuales merecen recibir el mismo amor que todas las dem\u00e1s personas, sin que su orientaci\u00f3n sexual las excluya de ese trato.", "Reconoce igual dignidad y afecto a todas las personas. Pero no expresa el prejuicio que limita la docencia por una supuesta influencia sobre la orientaci\u00f3n de estudiantes."),
        2: ("Las preferencias sexuales resultan de una interacci\u00f3n compleja entre factores biol\u00f3gicos y condiciones del medio ambiente, que act\u00faan conjuntamente sobre la persona.", "Propone una explicaci\u00f3n de la orientaci\u00f3n basada en biolog\u00eda y ambiente. Pero no afirma que un profesor homosexual cambie la orientaci\u00f3n de sus estudiantes al ense\u00f1ar.")
    },
    "soc-i005": {
        0: ("diferentes, porque una respalda legalizar el tr\u00e1fico y el consumo de drogas, mientras la otra propone combatirlos mediante sanciones penales m\u00e1s duras.", "Atribuye a la primera postura un apoyo a la legalizaci\u00f3n. Pero esa postura la considera indeseable y propone sensibilizar sobre riesgos; no legalizar el tr\u00e1fico ni el consumo."),
        1: ("similares, porque ambas consideran que regular legalmente el consumo de drogas es la v\u00eda para intervenir directamente sobre el negocio del narcotr\u00e1fico.", "Presenta la regulaci\u00f3n legal del consumo como estrategia compartida. Pero el texto contrapone sensibilizaci\u00f3n y endurecimiento de penas, sin plantear esa coincidencia."),
        3: ("similares, porque ambas rechazan la legalizaci\u00f3n y buscan ante todo proteger a los consumidores de los riesgos sanitarios que trae el consumo de drogas.", "Extiende a las dos posturas el objetivo sanitario de la primera. Pero la segunda propone penas para productores, expendedores y ciertos consumidores, no sensibilizaci\u00f3n sobre la salud.")
    },
    "cie-014": {
        1: ("Aumentar\u00e1, porque un l\u00edquido m\u00e1s denso ejerce menos empuje y obliga al cubo a sumergir una fracci\u00f3n mayor para flotar.", "Asocia mayor densidad con menor empuje para un mismo volumen. Pero al aumentar la densidad del agua basta desplazar menos volumen para equilibrar el peso."),
        2: ("Se mantendr\u00e1 en ochenta por ciento, porque la densidad del cubo determina por s\u00ed sola qu\u00e9 fracci\u00f3n queda sumergida.", "Conserva la fracci\u00f3n sumergida porque el cubo no cambia. Pero esa fracci\u00f3n depende tambi\u00e9n de la densidad del l\u00edquido, que ahora es mayor."),
        3: ("Se hundir\u00e1 por completo, porque la mayor densidad del agua de mar aumenta el peso del cubo sin modificar su volumen.", "Supone que cambiar de l\u00edquido aumenta el peso del pl\u00e1stico. Pero la masa del cubo permanece igual y el agua m\u00e1s densa favorece la flotaci\u00f3n.")
    },
    "cie-022": {
        0: ("El NaCl forma una red de enlaces met\u00e1licos que libera electrones en agua, mientras el CCl\u2084 tiene enlaces i\u00f3nicos que no se disocian.", "Interpreta la conducci\u00f3n en agua como liberaci\u00f3n de electrones met\u00e1licos. Pero el NaCl libera iones y el CCl\u2084 es molecular covalente, no una red i\u00f3nica."),
        2: ("El NaCl est\u00e1 formado por \u00e1tomos no met\u00e1licos que comparten electrones, mientras el CCl\u2084 contiene metales alcalinos que ceden electrones.", "Invierte la clasificaci\u00f3n de los elementos para explicar los enlaces. Pero el sodio es un metal y ni el carbono ni el cloro del CCl\u2084 son metales alcalinos."),
        3: ("El NaCl es una mezcla de sodio y cloro que se separa en agua, mientras el CCl\u2084 es un elemento puro cuyas part\u00edculas no se separan.", "Confunde una mezcla con un compuesto y una mol\u00e9cula con un elemento. Pero NaCl y CCl\u2084 son ambos compuestos puros, aunque sus estructuras y enlaces sean diferentes.")
    },
    "cie-025": {
        0: ("Filtraci\u00f3n con papel de poro fino para retener el etanol y dejar pasar el agua.", "Atribuye al filtro la separaci\u00f3n de mol\u00e9culas disueltas. Pero agua y etanol atraviesan juntos el papel porque forman una disoluci\u00f3n homog\u00e9nea."),
        1: ("Decantaci\u00f3n en embudo de separaci\u00f3n aprovechando las densidades de los l\u00edquidos.", "Usa la diferencia de densidades como si hubiera dos capas. Pero agua y etanol son miscibles y no forman una interfaz que permita decantarlos."),
        3: ("Centrifugaci\u00f3n a alta velocidad para separar el agua del etanol por su densidad.", "Aplica una separaci\u00f3n mec\u00e1nica propia de fases o part\u00edculas suspendidas. Pero la centrifugaci\u00f3n convencional no separa los componentes moleculares de esta disoluci\u00f3n.")
    },
    "cie-027": {
        0: ("El calor espec\u00edfico del agua se vuelve infinito a cero grados, por lo que el sistema puede absorber energ\u00eda sin que ocurra ning\u00fan cambio molecular.", "Interpreta la temperatura fija como un calor espec\u00edfico infinito. Pero durante la fusi\u00f3n la energ\u00eda s\u00ed cambia la estructura del material y se contabiliza como calor latente."),
        1: ("El term\u00f3metro deja de registrar los aumentos de energ\u00eda cin\u00e9tica mientras hay hielo, aunque la temperatura del agua suba durante toda la fusi\u00f3n.", "Atribuye la meseta a una incapacidad del instrumento. Pero un term\u00f3metro que funciona registra la temperatura constante de la mezcla en equilibrio durante el cambio de fase."),
        3: ("El aire extrae todo el calor que entrega el calentador, de modo que no queda energ\u00eda disponible para modificar el estado ni la temperatura del hielo.", "Plantea que toda la energ\u00eda suministrada se pierde hacia el aire. Pero el hielo se est\u00e1 fundiendo y ese cambio requiere absorber energ\u00eda neta, aunque la temperatura no aumente.")
    },
    "cie-028": {
        0: ("Actu\u00f3 como reactivo l\u00edmite, aportando el ox\u00edgeno del burbujeo y recuperando su masa al producirse agua.", "Lo considera fuente estequiom\u00e9trica del ox\u00edgeno. Pero un reactivo l\u00edmite se consume y la masa del di\u00f3xido de manganeso se recupera al terminar."),
        1: ("Actu\u00f3 como disolvente del per\u00f3xido, cambiando su punto de ebullici\u00f3n para producir el gas observado.", "Identifica el burbujeo con ebullici\u00f3n causada por un disolvente. Pero el gas es producto de la descomposici\u00f3n y el di\u00f3xido de manganeso es un catalizador s\u00f3lido."),
        3: ("Actu\u00f3 como inhibidor de la reacci\u00f3n, elevando la energ\u00eda de activaci\u00f3n sin consumirse en el proceso.", "Reconoce que no se consume y lo clasifica como inhibidor. Pero elevar la barrera de activaci\u00f3n retrasar\u00eda la reacci\u00f3n, en contra del burbujeo acelerado.")
    },
    "cie-029": {
        0: ("Endot\u00e9rmica, porque necesita absorber los ochocientos noventa kilojulios indicados para transformar reactivos en productos.", "Interpreta la energ\u00eda escrita a la derecha como calor absorbido. Pero aparece entre los productos, lo que indica liberaci\u00f3n de energ\u00eda hacia el entorno."),
        1: ("Adiab\u00e1tica, porque la energ\u00eda liberada permanece en los productos y la ecuaci\u00f3n demuestra que no sale calor hacia el entorno.", "Deduce ausencia de intercambio de calor de una ecuaci\u00f3n qu\u00edmica. Pero esta informa energ\u00eda liberada; una condici\u00f3n adiab\u00e1tica requerir\u00eda aislamiento que no se especifica."),
        3: ("Isot\u00e9rmica, porque los ochocientos noventa kilojulios liberados garantizan que la temperatura permanezca siempre constante.", "Asocia el calor liberado con temperatura necesariamente constante. Pero la ecuaci\u00f3n da un balance energ\u00e9tico y no impone control de temperatura.")
    },
    "cie-030": {
        0: ("Fijar directamente el di\u00f3xido de carbono en glucosa dentro del tilacoide, utilizando la luz absorbida por la clorofila.", "Le asigna al agua la fijaci\u00f3n directa del carbono en el tilacoide. Pero esa fijaci\u00f3n corresponde al ciclo de Calvin, no al papel del agua en la fase luminosa."),
        1: ("Absorber el exceso de calor solar como reserva t\u00e9rmica, sin participar en las transferencias de electrones de la fase luminosa.", "Reduce la funci\u00f3n del agua a amortiguar temperatura. Pero su fot\u00f3lisis suministra electrones y protones y libera ox\u00edgeno durante las reacciones luminosas."),
        3: ("Actuar como la enzima Rubisco que incorpora di\u00f3xido de carbono a compuestos org\u00e1nicos durante las reacciones del ciclo de Calvin.", "Identifica el agua con la enzima que fija carbono. Pero Rubisco es una prote\u00edna y act\u00faa en otro proceso; el agua aporta electrones en la fase luminosa.")
    },
    "cie-034": {
        0: ("El antibi\u00f3tico indujo en todas las bacterias la mutaci\u00f3n precisa para resistirlo; estas cambiaron sus genes como respuesta dirigida a la necesidad de sobrevivir al tratamiento.", "Supone mutaciones dirigidas por la necesidad de supervivencia. Pero la selecci\u00f3n favorece variantes resistentes existentes, sin ense\u00f1ar a las bacterias a producir la mutaci\u00f3n que necesitan."),
        1: ("El antibi\u00f3tico perdi\u00f3 su actividad al reaccionar con el aire del hospital; por ello las bacterias sensibles sobrevivieron sin que cambiara la frecuencia de variantes resistentes.", "Explica el fracaso por una degradaci\u00f3n del f\u00e1rmaco no descrita. Pero la pregunta pide explicar la resistencia de la cepa por selecci\u00f3n natural, que cambia la frecuencia de variantes."),
        2: ("Las bacterias sensibles adquirieron resistencia temporal al reducir su metabolismo durante el tratamiento; todas sobrevivieron por igual y la siguiente generaci\u00f3n volvi\u00f3 a ser sensible.", "Propone tolerancia temporal sin diferencias heredables de supervivencia. Pero eso no explica por selecci\u00f3n natural la expansi\u00f3n de una cepa resistente al antibi\u00f3tico.")
    },
    "cie-035": {
        0: ("El pat\u00f3geno atenuado elimina directamente los virus presentes y permanece circulando para destruir los de futuras infecciones.", "Presenta la vacuna como un antiviral permanente. Pero la protecci\u00f3n duradera depende de memoria inmunitaria, no de que el pat\u00f3geno vacunal destruya otros virus."),
        1: ("La vacuna mantiene activada de forma permanente la respuesta inflamatoria inespec\u00edfica, que impide la entrada de cualquier virus.", "Atribuye la protecci\u00f3n a inflamaci\u00f3n inespec\u00edfica constante. Pero la vacunaci\u00f3n genera reconocimiento y memoria frente a ant\u00edgenos concretos, no bloqueo universal de virus."),
        2: ("La vacuna modifica de forma permanente el ADN de todas las c\u00e9lulas, de modo que el virus ya no puede reconocerlas ni infectarlas.", "Explica la inmunidad por una alteraci\u00f3n del genoma de todo el organismo. Pero la memoria surge de la respuesta de linfocitos, sin reescribir el ADN de todas las c\u00e9lulas.")
    },
    "cie-036": {
        0: ("Elevar la temperatura interna para acelerar el metabolismo y aumentar el consumo de grasa durante el ejercicio realizado bajo el sol.", "Confunde la respuesta al exceso de calor con una forma de calentamiento. Pero sudoraci\u00f3n y vasodilataci\u00f3n cut\u00e1nea favorecen disipar calor para limitar la temperatura."),
        1: ("Interrumpir el flujo de sangre hacia los m\u00fasculos activos y dirigirlo exclusivamente a la piel para evitar que se produzca m\u00e1s calor metab\u00f3lico.", "Interpreta la redistribuci\u00f3n del flujo como interrupci\u00f3n del riego muscular. Pero los m\u00fasculos activos siguen necesitando ox\u00edgeno y nutrientes durante el ejercicio."),
        2: ("Conservar el agua y las sales del organismo mediante el cierre de los poros y la acumulaci\u00f3n del sudor sobre la piel sin que llegue a evaporarse.", "Asocia la sudoraci\u00f3n con evitar p\u00e9rdidas de agua y evaporaci\u00f3n. Pero la secreci\u00f3n de sudor pierde agua y su evaporaci\u00f3n permite retirar calor del cuerpo.")
    },
    "cie-037": {
        0: ("La madera talada retiene directamente m\u00e1s radiaci\u00f3n infrarroja que el bosque vivo; esa absorci\u00f3n por los troncos explica el calentamiento global sin necesidad de cambios en los gases atmosf\u00e9ricos.", "Atribuye el efecto global a radiaci\u00f3n retenida directamente por troncos. Pero el mecanismo biol\u00f3gico pedido implica menor fijaci\u00f3n de carbono y liberaci\u00f3n del carbono almacenado."),
        1: ("La tala libera el nitr\u00f3geno que los \u00e1rboles hab\u00edan absorbido del suelo; ese gas destruye la capa de ozono y permite que llegue m\u00e1s radiaci\u00f3n ultravioleta, causando el aumento global de temperatura.", "Mezcla nitr\u00f3geno y destrucci\u00f3n del ozono con el efecto invernadero. Pero el impacto descrito se relaciona directamente con el balance de di\u00f3xido de carbono, no con esa cadena causal."),
        2: ("Al desaparecer los \u00e1rboles se reduce la respiraci\u00f3n del ecosistema y, por ello, se acumula m\u00e1s di\u00f3xido de carbono en la atm\u00f3sfera, aunque la fotos\u00edntesis y el carbono del suelo no cambien.", "Relaciona menos respiraci\u00f3n con m\u00e1s di\u00f3xido de carbono y deja intacta la fotos\u00edntesis. Pero respirar libera ese gas, mientras la tala elimina organismos que lo fijaban y puede liberar carbono almacenado.")
    },
    "cie-039": {
        0: ("Las ra\u00edces de los frailejones extraen agua de acu\u00edferos profundos y la bombean hacia los r\u00edos, de modo que el suelo no participa en la regulaci\u00f3n del caudal.", "Atribuye el suministro al bombeo desde acu\u00edferos profundos. Pero el mecanismo descrito es retener agua de lluvia y neblina en vegetaci\u00f3n y suelo y liberarla gradualmente."),
        1: ("El fr\u00edo mantiene congelada de forma permanente el agua del suelo, evitando la infiltraci\u00f3n y permitiendo que llegue a los r\u00edos solo cuando sube la temperatura.", "Explica la regulaci\u00f3n mediante congelaci\u00f3n permanente. Pero estos p\u00e1ramos almacenan y liberan agua l\u00edquida; no dependen de una reserva de suelo siempre congelado."),
        2: ("Las hojas fabrican nuevas mol\u00e9culas de agua al absorber radiaci\u00f3n ultravioleta y las entregan al suelo, que act\u00faa solo como canal de salida hacia los r\u00edos.", "Confunde captar gotas de neblina con fabricar agua usando radiaci\u00f3n. Pero la vegetaci\u00f3n intercepta agua existente y el suelo la almacena, no es solo un canal de salida.")
    },
    "lec-001": {
        0: ("Que las bibliotecas de barrio presten muy pocos libros", "Deduce una queja por pocos pr\u00e9stamos. Pero el autor no informa su cantidad: cuestiona que ese sea el \u00fanico criterio para medir valor."),
        2: ("Que las bibliotecas permitan hacer tr\u00e1mites digitales", "Convierte los tr\u00e1mites en objeto de cr\u00edtica. Pero el texto los presenta como una utilidad adicional que el conteo de pr\u00e9stamos deja fuera."),
        3: ("Que haya pocas bibliotecas en los barrios de la ciudad", "Interpreta el argumento como una queja por cobertura. Pero el fragmento no compara cantidades de bibliotecas ni pide construir otras.")
    },
    "lec-004": {
        0: ("El mercado atrae vecinos porque ofrece los precios m\u00e1s bajos del barrio", "Reduce el atractivo del mercado al ahorro. Pero el texto dice que puede no ser lo m\u00e1s barato y destaca conversar y pertenecer a una comunidad."),
        1: ("Los supermercados deben cerrar para que el mercado conserve sus ventas", "Deduce una propuesta de cierre a partir de la comparaci\u00f3n con supermercados. Pero el autor no pide clausurarlos, sino que explica el valor comunitario del mercado."),
        3: ("La plaza necesita m\u00e1s puestos para competir en precio con supermercados", "Transforma la descripci\u00f3n de puestos en un plan de expansi\u00f3n comercial. Pero no se propone aumentar puestos ni competir mediante menores precios.")
    },
    "lec-005": {
        0: ("Introduce un ejemplo de lo dicho antes", "Entiende el conector como anuncio de un caso particular. Pero la frase siguiente explica por qu\u00e9 los vecinos siguen yendo, no presenta un ejemplo nuevo."),
        2: ("Introduce una objeci\u00f3n a lo dicho antes", "Lee el conector como una refutaci\u00f3n. Pero la continuidad de las visitas se deriva del trato comunitario descrito, no lo contradice."),
        3: ("Abre un tema distinto al del p\u00e1rrafo", "Interpreta una ruptura tem\u00e1tica. Pero la frase mantiene el tema del mercado y enlaza su valor social con la decisi\u00f3n de los vecinos.")
    },
    "lec-006": {
        0: ("Dejar\u00eda de existir como espacio f\u00edsico para los habitantes", "Confunde perder vida comunitaria con desaparecer f\u00edsicamente. Pero la \u00faltima frase afirma que la plaza seguir\u00eda existiendo sin el mercado."),
        2: ("Ofrecer\u00eda alimentos m\u00e1s baratos al desaparecer el mercado", "Deduce una bajada de precios sin datos de oferta o demanda. Pero el cierre se usa para explicar una p\u00e9rdida social, no para pronosticar precios."),
        3: ("Ser\u00eda ocupada por supermercados que sustituir\u00edan sus puestos", "A\u00f1ade una sustituci\u00f3n comercial que no aparece en el fragmento. Pero mencionar supermercados como contraste no implica que vayan a ocupar la plaza.")
    },
    "soc-001": {
        0: ("Modificar directamente las leyes aprobadas por el Congreso", "Confunde la protecci\u00f3n de un derecho con una reforma legislativa. Pero una tutela no modifica directamente el texto de las leyes del Congreso."),
        2: ("Elegir mediante un fallo al presidente de la Rep\u00fablica", "Atribuye a un juez de tutela la elecci\u00f3n presidencial. Pero esa elecci\u00f3n corresponde al voto ciudadano y no al mecanismo de protecci\u00f3n judicial."),
        3: ("Declarar el estado de guerra mediante una orden judicial", "Traslada a un fallo de tutela la decisi\u00f3n de declarar la guerra. Pero la tutela protege derechos fundamentales, no ejerce esa atribuci\u00f3n estatal.")
    }
}

for source, duplicate in [("mat-i013", "mth-i013"), ("soc-i003", "scc-i003"), ("soc-i005", "scc-i005")]:
    BALANCE[duplicate] = BALANCE[source]


def main():
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
    assert branch == "antigravity/v1", "Solo se permite antigravity/v1"
    paths = sorted((ROOT / "content/icfes").glob("*/preguntas.json"))
    paths += sorted((ROOT / "content/questions").glob("*.json"))
    paths += sorted((ROOT / "content/packs").rglob("*.json"))
    documents = {p: read(p) for p in paths}
    original = copy.deepcopy(documents)
    all_before = [q for d in documents.values() for q in questions(d)]
    before = length_stats(all_before)
    core_ids = {"mth-i002", "cfi-i008", "cfi-i105"}
    found = set()
    own_maps = {name: read(ROOT / f"content/{name}.json") for name in ("hojas", "enfoques", "guiones")}
    changed = []
    for path, data in documents.items():
        for q in questions(data):
            qid = q["id"]
            if qid not in core_ids and qid not in BALANCE:
                continue
            found.add(qid)
            old = copy.deepcopy(q)
            if qid in core_ids:
                core(q)
            for i, (option, reason) in BALANCE.get(qid, {}).items():
                assert i != q["correcta"]
                if qid == "mth-i013":
                    option = option[0].lower() + option[1:]
                q["opciones"][i] = option
                q["distractores"][i] = reason
            sync_reasons(q, old)
            assert q["correcta"] == old["correcta"]
            assert q["opciones"][q["correcta"]] == old["opciones"][old["correcta"]]
            assert q["distractores"][q["correcta"]] == ""
            assert q.get("revisar") == old.get("revisar")
            if q != old:
                changed.append(qid)
            if path.parent.parent.name == "icfes":
                hp = path.parent / "hojas" / f"{qid}.json"
                hd = read(hp)
                hd["hoja"] = q["hoja"]
                write(hp, hd)
                assert read(hp)["hoja"] == q["hoja"]
            else:
                for name, section in [("enfoques", "enfoque"), ("guiones", "guion")]:
                    if qid in own_maps[name]:
                        own_maps[name][qid] = q["hoja"][section]
                if qid in own_maps["hojas"]:
                    own_maps["hojas"][qid] = {k: v for k, v in q["hoja"].items() if k not in ("enfoque", "guion")}
        if data != original[path]:
            write(path, data)
    assert found == core_ids | BALANCE.keys(), "Falta algun identificador previsto"
    for name, data in own_maps.items():
        path = ROOT / f"content/{name}.json"
        if data != read(path):
            write(path, data)
    after = length_stats([q for d in documents.values() for q in questions(d)])
    assert not after[2], after[2]
    print(f"Preguntas modificadas: {len(changed)}; longitud equilibrada: {len(BALANCE)}")
    print(f"Banco completo: {before[0]}; clave mas larga: {before[1]} -> {after[1]}; casos llamativos: {len(before[2])} -> {len(after[2])}")
    for label, prefix in [("ICFES", "content/icfes/"), ("Propias y packs", "content/")]:
        selected = [p for p in paths if str(p.relative_to(ROOT)).startswith(prefix) and (label == "ICFES" or "icfes" not in p.parts)]
        b = length_stats([q for p in selected for q in questions(original[p])])
        a = length_stats([q for p in selected for q in questions(documents[p])])
        print(f"{label}: {b[0]}; clave mas larga {b[1]} -> {a[1]}; llamativos {len(b[2])} -> {len(a[2])}")


if __name__ == "__main__":
    main()
