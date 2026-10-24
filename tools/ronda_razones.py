"""Ronda de corrección (auditoría externa 2): razones de distractores específicas por opción.

- Reescribe a mano las razones de las preguntas señaladas (RAZONES).
- Sincroniza hoja.enfoque.no y las líneas de error del guion con q.distractores.
- Quita muletillas heredadas ("Parece tentador a simple vista. Pero …") de la hoja.
- Reemplaza la frase de catálogo "Explica explicar …" en enfoque.que.
- Reconstruye las hojas plantilla de cfi-i105 y eng-i018.
Idempotente: se puede ejecutar varias veces.
"""
import glob
import json
import re

L = 'ABCDEFGH'

# id -> {indice_opcion: razon}; OPC: id -> {indice: nuevo texto de opción}
RAZONES = {}
OPC = {}
EXTRA = {}  # id -> dict con que/tema/explicacion

_ENG_A = ("{{larger}} compara dos elementos («más grande que») y pide «than»; aquí no hay segundo término de "
          "comparación y el artículo «the» anuncia el superlativo del grupo.")
_ENG_C = ("{{large}} solo describe tamaño sin ubicar el grupo frente a los demás; tras «the» y entre varios grupos "
          "de lobos hace falta {{largest}}, el grado superlativo.")
_ENG_B = ("{{along}} se usa para recorrer algo de punta a punta (along the river); un parque es un área, "
          "así que los lobos existen dentro de él y no «a lo largo» de él.")
_ENG_C2 = ("{{on}} indica contacto con una superficie (on the table); un parque nacional es un territorio "
           "que se habita {{in}}, no encima.")
for i in ('ena-i038', 'eng-i038', 'ing-i038'):
    RAZONES[i] = {0: _ENG_A, 2: _ENG_C}
for i in ('ena-i039', 'eng-i039', 'ing-i039'):
    RAZONES[i] = {1: _ENG_B, 2: _ENG_C2}

RAZONES['mat-i002'] = {
    0: "El «sí» es correcto, pero la justificación no: si la tasa cambiara durante el mes, la ganancia en pesos "
       "dejaría de ser del 3 %. Aquí se conserva solo porque la tasa permanece constante.",
    1: "El porcentaje es una razón y no depende del monto: con 100 o con 10.000 dólares, la ganancia en pesos "
       "sigue siendo del 3 % mientras la tasa no cambie.",
    3: "El factor 4.000 multiplica por igual la inversión y la ganancia: en pesos la ganancia es mayor en "
       "cantidad, pero el porcentaje sigue siendo 3 %.",
}
OPC['mat-i002'] = {0: "Sí, porque el 3 % se conserva sin importar cómo varíe la tasa de cambio."}
RAZONES['mth-i002'] = {
    0: "La conclusión «correcta» coincide, pero la justificación falla: si la tasa variara durante el mes, la "
       "ganancia en pesos no sería del $3\\%$. Solo se conserva porque aquí la tasa es constante.",
    1: "El porcentaje es una razón y no depende del monto invertido: con 100 o con 10.000 dólares, la ganancia en "
       "pesos sigue siendo del $3\\%$ si la tasa no cambia.",
    3: "Con $1$ dólar $=2.000$ pesos, el capital y la ganancia se multiplican por $2.000$: la ganancia en pesos es "
       "mayor en cantidad, pero el porcentaje sigue siendo $3\\%$.",
}
RAZONES['cfi-i015'] = {
    0: "El $10$ sale de contar los enteros menores que $11$, pero la condición es sobre $j$: se necesita $j>11$, "
       "y hay infinitos enteros mayores que $11$, no solo diez.",
    2: "Con $j=11$ se obtiene exactamente $k+\\frac{1}{11}$, el límite; la pregunta pide los racionales menores "
       "que él, así que $j=11$ no cuenta.",
    3: "Con $j=10$ se obtiene $k+0,1$, que es mayor que $k+\\frac{1}{11}$ (porque $\\frac{1}{10}>\\frac{1}{11}$), "
       "y además no existe un racional «más cercano»: para cada $j$ hay otro mayor que se acerca más.",
}
_ACERO_B = ("El acero tiene cantidades distintas de hierro y carbono entre muestras; una sustancia pura "
            "(compuesto) tiene composición fija, así que el acero no lo es.")
