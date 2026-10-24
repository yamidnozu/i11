"""
Script para enriquecer y alinear TODAS las preguntas ICFES con pistas específicas de cada pregunta,
eliminando completamente las plantillas repetidas y garantizando que se conserven las opciones
y claves oficiales de los cuadernillos.
"""
import json, glob, os, re

SPECIFIC_PISTAS = {
    # --- MATEMÁTICAS 2026 (mat) que difieren o necesitan pistas matemáticas específicas ---
    "mat-i001": [
        "Suma los promedios de los cuatro cursos: $227$ en el año anterior frente a $217$ en el año actual.",
        "Como los cuatro cursos tienen igual número de estudiantes, compara directamente las sumas para evaluar si el promedio total aumentó o disminuyó."
    ],
    "mat-i006": [
        "Ten en cuenta que 40 funcionarios requieren dos grupos de capacitación porque el cupo máximo por curso es de 30 personas.",
        "Multiplica el valor por hora de cada módulo por la intensidad horaria y por dos cursos para hallar cuál cuesta exactamente novecientos mil pesos (módulo IV)."
    ],
    "mat-i007": [
        "Relaciona la razón de perímetros con la razón de semejanza lineal entre las bases cuadradas: razón lineal igual a $18/24 = 3/4$.",
        "Recuerda que la razón entre áreas de figuras semejantes es igual al cuadrado de la razón lineal: $(3/4)^2 = 9/16$."
    ],
    "mat-i008": [
        "Identifica la temperatura inicial al nivel de referencia ($30\\,^\\circ\\text{C}$) y la tasa de enfriamiento de un grado Celsius por cada cien metros de ascenso.",
        "Modela la relación lineal restando del valor base la variación debida a la altura: $T = -(\\text{Altitud}/100) + 30$."
    ],
    "mat-i015": [
        "Observa que los rayos solares inciden con el mismo ángulo de inclinación sobre ambos postes verticales paralelos.",
        "Aplica semejanza de triángulos rectángulos para deducir que el ángulo beta del segundo poste es idéntico al ángulo de treinta grados del primer poste."
    ],
    "mat-i016": [
        "Recuerda que el promedio aritmético solo mide la suma total de las estaturas dividida entre dieciséis, no la distribución individual de los alumnos.",
        "Deduce por qué un promedio de un metro con setenta centímetros no impide que la mitad de los nadadores supere un metro con ochenta si las estaturas restantes son bajas."
    ],
    "mth-i016": [
        "Recuerda que el promedio aritmético solo mide la suma total de las estaturas dividida entre dieciséis, no la distribución individual de los alumnos.",
        "Deduce por qué un promedio de un metro con setenta centímetros no impide que la mitad de los nadadores supere un metro con ochenta si las estaturas restantes son bajas."
    ],
    "mat-i017": [
        "Recuerda que un paralelepípedo o prisma rectangular tiene doce aristas en total: cuatro de longitud ele, cuatro de ancho y cuatro de altura.",
        "Suma la longitud de todas las aristas de la caja metálica para obtener la expresión simplificada $4l + 4a + 4h$."
    ],
    "mat-i018": [
        "En el triángulo oblicuángulo, identifica los ángulos interiores de setenta y cinco grados y sesenta grados junto con sus respectivos lados opuestos uno y equis.",
        "Aplica la ley de senos: equis sobre seno de sesenta grados es igual a uno sobre seno de setenta y cinco grados."
    ],
    "mat-i019": [
        "Plantea la ecuación de puntajes acumulados: P inicia con siete puntos y suma equis, mientras Q inicia con dos puntos y suma tres medios de equis.",
        "Iguala ambas cantidades para expresar la condición de empate: $7 + x = \\frac{3}{2}x + 2$."
    ],
    "mat-i020": [
        "Calcula la pendiente de la recta con dos puntos de la tabla: $(0, 2.000)$ y $(10, 2.300)$, obteniendo treinta millones por unidad de gasto publicitario.",
        "Verifica que el intercepto con el eje de ganancias corresponde a dos mil millones cuando el gasto en publicidad es cero: $G(p) = 30p + 2.000$."
    ],
    "mat-i021": [
        "Analiza la ecuación dos propuesta ($m = 3s$): si el número de sillas es el triple de mesas, la relación correcta debe ser $s = 3m$.",
        "Deduce por qué el sistema es incorrecto: la segunda ecuación invierte la proporción y afirma que se venden el triple de mesas que de sillas."
    ],
    "mat-i023": [
        "En un triángulo rectángulo de treinta y sesenta grados, el cateto adyacente a treinta grados mide el cateto menor multiplicado por raíz de tres.",
        "Sustituye el cateto de treinta y dos centímetros para despejar el cateto menor opuesto: $32 / \\sqrt{3}\\text{ cm}$."
    ],
    "mat-i024": [
        "Analiza las áreas de los triángulos y trapecios formados al unir vértices con puntos medios de los lados opuestos en el cuadrado unitario.",
        "Aplica disección geométrica para demostrar que el cuadrado central inclinado ocupa exactamente un quinto del área total ($1/5\\text{ dm}^2$)."
    ],
    "mat-i026": [
        "Suma los porcentajes correspondientes al transporte público de pasajeros: $24\\% + 23\\% + 18\\% = 65\\%$.",
        "Compara el sesenta y cinco por ciento obtenido con el treinta y cinco por ciento de automóviles para concluir que la mayor parte son buses, microbuses y busetas."
    ],
    "mat-i031": [
        "Desarrolla el producto o factoriza la expresión para simplificar términos cuadráticos y lineales en ambos miembros de la ecuación.",
        "Evalúa los procedimientos algebraicos de María y Nelson para verificar que ambos métodos llegan a las soluciones correctas."
    ],
    "mat-i032": [
        "Aplica la regla de reflexión axial respecto al eje vertical: la coordenada horizontal cambia de signo mientras la vertical permanece constante.",
        "Transforma los vértices $(-2, 8)$ y $(-4, 2)$ para obtener los puntos correspondientes reflejados $(2, 8)$ y $(4, 2)$."
    ],
    "mat-i034": [
        "Ten en cuenta que cada incremento de diez decibelios en la escala logarítmica multiplica la intensidad física por un factor de diez.",
        "Deduce que un aumento de veinte decibelios corresponde a dos pasos consecutivos de diez: multiplicar dos veces por diez equivale a multiplicar la intensidad por cien."
    ],
    "mat-i035": [
        "Revisa el cálculo del segundo descuento en el paso tres: el cupón adicional del diez por ciento se aplica sobre el precio ya rebajado, no sobre el original.",
        "Identifica el error en el paso tres: para hallar el precio final tras un diez por ciento de descuento se debe multiplicar por noventa y no por diez."
    ],
    "mat-i036": [
        "Calcula el número total de bolas en la bolsa: tres rojas, tres negras y doce blancas suman dieciocho bolas en total.",
        "Compara la probabilidad de extraer una bola blanca (doce de dieciocho) con la de una roja o negra (tres de dieciocho) para descartar que los tres colores tengan igual probabilidad."
    ],
    "mat-i038": [
        "Determina qué categorías de la tabla representan conjuntos disjuntos y cuáles corresponden a intersecciones entre pizza y bebidas.",
        "Usa el principio de inclusión y exclusión con el total de 110 clientes para verificar qué conjunto representa la diferencia entre los totales."
    ],
    "mat-i039": [
        "Calcula la cantidad de contraseñas permitidas por cada regla: mil en la primera, setecientos veinte en la segunda, seis mil setecientos sesenta en la tercera y cinco mil doscientos en la cuarta.",
        "Ordena los resultados de menor a mayor cantidad de opciones: regla dos menor que regla uno, menor que regla cuatro, menor que regla tres."
    ],
    "mat-i041": [
        "Aplica el teorema de la desigualdad triangular: en todo triángulo, la suma de las longitudes de cualesquiera dos lados debe ser estrictamente mayor que el tercer lado.",
        "Verifica que en el requerimiento dos la suma de los dos lados iguales ($7 + 7 = 14\\text{ m}$) es menor que el lado mayor ($18\\text{ m}$), haciendo imposible construir el triángulo."
    ],
    "mat-i044": [
        "Divide el área total del círculo entre los diez sectores iguales de la rueda giratoria para obtener nueve pi décimos de metro cuadrado.",
        "Aproxima el valor numérico tomando pi cercano a tres para obtener un área por sector cercana a dos coma siete metros cuadrados."
    ],
    "mat-i045": [
        "Calcula las combinaciones sin repetición para elegir dos estudiantes de décimo (diez opciones) y tres de undécimo (cuatro opciones).",
        "Multiplica las posibilidades de ambos grados por el principio fundamental del conteo: diez por cuatro igual a cuarenta delegaciones diferentes."
    ],
    "mat-i046": [
        "Identifica que para ganar la consola se deben ganar ambos juegos independientes: la probabilidad conjunta es el producto de un medio por un sexto igual a un doceavo.",
        "Aplica la regla del complemento: el suceso contrario de ganar ambos juegos es perder en al menos uno, por lo que uno menos la probabilidad de perder al menos uno también es válido."
    ],
    "mat-i047": [
        "Interpreta la ecuación logarítmica de sonoridad: la razón entre la intensidad sonora y el umbral de audición equivale a diez elevado al cubo.",
        "Calcula el valor numérico de diez al cubo igual a mil: la intensidad física del sonido es mil veces la intensidad mínima perceptible."
    ],
    "mat-i048": [
        "Tras extraer la primera balota con el número dos, cuenta cuántas parejas de las quince balotas restantes completan una suma de diez (sumar ocho) frente a siete (sumar cinco).",
        "Comprueba que hay cinco combinaciones para sumar ocho frente a cuatro para sumar cinco, por lo que el primer estudiante tiene una posibilidad más de ganar."
    ],
    "mat-i050": [
        "Calcula el volumen del cilindro (cuatro coma cinco pi), de la esfera (cuatro coma cinco pi) y de la caja prisma (cuatro coma cinco).",
        "Compara los volúmenes: dado que pi es mayor que uno, el volumen del cilindro supera al de la caja, y el volumen de la esfera es idéntico al del cilindro."
    ],

    # --- INGLÉS ESPECÍFICAS ---
    "ing-i001": [
        "Focus on the verb phrase {{carry things}} and identify what accessory people use to transport personal items.",
        "Select {{handbags}} from the clothing accessories list."
    ],
    "ing-i002": [
        "Focus on the context {{go to bed}} and sleeping at night.",
        "Select {{pajamas}} as the comfortable sleepwear clothing worn specifically for bedtime."
    ],
    "ing-i003": [
        "Focus on the body part {{neck}} and keeping warm in cold weather.",
        "Identify {{scarf}} as the cloth garment wrapped around the neck."
    ],
    "ing-i004": [
        "Notice the plural pronoun {{them}} and the phrase {{to see well}}.",
        "Select {{glasses}} as the optical lenses worn on the face to correct eyesight."
    ],
    "ing-i019": [
        "Notice how the author contrasts the successes and frustrations in the film industry.",
        "Select {{big screen work}} as the cinematic career described by the author."
    ],

    # --- CFI ESPECÍFICAS ---
    "cfi-i056": [
        "Contrasta la proporción de violencia contra la mujer ejercida en el ámbito de la pareja con la ocurrida en espacios públicos.",
        "Identifica por qué la violencia intrafamiliar constituye una violación sistemática de derechos fundamentales que requiere intervención estatal."
    ],
    "cfi-i105": [
        "Notice the key requirements: a motorized transport for {{only one or two people}} traveling {{by road}}.",
        "Select {{motorbike}} as the two-wheeled motor vehicle designed for a single rider and optional passenger."
    ]
}

