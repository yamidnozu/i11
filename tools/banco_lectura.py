"""Generador de preguntas originales de Lectura Crítica para el Banco Propio.
Crea 34 preguntas (lec-007 a lec-040) cumpliendo el estándar ICFES:
- Fragmentos de lectura reflexivos, argumentativos, literarios y filosóficos
- 4 opciones de respuesta distintas
- Explicaciones pedagógicas detalladas de comprensión lectora
- 3 distractores específicos explicando el error de comprensión (literalismo, sobreinterpretación, confusión de premisa, etc.)
- Competencias oficiales: Contenidos locales, Articulación global, Evaluación crítica y reflexiva
"""
import json

PREGUNTAS_LEC = [
    {
        "id": "lec-007",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "Lea el siguiente fragmento: «En la era digital, la atención humana se ha convertido en el recurso más codiciado del mercado. Las plataformas no nos cobran dinero; cobran en tiempo y concentración, pues esa es la moneda con la que comercian ante los anunciantes». Según el contexto del texto, ¿qué significa la palabra 'moneda'?",
        "opciones": [
            "Un disco metálico acuñado por el banco central para pagar compras físicas.",
            "El medio de intercambio y valor con el que las plataformas negocian y obtienen ganancias.",
            "Una reliquia histórica de colección numismática.",
            "Una tarjeta plástica bancaria con chip electrónico."
        ],
        "correcta": 1,
        "explicacion": "En el contexto figurado del texto, el autor utiliza 'moneda' como una metáfora económica para designar el bien valioso (el tiempo y la atención de los usuarios) que sirve como instrumento de cambio e intermediación para generar dividendos con los anunciantes publicitarios.",
        "distractores": [
            "Toma el sentido estrictamente literal de una moneda física de metal, ignorando el uso metafórico en el texto digital.",
            "",
            "Confunde el término con antigüedades o piezas de colección, descontextualizando el fragmento.",
            "Confunde la moneda con una tarjeta bancaria física, alejándose del significado del texto."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Comprende el significado contextual y figurado de palabras dentro de un texto argumentativo."
    },
    {
        "id": "lec-008",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "Lea la siguiente oración: «Muchos ciudadanos asumen que la democracia se agota en el acto solitario de depositar un voto cada cuatro años; sin embargo, esta constituye un ejercicio cotidiano de deliberación y vigilancia comunitaria». ¿A qué se refiere la palabra 'esta' en la oración?",
        "opciones": [
            "A la urna electoral.",
            "A la democracia.",
            "A la vigilancia comunitaria.",
            "A la periodicidad de cuatro años."
        ],
        "correcta": 1,
        "explicacion": "El pronombre demostrativo anafórico 'esta' remite al sujeto principal de la discusión contrastada: la democracia. El autor contrapone la visión pasiva de la democracia (reducida a votar) con su verdadera naturaleza activa y cotidiana.",
        "distractores": [
            "Refiere a la urna o al acto de votar, cuando el autor precisamente busca redefinir la democracia.",
            "",
            "Confunde el referente con el predicado que apenas se está introduciendo en la oración.",
            "Toma el complemento temporal de cuatro años, perdiendo el sentido gramatical de la concordancia de género."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Identifica referentes anafóricos y relaciones gramaticales dentro de una oración compuesta."
    },
    {
        "id": "lec-009",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "Lea el siguiente texto: «A pesar de las severas advertencias emitidas por los geólogos sobre la inestabilidad del terreno, los constructores, motivados por la especulación inmobiliaria y respaldados por licencias cuestionables, levantaron el edificio en la ladera». ¿Quiénes son los sujetos directos que realizaron la acción de levantar el edificio?",
        "opciones": [
            "Los geólogos.",
            "Los constructores.",
            "Las licencias cuestionables.",
            "Los habitantes de la ladera."
        ],
        "correcta": 1,
        "explicacion": "En la estructura sintáctica de la oración, el sujeto del verbo principal 'levantaron' son 'los constructores'. Las frases intermedias sobre los geólogos, la especulación y las licencias son complementos circunstanciales y modificadores explicativos.",
        "distractores": [
            "Atribuye la acción a los geólogos, quienes por el contrario fueron los que emitieron las advertencias de riesgo.",
            "",
            "Confunde los instrumentos administrativos (licencias) con los agentes humanos que ejecutan la construcción.",
            "Menciona a los habitantes, quienes no figuran como agentes constructores en el enunciado."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Identifica el sujeto gramatical y los agentes de la acción en oraciones con incisos explicativos."
    },
    {
        "id": "lec-010",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "Lea la frase: «Las palabras del viejo maestro fueron un bálsamo para el joven artista tras el rotundo fracaso de su primera exposición». ¿Qué figura retórica y sentido se emplea en la expresión subrayada?",
        "opciones": [
            "Una metáfora que sugiere que las palabras brindaron consuelo, alivio y serenidad emocional.",
            "Una hipérbole que indica que el maestro aplicó una crema medicinal sobre la piel del joven.",
            "Una personificación que atribuye vida humana a las pinturas fracasadas.",
            "Una ironía con la que el autor se burla del talento del joven artista."
        ],
        "correcta": 0,
        "explicacion": "El autor utiliza una metáfora ('fueron un bálsamo'): compara las palabras de aliento del maestro con una sustancia balsámica o medicinal que calma el dolor de las heridas físicas, transmitiendo que el consejo mitigó el sufrimiento moral y anímico del joven pintor.",
        "distractores": [
            "",
            "Interpreta el bálsamo en sentido literal farmacológico, confundiéndolo erróneamente con una hipérbole.",
            "Clasifica erróneamente la figura como personificación, figura que atribuye rasgos humanos a seres inanimados.",
            "Asume que hay tono irónico y burlesco, cuando el tono del fragmento es empático y reconfortante."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Interpreta figuras literarias (metáforas) y su significado emotivo en textos literarios y ensayísticos."
    },
    {
        "id": "lec-011",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "Lea el siguiente fragmento de una columna de opinión: «¡Qué proeza formidable! Nuestros ilustres gobernantes han tardado solo catorce años y triplicado el presupuesto original para inaugurar un puente peatonal de veinte metros que, para colmo, carece de rampas de acceso para personas con discapacidad». ¿Cuál es el tono predominante del autor?",
        "opciones": [
            "Elogioso y de profunda admiración hacia los ingenieros de la obra.",
            "Irónico y mordaz, criticando la ineficiencia y el despilfarro mediante alabanzas fingidas.",
            "Triste y resignado, aceptando la fatalidad como algo natural.",
            "Objetivo y estrictamente neutral, limitándose a reportar datos sin emitir juicios."
        ],
        "correcta": 1,
        "explicacion": "El autor recurre a la ironía clásica: califica de 'proeza formidable' y llama 'ilustres gobernantes' a quienes tardaron catorce años y malgastaron el erario en una obra deficiente. El elogio inicial contrasta violentamente con los hechos denunciados para ridiculizar la negligencia gubernamental.",
        "distractores": [
            "Toma el elogio al pie de la letra sin comprender el artificio de la ironía satírica.",
            "",
            "Confunde el sarcasmo indignado con una actitud de resignación pasiva.",
            "Sostiene que el texto es neutro, ignorando los signos de exclamación y adjetivos claramente valorativos."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Reconoce el tono, la actitud y la intención comunicativa (ironía, sarcasmo) del autor de un texto."
    },
    {
        "id": "lec-012",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "Lea el siguiente pasaje: «La serendipia no es una mera casualidad pasiva; se define con rigor como la facultad de encontrar hallazgos afortunados e inesperados mientras se está buscando afanosamente otra cosa, siempre y cuando la mente esté preparada para interpretarlos». Según el autor, ¿cuál condición es indispensable para que ocurra la serendipia?",
        "opciones": [
            "Quedarse en reposo esperando que la suerte actúe sin intervenir.",
            "Poseer una mente atenta y preparada capaz de reconocer e interpretar el valor del hallazgo imprevisto.",
            "Gastar grandes sumas de dinero en billetes de lotería.",
            "Buscar deliberadamente aquello que ya se conocía de antemano."
        ],
        "correcta": 1,
        "explicacion": "El texto define explícitamente que la serendipia exige dos factores complementarios: el hallazgo inesperado durante una búsqueda activa y la condición imprescindible de que 'la mente esté preparada para interpretarlos', como sentenció Pasteur con respecto a la ciencia.",
        "distractores": [
            "Afirma una actitud pasiva, lo cual es expresamente descartado en la primera línea del texto.",
            "",
            "Confunde la serendipia científica y cognitiva con juegos de azar comerciales.",
            "Propone buscar lo ya conocido, contradiciendo la naturaleza inesperada del descubrimiento."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Localiza e interpreta definiciones explícitas y condiciones causales en textos expositivos."
    },
    {
        "id": "lec-013",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "En la frase: «El testigo prefirió morderse la lengua durante el juicio para no incriminar a su hermano», la expresión subrayada 'morderse la lengua' significa que el testigo:",
        "opciones": [
            "Sufrió una herida accidental en la boca con sus propios dientes.",
            "Se contuvo deliberadamente de hablar o revelar lo que sabía.",
            "Fue obligado a comer alimentos picantes antes de declarar.",
            "Perdió la memoria y olvidó su testimonio."
        ],
        "correcta": 1,
        "explicacion": "La locución idiomática en lengua española 'morderse la lengua' se utiliza de manera figurada para denotar el esfuerzo voluntario y consciente que hace una persona para callar y reservarse una opinión o información que estaba tentada a decir.",
        "distractores": [
            "Interpreta la frase hecha en su sentido anatómico literal, ignorando el modismo coloquial.",
            "",
            "Inventa una situación de consumo de alimentos sin ningún asidero en el contexto judicial.",
            "Confunde el acto voluntario de guardar silencio con un problema patológico de amnesia."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Comprende el significado de modismos y expresiones idiomáticas en contextos narrativos."
    },
    {
        "id": "lec-014",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "Lea el fragmento: «A diferencia de las opiniones efímeras que florecen y mueren al ritmo frenético de las redes sociales, los clásicos de la literatura ofrecen verdades perdurables sobre la condición humana». En este fragmento, ¿cuál palabra funciona como antónimo directo del término 'efímeras'?",
        "opciones": [
            "Frenético.",
            "Perdurables.",
            "Sociales.",
            "Literarias."
        ],
        "correcta": 1,
        "explicacion": "El texto plantea una antítesis directa: contrapone las opiniones 'efímeras' (pasajeras, fugaces, de muy corta duración que nacen y mueren rápido) con las verdades 'perdurables' (duraderas, que subsisten a lo largo del tiempo) de los clásicos. Por ende, 'perdurables' es el antónimo contextual exacto.",
        "distractores": [
            "Elige 'frenético', adjetivo que califica el ritmo pero no es el opuesto de efímero.",
            "",
            "Elige 'sociales', término de pertenencia colectiva sin relación de oposición temporal.",
            "Elige 'literarias', campo artístico que no se opone semánticamente a la fugacidad."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Reconoce relaciones semánticas de antonimia y contrastes léxicos en fragmentos comparativos."
    },
    {
        "id": "lec-015",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "Lea la frase: «No es la ausencia de miedo lo que define al valiente, sino la capacidad de actuar con determinación a pesar de experimentarlo». Según esta afirmación, el valiente se caracteriza por:",
        "opciones": [
            "Carecer por completo de cualquier tipo de temor o angustia.",
            "Reconocer el miedo pero sobreponerse a él para llevar a cabo la acción necesaria.",
            "Huir velozmente ante el primer indicio de peligro.",
            "Obligar a los demás a asumir los riesgos en su lugar."
        ],
        "correcta": 1,
        "explicacion": "La estructura 'No es A sino B' desmiente explícitamente que la valentía sea la falta de miedo (A). Por el contrario, afirma que el rasgo definitorio del valiente radica en la capacidad moral y práctica de actuar a pesar de sentir el temor (B).",
        "distractores": [
            "Afirma que no tiene miedo, lo cual es textualmente negado por la primera parte de la frase ('No es la ausencia de miedo').",
            "",
            "Describe una actitud cobarde de evasión contraria a la valentía.",
            "Le atribuye un comportamiento manipulador ajeno al concepto de valentía formulado."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Interpreta oraciones contrastivas con la estructura adversativa 'no es... sino'."
    },
    {
        "id": "lec-016",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "Lea el fragmento: «El antropoceno es un término acuñado por los geocientíficos para designar la época geológica actual, caracterizada por el hecho inédito de que las actividades humanas se han convertido en la fuerza biofísica dominante que altera los ciclos planetarios». Según el texto, ¿qué distingue al antropoceno de las épocas geológicas precedentes?",
        "opciones": [
            "La total desaparición de la vida animal sobre la Tierra.",
            "El papel protagónico y masivo de la humanidad en la alteración de los sistemas y estratos biofísicos de la Tierra.",
            "El enfriamiento polar que cubrió de glaciares todos los continentes.",
            "La caída de un gran asteroide en la cuenca del océano Pacífico."
        ],
        "correcta": 1,
        "explicacion": "El rasgo distintivo del antropoceno formulado en el texto es que, por primera vez en la historia de la Tierra, una sola especie biológica (los seres humanos) ejerce una influencia de tal magnitud que transforma los ciclos climáticos, geológicos y biogeoquímicos planetarios.",
        "distractores": [
            "Afirma la extinción biológica total de la fauna, evento que no se menciona en la definición.",
            "",
            "Confunde el antropoceno con las glaciaciones del pleistoceno.",
            "Atribuye el origen a un impacto de meteorito, confundiendo la época actual con el límite Cretácico-Paleógeno."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Comprende conceptos especializados y tecnicismos a partir de su definición textual."
    },
    {
        "id": "lec-017",
        "area": "lectura_critica",
        "evidencia": "LEC_E1.1",
        "nivel": 2,
        "enunciado": "En el enunciado: «El informe corporativo asegura que la compañía es 'completamente ecológica', mientras sus chimeneas arrojan toneladas de humo negro al amanecer», ¿qué función cumplen las comillas en la frase 'completamente ecológica'?",
        "opciones": [
            "Indican que el autor está plenamente de acuerdo con la afirmación de la empresa.",
            "Expresan distanciamiento, duda o ironía crítica respecto a la veracidad de la afirmación de la compañía.",
            "Destacan un término científico en un idioma extranjero.",
            "Indican el título de una novela premiada internacionalmente."
        ],
        "correcta": 1,
        "explicacion": "El uso de comillas irónicas o de distanciamiento se emplea para citar palabras ajenas de las cuales el autor no se hace responsable o cuya veracidad cuestiona abiertamente, como se evidencia por el contraste con las chimeneas humeantes.",
        "distractores": [
            "Supone que el autor respalda la afirmación, cuando la segunda mitad del texto la desmiente como una contradicción flagrante.",
            "",
            "Confunde las comillas irónicas con comillas de préstamos lingüísticos o extranjerismos.",
            "Confunde una expresión publicitaria cuestionada con el título de una obra literaria."
        ],
        "origen": "original",
        "competencia": "Identificar y entender contenidos locales",
        "afirmacion": "Identifica las funciones discursivas de los signos de puntuación (uso de comillas para distanciamiento e ironía)."
    },
    {
        "id": "lec-018",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Lea el siguiente texto argumentativo: «La creencia de que la automatización y la inteligencia artificial destruirán todo el empleo humano pasa por alto la historia económica. Cada gran revolución tecnológica eliminó ocupaciones obsoletas, pero a la vez creó sectores productivos enteros que antes eran inimaginables. El verdadero desafío ético y educativo no es frenar la tecnología, sino reformar nuestros sistemas educativos para preparar a las personas en habilidades creativas, empáticas y de juicio crítico que las máquinas jamás podrán replicar». ¿Cuál es la tesis central defendida por el autor?",
        "opciones": [
            "La inteligencia artificial debe ser prohibida por decreto para proteger a los trabajadores.",
            "Las máquinas reemplazarán de forma inevitable e irreversible el 100 % de los puestos de trabajo.",
            "El reto frente a la automatización no es oponerse a la tecnología, sino transformar la educación hacia habilidades humanas insustituibles.",
            "La historia económica demuestra que la tecnología nunca ha cambiado el mercado laboral."
        ],
        "correcta": 2,
        "explicacion": "La tesis central es la proposición nuclear que el autor sostiene y argumenta a lo largo del párrafo: rechaza el pánico catastrofista sobre el fin del trabajo y plantea que la solución radica en adaptar el modelo educativo para potenciar las destrezas exclusivamente humanas (creatividad, empatía y pensamiento crítico).",
        "distractores": [
            "Propone una prohibición estatal de la IA, postura frontalmente opuesta a lo que argumenta el autor.",
            "Asume la postura catastrofista que el texto busca refutar expresamente desde la primera línea.",
            "",
            "Afirma falsamente que la tecnología no cambia el mercado, cuando el autor reconoce que sí destruye empleos obsoletos y crea nuevos."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Identifica la tesis principal y los argumentos centrales en textos ensayísticos y de opinión."
    },
    {
        "id": "lec-019",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Lea la frase: «El candidato dedicó meses enteros a recorrer los municipios más apartados y presentó un plan de gobierno riguroso; no obstante, su bajo índice de popularidad en los centros urbanos le impidió ganar las elecciones». ¿Qué relación lógica introduce el conector 'no obstante'?",
        "opciones": [
            "Una relación de causa y efecto.",
            "Una relación de oposición o concesión entre el esfuerzo desplegado y el resultado electoral adverso.",
            "Una relación temporal de simultaneidad.",
            "Una relación de adición o suma de argumentos favorables."
        ],
        "correcta": 1,
        "explicacion": "'No obstante' es un conector discursivo adversativo o concesivo. Se utiliza para introducir una limitación, contraste o resultado contrario a lo que lógicamente cabría esperar de la premisa anterior (a pesar del arduo recorrido y buen plan de gobierno, el resultado final fue desfavorable).",
        "distractores": [
            "Confunde la adversación con la causa-efecto (que usaría conectores como 'porque' o 'por tanto').",
            "",
            "Confunde el contraste lógico con una marca cronológica de tiempo (como 'mientras tanto').",
            "Confunde la oposición de ideas con una adición acumulativa (como 'además' o 'asimismo')."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Reconoce la función de los conectores lógicos de oposición y concesión en la cohesión textual."
    },
    {
        "id": "lec-020",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Complete adecuadamente el siguiente enunciado respetando la coherencia semántica: «Las pruebas de laboratorio demostraron de manera concluyente que la muestra de agua contenía concentraciones de mercurio diez veces superiores a la norma máxima permitida; _______, las autoridades sanitarias ordenaron la clausura inmediata del pozo de abastecimiento».",
        "opciones": [
            "por consiguiente",
            "en cambio",
            "a pesar de que",
            "en primer lugar"
        ],
        "correcta": 0,
        "explicacion": "La segunda proposición (la clausura de la fuente de agua) es la consecuencia directa, obligada y lógica del hallazgo de contaminación extrema expresado en la primera proposición. Por ello, requiere un conector consecutivo de causa-efecto como 'por consiguiente' (o 'por tanto', 'en consecuencia').",
        "distractores": [
            "",
            "Utiliza 'en cambio', conector de contraste que sugeriría que la clausura es opuesta al hallazgo.",
            "Utiliza 'a pesar de que', conector concesivo que rompería la relación de causa y efecto.",
            "Utiliza 'en primer lugar', marcador de orden u ordenación discursiva que no expresa consecuencia lógica."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Selecciona conectores lógicos consecutivos para restablecer la coherencia argumentativa en oraciones complejas."
    },
    {
        "id": "lec-021",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Un ensayo sobre la soledad contemporánea inicia con la narración detallada de un anciano en Tokio que contrata a actores profesionales para que simulen ser sus hijos y almuercen con él los domingos. En el segundo párrafo, el autor comienza a analizar estadísticas globales sobre el aislamiento social en las metrópolis. ¿Qué función cumple el relato del primer párrafo respecto al resto del texto?",
        "opciones": [
            "Desmentir las estadísticas científicas que se presentarán más adelante.",
            "Servir como un caso ilustrativo conmovedor que engancha al lector y contextualiza vivencialmente el problema abstracto.",
            "Concluir definitivamente el ensayo sin necesidad de más argumentos.",
            "Hacer publicidad a las agencias teatrales japonesas."
        ],
        "correcta": 1,
        "explicacion": "En la retórica del ensayo moderno, el gancho narrativo o anécdota inicial cumple una función pedagógica y persuasiva: aterriza un fenómeno social abstracto y complejo en una vivencia humana singular y tangible, despertando el interés y la empatía del lector antes de desplegar el análisis conceptual y estadístico.",
        "distractores": [
            "Sostiene que el relato busca desmentir las estadísticas, cuando en realidad las dos partes se complementan.",
            "",
            "Confunde una introducción anecdótica con la conclusión final del texto.",
            "Le atribuye un propósito publicitario comercial que desconoce la naturaleza sociológica y literaria del ensayo."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Analiza la función estructural de anécdotas y casos particulares en la introducción de textos argumentativos."
    },
    {
        "id": "lec-022",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Lea el fragmento: «Muchos defensores del transporte individual argumentan que los automóviles eléctricos resolverán por sí solos la crisis ambiental urbana porque no emiten gases de escape en el tubo de escape. Sin embargo, este argumento ignora que la fabricación de sus baterías requiere una minería intensiva de litio y cobalto, y que si la electricidad que los recarga proviene de plantas de carbón, la contaminación simplemente se traslada de lugar geográfico». En este pasaje, la mención de la minería de litio y las plantas de carbón cumple la función de:",
        "opciones": [
            "Apoyar sin reservas la masificación de los automóviles particulares.",
            "Actuar como un contraargumento que evidencia los límites y costos ambientales ocultos de la movilidad eléctrica individual.",
            "Demostrar que los automóviles a gasolina son completamente limpios y renovables.",
            "Prohibir el uso de cualquier batería en los teléfonos celulares."
        ],
        "correcta": 1,
        "explicacion": "El autor introduce una objeción crítica fundamentada (contraargumento): desarticula la tesis ingenua de que el carro eléctrico tiene impacto ecológico cero, demostrando mediante el ciclo de vida de los materiales y la matriz energética que la tecnología traslada externalidades contaminantes a la fase de extracción y generación.",
        "distractores": [
            "Afirma que apoya la masificación, cuando el fragmento se orienta precisamente a problematizarla.",
            "",
            "Infiere erróneamente que el autor defiende la gasolina, cuando la crítica se enfoca en el análisis sistémico de la sostenibilidad.",
            "Generaliza la crítica a todos los dispositivos electrónicos de forma desproporcionada."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Identifica contraargumentos y objeciones que matizan o refutan tesis previas en un ensayo."
    },
    {
        "id": "lec-023",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Lea el siguiente fragmento: «Intentar comprender el funcionamiento de la mente humana estudiando únicamente las neuronas de manera aislada es como querer entender una sinfonía de Beethoven analizando las propiedades físicas del metal del trombón». ¿Cuál es el propósito del autor al utilizar esta comparación analógica?",
        "opciones": [
            "Sostener que la neurociencia solo debe ser estudiada por músicos profesionales.",
            "Argumentar que los fenómenos complejos de la conciencia surgen de la interacción del sistema global y no de la simple suma de sus partes materiales aisladas.",
            "Demostrar que la música clásica es superior a cualquier disciplina científica.",
            "Afirmar que los trombones están hechos de neuronas artificiales."
        ],
        "correcta": 1,
        "explicacion": "El autor emplea una analogía explicativa para criticar el reduccionismo materialista extremo: una sinfonía es una obra estética que depende de la armonía, el tiempo y la composición conjunta, no de la materia prima de un instrumento. De igual modo, la mente es una propiedad emergente de redes complejas que no se explica analizando una neurona solitaria.",
        "distractores": [
            "Interpreta la analogía en sentido literal restringiendo la ciencia a músicos.",
            "",
            "Confunde una herramienta retórica comparativa con un juicio de valor sobre la superioridad de la música clásica.",
            "Plantea una inversión disparatada sobre la composición anatómica de los instrumentos musicales."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Interpreta el propósito comunicativo de analogías y metáforas en la argumentación de ideas abstractas."
    },
    {
        "id": "lec-024",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Lea el siguiente texto: «A lo largo de los siglos, las bibliotecas han sido concebidas como santuarios del silencio, donde el contacto humano se reducía a susurros reverentes ante los anaqueles. Sin embargo, en el siglo XXI, las bibliotecas públicas han mutado en vibrantes centros de encuentro comunitario: albergan clubes de debate, talleres de robótica, laboratorios de alfabetización digital y refugios climáticos durante olas de calor extremo. Los libros siguen estando allí, pero el verdadero corazón del espacio es ahora la interacción social». ¿Cuál es la idea que mejor sintetiza el texto?",
        "opciones": [
            "Las bibliotecas modernas han dejado de comprar libros impresos para convertirse exclusivamente en salas de cine.",
            "La biblioteca pública ha evolucionado de un espacio solitario y silencioso de consulta a un centro dinámico de cohesión comunitaria e inclusión social.",
            "El silencio estricto sigue siendo la única norma que define a una biblioteca en la actualidad.",
            "Los talleres de robótica han destruido el valor cultural de la literatura tradicional."
        ],
        "correcta": 1,
        "explicacion": "La síntesis óptima recoge los dos momentos del texto y su tesis central: contrasta el modelo tradicional de templo del silencio con la transformación contemporánea de la biblioteca como espacio vivo de encuentro ciudadano, aprendizaje diverso y apoyo social.",
        "distractores": [
            "Afirma falsamente que ya no hay libros y que son salas de cine, exagerando la transformación descrita.",
            "",
            "Sostiene que el silencio sigue siendo la única norma, ignorando todo el cuerpo argumentativo del fragmento.",
            "Emite un juicio condenatorio contra la robótica que el texto no comparte en lo absoluto."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Elabora síntesis globales que recogen fielmente la idea principal y las transformaciones expuestas en el texto."
    },
    {
        "id": "lec-025",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "En un texto sobre la libertad de cátedra, el autor cita textualmente un fallo emblemático de la Corte Constitucional y dos artículos de la Declaración Universal de los Derechos Humanos. ¿Con qué propósito retórico incluye el autor estas citas?",
        "opciones": [
            "Para alargar el texto y cumplir con un número mínimo de palabras exigido por el editor.",
            "Para respaldar su postura mediante argumentos de autoridad jurídica reconocidos internacionalmente.",
            "Para confundir al lector con tecnicismos legales incomprensibles.",
            "Para demostrar que los derechos humanos ya no tienen vigencia en Colombia."
        ],
        "correcta": 1,
        "explicacion": "La inclusión de citas directas de altas cortes o tratados internacionales constituye un 'argumento de autoridad' (autoridad epistémica y jurídica). Su propósito es fundamentar la validez de la postura del autor en consensos y normas con fuerza vinculante y prestigio formal, otorgándole peso y credibilidad a su tesis.",
        "distractores": [
            "Atribuye un motivo banal de relleno cuantitativo ajeno a la técnica argumentativa del ensayo.",
            "",
            "Supone una intención maliciosa de confundir, cuando la cita busca dar claridad y sustento.",
            "Afirma una pérdida de vigencia de los derechos que contradice el uso probatorio de las fuentes citadas."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Reconoce la función probatoria de los argumentos de autoridad y las citas textuales en un ensayo."
    },
    {
        "id": "lec-026",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Lea el fragmento: «Si continuamos vertiendo plásticos a los océanos al ritmo actual, en el año 2050 habrá más peso en plástico que en peces en todos los mares del planeta. Esta no es una profecía de ciencia ficción; es la proyección matemática rigurosa de las Naciones Unidas si los gobiernos y consumidores no prohíben hoy mismo los empaques de un solo uso». ¿Cuál es el propósito comunicativo primordial del autor?",
        "opciones": [
            "Felicitar a las industrias químicas por su gran volumen de producción de plásticos.",
            "Concientizar y alertar con urgencia al lector para movilizar cambios normativos y de consumo inmediatos frente a la contaminación marina.",
            "Describir entretenidamente una escena cinematográfica de aventuras submarinas.",
            "Promover la pesca deportiva intensiva en altamar."
        ],
        "correcta": 1,
        "explicacion": "El texto utiliza un dato contundente de proyección futura y un llamado imperativo a la acción ('si no prohíben hoy mismo'). Su objetivo central no es meramente informar, sino persuadir, conmover y generar alarma ética y política para impulsar un cambio de conducta individual y estatal frente al plástico.",
        "distractores": [
            "Infiere una felicitación a la industria, lo cual es opuesto al mensaje de advertencia del fragmento.",
            "",
            "Lo clasifica como entretenimiento de ficción, cuando el texto insiste en que no es ciencia ficción.",
            "Sugiere promover la pesca, tema que no guarda relación con la denuncia de la contaminación por plásticos."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Identifica la intención comunicativa y el propósito persuasivo en textos de divulgación ecológica."
    },
    {
        "id": "lec-027",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Considere las dos siguientes premisas: Premisa 1: «Todos los metales son buenos conductores del calor y la electricidad». Premisa 2: «El cobre es un metal». A partir de estas dos premisas, ¿cuál conclusión se deduce lógicamente de manera necesaria?",
        "opciones": [
            "El cobre es un excelente aislante térmico.",
            "El cobre es un buen conductor del calor y la electricidad.",
            "Todos los buenos conductores son necesariamente de cobre.",
            "Ningún metal conduce la electricidad mejor que el cobre."
        ],
        "correcta": 1,
        "explicacion": "Se trata de un silogismo categórico clásico de lógica deductiva (Modus Ponens): si todo elemento perteneciente a la clase M (metales) posee la propiedad C (conducción), y el objeto particular X (cobre) pertenece a la clase M, entonces necesariamente X posee la propiedad C (el cobre es buen conductor).",
        "distractores": [
            "Llega a una conclusión diametralmente opuesta a lo postulado en las premisas universales.",
            "",
            "Comete la falacia de afirmación del consecuente: que todos los metales conduzcan no implica que todo conductor sea metal o de cobre.",
            "Introduce un juicio superlativo ('mejor que ningún otro') que no está respaldado por las premisas dadas."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Evalúa deducciones lógicas formales y silogismos a partir de premisas universales y particulares."
    },
    {
        "id": "lec-028",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Un artículo de divulgación científica inicia con la siguiente pregunta: «¿Es posible que el universo en que vivimos no sea el único, sino tan solo una burbuja flotando en un océano infinito de universos paralelos?». ¿Cuál es la función discursiva de esta pregunta al comienzo del texto?",
        "opciones": [
            "Demostrar que el autor desconoce por completo el tema sobre el cual va a escribir.",
            "Enganchar la curiosidad intelectual del lector y plantear el problema central que se desarrollará en el artículo.",
            "Exigir que el lector responda la pregunta de forma escrita antes de continuar leyendo.",
            "Negar la validez de todas las teorías de la física moderna."
        ],
        "correcta": 1,
        "explicacion": "El recurso retórico de abrir con una pregunta abierta o problema provocador busca despertar el asombro y la curiosidad del lector, delimitando desde el primer renglón el interrogante científico central (el multiverso) que el resto del artículo se encargará de explorar y fundamentar teóricamente.",
        "distractores": [
            "Atribuye ignorancia al autor, cuando la pregunta retórica es un artificio deliberado de apertura divulgativa.",
            "",
            "Interpreta la pregunta como un cuestionario interactivo de respuesta obligatoria.",
            "Supone que plantear una hipótesis teórica equivale a negar la validez de la física."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Reconoce la función retórica de preguntas de apertura en artículos de divulgación científica."
    },
    {
        "id": "lec-029",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Lea el fragmento: «Tanto la pintura como la fotografía congelan un instante de la realidad visual sobre un soporte bidimensional. Sin embargo, mientras la pintura es un proceso lento de adición sucesiva donde el artista construye cada pincelada desde el lienzo en blanco, la fotografía es un acto instantáneo de sustracción donde el fotógrafo recorta un fragmento del caos del mundo exterior». ¿En qué radica la diferencia esencial señalada por el autor entre ambas artes?",
        "opciones": [
            "En que la pintura es un arte hermoso y la fotografía carece de cualquier valor estético.",
            "En la naturaleza constructiva y acumulativa de la pintura frente a la naturaleza selectiva e instantánea de la fotografía.",
            "En que la fotografía usa pinturas al óleo y la pintura utiliza cámaras oscuras.",
            "En que ninguna de las dos puede representar la realidad visual."
        ],
        "correcta": 1,
        "explicacion": "El autor establece un contraste preciso: ambas comparten el objetivo visual, pero difieren en su método operativo: la pintura opera por adición constructiva paulatina (añade materia al lienzo), mientras que la fotografía opera por selección y sustracción instantánea (captura y recorta un fragmento de lo que ya existe).",
        "distractores": [
            "Emite un juicio de desprecio contra la fotografía que el texto en ningún momento formula.",
            "",
            "Invierte los instrumentos técnicos atribuyendo óleo a la fotografía y cámaras a la pintura.",
            "Afirma que no representan la realidad, contradiciendo la primera frase que afirma que ambas congelan la realidad visual."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Identifica semejanzas y diferencias estructuradas en textos con patrones de comparación y contraste."
    },
    {
        "id": "lec-030",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "Al final de un riguroso ensayo sobre la corrupción institucional, el autor concluye con la frase: «Las leyes más severas y los códigos penales más estrictos serán letra muerta si la sociedad continúa tolerando y premiando las pequeñas trampas cotidianas». ¿Cuál es el sentido de esta conclusión?",
        "opciones": [
            "Que las leyes deben ser quemadas porque no sirven para nada.",
            "Que la reforma legal e institucional es estéril si no va acompañada de una transformación cultural y ética en las conductas individuales de los ciudadanos.",
            "Que las pequeñas trampas cotidianas son recomendables para dinamizar la economía.",
            "Que solo los jueces tienen la culpa de la corrupción en el país."
        ],
        "correcta": 1,
        "explicacion": "El autor cierra su tesis sintetizando la relación entre el marco jurídico formal y la cultura ciudadana: las normas legales ('letra muerta') no pueden tener eficacia real si el tejido ético social convalida la deshonestidad en la vida diaria (cultura del 'vivo').",
        "distractores": [
            "Interpreta la expresión 'letra muerta' como una incitación vandálica a quemar libros de leyes.",
            "",
            "Sostiene que el autor recomienda hacer trampa, invirtiendo por completo el sentido moral del cierre.",
            "Descarga toda la responsabilidad en los jueces, omitiendo la corresponsabilidad ciudadana señalada."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Interpreta el sentido global de las conclusiones y su articulación con la tesis del ensayo."
    },
    {
        "id": "lec-031",
        "area": "lectura_critica",
        "evidencia": "LEC_E2.2",
        "nivel": 2,
        "enunciado": "En una viñeta cómica (texto discontinuo), un náufrago solitario en una diminuta isla desierta ve acercarse una botella flotando en el mar. Corre emocionado a abrirla esperando un mensaje de auxilio o esperanza, pero al desenrollar el papel encuentra un folleto publicitario que dice: '¡Felicidades, ha ganado un descuento en seguros de vida!'. ¿Cuál es el recurso humorístico y crítico central de la viñeta?",
        "opciones": [
            "La burla contra los náufragos que no saben nadar.",
            "El contraste irónico entre la dramática expectativa vital de rescate del ser humano y la invasión absurda e inservible de la publicidad comercial consumista.",
            "La recomendación de comprar seguros de vida para viajar por altamar.",
            "El elogio a las botellas de vidrio como medio ecológico de comunicación."
        ],
        "correcta": 1,
        "explicacion": "El humor satírico se basa en la ruptura violenta de expectativas: en una situación extrema de vida o muerte donde se espera solidaridad humana, irrumpe la lógica del mercadeo invasivo, evidenciando de forma cómica y mordaz cómo la sociedad de consumo mercantiliza incluso los espacios de mayor desamparo.",
        "distractores": [
            "Interpreta la viñeta como una burla sobre la capacidad de natación del náufrago.",
            "",
            "Interpreta el chiste como un anuncio publicitario serio para la adquisición de pólizas de seguros.",
            "Desvía el análisis hacia las propiedades del vidrio perdiendo de vista el mensaje satírico."
        ],
        "origen": "original",
        "competencia": "Comprender cómo se articulan las partes de un texto",
        "afirmacion": "Interpreta la ironía y el sentido crítico en textos discontinuos (caricaturas y viñetas cómicas)."
    },
    {
        "id": "lec-032",
        "area": "lectura_critica",
        "evidencia": "LEC_E3.1",
        "nivel": 2,
        "enunciado": "Durante un debate académico sobre políticas de salud pública, un panelista expone una propuesta basada en estudios epidemiológicos sobre el etiquetado frontal de alimentos ultraprocesados. Su contradictor le responde: «No podemos tomar en cuenta la propuesta del doctor Pérez porque él es una persona antipática, divorciada dos veces y que viste de forma descuidada». ¿En qué falacia argumentativa incurre el contradictor?",
        "opciones": [
            "Falacia de apelación a la autoridad (ad verecundiam).",
            "Falacia contra la persona (ad hominem), descalificando al individuo en lugar de refutar sus argumentos epidemiológicos.",
            "Falacia de causa falsa (post hoc ergo propter hoc).",
            "Falacia de apelación a la compasión (ad misericordiam)."
        ],
        "correcta": 1,
        "explicacion": "La falacia *ad hominem* consiste en atacar a la persona que emite un argumento (sus rasgos físicos, vida personal, carácter o vestimenta) en lugar de examinar y refutar la validez lógica o las evidencias empíricas de su afirmación.",
        "distractores": [
            "Confunde el ataque personal con una apelación a la autoridad indiscutible.",
            "",
            "Confunde el ataque personal con una relación espuria de causa y efecto temporal.",
            "Confunde la descalificación con un intento de conmover o generar lástima hacia el orador."
        ],
        "origen": "original",
        "competencia": "Reflexionar a partir de un texto y evaluar su contenido",
        "afirmacion": "Identifica falacias argumentativas lógicas (falacia ad hominem) en debates y textos de opinión."
    },
    {
        "id": "lec-033",
        "area": "lectura_critica",
        "evidencia": "LEC_E3.1",
        "nivel": 2,
        "enunciado": "Un transeúnte afirma en una entrevista: «Mi primo compró un automóvil de la marca X y a los tres meses se le dañó la caja de velocidades; por lo tanto, todos los automóviles fabricados por esa marca son defectuosos y una estafa». ¿Qué error de razonamiento comete el transeúnte?",
        "opciones": [
            "Incurre en una generalización apresurada, extrayendo una conclusión universal sobre miles de vehículos a partir de un único caso aislado.",
            "Aplica con rigor el método científico experimental de muestreo representativo.",
            "Demuestra matemáticamente que el automóvil de su primo no existe.",
            "Utiliza un argumento circular indiscutible."
        ],
        "correcta": 0,
        "explicacion": "La generalización indebida o apresurada ocurre cuando se formula una regla universal o juicio categórico sobre toda una población basándose en una muestra estadísticamente insignificante o no representativa (un solo caso particular de un familiar).",
        "distractores": [
            "",
            "Valida el testimonio anecdótico como un experimento científico riguroso, desconociendo el método estadístico.",
            "Sostiene que el auto no existe, lo cual distorsiona el hecho narrado.",
            "Clasifica erróneamente la generalización empírica como una tautología o petición de principio circular."
        ],
        "origen": "original",
        "competencia": "Reflexionar a partir de un texto y evaluar su contenido",
        "afirmacion": "Reconoce la falacia de generalización apresurada en argumentos inductivos defectuosos."
    },
    {
        "id": "lec-034",
        "area": "lectura_critica",
        "evidencia": "LEC_E3.1",
        "nivel": 2,
        "enunciado": "Lea el siguiente argumento: «Debemos prohibir de inmediato la instalación de paneles solares en las zonas residenciales porque reducen la demanda de energía fósil de las grandes termoeléctricas». ¿Cuál es el supuesto o premisa implícita no dicha que sostiene este razonamiento?",
        "opciones": [
            "Que la protección de los intereses económicos de las termoeléctricas fósiles debe ser prioritaria sobre la transición hacia energías limpias.",
            "Que los paneles solares aumentan las emisiones de dióxido de carbono a la atmósfera.",
            "Que la energía solar es más barata que el petróleo y el carbón.",
            "Que las termoeléctricas funcionan exclusivamente con agua de lluvia."
        ],
        "correcta": 0,
        "explicacion": "Para que la conclusión ('debemos prohibir los paneles solares') se derive lógicamente de la razón dada ('reducen la demanda de termoeléctricas'), es indispensable asumir la premisa implícita de que proteger las ganancias del negocio fósil es un bien superior y preferible a la adopción de fuentes renovables.",
        "distractores": [
            "",
            "Atribuye al autor una afirmación técnica falsa sobre emisiones solares que no está implícita en la lógica del argumento.",
            "Menciona una ventaja de costos que socavaría el argumento proteccionista fósil.",
            "Propone una definición absurda sobre el funcionamiento hídrico de las plantas termoeléctricas."
        ],
        "origen": "original",
        "competencia": "Reflexionar a partir de un texto y evaluar su contenido",
        "afirmacion": "Identifica premisas no explícitas y supuestos ideológicos subyacentes en un argumento."
    },
    {
        "id": "lec-035",
        "area": "lectura_critica",
        "evidencia": "LEC_E3.1",
        "nivel": 2,
        "enunciado": "Lea las dos siguientes afirmaciones sobre el cambio climático: Afirmación A: «El 97 % de los científicos del clima a nivel mundial y los informes del IPCC confirman que el calentamiento global actual es inequívoco y antropogénico, respaldado por mediciones satelitales y testigos de hielo». Afirmación B: «A mí me parece que no hay cambio climático porque ayer en mi ciudad hizo un frío espantoso por la tarde». ¿Cómo se evalúa la solidez epistemológica de ambas afirmaciones?",
        "opciones": [
            "Ambas afirmaciones tienen exactamente el mismo valor científico porque toda opinión humana es igualmente respetable y válida en la ciencia.",
            "La afirmación A tiene solidez científica al sustentarse en consenso metodológico y datos empíricos globales, mientras que la afirmación B confunde el clima a largo plazo con el tiempo meteorológico local anecdótico.",
            "La afirmación B es más confiable porque la experiencia directa personal supera cualquier medición instrumental de laboratorio.",
            "Ninguna de las dos afirmaciones se refiere al clima del planeta Tierra."
        ],
        "correcta": 1,
        "explicacion": "En el análisis crítico de textos científicos se distingue el consenso empírico fundamentado (múltiples líneas de evidencia sistemática global acumulada durante décadas) de la percepción sensorial subjetiva puntual. Una tarde fría en una ciudad es una variación meteorológica local del tiempo, no una refutación del calentamiento del sistema climático global.",
        "distractores": [
            "Incurre en un relativismo epistemológico extremo que equipara el rigor científico con la opinión desinformada.",
            "",
            "Privilegia la anécdota personal sobre la metodología científica rigurosa.",
            "Niega que los enunciados aborden el clima terrestre, en abierta contradicción con el texto."
        ],
        "origen": "original",
        "competencia": "Reflexionar a partir de un texto y evaluar su contenido",
        "afirmacion": "Evalúa la solidez y el sustento empírico de argumentos científicos frente a opiniones subjetivas."
    },
    {
        "id": "lec-036",
        "area": "lectura_critica",
        "evidencia": "LEC_E3.1",
        "nivel": 2,
        "enunciado": "Un artículo firmado por el director de relaciones públicas de una empresa azucarera sostiene en una revista de circulación nacional que «el consumo diario de refrescos azucarados no guarda ninguna relación con la obesidad ni la diabetes infantil, y que toda la culpa recae en la falta de voluntad para hacer ejercicio de los niños». Al evaluar críticamente el texto, ¿qué elemento debe considerar el lector para juzgar su credibilidad?",
        "opciones": [
            "La tipografía elegante y los colores utilizados en la diagramación de la revista.",
            "El evidente conflicto de interés económico y corporativo del autor, cuya empresa se beneficia directamente de la venta masiva de azúcar.",
            "La nacionalidad del tipógrafo que imprimió la revista.",
            "La longitud del párrafo introductorio."
        ],
        "correcta": 1,
        "explicacion": "El pensamiento crítico exige evaluar la postura del emisor y sus posibles sesgos o conflictos de interés. Cuando un vocero comercial defiende una tesis contraria al consenso médico mundial que beneficia financieramente a la corporación que le paga su salario, sus afirmaciones no pueden asumirse como neutrales ni desinteresadas.",
        "distractores": [
            "Toma aspectos puramente estéticos de diagramación que no determinan la veracidad científica de los argumentos.",
            "",
            "Considera elementos biográficos intrascendentes del personal técnico de imprenta.",
            "Mide la credibilidad por el número de líneas, un criterio cuantitativo irrelevante."
        ],
        "origen": "original",
        "competencia": "Reflexionar a partir de un texto y evaluar su contenido",
        "afirmacion": "Identifica sesgos y conflictos de interés en textos argumentativos y columnas corporativas."
    },
    {
        "id": "lec-037",
        "area": "lectura_critica",
        "evidencia": "LEC_E3.1",
        "nivel": 2,
        "enunciado": "Lea el fragmento: «En las democracias deliberativas, el disenso razonado no es un síntoma de debilidad ni de anarquía, sino el motor fundamental que evita que las mayorías impongan dogmas incuestionables. Cuando se silencia al que piensa diferente bajo el pretexto de la unidad nacional, la democracia se degrada en tiranía de la mayoría». ¿Qué deducción se desprende necesariamente de este fragmento?",
        "opciones": [
            "Que la unidad nacional solo se logra encarcelando a los opositores políticos.",
            "Que el respeto y la escucha de opiniones divergentes es una condición indispensable para la salud democrática.",
            "Que en una democracia nadie debe ponerse de acuerdo nunca en ninguna ley.",
            "Que las minorías deben gobernar sin tener en cuenta a las mayorías."
        ],
        "correcta": 1,
        "explicacion": "El texto plantea de manera directa que el debate y la coexistencia de posturas diversas ('el disenso razonado') es lo que protege a la democracia de la degeneración tiránica. Por consiguiente, respetar y permitir la deliberación de quienes disienten es un pilar indispensable del régimen democrático.",
        "distractores": [
            "Defiende el autoritarismo carcelario que el texto califica precisamente como degradación en tiranía.",
            "",
            "Extrema la idea hacia una anarquía absoluta donde ningún acuerdo es posible.",
            "Propone una dictadura de las minorías, invirtiendo la idea de equilibrio deliberativo."
        ],
        "origen": "original",
        "competencia": "Reflexionar a partir de un texto y evaluar su contenido",
        "afirmacion": "Infiere conclusiones válidas a partir de premisas sobre teoría política y valores democráticos."
    },
    {
        "id": "lec-038",
        "area": "lectura_critica",
        "evidencia": "LEC_E3.1",
        "nivel": 2,
        "enunciado": "Considere los dos siguientes puntos de vista: Texto 1: «La educación virtual democratiza el saber: permite que jóvenes de veredas remotas accedan a clases con los mejores profesores del mundo a su propio ritmo y sin gastar en transporte ni vivienda urbana». Texto 2: «La educación virtual profundiza la exclusión: en países donde millones de familias carecen de conectividad estable y computadores, trasladar la escuela a internet es abandonar a los más pobres a la deserción escolar». ¿Cuál es la relación conceptual entre ambos textos?",
        "opciones": [
            "El Texto 2 niega que internet exista en el planeta.",
            "Presentan perspectivas divergentes y complementarias sobre el impacto de la virtualidad educativa según el nivel de acceso a infraestructura de los estudiantes.",
            "El Texto 1 demuestra que los profesores de colegio ya no son necesarios.",
            "Ambos textos concluyen que la educación debe ser abolida en las veredas rurales."
        ],
        "correcta": 1,
        "explicacion": "Los textos abordan el mismo fenómeno desde ángulos socioeconómicos contrapuestos pero articulados: el Texto 1 resalta el potencial democratizador intrínseco de la tecnología bajo condiciones de acceso, mientras que el Texto 2 señala la brecha digital material como factor de exclusión cuando no se garantizan previamente la conectividad y los equipos.",
        "distractores": [
            "Infiere una negación absurda de la tecnología inexistente en el texto de crítica.",
            "",
            "Afirma la eliminación de los docentes, cuando el Texto 1 menciona 'los mejores profesores del mundo'.",
            "Atribuye una conclusión destructiva de abolición educativa ajena a ambos planteamientos."
        ],
        "origen": "original",
        "competencia": "Reflexionar a partir de un texto y evaluar su contenido",
        "afirmacion": "Compara y articula puntos de vista divergentes sobre un mismo fenómeno sociocultural."
    },
    {
        "id": "lec-039",
        "area": "lectura_critica",
        "evidencia": "LEC_E3.1",
        "nivel": 2,
        "enunciado": "El filósofo Immanuel Kant formuló el imperativo categórico con la máxima: «Actúa de tal modo que trates a la humanidad, tanto en tu persona como en la persona de cualquier otro, siempre como un fin al mismo tiempo y nunca meramente como un medio». Si una empresa contrata trabajadores en condiciones de extrema precariedad pagándoles salarios de hambre para maximizar las ganancias de sus accionistas, ¿cómo se juzgaría esta conducta desde la ética kantiana?",
        "opciones": [
            "Es una conducta plenamente moral porque las ganancias financieras son el fin supremo de la vida humana.",
            "Es una conducta inmoral porque está instrumentalizando a los trabajadores, reduciéndolos a meros medios económicos y violando su dignidad intrínseca como personas.",
            "Es una conducta neutra que no tiene ninguna relación con los juicios éticos ni filosóficos.",
            "Kant la aplaudiría porque la empresa les proporciona trabajo sin importar las condiciones."
        ],
        "correcta": 1,
        "explicacion": "En el marco ético deontológico kantiano, todo ser humano posee dignidad intrínseca y no precio; debe ser considerado siempre como un fin en sí mismo. Usar a los empleados únicamente como herramientas o instrumentos prescindibles (meros medios) para el enriquecimiento exclusivo de otros viola el principio moral fundamental.",
        "distractores": [
            "Postula el lucro económico como fin ético supremo, posición contraria a la ética moral kantiana.",
            "",
            "Desvincula la economía de la reflexión moral, contradiciendo el propósito del dilema ético formulado.",
            "Afirma falsamente que Kant aprobaría la explotación laboral, malinterpretando el imperativo de la dignidad humana."
        ],
        "origen": "original",
        "competencia": "Reflexionar a partir de un texto y evaluar su contenido",
        "afirmacion": "Aplica conceptos y principios ético-filosóficos clásicos (imperativo categórico) a dilemas socioeconómicos contemporáneos."
    },
    {
        "id": "lec-040",
        "area": "lectura_critica",
        "evidencia": "LEC_E3.1",
        "nivel": 2,
        "enunciado": "Lea el fragmento de un discurso político: «Nuestra nación es la cuna irrestricta de la libertad de expresión y la diversidad de pensamiento en todo el hemisferio; por esa razón patriótica, clausuraremos de por vida todos los periódicos y canales de televisión que publiquen columnas de opinión críticas contra las decisiones de nuestro gobierno». ¿Qué contradicción lógica interna vicia de invalidez este discurso?",
        "opciones": [
            "El orador afirma ser defensor absoluto de la libertad y diversidad de pensamiento, pero simultáneamente decreta la censura y cierre de medios opositores, incurriendo en una incoherencia flagrante.",
            "El discurso es completamente coherente porque la libertad de expresión consiste en repetir solo lo que aprueba el gobernante de turno.",
            "La contradicción radica en que los periódicos se imprimen en papel y no en pantallas de televisión.",
            "No hay contradicción porque los canales de televisión no tienen libertad de expresión."
        ],
        "correcta": 0,
        "explicacion": "El discurso incurre en una contradicción performativa o incoherencia lógica irreconciliable: la premisa mayor proclama que la nación es 'cuna irrestricta de la libertad y diversidad', pero la conclusión operativa anuncia la clausura y censura forzada de las voces discrepantes, negando en la práctica el principio que pretendía ensalzar.",
        "distractores": [
            "",
            "Redefine la libertad como sumisión autoritaria al gobierno, normalizando la contradicción lógica.",
            "Desvía el análisis hacia el soporte material de los medios de comunicación.",
            "Niega los derechos de la prensa para justificar la censura gubernamental."
        ],
        "origen": "original",
        "competencia": "Reflexionar a partir de un texto y evaluar su contenido",
        "afirmacion": "Evalúa la consistencia lógica interna de un texto identificando contradicciones argumentativas."
    }
]

def actualizar_lectura():
    with open('content/questions/lectura_critica.json', 'r', encoding='utf-8') as f:
        existentes = json.load(f)
    
    print(f'Preguntas de lectura existentes antes: {len(existentes)}')
    ids_existentes = {q['id'] for q in existentes}
    
    nuevas = []
    for q in PREGUNTAS_LEC:
        if q['id'] not in ids_existentes:
            nuevas.append(q)
            
    existentes.extend(nuevas)
    print(f'Agregadas {len(nuevas)} preguntas nuevas de lectura crítica. Total ahora: {len(existentes)}')
    
    with open('content/questions/lectura_critica.json', 'w', encoding='utf-8') as f:
        json.dump(existentes, f, indent=2, ensure_ascii=False)
    print('Guardado content/questions/lectura_critica.json exitosamente.')

    # Actualizar unidades en content/unidades.json
    with open('content/unidades.json', 'r', encoding='utf-8') as f:
        units = json.load(f)
        
    unit_map = {u['id']: u for u in units}
    unit_map['u-lectura']['preguntas'].extend(['lec-007', 'lec-008', 'lec-009', 'lec-010', 'lec-011', 'lec-012', 'lec-013', 'lec-014', 'lec-015', 'lec-016', 'lec-017'])
    unit_map['u-logica']['preguntas'].extend(['lec-018', 'lec-019', 'lec-020', 'lec-021', 'lec-022', 'lec-023', 'lec-024'])
    
    # Nuevas unidades de lectura crítica
    units.append({
        'id': 'u-articula-texto',
        'area': 'lectura_critica',
        'titulo': 'Estructura y cohesión textual',
        'resumen': 'Conectores lógicos, citas de autoridad, analogías y textos discontinuos.',
        'preguntas': ['lec-025', 'lec-026', 'lec-027', 'lec-028', 'lec-029', 'lec-030', 'lec-031'],
        'sim': None,
        'leccion': None,
        'min': 20
    })
    units.append({
        'id': 'u-evalua-texto',
        'area': 'lectura_critica',
        'titulo': 'Evaluación crítica, sesgos y falacias',
        'resumen': 'Falacias lógicas, supuestos implícitos, contradicciones y juicios éticos.',
        'preguntas': ['lec-032', 'lec-033', 'lec-034', 'lec-035', 'lec-036', 'lec-037', 'lec-038', 'lec-039', 'lec-040'],
        'sim': None,
        'leccion': None,
        'min': 20
    })
    
    with open('content/unidades.json', 'w', encoding='utf-8') as f:
        json.dump(units, f, indent=1, ensure_ascii=False)
    print('Guardado content/unidades.json con las unidades de lectura crítica actualizadas.')

if __name__ == '__main__':
    actualizar_lectura()
