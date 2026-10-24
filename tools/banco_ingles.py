"""Generador de preguntas originales de Inglés para el Banco Propio.
Crea 36 preguntas (ing-005 a ing-040) cumpliendo el estándar ICFES Saber 11:
- Partes 1 (avisos), 2 (definiciones), 3 (diálogos), 4 (gramática) y 5/6 (lectura)
- 4 opciones distintas por pregunta
- Explicaciones pedagógicas en español detallando reglas gramaticales y contexto
- 3 distractores específicos explicando el error léxico o gramatical
- Competencias oficiales: Gramática y vocabulario, Comprensión lectora, Pragmática
"""
import json

PREGUNTAS_ING = [
    {
        "id": "ing-005",
        "area": "ingles",
        "evidencia": "ING_E2.1",
        "nivel": 1,
        "enunciado": "Where can you see this notice?\n«Please fasten your seat belt while seated and turn off electronic devices during takeoff»",
        "opciones": [
            "On an airplane",
            "In a library",
            "At a swimming pool",
            "In a supermarket"
        ],
        "correcta": 0,
        "explicacion": "El aviso utiliza vocabulario propio de la aviación comercial: «fasten your seat belt» (abróchese el cinturón de seguridad) y «takeoff» (despegue). Esta advertencia de seguridad es característica exclusiva de los aviones durante el vuelo.",
        "distractores": [
            "",
            "En una biblioteca se exige silencio («quiet please»), pero no hay despegues ni cinturones de seguridad.",
            "En una piscina las normas refieren a profundidad («no diving») y no a dispositivos electrónicos ni despegues.",
            "En un supermercado los avisos se relacionan con precios, ofertas o cajas registradoras."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Identifica el lugar y propósito de avisos públicos en inglés a partir del vocabulario clave."
    },
    {
        "id": "ing-006",
        "area": "ingles",
        "evidencia": "ING_E2.1",
        "nivel": 1,
        "enunciado": "Where can you see this notice?\n«Quiet please! National examination in progress. Do not enter without authorization»",
        "opciones": [
            "In a restaurant kitchen",
            "At a school or university hallway",
            "Inside a cinema",
            "At a soccer stadium"
        ],
        "correcta": 1,
        "explicacion": "La frase «examination in progress» (examen en curso) y la petición de silencio «Quiet please» son típicas de los pasillos de instituciones educativas (colegios o universidades) durante la aplicación de pruebas académicas.",
        "distractores": [
            "En la cocina de un restaurante los avisos son de higiene o seguridad alimentaria («wash hands»), no de exámenes.",
            "",
            "En un cine se pide apagar los celulares durante la película, pero no se realizan exámenes académicos.",
            "En un estadio deportivo reina el ruido y los vítores de la multitud, incompatible con la solicitud de silencio para un examen."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Reconoce el contexto comunicativo de avisos públicos escolares en inglés."
    },
    {
        "id": "ing-007",
        "area": "ingles",
        "evidencia": "ING_E2.1",
        "nivel": 1,
        "enunciado": "Where can you see this notice?\n«Danger! Do not feed the monkeys or touch the safety wire»",
        "opciones": [
            "At a zoo",
            "In a bakery",
            "At a bus station",
            "In a shoe shop"
        ],
        "correcta": 0,
        "explicacion": "El término «monkeys» (monos) y la instrucción «do not feed» (no alimentar) señalan directamente a un zoológico o parque de vida silvestre con vallas de seguridad para animales.",
        "distractores": [
            "",
            "En una panadería se venden alimentos para humanos, no hay exhibición de primates ni alambrados de seguridad.",
            "En una terminal de autobuses los avisos indican horarios, andenes o destinos de viaje.",
            "En una tienda de calzado los letreros muestran tallas, modelos o precios de zapatos."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Asocia términos de animales y normas de seguridad con su ubicación en zoológicos y parques."
    },
    {
        "id": "ing-008",
        "area": "ingles",
        "evidencia": "ING_E2.1",
        "nivel": 1,
        "enunciado": "Where can you see this notice?\n«Platform 3: Express train to Manchester departs at 10:15 a.m. Please stand behind the yellow line»",
        "opciones": [
            "At a railway station",
            "At a gas station",
            "In a pharmacy",
            "In an art museum"
        ],
        "correcta": 0,
        "explicacion": "Las palabras clave «Platform» (plataforma / andén), «Express train» (tren expreso) y «yellow line» (línea amarilla de seguridad) son exclusivas de una estación de ferrocarril o metro.",
        "distractores": [
            "",
            "En una gasolinera los avisos prohíben fumar o apagar el motor al cargar combustible, no hay trenes ni plataformas.",
            "En una farmacia se venden medicamentos con receta y productos de cuidado personal.",
            "En un museo de arte los avisos prohíben tocar las pinturas o usar flash fotográfico."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Identifica vocabulario relativo a medios de transporte masivo (trenes y estaciones)."
    },
    {
        "id": "ing-009",
        "area": "ingles",
        "evidencia": "ING_E2.1",
        "nivel": 1,
        "enunciado": "Where can you see this notice?\n«Authorized personnel only! High voltage electrical equipment. Risk of electric shock»",
        "opciones": [
            "At a clothing boutique",
            "In a power station or electrical room",
            "At a public playground",
            "In a pet shop"
        ],
        "correcta": 1,
        "explicacion": "«High voltage» (alto voltaje) y «risk of electric shock» (riesgo de descarga eléctrica) son advertencias técnicas e industriales presentes en cuartos de control eléctrico, transformadores o plantas de energía.",
        "distractores": [
            "En una boutique de ropa los letreros anuncian probadores («fitting rooms») o descuentos de temporada.",
            "",
            "En un parque infantil público los avisos velan por la seguridad de los niños y juegos recreativos.",
            "En una tienda de mascotas los avisos señalan alimentos para perros o gatos y acuarios."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Interpreta avisos de señalización industrial y prevención de riesgos laborales en inglés."
    },
    {
        "id": "ing-010",
        "area": "ingles",
        "evidencia": "ING_E2.1",
        "nivel": 1,
        "enunciado": "Where can you see this notice?\n«Insert your debit card, enter your 4-digit PIN, and remember to take your receipt»",
        "opciones": [
            "At an ATM or cash machine",
            "At a bowling alley",
            "In a botanical garden",
            "At a dental clinic"
        ],
        "correcta": 0,
        "explicacion": "Las instrucciones paso a paso: «insert your debit card» (inserte su tarjeta de débito), «4-digit PIN» (clave de 4 dígitos) y «take your receipt» (retire su recibo) corresponden a un cajero automático bancario (ATM).",
        "distractores": [
            "",
            "En una bolera los avisos indican la pista de juego asignada y el alquiler de zapatos deportivos especiales.",
            "En un jardín botánico los carteles informan sobre especies vegetales, flores y senderos naturales.",
            "En una clínica odontológica los letreros refieren a consultas odontológicas y salas de espera."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Reconoce instrucciones tecnológicas y financieras en servicios bancarios cotidianos."
    },
    {
        "id": "ing-011",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 1,
        "enunciado": "Read the definition and choose the correct word:\n«A professional who is qualified to design buildings, houses, and large structures»",
        "opciones": [
            "An architect",
            "A plumber",
            "A dentist",
            "A journalist"
        ],
        "correcta": 0,
        "explicacion": "La definición describe a un arquitecto («architect»): la persona capacitada profesionalmente para concebir, diseñar y proyectar planos de edificios y viviendas.",
        "distractores": [
            "",
            "«Plumber» es un fontanero o plomero que repara tuberías e instalaciones sanitarias de agua.",
            "«Dentist» es el profesional de la salud que cuida y trata los dientes.",
            "«Journalist» es un periodista que redacta noticias e investiga acontecimientos para medios de comunicación."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Relaciona descripciones de ocupaciones y profesiones con el término en inglés correspondiente."
    },
    {
        "id": "ing-012",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 1,
        "enunciado": "Read the definition and choose the correct word:\n«A special vehicle equipped with medical instruments to transport sick or injured people quickly to a hospital»",
        "opciones": [
            "A bicycle",
            "An ambulance",
            "A submarine",
            "A tractor"
        ],
        "correcta": 1,
        "explicacion": "Un vehículo médico de emergencia diseñado para trasladar pacientes enfermos o heridos al hospital se denomina ambulancia («ambulance»).",
        "distractores": [
            "«Bicycle» es un vehículo de dos ruedas impulsado a pedales para transporte personal o deporte.",
            "",
            "«Submarine» es una nave acuática diseñada para navegar bajo la superficie del mar.",
            "«Tractor» es una máquina pesada utilizada en labores agrícolas del campo para arar la tierra."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Identifica vocabulario sobre medios de transporte y servicios médicos de emergencia."
    },
    {
        "id": "ing-013",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 1,
        "enunciado": "Read the definition and choose the correct word:\n«An optical instrument designed with lenses or mirrors to make distant objects, like stars and planets, appear closer and brighter»",
        "opciones": [
            "A microscope",
            "A telescope",
            "A stethoscope",
            "A thermometer"
        ],
        "correcta": 1,
        "explicacion": "El telescopio («telescope») es el instrumento astronómico que amplía la imagen de cuerpos celestes lejanos en el espacio como estrellas y planetas.",
        "distractores": [
            "«Microscope» se utiliza para observar objetos microscópicos diminutos (células, bacterias), no astros lejanos.",
            "",
            "«Stethoscope» es el fonendoscopio utilizado por médicos para auscultar los latidos del corazón y pulmones.",
            "«Thermometer» mide la temperatura corporal o ambiental."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Diferencia términos científicos e instrumentos de observación óptica en inglés."
    },
    {
        "id": "ing-014",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 1,
        "enunciado": "Read the definition and choose the correct word:\n«A rectangular case with a handle, used for carrying clothes and personal belongings when you travel»",
        "opciones": [
            "A wallet",
            "A suitcase",
            "An umbrella",
            "A key"
        ],
        "correcta": 1,
        "explicacion": "Una maleta o valija para empacar ropa y pertenencias de viaje se denomina maleta («suitcase»).",
        "distractores": [
            "«Wallet» es una billetera pequeña para guardar dinero en efectivo y tarjetas de crédito.",
            "",
            "«Umbrella» es una sombrilla o paraguas para protegerse de la lluvia o el sol.",
            "«Key» es una llave metálica empleada para abrir o cerrar cerraduras."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Reconoce vocabulario relativo a equipaje y artículos personales de viaje."
    },
    {
        "id": "ing-015",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 1,
        "enunciado": "Read the definition and choose the correct word:\n«A book with blank pages where a person regularly writes down private personal experiences and daily thoughts»",
        "opciones": [
            "A dictionary",
            "A diary",
            "A timetable",
            "A newspaper"
        ],
        "correcta": 1,
        "explicacion": "Un diario íntimo personal donde se registran reflexiones y vivencias de cada día se denomina diario («diary»).",
        "distractores": [
            "«Dictionary» es un libro de consulta con listas alfabéticas de palabras y sus definiciones lingüísticas.",
            "",
            "«Timetable» es un horario o tabla con las horas de salida de transportes o clases escolares.",
            "«Newspaper» es un periódico o diario público de noticias de actualidad."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Diferencia tipos de textos y publicaciones personales e informativas en inglés."
    },
    {
        "id": "ing-016",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 1,
        "enunciado": "Read the definition and choose the correct word:\n«The season of the year between summer and winter, when the weather turns cooler and leaves fall from trees»",
        "opciones": [
            "Spring",
            "Autumn",
            "Summer",
            "Midnight"
        ],
        "correcta": 1,
        "explicacion": "La estación en la que bajan las temperaturas y caen las hojas secas de los árboles antes del invierno es el otoño («autumn» en inglés británico, o «fall» en inglés americano).",
        "distractores": [
            "«Spring» es la primavera, la estación que precede al verano donde florecen las plantas.",
            "",
            "«Summer» es el verano, la temporada más cálida del año con días largos.",
            "«Midnight» es la medianoche (las doce de la noche), una medida horaria y no una estación del año."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Identifica las cuatro estaciones del año y sus características climáticas en inglés."
    },
    {
        "id": "ing-017",
        "area": "ingles",
        "evidencia": "ING_E1.2",
        "nivel": 1,
        "enunciado": "Complete the conversation:\n— «How often do you practice swimming at the sports center?»\n— «____________________»",
        "opciones": [
            "Yes, I love water.",
            "Twice a week, on Tuesdays and Thursdays.",
            "Last summer with my family.",
            "It is five meters deep."
        ],
        "correcta": 1,
        "explicacion": "La pregunta inicia con «How often...?» (¿Con qué frecuencia...?). La única respuesta pragmática y gramaticalmente adecuada es un adverbio o frase de frecuencia temporal: «Twice a week...» (Dos veces a la semana...).",
        "distractores": [
            "Responde «Yes...», lo cual sería apropiado para una pregunta cerrada de sí/no («Do you like...?»), pero no a «How often».",
            "",
            "Responde con tiempo pasado («Last summer»), respondiendo a «When» y no a la frecuencia habitual.",
            "Indica la profundidad de la piscina («five meters deep»), respondiendo a «How deep»."
        ],
        "origen": "original",
        "competencia": "Pragmática y sociolingüística",
        "afirmacion": "Responde adecuadamente a preguntas sobre frecuencia y rutinas cotidianas en diálogos en inglés."
    },
    {
        "id": "ing-018",
        "area": "ingles",
        "evidencia": "ING_E1.2",
        "nivel": 1,
        "enunciado": "Complete the conversation:\n— «Could you lend me your dictionary for the English test?»\n— «____________________»",
        "opciones": [
            "Sure, here you go! Take good care of it.",
            "No, I am sleeping right now.",
            "I arrived yesterday morning.",
            "The test is tomorrow."
        ],
        "correcta": 0,
        "explicacion": "A una petición formal cortés de préstamo («Could you lend me...?»), la respuesta socialmente convencional y colaborativa es aceptar amablemente diciendo: «Sure, here you go!» (¡Claro, aquí tienes!).",
        "distractores": [
            "",
            "Afirma estar durmiendo mientras habla despierto, una contradicción inverosímil en una conversación real.",
            "Menciona una hora de llegada en pasado sin responder a la solicitud de préstamo del diccionario.",
            "Informa la fecha del examen pero evade responder a la petición directa."
        ],
        "origen": "original",
        "competencia": "Pragmática y sociolingüística",
        "afirmacion": "Acepta o responde cortésmente a peticiones y solicitudes en situaciones comunicativas cotidianas."
    },
    {
        "id": "ing-019",
        "area": "ingles",
        "evidencia": "ING_E1.2",
        "nivel": 1,
        "enunciado": "Complete the conversation:\n— «I failed my driving test yesterday because I was very nervous.»\n— «____________________»",
        "opciones": [
            "Congratulations on your new license!",
            "I'm sorry to hear that. Don't worry, you'll pass next time!",
            "I have two cars at home.",
            "Driving is very expensive."
        ],
        "correcta": 1,
        "explicacion": "Ante una mala noticia compartida por un interlocutor («I failed...»), la convención sociolingüística de cortesía y empatía en inglés es expresar condolencia y ánimo: «I'm sorry to hear that. Don't worry...» (Lamento escuchar eso. No te preocupes...).",
        "distractores": [
            "Felicita por una licencia inexistente, ignorando que el hablante acaba de reprobar el examen.",
            "",
            "Presume tener dos autos de forma egocéntrica y descontextualizada.",
            "Emite un juicio sobre el costo del automovilismo sin ofrecer consuelo ni empatía."
        ],
        "origen": "original",
        "competencia": "Pragmática y sociolingüística",
        "afirmacion": "Expresa empatía, solidaridad y aliento ante situaciones desafortunadas en interacciones orales en inglés."
    },
    {
        "id": "ing-020",
        "area": "ingles",
        "evidencia": "ING_E1.2",
        "nivel": 1,
        "enunciado": "Complete the conversation:\n— «Would you like to come to my birthday party this Saturday evening?»\n— «____________________»",
        "opciones": [
            "I would love to! Thank you so much for inviting me.",
            "Happy birthday to me!",
            "I am fifteen years old.",
            "The cake was delicious yesterday."
        ],
        "correcta": 0,
        "explicacion": "A una invitación formal y amable formulada con «Would you like to come...?», la respuesta estándar de aceptación agradecida es: «I would love to! Thank you so much...» (¡Me encantaría! Muchas gracias por invitarme).",
        "distractores": [
            "",
            "Se felicita a sí mismo en lugar de responder a la invitación del anfitrión.",
            "Informa su propia edad, dato irrelevante para contestar a la invitación de la fiesta.",
            "Comenta sobre un pastel comido ayer en tiempo pasado, cuando la fiesta es este sábado por la noche."
        ],
        "origen": "original",
        "competencia": "Pragmática y sociolingüística",
        "afirmacion": "Acepta invitaciones sociales con fórmulas de cortesía apropiadas en lengua inglesa."
    },
    {
        "id": "ing-021",
        "area": "ingles",
        "evidencia": "ING_E1.2",
        "nivel": 1,
        "enunciado": "Complete the conversation in a clothing store:\n— «Excuse me, how much is this blue wool jacket?»\n— «____________________»",
        "opciones": [
            "It is size medium.",
            "It is made of cotton.",
            "It is eighty thousand pesos.",
            "It is in the fitting room."
        ],
        "correcta": 2,
        "explicacion": "La pregunta «How much is...?» indaga expresamente por el precio monetario del artículo. La única respuesta coherente indica el valor en dinero: «It is eighty thousand pesos».",
        "distractores": [
            "Indica la talla («size medium»), respondiendo a «What size is it?».",
            "Indica el material («made of cotton»), respondiendo a «What is it made of?».",
            "",
            "Indica la ubicación en el probador («in the fitting room»), respondiendo a «Where is it?»."
        ],
        "origen": "original",
        "competencia": "Pragmática y sociolingüística",
        "afirmacion": "Comprende transacciones comerciales y preguntas de precio en compras cotidianas en inglés."
    },
    {
        "id": "ing-022",
        "area": "ingles",
        "evidencia": "ING_E1.2",
        "nivel": 1,
        "enunciado": "Complete the conversation:\n— «Have you ever visited the Tatacoa Desert in Huila?»\n— «____________________»",
        "opciones": [
            "Yes, I went there with my school two years ago.",
            "No, I never eat dessert after lunch.",
            "Yes, I will visit it tomorrow at noon.",
            "The desert is very cold at midnight."
        ],
        "correcta": 0,
        "explicacion": "Una pregunta en presente perfecto con «Have you ever visited...?» indaga por experiencias de vida pasadas. La respuesta confirma la experiencia en pasado simple: «Yes, I went there with my school two years ago».",
        "distractores": [
            "",
            "Confunde por pronunciación la palabra «desert» (desierto) con «dessert» (postre dulce).",
            "Responde en futuro («I will visit tomorrow») ante una confirmación de experiencia previa con «Yes».",
            "Menciona una característica climática pero evade responder si ha estado allí o no."
        ],
        "origen": "original",
        "competencia": "Pragmática y sociolingüística",
        "afirmacion": "Responde con coherencia temporal a preguntas de experiencias previas usando Present Perfect."
    },
    {
        "id": "ing-023",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 2,
        "enunciado": "Choose the correct preposition to complete the sentence:\n«My family has lived in the same neighborhood in Medellín _______ more than ten years.»",
        "opciones": [
            "since",
            "for",
            "during",
            "at"
        ],
        "correcta": 1,
        "explicacion": "En el presente perfecto, la preposición «for» se utiliza para indicar la duración o periodo de tiempo transcurrido («for ten years», «for three hours»). Por el contrario, «since» se usa únicamente con un punto de inicio específico en el tiempo («since 2014», «since Monday»).",
        "distractores": [
            "Usa erróneamente «since», la cual requeriría un año específico o fecha fija de inicio y no un periodo acumulado.",
            "",
            "Usa «during», la cual se acompaña de sustantivos de eventos («during the vacation») y no de lapsos cuantitativos con Present Perfect.",
            "Usa «at», preposición espacial o de hora fija puntual («at 3 p.m.»), gramaticalmente incorrecta aquí."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Diferencia el uso de las preposiciones temporales 'for' y 'since' con el tiempo Present Perfect."
    },
    {
        "id": "ing-024",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 2,
        "enunciado": "Choose the correct verb form to complete the sentence in passive voice:\n«Penicillin, the first effective modern antibiotic, _______ by Alexander Fleming in 1928.»",
        "opciones": [
            "was discovered",
            "is discovering",
            "discovered",
            "will discover"
        ],
        "correcta": 0,
        "explicacion": "El sujeto de la oración («Penicillin») es paciente y la acción ocurrió en un año pasado concluido («in 1928»). La voz pasiva en pasado simple se forma con el auxiliar 'was' (tercera persona singular) más el participio pasado del verbo principal: «was discovered» (fue descubierta).",
        "distractores": [
            "",
            "Usa la forma continua presente activa («is discovering»), sugiriendo que la penicilina está descubriendo algo ahora.",
            "Usa la voz activa en pasado («discovered»), lo que diría erróneamente que la penicilina descubrió a Alexander Fleming.",
            "Usa el tiempo futuro («will discover») para un acontecimiento histórico ya sucedido en 1928."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Aplica la estructura gramatical de la voz pasiva en pasado simple (was/were + participio)."
    },
    {
        "id": "ing-025",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 2,
        "enunciado": "Choose the correct modal verb of strict rule or obligation:\n«According to airport security regulations, all international passengers _______ show their valid passport before boarding the plane.»",
        "opciones": [
            "must",
            "might",
            "could",
            "shouldn't"
        ],
        "correcta": 0,
        "explicacion": "Para expresar una obligación formal ineludible impuesta por una ley o reglamento de seguridad («regulations»), se emplea el verbo modal de mandato estricto «must» (deben mostrar).",
        "distractores": [
            "",
            "«Might» expresa una posibilidad remota o duda («podrían quizás»), insuficiente para una regla aeroportuaria obligatoria.",
            "«Could» expresa habilidad en pasado o una sugerencia cortés («podrían»), no una norma estricta.",
            "«Shouldn't» es una recomendación negativa de abstención («no deberían»), contraria a la obligación de mostrar el pasaporte."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Selecciona el verbo modal adecuado (must, might, could) según el grado de obligatoriedad."
    },
    {
        "id": "ing-026",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 2,
        "enunciado": "Complete the second conditional sentence:\n«If I had enough savings, I _______ a small bookstore in the historic town center.»",
        "opciones": [
            "would open",
            "will open",
            "opened",
            "open"
        ],
        "correcta": 0,
        "explicacion": "El segundo condicional expresa situaciones hipotéticas o imaginarias en el presente/futuro. Su estructura gramatical estándar es: «If + sujeto + Past Simple, sujeto + would + verbo en forma base». Por lo tanto: «If I had... I would open...».",
        "distractores": [
            "",
            "Usa «will open», propia del primer condicional con presente simple («If I have... I will open...»).",
            "Repite el verbo en pasado simple sin el modal «would», rompiendo la estructura de la cláusula principal.",
            "Usa el verbo en presente simple sin auxiliar modal."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Estructura correctamente oraciones del segundo condicional (Second Conditional: if + past, would + base form)."
    },
    {
        "id": "ing-027",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 1,
        "enunciado": "Choose the correct superlative adjective:\n«Mount Everest, located in the Himalayas, is the _______ mountain peak in the entire world.»",
        "opciones": [
            "higher",
            "highest",
            "most high",
            "more higher"
        ],
        "correcta": 1,
        "explicacion": "Para adjetivos cortos de una sola sílaba como «high», el superlativo regular se forma anteponiendo el artículo «the» y agregando el sufijo «-est» al adjetivo: «the highest» (el más alto).",
        "distractores": [
            "Usa el comparativo «higher», el cual se emplea para comparar dos elementos («higher than...») y no para el superlativo absoluto.",
            "",
            "Usa «most high», una construcción gramaticalmente incorrecta para adjetivos monosílabos.",
            "Comete un doble comparativo redundante («more higher»), error gramatical común."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Aplica las reglas de formación de adjetivos comparativos y superlativos cortos en inglés."
    },
    {
        "id": "ing-028",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 2,
        "enunciado": "Choose the correct phrasal verb:\n«To conserve electricity and reduce emissions, please _______ the lights and computers before leaving the office.»",
        "opciones": [
            "turn off",
            "turn on",
            "look after",
            "give up"
        ],
        "correcta": 0,
        "explicacion": "El phrasal verb para apagar luces o aparatos eléctricos es «turn off» (o «switch off»). En el contexto de ahorro de energía («to conserve electricity»), apagar los equipos al salir de la oficina es la acción correcta.",
        "distractores": [
            "",
            "«Turn on» significa encender, lo cual consumiría más energía eléctrica en lugar de ahorrarla.",
            "«Look after» significa cuidar o vigilar a alguien (por ejemplo a un niño o una mascota).",
            "«Give up» significa rendirse o abandonar un hábito."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Reconoce el significado y uso de 'phrasal verbs' frecuentes en contextos cotidianos (turn off/on)."
    },
    {
        "id": "ing-029",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 2,
        "enunciado": "Choose the correct relative pronoun:\n«Marie Curie was the pioneering female scientist _______ discovered polonium and radium and won two Nobel Prizes.»",
        "opciones": [
            "which",
            "who",
            "where",
            "whose"
        ],
        "correcta": 1,
        "explicacion": "El pronombre relativo adecuado para referirse a personas como sujeto de una cláusula adjetiva es «who» (quien / que).",
        "distractores": [
            "«Which» se utiliza exclusivamente para animales o cosas inanimadas, no para seres humanos.",
            "",
            "«Where» es un adverbio relativo de lugar físico («donde»).",
            "«Whose» es un pronombre posesivo que indica pertenencia («cuyo / cuya»), requiriendo un sustantivo posterior."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Utiliza pronombres relativos adecuados (who, which, where, whose) según el antecedente."
    },
    {
        "id": "ing-030",
        "area": "ingles",
        "evidencia": "ING_E1.1",
        "nivel": 2,
        "enunciado": "Choose the correct verb form after a preposition:\n«Carolina is very enthusiastic about _______ abroad next year to improve her foreign language skills.»",
        "opciones": [
            "travel",
            "traveling",
            "traveled",
            "travels"
        ],
        "correcta": 1,
        "explicacion": "En la gramática inglesa rige una regla estricta: todo verbo que se coloque inmediatamente después de una preposición (en este caso «about») debe adoptar obligatoriamente la forma de gerundio terminada en «-ing» («traveling»).",
        "distractores": [
            "Usa la forma base en infinitivo («travel»), violando la regla del gerundio tras preposición.",
            "",
            "Usa el tiempo pasado simple («traveled»), gramaticalmente incompatible tras preposición.",
            "Usa la tercera persona presente con 's' («travels»), incorrecta en este patrón preposicional."
        ],
        "origen": "original",
        "competencia": "Gramática y vocabulario",
        "afirmacion": "Aplica la regla del gerundio (-ing form) tras preposiciones en inglés."
    },
    {
        "id": "ing-031",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the text and answer the question:\n«More than eight million metric tons of plastic waste enter the world's oceans every year, threatening marine life. Sea turtles often mistake plastic bags for jellyfish, their primary food source, which causes fatal blockages. To combat this crisis, cities around the world are banning single-use shopping bags and encouraging citizens to use reusable cloth bags whenever they go shopping.»\nAccording to the text, why do sea turtles consume plastic bags?",
        "opciones": [
            "Because they find plastic bags more nutritious than fish.",
            "Because they confuse plastic bags with jellyfish, which are their natural food.",
            "Because fishermen feed them plastic bags deliberately.",
            "Because turtles use plastic bags to build their nests."
        ],
        "correcta": 1,
        "explicacion": "El texto afirma literalmente: «Sea turtles often mistake plastic bags for jellyfish, their primary food source» (las tortugas marinas a menudo confunden las bolsas de plástico con medusas, su principal fuente de alimento).",
        "distractores": [
            "Sostiene que el plástico es nutritivo, lo cual es falso y desmentido por el texto («causes fatal blockages»).",
            "",
            "Acusa a los pescadores de alimentar a las tortugas con plástico, dato inexistente en la lectura.",
            "Afirma que usan plástico para nidos, confundiéndolo con hábitos de aves."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Localiza información literal y relaciones causales directas en un texto informativo ambiental."
    },
    {
        "id": "ing-032",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the text and answer the question:\n«In remote rural areas of the Colombian Pacific coast, many communities have never had access to the national electric grid. For decades, families relied on noisy, polluting diesel generators that could only run for three hours each night due to high fuel costs. Recently, a community solar project installed photovoltaic panels on school rooftops. Now, children can study in the evenings, vaccines are safely refrigerated at the local health clinic, and women have formed a cooperative to freeze and preserve fresh fish for sale.»\nWhat is the main benefit of the solar project described in the text?",
        "opciones": [
            "It provided diesel generators to every household in the town.",
            "It brought clean, continuous energy that improved education, healthcare, and local economic activities.",
            "It forced the communities to relocate to large cities.",
            "It closed all the schools in the region."
        ],
        "correcta": 1,
        "explicacion": "El texto sintetiza múltiples impactos positivos derivados de la energía solar: permite a los niños estudiar con luz de noche (educación), refrigera vacunas (salud) y permite congelar pescado para el comercio cooperativo (economía local).",
        "distractores": [
            "Afirma que entregó generadores diésel, cuando precisamente el proyecto solar vino a sustituir esa fuente sucia y cara.",
            "",
            "Sostiene que obligó a las personas a mudarse a las ciudades, lo contrario a fortalecer la permanencia en sus territorios.",
            "Afirma que cerró las escuelas, cuando el texto señala que las escuelas fueron beneficiadas con paneles en sus techos."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Identifica la idea principal y las consecuencias de proyectos sociales en textos descriptivos."
    },
    {
        "id": "ing-033",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the short text:\n«Gabriel García Márquez, born in Aracataca, Colombia, in 1927, published his masterpiece 'One Hundred Years of Solitude' in 1967. The novel became a worldwide phenomenon, establishing magical realism as a major literary movement. In 1982, his extraordinary contributions to world literature were crowned when he received the Nobel Prize in Literature in Stockholm.»\nIn which year did Gabriel García Márquez receive the Nobel Prize in Literature?",
        "opciones": [
            "In 1927",
            "In 1967",
            "In 1982",
            "In 1999"
        ],
        "correcta": 2,
        "explicacion": "El texto señala con precisión cronológica: «In 1982, his extraordinary contributions... were crowned when he received the Nobel Prize in Literature in Stockholm».",
        "distractores": [
            "1927 corresponde al año de su nacimiento en Aracataca.",
            "1967 corresponde a la fecha de publicación de Cien años de soledad.",
            "",
            "1999 es un año no mencionado en el fragmento biográfico."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Extrae fechas y datos biográficos puntuales de textos históricos y culturales en inglés."
    },
    {
        "id": "ing-034",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the following paragraph:\n«The spectacled bear, South America's only native bear species, plays an indispensable role in maintaining the health of Andean cloud forests and páramos. By feeding on fruits and wandering across vast territories, these gentle giants disperse seeds that allow native trees to regenerate. However, habitat fragmentation caused by unauthorized roads and agricultural expansion is pushing them to the brink of extinction. Without urgent conservation corridors, we risk losing this majestic guardian of our mountains forever.»\nWhat is the author's primary intention in this text?",
        "opciones": [
            "To promote hunting expeditions to capture Andean bears.",
            "To describe recipes using wild fruits collected from cloud forests.",
            "To raise urgent awareness about the ecological importance of the spectacled bear and advocate for its conservation.",
            "To explain how to construct commercial highways in national parks."
        ],
        "correcta": 2,
        "explicacion": "El autor destaca el rol vital del oso de anteojos como dispersor de semillas y alerta con vehemencia sobre el peligro de extinción por fragmentación de su hábitat, concluyendo con un llamado a la acción para crear corredores de conservación («Without urgent conservation corridors, we risk losing...»).",
        "distractores": [
            "Sugiere promover la cacería, lo cual es frontalmente opuesto al propósito ecologista de conservación.",
            "Habla de recetas de cocina, desvirtuando el tema zoológico y ambiental.",
            "",
            "Propone construir carreteras, cuando el texto denuncia que las vías no autorizadas fragmentan y amenazan el hábitat del oso."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Identifica el propósito y la actitud del autor en textos de divulgación científica y ambiental."
    },
    {
        "id": "ing-035",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the text and answer the question:\n«Scientific research confirms that chronic sleep deprivation severely impairs cognitive performance, memory consolidation, and emotional regulation in adolescents. Teenagers who consistently sleep fewer than eight hours per night are significantly more likely to experience academic difficulties, anxiety, and weakened immune systems. Experts recommend keeping electronic screens out of the bedroom at least one hour before bedtime to promote healthy melatonin production.»\nWhat is the main advice given by experts in the text?",
        "opciones": [
            "To drink energetic drinks before studying at night.",
            "To avoid using electronic screens in the bedroom before sleeping to ensure quality rest.",
            "To sleep only four hours to have more time for homework.",
            "To exercise vigorously immediately before going to sleep."
        ],
        "correcta": 1,
        "explicacion": "La recomendación explícita de los expertos en la última oración del texto es: «Experts recommend keeping electronic screens out of the bedroom at least one hour before bedtime» (mantener las pantallas electrónicas fuera de la habitación al menos una hora antes de dormir).",
        "distractores": [
            "Sugiere tomar bebidas energéticas, lo cual aumentaría el insomnio y empeoraría la falta de sueño.",
            "",
            "Aconseja dormir solo 4 horas, recomendación dañina y opuesta a las 8 horas mínimas aconsejadas.",
            "Propone ejercicio vigoroso antes de dormir, práctica no mencionada en el fragmento."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Reconoce recomendaciones e instrucciones de salud y bienestar en textos expositivos en inglés."
    },
    {
        "id": "ing-036",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the excerpt:\n«High-altitude Arabica coffee thrives on the steep slopes of the Colombian Andes, typically between 1,200 and 1,800 meters above sea level. In these microclimates, moderate temperatures and frequent cloud cover slow down the ripening process of the coffee cherry. This prolonged maturation allows the bean to develop complex sugars, delicate acidity, and rich aromas that are celebrated by baristas and coffee connoisseurs worldwide.»\nAccording to the passage, why is slow ripening beneficial for coffee quality?",
        "opciones": [
            "Because it allows the coffee bean to develop complex sugars, acidity, and rich aromas.",
            "Because it makes the coffee plants produce twice as many beans in a single week.",
            "Because it turns the coffee cherries completely black and dry.",
            "Because it allows farmers to pick the fruit during heavy snowstorms."
        ],
        "correcta": 0,
        "explicacion": "El texto explica claramente la relación biológica: «This prolonged maturation allows the bean to develop complex sugars, delicate acidity, and rich aromas that are celebrated...» (esta maduración prolongada permite al grano desarrollar azúcares complejos, acidez delicada y aromas intensos).",
        "distractores": [
            "",
            "Afirma que duplica la cantidad de granos en una semana, confundiendo la calidad química del sabor con la cantidad acelerada.",
            "Sostiene que seca y ennegrece los frutos, lo que denotaría daño o pudrición de la cosecha.",
            "Habla de tormentas de nieve, fenómeno inexistente en las zonas cafeteras tropicales andinas de Colombia."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Infiere y relaciona factores agrícolas y climáticos que determinan la calidad del café colombiano."
    },
    {
        "id": "ing-037",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the text:\n«Artificial intelligence algorithms are revolutionizing early medical diagnosis. In ophthalmology and radiology, machine learning models can scan retinal images or chest X-rays in seconds, detecting signs of diabetic retinopathy or lung tumors with accuracy comparable to senior specialists. While these tools will never replace the empathy, clinical judgment, and bedside manner of a human doctor, they represent an invaluable assistant to expand quality healthcare to underserved rural communities.»\nWhat is the author's tone and attitude toward artificial intelligence in healthcare?",
        "opciones": [
            "Entirely hostile, demanding a total ban on medical algorithms.",
            "Cautiously optimistic and balanced, acknowledging its diagnostic power while emphasizing that human doctors remain indispensable.",
            "Indifferent, showing no interest in healthcare technologies.",
            "Fearful, claiming that robots will eradicate all human medical professionals next month."
        ],
        "correcta": 1,
        "explicacion": "El autor muestra un equilibrio reflexivo (cautelosamente optimista): reconoce el inmenso valor técnico de la IA para salvar vidas y llegar a zonas rurales, pero matiza con claridad que nunca podrá sustituir la empatía y el juicio clínico de los médicos humanos.",
        "distractores": [
            "Afirma una hostilidad total, cuando el texto califica a la IA de 'asistente invaluable' («invaluable assistant»).",
            "",
            "Lo describe como indiferente, ignorando el entusiasmo informado con que describe los avances diagnósticos.",
            "Afirma un pánico catastrofista sobre el reemplazo inmediato de médicos el próximo mes."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Evalúa el tono y la postura crítica del autor en artículos de divulgación médica y tecnológica."
    },
    {
        "id": "ing-038",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the formal invitation:\n«Dear Student Council Representative,\nYou are cordially invited to attend the 5th Annual Youth Environmental Summit, taking place on Friday, November 14, at the City Conference Hall from 8:30 a.m. to 4:00 p.m. Admission is completely free, but prior online registration is mandatory due to limited auditorium seating. Please confirm your attendance before November 5 by filling out the form on our official website.»\nWhat is an essential requirement to attend the Summit?",
        "opciones": [
            "Paying an entrance fee of one hundred dollars at the door.",
            "Completing the mandatory online registration form before November 5.",
            "Bringing your own microphone and camera.",
            "Attending only if you are over fifty years old."
        ],
        "correcta": 1,
        "explicacion": "El texto especifica que aunque la entrada es gratuita («Admission is completely free»), el registro previo por internet es obligatorio debido a cupos limitados («prior online registration is mandatory») y debe realizarse antes del 5 de noviembre («before November 5»).",
        "distractores": [
            "Afirma que se debe pagar cien dólares, contradiciendo la gratuidad explícita anunciada («Admission is completely free»).",
            "",
            "Exige llevar micrófonos propios, requisito no solicitado a los asistentes.",
            "Restringe a mayores de 50 años, cuando se trata de una cumbre de líderes juveniles («Youth Environmental Summit»)."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Extrae requisitos y condiciones de participación de cartas y correos de invitación formal en inglés."
    },
    {
        "id": "ing-039",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the book review:\n«'The Last Colony' is a gripping science fiction novel that combines thrilling space battles with deep philosophical questions about human ethics and colonial exploitation. Author Sarah Jenkins creates complex, flawed characters whose difficult moral choices will resonate with readers long after finishing the final chapter. While the middle section suffers from slightly slow pacing, the breathtaking climax more than compensates for it. Highly recommended for fans of intelligent speculative fiction.»\nWhat is the reviewer's overall verdict on the book?",
        "opciones": [
            "The book is terrible and nobody should waste time reading it.",
            "The book is highly recommended for its compelling characters and thought-provoking themes, despite a minor pacing flaw in the middle.",
            "The book is a historical biography of an ancient Roman general.",
            "The reviewer did not read the book."
        ],
        "correcta": 1,
        "explicacion": "La reseña concluye recomendando enfáticamente la obra («Highly recommended for fans of intelligent speculative fiction»), elogiando sus personajes complejos y reflexiones éticas, a pesar de señalar una pequeña objeción sobre el ritmo en la sección intermedia.",
        "distractores": [
            "Califica el libro de terrible, ignorando la calificación de «gripping» (cautivador) y «highly recommended».",
            "",
            "Confunde una novela de ciencia ficción espacial con una biografía militar romana.",
            "Sostiene que no leyó el libro, cuando comenta detalladamente la trama, los personajes y el clímax final."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Identifica la valoración crítica global y los argumentos de apoyo en reseñas literarias en inglés."
    },
    {
        "id": "ing-040",
        "area": "ingles",
        "evidencia": "ING_E2.2",
        "nivel": 2,
        "enunciado": "Read the narrative paragraph:\n«For eight grueling hours, the three mountaineers battled freezing blizzards and steep icy cliffs on their ascent to the snow-capped peak of Nevado del Ruiz. Exhaustion was creeping in, and their oxygen reserves were running dangerously low. Just when despair threatened to force a retreat, the fierce winds suddenly subsided, the dense storm clouds parted, and the golden rays of the sunrise illuminated the majestic summit only fifty meters ahead. With renewed energy, they took their final steps and planted their flag in triumph.»\nWhat was the turning point that motivated the climbers to reach the summit?",
        "opciones": [
            "They received a helicopter rescue delivery with warm food.",
            "The storm clouds suddenly cleared and the sunrise revealed that the summit was only fifty meters away.",
            "They decided to abandon the climb and return to the base camp.",
            "Their oxygen tanks broke completely."
        ],
        "correcta": 1,
        "explicacion": "El punto de quiebre narrativo (turning point) ocurre cuando cesa el viento, las nubes de tormenta se abren y la luz del amanecer les muestra la cima dorada a tan solo cincuenta metros de distancia, infundiéndoles la energía renovada para culminar la hazaña.",
        "distractores": [
            "Menciona un rescate en helicóptero con comida que no aparece en el relato épico de montaña.",
            "",
            "Afirma que abandonaron el ascenso, cuando por el contrario lograron llegar a la cumbre y plantar su bandera.",
            "Sostiene que sus tanques se rompieron, contradiciendo el desenlace victorioso narrado."
        ],
        "origen": "original",
        "competencia": "Comprensión lectora",
        "afirmacion": "Identifica el clímax y los puntos de inflexión en fragmentos narrativos y crónicas de aventura en inglés."
    }
]

def actualizar_ingles():
    with open('content/questions/ingles.json', 'r', encoding='utf-8') as f:
        existentes = json.load(f)
    
    print(f'Preguntas de inglés existentes antes: {len(existentes)}')
    ids_existentes = {q['id'] for q in existentes}
    
    nuevas = []
    for q in PREGUNTAS_ING:
        if q['id'] not in ids_existentes:
            nuevas.append(q)
            
    existentes.extend(nuevas)
    print(f'Agregadas {len(nuevas)} preguntas nuevas de inglés. Total ahora: {len(existentes)}')
    
    with open('content/questions/ingles.json', 'w', encoding='utf-8') as f:
        json.dump(existentes, f, indent=2, ensure_ascii=False)
    print('Guardado content/questions/ingles.json exitosamente.')

    # Actualizar unidades en content/unidades.json
    with open('content/unidades.json', 'r', encoding='utf-8') as f:
        units = json.load(f)
        
    unit_map = {u['id']: u for u in units}
    unit_map['u-vocab']['preguntas'].extend(['ing-005', 'ing-006', 'ing-007', 'ing-008', 'ing-009', 'ing-010', 'ing-011', 'ing-012', 'ing-013', 'ing-014', 'ing-015', 'ing-016'])
    unit_map['u-gram']['preguntas'].extend(['ing-017', 'ing-018', 'ing-019', 'ing-020', 'ing-021', 'ing-022', 'ing-023', 'ing-024', 'ing-025', 'ing-026', 'ing-027', 'ing-028', 'ing-029', 'ing-030'])
    
    # Nueva unidad de lectura de inglés
    units.append({
        'id': 'u-ing-reading',
        'area': 'ingles',
        'titulo': 'Comprensión lectora y análisis textual en inglés',
        'resumen': 'Lectura literal e inferencial de textos informativos, biografías, invitaciones y reseñas.',
        'preguntas': ['ing-031', 'ing-032', 'ing-033', 'ing-034', 'ing-035', 'ing-036', 'ing-037', 'ing-038', 'ing-039', 'ing-040'],
        'sim': None,
        'leccion': None,
        'min': 20
    })
    
    with open('content/unidades.json', 'w', encoding='utf-8') as f:
        json.dump(units, f, indent=1, ensure_ascii=False)
    print('Guardado content/unidades.json con las unidades de inglés actualizadas.')

if __name__ == '__main__':
    actualizar_ingles()