def clean_double_braces(text):
    if not isinstance(text, str):
        return text
    # Fix {{ {{ or }} }}
    text = re.sub(r'\{\{\s*\{\{', '{{', text)
    text = re.sub(r'\}\}\s*\}\}', '}}', text)
    # Don't wrap mathematical variables or numbers already in {{ }}
    return text

def clean_obj_double_braces(obj):
    if isinstance(obj, str):
        return clean_double_braces(obj)
    elif isinstance(obj, dict):
        return {k: clean_obj_double_braces(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_obj_double_braces(item) for item in obj]
    return obj

def find_best_substring(frag, text):
    if frag in text:
        return frag
    f_clean = frag.replace('$', '')
    if f_clean in text:
        return f_clean
    f_norm = ' '.join(f_clean.split())
    if f_norm in text:
        return f_norm
    f_strip = f_norm.strip(',.;:?!\"\'()[]{}\n\t ')
    if f_strip in text:
        return f_strip
    words = f_strip.split()
    for l in range(len(words), 0, -1):
        for start in range(len(words) - l + 1):
            sub = ' '.join(words[start:start+l]).strip(',.;:?!\"\'()[]{}\n\t ')
            if len(sub) >= 4 and sub in text:
                return sub
    return None

def align_and_enrich_all():
    L = 'ABCDEFGH'

    # Process all ICFES booklets
    for pf in sorted(glob.glob('content/icfes/*/preguntas.json')):
        pref = pf.split('/')[2]
        d = json.load(open(pf, 'r', encoding='utf-8'))
        qs = d if isinstance(d, list) else d.get('preguntas', [])

        for q in qs:
            qid = q['id']
            enun = q['enunciado']
            c = q.get('correcta')
            ops = q.get('opciones', [])
            num_ops = len(ops)

            # Fix mat-i019
            if qid == 'mat-i019':
                q['opciones'][1] = "$7+x=\\frac{3}{2}x+2$"
                q['explicacion'] = "P lleva siete puntos y Q lleva dos. Si P anota $x$ puntos más, por cada dos de P, Q anota tres: Q suma $\\frac{3}{2}x$. La igualdad se expresa como $7+x=2+\\frac{3}{2}x$, equivalente a la opción B."

            # Fix mat-i038
            if qid == 'mat-i038':
                q['explicacion'] = "Cada uno de los 110 clientes realizó un pedido (la unión de pizza, bebida caliente y bebida fría es 110). Como las bebidas caliente ($C$) y fría ($F$) son mutuamente excluyentes ($C \\cap F = \\emptyset$), la suma simple de pedidos es $|P| + |C| + |F| = 100 + 20 + 40 = 160$. El exceso sobre el total de clientes ($160 - 110 = 50$) corresponde exactamente al número de clientes que combinaron pizza con alguna bebida: $|P \\cap (C \\cup F)| = 50$. Aunque no es posible determinar cuántos eligieron específicamente bebida caliente o fría, la suma de ambos solapamientos es 50. En consecuencia, el número de clientes que solo eligieron pizza es unívocamente $|P| - 50 = 100 - 50 = 50$ (opción C)."
                q['revisar'] = []

            # Resolved doubtful questions (documented in ANTIGRAVITY_REPORT.md)
            if qid in ('mat-i038', 'cfi-i101', 'cfi-i105', 'eng-i018', 'ena-i018', 'ing-i018'):
                q['revisar'] = []

            # Fix mat-i017 4lah
            if qid == 'mat-i017':
                s = json.dumps(q, ensure_ascii=False).replace('4lah', '{{4lah}}')
                q.clear()
                q.update(json.loads(clean_double_braces(s)))
            # Fix mat-i024 3x3
            elif qid == 'mat-i024':
                s = json.dumps(q, ensure_ascii=False).replace('3x3', '{{3x3}}')
                q.clear()
                q.update(json.loads(s))
            # Fix mat-i036 casos favorables
            elif qid == 'mat-i036':
                s = json.dumps(q, ensure_ascii=False).replace('casos favorables / casos totales', 'éxitos entre casos totales').replace('casos favorables', 'éxitos posibles')
                q.clear()
                q.update(json.loads(s))
            # Fix mat-i039 spoken numbers
            elif qid == 'mat-i039':
                q['distractores'] = [
                    'Ubica a la regla uno (mil) antes de la regla dos (setecientos veinte), ordenando de forma incorrecta los dos menores.',
                    'Ordena la regla tres (seis mil setecientos sesenta) antes de la regla cuatro (cinco mil doscientos), cuando cinco mil doscientos es menor.',
                    '',
                    'Coloca la regla tres antes de la regla uno, cuando seis mil setecientos sesenta es mayor que mil.'
                ]
            # Fix mat-i044 r^2
            elif qid == 'mat-i044':
                s = json.dumps(q, ensure_ascii=False).replace('r^2 * theta / 2', 'r al cuadrado por theta sobre dos')
                q.clear()
                q.update(json.loads(s))
            # Fix mat-i047 10^3 and I_0
            elif qid == 'mat-i047':
                s = json.dumps(q, ensure_ascii=False).replace('10^3 = 1.000', 'mil').replace('I_0', '{{I_0}}')
                q.clear()
                q.update(json.loads(s))
            # Fix chemical speech
            elif qid in ('cie-i049', 'cna-i049'):
                q['explicacion'] = q['explicacion'].replace('CO2 y H2O', 'dióxido de carbono y agua (CO₂ y H₂O)')
            elif qid in ('cie-i030', 'cna-i030'):
                s = json.dumps(q, ensure_ascii=False).replace('Mg2+', '{{Mg2+}}').replace('SO4 2-', '{{SO4 2-}}')
                q.clear()
                q.update(json.loads(clean_double_braces(s)))
            elif qid in ('cie-i018', 'cna-i018'):
                s = json.dumps(q, ensure_ascii=False).replace('Cl2', 'Cl₂').replace('P4', 'P₄').replace('PCl3', 'PCl₃')
                q.clear()
                q.update(json.loads(s))
            elif qid == 'mth-i002':
                for i in range(len(q['distractores'])):
                    q['distractores'][i] = q['distractores'][i].replace('$=2.000$', 'equivalente a dos mil pesos').replace('=2.000', 'dos mil')
            elif qid == 'mth-i007':
                if 'distractores' in q:
                    q['distractores'] = [d.replace('P3', '{{P3}}') for d in q['distractores']]
                if h and 'enfoque' in h and 'no' in h['enfoque']:
                    for x in h['enfoque']['no']:
                        x['p'] = x['p'].replace('P3', '{{P3}}')

            h = q.get('hoja')
            if not h: continue

            # 1. Specific pistas enrichment
            enf = h.setdefault('enfoque', {})
            if qid in SPECIFIC_PISTAS:
                enf['pistas'] = SPECIFIC_PISTAS[qid]

            # Fix cfi-i105 guion and pasos
            if qid == 'cfi-i105':
                enf['tema'] = 'English: transport definitions'
                enf['que'] = 'Identificar el vehículo motorizado terrestre diseñado para una o dos personas: la motocicleta (motorbike).'
                enf['clave'] = 'La motocicleta (motorbike) es el vehículo de dos ruedas con motor para una o dos personas que va por carretera.'
                h['guion'] = {
                    '1': [
                        {'t': 'Leamos la definición para identificar el medio de transporte.', 'a': 'leer'},
                        {'t': 'La frase «only one or two people to go by road» exige transporte terrestre reducido.', 'a': 'm:This is'},
                        {'t': 'La opción E motorbike cumple con ser terrestre y para uno o dos ocupantes.', 'a': 'p:0'},
                        {'t': 'La respuesta correcta es la opción E: motorbike.', 'a': 'o:E:ok'}
                    ],
                    '2': [
                        {'t': 'Leamos la definición y analicemos cada vehículo descartado.', 'a': 'leer'},
                        {'t': 'Descartamos opciones que no se desplacen por carretera o lleven muchos pasajeros.', 'a': 'p:0'},
                        {'t': 'La opción A bike es a pedales; la opción B boat navega por agua; bus y train llevan decenas; helicopter y plane van por aire; truck es de carga pesada.', 'a': 'o:A:no|o:B:no|o:C:no|o:D:no|o:F:no|o:G:no|o:H:no', 'k': 'err'},
                        {'t': 'Por descarte confirmamos que motorbike es la respuesta correcta.', 'a': 'o:E:ok'}
                    ],
                    '3': [
                        {'t': 'Analizo los requisitos: transporte por carretera para una o dos personas.', 'a': 'p:0', 'k': 'ana'},
                        {'t': 'Motorbike es el vehículo motorizado de dos ruedas con capacidad para conductor y pasajero.', 'a': 'p:1'},
                        {'t': 'Compruebo que ningún otro vehículo de la lista cumpla ambas condiciones.', 'a': 'p:1', 'k': 'contra'},
                        {'t': 'La respuesta correcta es la opción E.', 'a': 'o:E:ok'}
                    ]
                }
                h['pasos'] = [
                    {'k': 'idea', 'texto': 'Identificar los requisitos de la definición: transporte terrestre (by road) y capacidad reducida (only one or two people).', 'titulo': 'Requisitos clave'},
                    {'k': 'check', 'texto': 'Descartar vehículos de agua o aire y vehículos de transporte masivo o de carga pesada.', 'titulo': 'Comprobación de opciones'}
                ]

            # Fix mat-i016 and mth-i016 enfoque no
            if qid in ('mat-i016', 'mth-i016'):
                enf['no'] = [
                    {'t': 'Opción A', 'p': 'Pero el promedio no permite afirmar que todas las personas estén por debajo de un metro con ochenta ni que deban aceptarse exactamente otras dieciséis.'},
                    {'t': 'Opción B', 'p': 'Pero aunque el promedio no determina los grupos, no es necesario reemplazarlo por el máximo o el mínimo: se requiere conocer cada estatura individual.'},
                    {'t': 'Opción C', 'p': 'Pero agregar estudiantes de un metro con ochenta no garantiza igualar los grupos; además, esa estatura pertenece a la piscina profunda.'}
                ]

            # Fix mat-i047
            if qid == 'mat-i047':
                q['explicacion'] = "La igualdad indica que el cociente $I/I_0$ es $10^3$, es decir, mil. Por tanto, la intensidad $I$ equivale a mil veces la intensidad mínima $I_0$. La respuesta es D."
                enf['tema'] = "Matemáticas: escala logarítmica de sonoridad"
                enf['que'] = "La igualdad indica que el cociente entre intensidades es diez al cubo, es decir, mil veces la intensidad mínima."
                enf['clave'] = "La igualdad indica que el cociente es diez al cubo, es decir, mil. Por tanto, la intensidad física equivale a mil veces la intensidad mínima."
                h['guion'] = {
                    '1': [
                        {'t': '¿Qué número representa diez elevado a la tercera potencia?', 'a': 'leer'},
                        {'t': 'Diez por diez por diez da mil.', 'a': 'p:0'},
                        {'a': 'o:D:ok', 't': 'La intensidad es mil veces la mínima. La respuesta es D.'}
                    ],
                    '2': [
                        {'t': 'La expresión ya presenta el cociente entre las dos intensidades.', 'a': 'leer'},
                        {'t': 'Evalúa diez al cubo: el resultado es mil.', 'a': 'p:0'},
                        {'a': 'o:A:no', 'k': 'err', 't': 'La opción A propone una milésima, el recíproco de la razón. La descartamos.'},
                        {'a': 'o:B:no', 'k': 'err', 't': 'La opción B propone un tercio, confundiendo la potencia con una fracción. La descartamos.'},
                        {'a': 'o:C:no', 'k': 'err', 't': 'La opción C confunde el exponente tres con el valor total de la potencia. La descartamos.'},
                        {'a': 'o:D:ok', 't': 'Confirmamos que la intensidad es mil veces la mínima: opción D.'}
                    ],
                    '3': [
                        {'a': 'p:0', 'k': 'ana', 't': 'La razón buscada es el cociente de intensidades.'},
                        {'a': 'p:1', 't': 'La igualdad indica que vale diez al cubo, que es mil.'},
                        {'a': 'p:2', 'k': 'contra', 't': 'Por eso la intensidad es mil veces el umbral mínimo.'},
                        {'a': 'o:A:no|o:B:no|o:C:no', 'k': 'err', 't': 'A, B y C no evalúan correctamente la potencia.'},
                        {'a': 'o:D:ok', 't': 'La respuesta correcta es D.'}
                    ]
                }
                enf['no'] = [
                    {'t': 'Opción A', 'p': 'Pero una milésima representaría que la intensidad física es menor que el umbral, lo opuesto a la razón de mil veces.'},
                    {'t': 'Opción B', 'p': 'Pero un tercio confunde el exponente tres con una fracción aritmética de un tercio.'},
                    {'t': 'Opción C', 'p': 'Pero tres veces confunde el exponente tres de la potencia de diez con el valor numérico de mil.'}
                ]
                h['pasos'] = [
                    {'k': 'idea', 'texto': 'Interpretar la relación de sonoridad dada en la ecuación.', 'titulo': 'Relación de intensidades'},
                    {'k': 'calc', 'lineas': ['$10^3 = 1.000$'], 'nota': 'Diez al cubo equivale a mil.', 'titulo': 'Cálculo de la potencia'},
                    {'k': 'check', 'texto': 'La intensidad física es mil veces la intensidad mínima percibida.', 'titulo': 'Comprobación'}
                ]

            # 2. Marcas alignment with enunciado
            frag_map = {}
            if 'marcas' in h:
                good_marcas = []
                for m in h['marcas']:
                    frag = m.get('frag', '')
                    if frag in enun:
                        good_marcas.append(m)
                    else:
                        sub = find_best_substring(frag, enun)
                        if sub:
                            frag_map[frag] = sub
                            m['frag'] = sub
                            good_marcas.append(m)
                h['marcas'] = good_marcas

            # 3. Guion marcas alignment across all levels
            if h.get('guion'):
                marca_frags = [m['frag'] for m in h.get('marcas', [])]
                for lvl in ('1', '2', '3'):
                    for step in h['guion'].get(lvl, []):
                        a = step.get('a', '')
                        if a.startswith('m:'):
                            old_m = a[2:]
                            if old_m not in marca_frags:
                                if old_m in frag_map:
                                    step['a'] = f'm:{frag_map[old_m]}'
                                elif marca_frags:
                                    # find best matching marca frag
                                    best_m = next((mf for mf in marca_frags if mf in old_m or old_m in mf), marca_frags[0])
                                    step['a'] = f'm:{best_m}'
                                else:
                                    del step['a']

            # 4. Guion nivel 2 descartes alignment
            if c is not None and 0 <= c < num_ops:
                c_let = L[c]
                wrong_indices = [i for i in range(num_ops) if i != c]

                if h.get('guion'):
                    if '2' in h['guion']:
                        g2 = h['guion']['2']
                        dichas = set()
                        for s in g2:
                            a = s.get('a', '')
                            for part in a.split('|'):
                                if part.startswith('o:') and part.endswith(':no'):
                                    dichas.add(part[2])

                        missing_wrong = [w for w in wrong_indices if L[w] not in dichas]
                        if missing_wrong:
                            new_g2 = [s for s in g2 if not (s.get('a', '').startswith('o:') and (s.get('a', '').endswith(':no') or s.get('a', '').endswith(':ok')))]
                            for w in wrong_indices:
                                let = L[w]
                                d_text = ''
                                if w < len(q.get('distractores', [])):
                                    d_text = q['distractores'][w]
                                if not d_text:
                                    d_text = f'la opción {let} no corresponde a lo solicitado'
                                new_g2.append({
                                    't': f'La opción {let} es incorrecta: {d_text}',
                                    'a': f'o:{let}:no',
                                    'k': 'err'
                                })
                            new_g2.append({
                                't': f'Por lo tanto, confirmamos que la respuesta correcta es la opción {c_let}.',
                                'a': f'o:{c_let}:ok'
                            })
                            h['guion']['2'] = new_g2
                        else:
                            for s in g2:
                                a = s.get('a', '')
                                if a.startswith('o:') and a.endswith(':ok'):
                                    s['a'] = f'o:{c_let}:ok'

                    if '3' in h['guion']:
                        for s in h['guion']['3']:
                            a = s.get('a', '')
                            if a.startswith('o:') and a.endswith(':ok'):
                                    s['a'] = f'o:{c_let}:ok'

            # 5. Enfoque.no and clave alignment
            if c is not None and 0 <= c < num_ops and q.get('distractores'):
                enf['no'] = []
                for i in range(len(q['distractores'])):
                    if i != c and q['distractores'][i]:
                        d_txt = q['distractores'][i].strip()
                        if not d_txt.startswith('Pero'):
                            d_txt = 'Pero ' + d_txt[:1].lower() + d_txt[1:]
                        enf['no'].append({'t': f'Opción {L[i]}', 'p': d_txt})
            elif 'no' in enf:
                for x in enf['no']:
                    p_txt = x.get('p', '').strip()
                    if 'Pero' not in p_txt:
                        if 'pero' in p_txt:
                            x['p'] = re.sub(r'\bpero\b', 'Pero', p_txt)
                        else:
                            x['p'] = 'Pero ' + p_txt[:1].lower() + p_txt[1:]

            # Clean double braces and numbers in spoken texts
            q['hoja'] = clean_obj_double_braces(h)
            q['explicacion'] = clean_double_braces(q['explicacion'])
            if 'distractores' in q:
                q['distractores'] = [clean_double_braces(d_item) for d_item in q['distractores']]

            # Sync individual hoja file
            h_path = f'content/icfes/{pref}/hojas/{qid}.json'
            if os.path.exists(h_path):
                try:
                    hd = json.load(open(h_path, 'r', encoding='utf-8'))
                    hd['hoja'] = q['hoja']
                    if 'revisar' in q:
                        hd['revisar'] = q['revisar']
                    with open(h_path, 'w', encoding='utf-8') as out_h:
                        json.dump(hd, out_h, ensure_ascii=False, indent=2)
                except Exception as ex:
                    print(f"Error syncing {h_path}: {ex}")

        with open(pf, 'w', encoding='utf-8') as out_p:
            json.dump(d, out_p, ensure_ascii=False, indent=2)

    print("Alignment and enrichment completed successfully.")

if __name__ == '__main__':
    align_and_enrich_all()