_ACERO_C = ("Estar formado por varios elementos sí lo hace mezcla, pero «heterogénea» exige fases o partes "
            "visibles; el enunciado dice que ambas muestras son uniformes, es decir, homogéneas.")
_ACERO_D = ("Que dos muestras difieran en composición es justo la señal de una mezcla: una sustancia pura "
            "siempre tiene la misma composición, sin importar la muestra.")
for i in ('cfi-i077', 'cna-i028', 'cie-i028'):
    RAZONES[i] = {1: _ACERO_B, 2: _ACERO_C, 3: _ACERO_D}
_QUE_ACERO = ("El acero tiene composición variable pero uniforme: eso lo hace una mezcla homogénea, "
              "no una sustancia pura ni una mezcla heterogénea.")
for i in ('cfi-i077', 'cna-i028', 'cie-i028'):
    EXTRA[i] = {'que': _QUE_ACERO, 'tema': 'Clasificación de la materia: mezclas y sustancias puras'}

RAZONES['cfi-i085'] = {
    0: "A pone el vagón alto en t1 y bajo en t2, justo al revés de la gráfica, que parte de una energía "
       "potencial baja y sube en t2.",
    1: "B deja el vagón abajo en t1, t2 y t3; la gráfica pide un máximo de altura en t2, que B no tiene.",
    2: "C sí sube en t2, pero lo hace descender en t3 y t4; la gráfica muestra que vuelve a bajar en t3 y "
       "termina en una altura intermedia en t4, no en el suelo.",
}
_BOIL = {
    1: "Acierta en que la presión es menor, pero invierte la consecuencia: con menos presión atmosférica, "
       "la presión de vapor la iguala antes y el agua hierve a menos de 100 °C, no a más.",
    2: "Con poca presión hervir es más fácil, no imposible: el agua sí hierve, solo que a una temperatura "
       "menor que 100 °C.",
    3: "El enunciado relaciona la ebullición con la presión de vapor; bajar la presión no enfría el agua hasta "
       "congelarla, solo baja la temperatura a la que hierve.",
}
for i in ('cna-i027', 'cie-i027'):
    RAZONES[i] = _BOIL
_REF = {
    0: "Es el error de creer que el agua «hunde» el farol; al salir del agua el rayo se desvía y el ojo lo "
       "prolonga en línea recta hacia arriba, así que lo ve más alto, no más bajo.",
    1: "Ignora que el rayo cambia de dirección al pasar del agua al aire (Figura 2); con otra dirección, la "
       "prolongación recta apunta a otra altura y el farol no se ve igual.",
    3: "Invertir una imagen requiere una lente o un espejo que crucen los rayos; la refracción en una "
       "superficie plana solo desplaza la imagen aparente, no la voltea.",
}
for i in ('cna-i032', 'cie-i032'):
    RAZONES[i] = _REF
    EXTRA[i] = {'que': "Al pasar del agua al aire el rayo se aleja de la normal; el ojo lo prolonga en línea recta "
                       "y ve el farol más alto de donde está.",
                'tema': 'Refracción de la luz y posición aparente de los objetos'}
RAZONES['cfi-i105'] = {
    0: "A bike también lleva a una o dos personas, pero se mueve a pedal; el vehículo de la lista que va por "
       "carretera con motor para una o dos personas es la motorbike.",
    1: "A boat navega por el agua; la definición dice «by road», es decir, por carretera.",
    2: "A bus lleva a decenas de pasajeros; la definición habla de solo una o dos personas.",
    3: "A helicopter se desplaza por el aire; la definición pide un vehículo que vaya por carretera.",
    5: "A plane es transporte aéreo para muchos viajeros; ni va por carretera ni es para una o dos personas.",
    6: "A truck sí va por carretera, pero es un vehículo pesado de carga; no es para una o dos personas.",
    7: "A train circula por vías férreas y lleva a muchos pasajeros; no va por carretera ni es para uno o dos.",
}
OPC['cfi-i040'] = {0: "Que en esa comunidad no existe amor alguno entre los esposos, ni antes ni después de casarse."}
RAZONES['cfi-i040'] = {
    0: "Afirma que nunca hay amor entre esposos; el texto dice que algunas mujeres lo niegan y otras lo "
       "aceptan después del matrimonio, así que no es una ausencia total.",
    2: "El texto no menciona temor a enamorarse; habla de negar el apego o de aceptarlo más tarde, "
       "no de miedo.",
    3: "El pasaje no dice que el amor de las mujeres quede sin correspondencia; habla de cuándo se acepta "
       "el amor, no de si el marido lo devuelve.",
}

MULETILLA = re.compile(r'(Parece tentador a simple vista|Parece posible al mirar un dato aislado|'
                       r'Parece una alternativa posible)\.\s*Pero,?\s+(\w)')
CATALOGO = 'Explica explicar'


def limpiar_muletilla(o):
    if isinstance(o, dict):
        return {k: limpiar_muletilla(v) for k, v in o.items()}
    if isinstance(o, list):
        return [limpiar_muletilla(v) for v in o]
    if isinstance(o, str):
        return MULETILLA.sub(lambda m: m.group(2).upper(), o)
    return o


def primera_oracion(t):
    m = re.match(r'(.+?[.!?])(\s|$)', t.strip())
    return m.group(1) if m else t.strip()


def sync(q):
    hj = q.get('hoja')
    if not hj:
        return
    d = q['distractores']
    enf = hj.setdefault('enfoque', {})
    enf['no'] = [{'t': f'Opción {L[k]}', 'p': d[k]} for k in range(len(d)) if k != q['correcta'] and d[k]]
    for nivel, pref in (('2', 'no corresponde'), ('3', 'no encaja')):
        for ev in (hj.get('guion') or {}).get(nivel, []):
            m = re.match(r'o:([A-H]):no$', ev.get('a', ''))
            if m:
                k = L.index(m.group(1))
                if k < len(d) and d[k]:
                    ev['t'] = f'La opción {m.group(1)} {pref}: {d[k]}'


def hoja_plantilla_ing(q, tema, que, pistas, frag, plan):
    c = q['correcta']
    letra = L[c]
    op = q['opciones'][c]
    nodes = [k for k in range(len(q['opciones'])) if k != c]
    lvl2 = [{'a': 'leer', 't': 'Relacionemos la pista con la información del texto o la definición.'},
            {'a': 'p:1', 't': que}]
    lvl2 += [{'a': f'o:{L[k]}:no', 'k': 'err', 't': f'La opción {L[k]} no corresponde: {q["distractores"][k]}'}
             for k in nodes]
    lvl2 += [{'a': f'o:{letra}:ok', 't': f'La opción {{{{{op}}}}} sí responde a la pista.'}]
    lvl3 = [{'a': 'p:0', 'k': 'ana', 't': 'Identifica qué dato o relación pide la pregunta.'},
            {'a': 'p:1', 'k': 'por', 't': que}]
    lvl3 += [{'a': f'o:{L[k]}:no', 'k': 'err', 't': f'La opción {L[k]} no encaja: {q["distractores"][k]}'}
             for k in nodes]
    lvl3 += [{'a': f'o:{letra}:ok', 't': f'La evidencia respalda {{{{{op}}}}}.'}]
    return {
        'modo': 'lectura',
        'marcas': [{'campo': 'Pista del enunciado', 'frag': frag, 'rol': 'pide',
                    'nota': 'Esta frase indica qué información debes localizar o qué definición debes reconocer.'}],
        'pasos': [{'k': 'idea', 'titulo': 'Lee la pista', 'texto': pistas[0]},
                  {'k': 'idea', 'titulo': 'Relaciona la información', 'texto': que},
                  {'k': 'check', 'texto': 'Comprueba que la opción elegida cumple todas las ideas de la pista.'}],
        'enfoque': {'tema': tema, 'que': que, 'clave': que, 'pistas': pistas, 'plan': [{'t': t} for t in plan],
                    'no': []},
        'guion': {'1': [{'a': 'leer', 't': 'Leamos la pista y ubiquemos qué información necesitamos.'},
                        {'a': f'm:{frag}', 't': pistas[0]},
                        {'a': 'p:1', 't': que},
                        {'a': f'o:{letra}:ok', 't': f'La respuesta correcta es {{{{{op}}}}}.'}],
                  '2': lvl2, '3': lvl3},
    }


def main():
    cambios = 0
    for f in sorted(glob.glob('content/icfes/*/preguntas.json')):
        d = json.load(open(f))
        ov_f = f.replace('preguntas.json', 'overrides.json')
        try:
            ov = json.load(open(ov_f))
        except FileNotFoundError:
            ov = {}
        ch = False
        ov_ch = False
        for q in d['preguntas']:
            antes = json.dumps(q, ensure_ascii=False, sort_keys=True)
            i = q['id']
            for k, t in OPC.get(i, {}).items():
                q['opciones'][k] = t
            for k, r in RAZONES.get(i, {}).items():
                q['distractores'][k] = r
            if i in EXTRA:
                for kk, vv in EXTRA[i].items():
                    if kk in ('que', 'tema'):
                        q['hoja']['enfoque'][kk] = vv
                    else:
                        q[kk] = vv
            if q.get('hoja'):
                q['hoja'] = limpiar_muletilla(q['hoja'])
                enf = q['hoja'].get('enfoque', {})
                if CATALOGO in enf.get('que', ''):
                    enf['que'] = primera_oracion(q['explicacion'])
                if CATALOGO in enf.get('tema', ''):
                    enf['tema'] = EXTRA.get(i, {}).get('tema', enf['tema'].replace(CATALOGO, 'Explicar'))
                nos = [x['p'] for x in enf.get('no', [])]
                if i in RAZONES or len(set(nos)) < len(nos) or 'Pendiente' in ' '.join(nos):
                    sync(q)
            if i == 'cfi-i105':
                q['hoja'] = hoja_plantilla_ing(
                    q, 'Vocabulario: medios de transporte',
                    '«One or two people» y «by road» describen un vehículo de carretera para pocas personas: '
                    '{{motorbike}}, la motocicleta.',
                    ['Subraya las ideas clave de la definición: «only one or two people» y «go by road».',
                     'Descarta primero por el medio (agua, aire, vías) y luego por la capacidad de personas.'],
                    'only one or two people',
                    ['Lee la definición completa y busca qué vehículo describe.',
                     'Descarta los que no van por carretera: boat, helicopter, plane, train.',
                     'Entre los que sí van por carretera, elige el que lleva solo una o dos personas: motorbike.'])
                sync(q)
            if i == 'eng-i018':
                q['hoja'] = hoja_plantilla_ing(
                    q, 'Comprensión de lectura: tipo de obra',
                    'El texto cuenta que el libro Burning the Days fue llevado al cine con el título Passionate '
                    'Falsehoods, así que es {{a movie}}.',
                    ['Busca en el texto dónde aparece el título «Passionate Falsehoods».',
                     'Fíjate en qué industria se habla en esa parte: cine y películas.'],
                    'Passionate Falsehoods is',
                    ['Identifica qué pregunta el enunciado: qué tipo de obra es.',
                     'Localiza «Passionate Falsehoods» en el texto y lee la frase completa.',
                     'Comprueba qué opción coincide con lo que dice el texto: una película.'])
                sync(q)
            if json.dumps(q, ensure_ascii=False, sort_keys=True) != antes:
                ch = True
                cambios += 1
                o = ov.get(i)
                if o is not None:
                    for k in ('opciones', 'distractores'):
                        if k in o and k in q:
                            o[k] = q[k]
                            ov_ch = True
        if ch:
            json.dump(d, open(f, 'w'), ensure_ascii=False, indent=2)
        if ov_ch:
            json.dump(ov, open(ov_f, 'w'), ensure_ascii=False, indent=2)
    print('preguntas modificadas:', cambios)


if __name__ == '__main__':
    main()
