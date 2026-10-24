"""Datos de las preguntas 41 a 62 de Odontología (Endodoncia).
Alineadas con la Clase 1 y Clase 2, cubriendo todos los temas faltantes.
"""

def get_questions_41_to_62(make_q):
    qs = []

    # 41 (Key A = 0)
    qs.append(make_q(
        qid="odo-041", nivel=2,
        enunciado="En el análisis del formato clínico y preparación del diente, el docente advierte sobre el riesgo de colocar la grapa de aislamiento absoluto sobre dientes severamente destruidos por caries (líneas cuatrocientos cincuenta y nueve a cuatrocientos sesenta y cinco). ¿Cuál es la indicación biomecánica previa antes de aislar un diente con destrucción coronal extensa mayor al sesenta por ciento?",
        opciones=[
            "Realizar una reconstrucción previa de paredes coronales con ionómero de vidrio o resina para brindar soporte biomecánico y evitar que la tensión de la grapa fracture la raíz.",
            "Aislar exclusivamente con rollos de algodón en seco sin dique de goma para no presionar la encía marginal en ningún momento de la cita.",
            "Fracturar intencionalmente las cúspides remanentes con una pinza gubia para nivelar el margen a la altura del hueso alveolar.",
            "Colocar cinco cartuchos de anestésico local infiltrativo en el ligamento periodontal para ablandar la dureza de la corona antes de aislar."
        ],
        correcta=0,
        distractores=[
            "",
            "El aislamiento relativo con algodón está totalmente contraindicado en endodoncia por el riesgo de aspiración de limas y contaminación salival masiva.",
            "La fractura destructiva intencional de cúspides elimina el remanente coronal y condena al diente a una exodoncia innecesaria.",
            "El anestésico local actúa sobre las terminaciones nerviosas y no modifica las propiedades mecánicas ni la rigidez de los tejidos dentarios."
        ],
        explicacion="El docente destacó que el aislamiento absoluto con dique de goma es un estándar intransigible en endodoncia. Sin embargo, cuando un diente presenta caries severa que ha destruido más del sesenta por ciento de la corona, las paredes de esmalte y dentina remanentes están socavadas y desprovistas de soporte. Los mordientes metálicos de la grapa ejercen una fuerza de tracción elástica considerable; si se colocan directamente sobre una pared socavada, pueden fracturar verticalmente el diente hacia la furca o el tercio radicular, volviéndolo no restaurable. Por ello, la indicación obligatoria es remover la caries y reconstruir previamente las paredes con ionómero de vidrio o resina (reconstrucción pre-endodóntica) para que la grapa abrace una estructura sólida y garantice un sellado hermético frente a la saliva.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Historia clínica y bioseguridad: aislamiento y reconstrucción pre-endodóntica",
        que="Indicar la reconstrucción coronal previa antes de aislar con grapa un diente con destrucción mayor al sesenta por ciento.",
        clave="En dientes con caries mayor al sesenta por ciento se reconstruyen las paredes previamente para evitar fracturas radiculares por la grapa.",
        pistas=[
            "Recuerda la advertencia del profesor sobre el peligro de colocar grapas directamente en paredes huecas socavadas.",
            "Ten en cuenta que el aislamiento absoluto exige un perímetro hermético que soporte la tensión de los mordientes metálicos."
        ],
        plan=[
            "Evaluar el grado de destrucción coronaria respecto al umbral crítico del sesenta por ciento.",
            "Reconocer el riesgo biomecánico de fractura vertical por la fuerza de los mordientes de la grapa.",
            "Ejecutar la reconstrucción pre-endodóntica con ionómero o resina para asegurar el dique de goma."
        ],
        marcas_data=[
            ("destrucción coronal extensa mayor al sesenta por ciento", "clave", "Umbral crítico de debilitamiento", "Apunta a socavado masivo de paredes"),
            ("¿Cuál es la indicación biomecánica previa antes de aislar un diente", "pide", "Conducta preventiva obligatoria", "Demanda seleccionar la reconstrucción pre-endodóntica")
        ],
        steps_ideas=[
            ("idea", "Fuerza de la grapa", "La grapa de acero ejerce gran presión elástica lateral contra las paredes del diente."),
            ("idea", "Paredes socavadas", "Si la caries destruyó más del sesenta por ciento, la grapa quiebra la raíz hacia la furca."),
            ("idea", "Reconstrucción previa", "Se limpian bordes y se levantan paredes con ionómero o resina antes de poner el dique."),
            ("check", "Comprobación clínica", "Confirmamos reconstrucción previa de paredes coronales para resistir la tensión de la grapa.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta situación clínica cotidiana en dientes con caries extensas explicada por el profesor."),
            ("m:destrucción coronal extensa mayor al sesenta por ciento", "Observa que al diente le falta más del sesenta por ciento de su volumen coronario."),
            ("leer", "El docente advirtió: si el estudiante llega y coloca la grapa de metal de una vez, la presión puede reventar la raíz."),
            ("leer", "Para evitar fracturas irreparables y filtraciones de saliva, se deben reconstruir primero las paredes con ionómero o resina."),
            ("leer", "Por lo tanto, la conducta biomecánica correcta es reconstruir previamente las paredes antes de aislar.")
        ]
    ))

    # 42 (Key B = 1)
    qs.append(make_q(
        qid="odo-042", nivel=2,
        enunciado="Al explicar el consentimiento informado en el formato de la clínica universitaria (líneas seiscientos noventa a seiscientos noventa y siete), el docente enumera los riesgos inherentes al tratamiento endodóntico que deben ser explicados al paciente y aceptados con su firma. ¿Cuáles son estos cuatro riesgos clínicos propios del procedimiento?",
        opciones=[
            "Pérdida permanente del sentido del gusto, ceguera transitoria y parálisis de las extremidades inferiores por difusión del hipoclorito.",
            "Dolor e inflamación postoperatoria, sobreinfección temporal, riesgo de perforación radicular o de furca, y fractura accidental de instrumentos intraconducto.",
            "Aumento de peso corporal inmediato, caída del cabello y decoloración permanente de toda la arcada dentaria opuesta.",
            "Crecimiento óseo espontáneo de dientes supernumerarios en los cuadrantes no tratados por estimulación del periostio."
        ],
        correcta=1,
        distractores=[
            "La pérdida del gusto, ceguera o parálisis no son riesgos biológicos inherentes a un tratamiento de conductos bien conducido.",
            "",
            "El peso, el cabello o la decoloración generalizada no guardan ninguna relación con la biomecánica ni farmacología endodóntica.",
            "La estimulación periosteal no induce la formación embrionaria de nuevos gérmenes dentarios supernumerarios en adultos."
        ],
        explicacion="En las líneas seiscientos noventa a seiscientos noventa y siete, el profesor enfatizó que el consentimiento informado no es un simple papel rutinario, sino un diálogo clínico y legal obligatorio. Los riesgos inherentes a la endodoncia que todo profesional debe explicar con claridad al paciente son: 1) Molestia, dolor o inflamación postoperatoria derivada de la manipulación química y mecánica del ligamento; 2) Posibilidad de agudización o sobreinfección temporal durante el tratamiento; 3) Riesgo de perforación de la corona, de la furca o de la raíz en dientes con anatomía compleja o conductos calcificados; y 4) Posibilidad de fractura por fatiga cíclica de instrumentos endodónticos finos dentro del conducto radicular.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Historia clínica: consentimiento informado y riesgos endodónticos",
        que="Identificar los cuatro riesgos inherentes al tratamiento endodóntico detallados en el consentimiento informado.",
        clave="Los riesgos del consentimiento informado son dolor postoperatorio, sobreinfección, perforación radicular y fractura de instrumentos.",
        pistas=[
            "Recuerda la lista de complicaciones accidentales que el docente explicó que deben advertirse previamente al paciente.",
            "Ten en cuenta los riesgos mecánicos (limas rotas, perforaciones) y biológicos (dolor, inflamación)."
        ],
        plan=[
            "Reconocer el valor médico-legal del consentimiento informado en la práctica odontológica.",
            "Identificar los riesgos biológicos postoperatorios esperados de dolor e inflamación.",
            "Detallar los accidentes mecánicos inherentes de perforación y separación de instrumentos."
        ],
        marcas_data=[
            ("consentimiento informado en el formato de la clínica universitaria", "dato", "Documento médico-legal obligatorio", "Apunta a deber de información previa"),
            ("¿Cuáles son estos cuatro riesgos clínicos propios del procedimiento?", "clave", "Riesgos inherentes a la endodoncia", "Demanda identificar dolor, sobreinfección, perforación y lima rota")
        ],
        steps_ideas=[
            ("idea", "Deber de información", "El paciente debe conocer los riesgos antes de que el profesional inicie el procedimiento."),
            ("idea", "Riesgos biológicos", "El ligamento periodontal puede inflamarse provocando dolor o agudización temporal tras la cita."),
            ("idea", "Riesgos de instrumental", "Una lima fina puede fracturarse en una curva, o la fresa desviarse y perforar la raíz."),
            ("check", "Comprobación clínica", "Confirmamos los cuatro riesgos inherentes: dolor, sobreinfección, perforación y fractura de lima.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta enseñanza médico-legal explicada por el profesor en la revisión del formato clínico."),
            ("m:consentimiento informado en el formato de la clínica universitaria", "Observa que el consentimiento informado exige explicar al paciente los riesgos propios de la endodoncia."),
            ("leer", "El docente explicó que el paciente debe saber que puede quedar con dolor o inflamación en los días posteriores."),
            ("leer", "También debe saber que existe el riesgo de perforar una raíz curva o de que una lima fina se parta adentro."),
            ("leer", "Por lo tanto, la opción que enumera dolor, sobreinfección, perforación y fractura de instrumentos es la correcta.")
        ]
    ))

    # 43 (Key C = 2)
    qs.append(make_q(
        qid="odo-043", nivel=2,
        enunciado="En la sección de anestesia local odontológica y técnicas tronculares para molares inferiores con dolor agudo (líneas seiscientos cuarenta y seis a seiscientos setenta y dos), ¿cuáles son los principios de la técnica correcta del bloqueo del nervio dentario inferior y la conducta si persiste dolor al abrir la cámara pulpar?",
        opciones=[
            "Introducir la aguja sin aspirar y descargar el cartucho completo en tres segundos; si duele, aumentar la velocidad de fresado cameral.",
            "Orientar el bisel hacia la lengua, aspirar una sola vez y prescribir antibióticos sistémicos en vez de continuar con la anestesia local.",
            "Orientar el bisel hacia el hueso, aspirar en dos planos para descartar vaso sanguíneo y depositar lentamente; si persiste dolor por inflamación pulpar severa, aplicar anestesia intrapulpar a presión.",
            "Realizar exclusivamente anestesia tópica mucosa con torunda de algodón durante veinte minutos sin usar aguja en molares inferiores."
        ],
        correcta=2,
        distractores=[
            "No aspirar e inyectar rápido puede causar inyección intravascular con taquicardia severa y toxicidad del anestésico.",
            "El bisel debe orientarse hacia la cortical ósea para deslizarse suavemente sin raspar el periostio ni doblarse.",
            "",
            "La anestesia tópica superficial solo duerme el epitelio de la mucosa y no tiene penetración al nervio dentario inferior en hueso."
        ],
        explicacion="En las líneas seiscientos cuarenta y seis a seiscientos setenta y dos, el docente detalló los principios biomecánicos de la técnica anestésica del dentario inferior: 1) Orientar el bisel de la aguja hacia la cortical ósea de la rama mandibular; 2) Aspirar obligatoriamente en dos planos rotando noventa grados la jeringa carpule para garantizar que no se está dentro de la arteria o vena alveolar inferior; 3) Inyectar el cartucho de anestésico lentamente (al menos un minuto por carpule) para evitar dolor y toxicidad sistémica. Asimismo, el docente explicó que en casos de pulpitis irreversible severa el pH del tejido inflamado acidifica el medio e inactiva parcialmente la anestesia troncular; cuando al tocar el techo cameral el paciente manifiesta molestia aguda, se debe aplicar anestesia intrapulpar directa con aguja fina introducida a presión dentro del tejido pulpar, lo que genera analgesia inmediata por compresión hidrostática y acción farmacológica.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Técnicas anestésicas: bloqueo del dentario inferior y anestesia intrapulpar",
        que="Describir los pasos del bloqueo del dentario inferior (bisel, aspiración, depósito lento) y la técnica intrapulpar complementaria.",
        clave="El bloqueo del dentario exige bisel hacia hueso, aspiración en dos planos y depósito lento; el dolor residual se controla con anestesia intrapulpar a presión.",
        pistas=[
            "Recuerda la posición del bisel de la aguja y la maniobra de seguridad para no inyectar dentro de una arteria o vena.",
            "Ten en cuenta la técnica de rescate enseñada por el profesor cuando la troncular no duerme del todo una pulpa muy inflamada."
        ],
        plan=[
            "Aplicar las normas biomecánicas de seguridad de la punción troncular mandibular.",
            "Realizar la aspiración en dos planos para prevenir complicaciones intravasculares.",
            "Manejar la falla anestésica por acidez tisular mediante anestesia intrapulpar a presión."
        ],
        marcas_data=[
            ("principios de la técnica correcta del bloqueo del nervio dentario inferior", "clave", "Técnica de anestesia troncular", "Demanda bisel hacia hueso, aspiración doble y lentitud"),
            ("conducta si persiste dolor al abrir la cámara pulpar", "pide", "Técnica anestésica complementaria", "Demanda formular anestesia intrapulpar a presión")
        ],
        steps_ideas=[
            ("idea", "Bisel y hueso", "El bisel mira hacia el hueso de la rama para no desgarrar tejidos ni deflectarse."),
            ("idea", "Aspiración en dos planos", "Se aspira, se gira la jeringa un cuarto de vuelta y se vuelve a aspirar para confirmar que no sale sangre."),
            ("idea", "Anestesia intrapulpar", "Si la pulpa sigue doliendo por la inflamación ácida, se inyecta con aguja corta a presión dentro de la cámara."),
            ("check", "Comprobación clínica", "Confirmamos bisel a hueso, aspiración en dos planos, inyección lenta y anestesia intrapulpar a presión.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos con atención la técnica anestésica troncular enseñada por el profesor para molares inferiores."),
            ("m:principios de la técnica correcta del bloqueo del nervio dentario inferior", "Fíjate en las tres reglas de oro: cómo va el bisel, cómo se aspira y a qué velocidad se inyecta."),
            ("leer", "El docente enseñó: bisel hacia el hueso, aspirar en dos planos girando la jeringa y depositar el líquido con calma."),
            ("leer", "Si al abrir la muela la pulpa todavía duele por la inflamación severa, se aplica anestesia intrapulpar a presión directa."),
            ("leer", "Por lo tanto, la opción que describe estos pasos exactos de la clase es la correcta.")
        ]
    ))

    # 44 (Key D = 3) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-044", nivel=2,
        enunciado="En el inicio de la Clase 2 sobre histología y patología pulpar (líneas novecientos cincuenta y tres a novecientos ochenta y uno), el profesor describe la estructura tisular interna de la pulpa dental dividiéndola en cuatro capas o zonas concéntricas desde la predentina hacia el centro. ¿Cuál es el orden secuencial correcto de estas cuatro capas histológicas?",
        opciones=[
            "Cemento celular periférico, ligamento periodontal elástico, hueso alveolar esponjoso y médula hematopoyética mandibular.",
            "Esmalte adamantino externo, dentina secundaria media, unión amelocementaria y foramen apical permeable.",
            "Epitelio plano estratificado no queratinizado, membrana basal celular, tejido conectivo laxo submucoso y periostio óseo.",
            "Capa de odontoblastos en la periferia, zona acelular o pobre en células de Weil, zona rica en células (fibroblastos y células de Höhl), y el estroma o núcleo pulpar central."
        ],
        correcta=3,
        distractores=[
            "El cemento, ligamento y hueso corresponden al periodonto de inserción periapical, no a las capas internas de la pulpa dental.",
            "El esmalte y la dentina son tejidos duros mineralizados de la corona, no las capas histológicas celulares del tejido pulpar blando.",
            "El epitelio plano estratificado y la submucosa corresponden a la mucosa gingival oral, no a la pulpa dental que es mesenquimal.",
            ""
        ],
        explicacion="En las líneas novecientos cincuenta y tres a novecientos ochenta y uno del texto fuente, el profesor expuso minuciosamente la arquitectura histológica de la pulpa dental, detallando sus cuatro zonas concéntricas: 1) Capa de odontoblastos: capa periférica de células cilíndricas altamente especializadas cuyos cuerpos celulares se alinean contra la predentina y sus prolongaciones recorren los túbulos dentinarios; 2) Zona acelular de Weil (o zona pobre en células): capa estrecha situada inmediatamente por debajo de los odontoblastos por donde transcurre el plexo capilar y el plexo nervioso de Raschkow; 3) Zona rica en células: caracterizada por una alta densidad de fibroblastos, células de reserva y células ectomesenquimales indiferenciadas (células de Höhl) capaces de diferenciarse en nuevos odontoblastoides; 4) Estroma o núcleo pulpar central: compuesto por tejido conectivo laxo con los grandes troncos vasculares, vénulas, vasos linfáticos y paquetes nerviosos que entran por el foramen apical.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Anatomía e histología pulpar: las cuatro capas concéntricas",
        que="Ordenar secuencialmente las cuatro zonas histológicas concéntricas de la pulpa dental desde la periferia al centro.",
        clave="Las cuatro capas concéntricas pulpares son: odontoblastos, zona acelular de Weil, zona rica en células y estroma o núcleo central.",
        pistas=[
            "Recuerda el esquema de la pulpa dental dibujado en clase desde la pared de dentina hacia el corazón de la cámara.",
            "Identifica la secuencia: primero los odontoblastos pegados a la dentina, luego la zona de Weil, luego la zona rica y al centro el estroma."
        ],
        plan=[
            "Reconocer la capa odontoblástica periférica en contacto directo con la predentina.",
            "Identificar la zona acelular de Weil que contiene los plexos nervioso y capilar.",
            "Ordenar la zona rica en células y el estroma o núcleo conectivo vascular central."
        ],
        marcas_data=[
            ("cuatro capas o zonas concéntricas desde la predentina hacia el centro", "clave", "Arquitectura histológica de la pulpa", "Demanda el orden concéntrico de odontoblastos a estroma central"),
            ("¿Cuál es el orden secuencial correcto de estas cuatro capas histológicas?", "pide", "Secuencia histológica", "Demanda seleccionar la alternativa con las cuatro zonas exactas")
        ],
        steps_ideas=[
            ("idea", "Capa odontoblástica", "Los odontoblastos están en la orilla exterior fabricando dentina."),
            ("idea", "Zona acelular de Weil", "Justo debajo de los odontoblastos hay una franja clarita con pocos núcleos celulares (zona de Weil)."),
            ("idea", "Zona rica y estroma", "Sigue una zona densa repleta de células de defensa y reserva, y en el centro está el núcleo con los grandes vasos."),
            ("check", "Comprobación histológica", "Confirmamos odontoblastos, zona acelular de Weil, zona rica en células y núcleo pulpar central.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos este fundamento biológico de la Clase dos sobre las capas internas de la pulpa."),
            ("m:cuatro capas o zonas concéntricas desde la predentina hacia el centro", "Observa que el docente pide el orden de afuera hacia adentro, desde la pared del diente hacia el centro."),
            ("leer", "En la orilla están pegados los odontoblastos formando predentina."),
            ("leer", "Debajo de ellos está la zona acelular o pobre en células de Weil, y luego la zona rica en células de reserva."),
            ("leer", "En el centro de la pulpa se encuentra el estroma o núcleo pulpar con los vasos principales.")
        ]
    ))

    # 45 (Key A = 0) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-045", nivel=2,
        enunciado="Siguiendo con la biología pulpar en la Clase 2 (líneas novecientos ochenta y tres a mil uno), el docente detalla las cinco funciones fundamentales que cumple el complejo dentinopulpar a lo largo de toda la vida del diente. ¿Cuáles son estas cinco funciones biológicas?",
        opciones=[
            "Formativa (sintetiza dentina primaria, secundaria y terciaria), nutritiva (aporta nutrientes por lecho capilar), sensitiva (inervación sensorial), defensiva (reacción inflamatoria y esclerosis) e inductora (guía el desarrollo embrionario).",
            "Masticatoria de trituración, fonética de pronunciación, deglutoria de bolo alimenticio, gustativa de sabores y salival por secreción de amilasa directa.",
            "Digestiva de carbohidratos en cámara, lubricante de la mucosa lingual, excretora de urea plasmática y termorreguladora sistémica facial.",
            "Inmunológica de rechazo de implantes óseos, productora de esmalte permanente, queratinizante gingival y propioceptiva articular temporomandibular."
        ],
        correcta=0,
        distractores=[
            "",
            "La masticación, fonética y deglución son funciones del sistema estomatognático completo, no de la pulpa dental interna.",
            "La pulpa dental no cumple funciones digestivas de alimentos ni de excreción de urea en la cavidad oral.",
            "La pulpa no produce esmalte dental (el esmalte lo producen los ameloblastos del órgano del esmalte) ni queratiniza encías."
        ],
        explicacion="En las líneas novecientos ochenta y tres a mil uno, el profesor expuso las cinco funciones capitales de la pulpa dental: 1) Formativa: sintetiza la dentina a lo largo de toda la vida (dentina primaria durante la odontogénesis, dentina secundaria fisiológica tras la erupción, y dentina terciaria reactiva o reparativa ante agresiones); 2) Nutritiva: mantiene la vitalidad y el intercambio metabólico de la dentina mediante la red microvascular capilar; 3) Sensitiva: transmite sensaciones dolorosas ante estímulos térmicos, osmóticos, químicos o mecánicos mediante fibras A-delta y C; 4) Defensiva: responde a las agresiones microbianas con vasodilatación, quimiotaxis leucocitaria, aposición de dentina esclerótica y dentina terciaria para proteger el tejido vital; 5) Inductora: durante la embriogénesis induce al epitelio odontogénico circundante para la formación del esmalte dental.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Biología pulpar: las cinco funciones del complejo dentinopulpar",
        que="Reconocer las cinco funciones cardinales de la pulpa: formativa, nutritiva, sensitiva, defensiva e inductora.",
        clave="Las cinco funciones pulpares son formativa (dentina), nutritiva (vasos), sensitiva (dolor), defensiva (reparación) e inductora (embriogénesis).",
        pistas=[
            "Recuerda la lista de las cinco funciones que el profesor explicó que hacen de la pulpa un tejido vivo único.",
            "Ten en cuenta que la pulpa forma dentina, nutre el diente, avisa con dolor, se defiende y en el embrión induce la formación dental."
        ],
        plan=[
            "Enumerar las cinco funciones biológicas del complejo dentinopulpar.",
            "Comprender la función formativa continua de dentina primaria, secundaria y terciaria.",
            "Reconocer las funciones protectoras defensivas y la función inductora embrionaria."
        ],
        marcas_data=[
            ("cinco funciones fundamentales que cumple el complejo dentinopulpar a lo largo de toda la vida del diente", "clave", "Funciones biológicas pulpares", "Demanda identificar formativa, nutritiva, sensitiva, defensiva e inductora"),
            ("¿Cuáles son estas cinco funciones biológicas?", "pide", "Lista de funciones", "Demanda seleccionar la descripción funcional exacta")
        ],
        steps_ideas=[
            ("idea", "Formativa y nutritiva", "La pulpa forma dentina todos los días y nutre los túbulos con sus capilares."),
            ("idea", "Sensitiva y defensiva", "Transmite dolor para avisar que hay peligro y produce dentina de defensa ante las caries."),
            ("idea", "Inductora", "En el embrión la papila pulpar induce al epitelio para que fabrique el esmalte."),
            ("check", "Comprobación biológica", "Confirmamos las cinco funciones: formativa, nutritiva, sensitiva, defensiva e inductora.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este tema conceptual de la Clase dos sobre para qué sirve la pulpa dental."),
            ("m:cinco funciones fundamentales que cumple el complejo dentinopulpar a lo largo de toda la vida del diente", "Observa que el docente enumeró cinco funciones biológicas específicas del tejido pulpar."),
            ("leer", "La pulpa es formativa porque crea dentina, y nutritiva porque aporta sangre a los odontoblastos."),
            ("leer", "Es sensitiva porque transmite el dolor con sus nervios, y defensiva porque se inflama y se protege ante la caries."),
            ("leer", "Y es inductora porque en el embrión guía el desarrollo del diente completo.")
        ]
    ))

    # 46 (Key B = 1) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-046", nivel=2,
        enunciado="En la explicación sobre los tejidos periapicales (líneas mil tres a mil cuarenta), el profesor profundiza sobre el foramen apical, el ligamento periodontal, el cemento y el hueso alveolar. ¿Cuál es el rol propioceptivo y biomecánico fundamental del ligamento periodontal ante las fuerzas oclusales y los procesos inflamatorios?",
        opciones=[
            "Bloquear completamente el flujo sanguíneo de la mandíbula cuando el paciente abre la boca durante la masticación en el sillón.",
            "Amortiguar el impacto mecánico oclusal distribuyendo las fuerzas al hueso alveolar y albergar mecanorreceptores y propioceptores que localizan con exactitud el diente inflamado.",
            "Producir esmalte dental accesorio en la raíz para sellar las cavidades de caries subgingivales en el tercio apical.",
            "Inervar la lengua y los músculos de la mímica facial mediante axones motores eferentes procedentes del ganglio ótico."
        ],
        correcta=1,
        distractores=[
            "El ligamento periodontal no interrumpe el flujo sanguíneo de la arteria alveolar inferior ni de la mandíbula al masticar.",
            "",
            "El esmalte dental solo es producido por los ameloblastos en la corona durante el desarrollo y nunca en la raíz por el ligamento.",
            "La inervación del ligamento es sensitiva sensorial trigeminal, no inerva la musculatura lingual ni facial motora."
        ],
        explicacion="En las líneas mil tres a mil cuarenta del texto fuente, el profesor explicó la anatomía y fisiología de los tejidos periapicales: el ligamento periodontal es una estructura de tejido conectivo denso situada entre el cemento radicular y la lámina dura del alvéolo óseo. Cumple una doble función esencial: 1) Biomecánica: actúa como amortiguador hidráulico transformando las presiones oclusales en fuerzas de tracción elástica distribuidas al hueso alveolar; 2) Sensorial y propioceptiva: a diferencia de la pulpa (cuyas fibras solo transmiten dolor sordo o agudo y no poseen propiocepción para identificar qué diente duele), el ligamento periodontal está ricamente inervado por mecanorreceptores y propioceptores especializados. Por ello, cuando un proceso inflamatorio se extiende de la pulpa al ligamento (periodontitis apical), el paciente es capaz de señalar con el dedo exactamente cuál diente le duele ante el más leve contacto.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Tejidos periapicales: rol biomecánico y propioceptivo del ligamento",
        que="Explicar las funciones biomecánicas y la propiocepción del ligamento periodontal en la localización del dolor dental.",
        clave="El ligamento periodontal amortigua fuerzas y alberga mecanorreceptores que permiten al paciente localizar con exactitud el diente inflamado.",
        pistas=[
            "Recuerda que la pulpa no sabe cuál diente duele, pero el ligamento periodontal sí porque tiene propiocepción.",
            "Ten en cuenta la función de suspensión elástica que amortigua la fuerza de la mordida sobre el hueso."
        ],
        plan=[
            "Describir la inserción de las fibras colágenas del ligamento entre el cemento y el hueso alveolar.",
            "Comprender la transformación biomecánica de presiones masticatorias en tracciones óseas.",
            "Explicar la función propioceptiva que permite localizar con precisión el diente con periodontitis apical."
        ],
        marcas_data=[
            ("profundiza sobre el foramen apical, el ligamento periodontal, el cemento y el hueso alveolar", "clave", "Tejidos periapicales", "Apunta a anatomía y fisiología del soporte dental"),
            ("¿Cuál es el rol propioceptivo y biomecánico fundamental del ligamento periodontal ante las fuerzas oclusales y los procesos inflamatorios?", "pide", "Rol fisiológico", "Demanda contrastar con la falta de propiocepción pulpar")
        ],
        steps_ideas=[
            ("idea", "Amortiguador elástico", "El ligamento periodontal suspende el diente en el alvéolo y reparte la fuerza de masticación al hueso."),
            ("idea", "Propiocepción periapical", "El docente explicó que el ligamento tiene mecanorreceptores que le avisan al cerebro exactamente cuál diente se tocó."),
            ("idea", "Dolor pulpar vs periodontal", "En la pulpa el dolor es difuso; en el ligamento el paciente pone el dedo exactamente en la muela que duele."),
            ("check", "Comprobación funcional", "Confirmamos amortiguación oclusal y propiocepción sensorial para localizar el diente inflamado.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta diferencia clave entre la pulpa y el ligamento periodontal explicada por el docente."),
            ("m:profundiza sobre el foramen apical, el ligamento periodontal, el cemento y el hueso alveolar", "Observa qué estructuras forman los tejidos periapicales y cómo protegen al diente."),
            ("leer", "El docente explicó que la pulpa no tiene propiocepción (por eso el dolor pulpar es difuso y confuso)."),
            ("leer", "Pero el ligamento periodontal está lleno de receptores mecánicos y propioceptivos."),
            ("leer", "Por eso, cuando el ligamento se inflama, amortigua la carga y le permite al paciente señalar con el dedo qué diente duele.")
        ]
    ))

    # 47 (Key C = 2) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-047", nivel=2,
        enunciado="Al analizar las causas de las enfermedades pulpares (líneas mil cuarenta y uno a mil ciento cincuenta y cinco, y dos mil cuatrocientos veinticuatro a dos mil cuatrocientos cuarenta y dos), el docente describe las vías bacterianas, traumáticas e iatrogénicas, y destaca un fenómeno biológico denominado «anacoresis». ¿Cómo define el profesor la anacoresis pulpar en la clase?",
        opciones=[
            "La destrucción física del esmalte coronal causada por el uso de cepillos dentales con cerdas demasiado duras y pastas ácidas.",
            "La fusión anatómica de dos gérmenes dentarios vecinos durante la fase de campana del desarrollo embrionario maxilar.",
            "La migración y fijación de microorganismos a través del torrente sanguíneo hacia una pulpa previamente inflamada o traumatizada, provocando necrosis en dientes aparentemente sanos.",
            "La regeneración espontánea de odontoblastos inducida por el consumo de suplementos vitamínicos diarios en la dieta del paciente."
        ],
        correcta=2,
        distractores=[
            "La destrucción por cepillado y abrasivos es una lesión no cariosa mecánica en esmalte, no el fenómeno biológico de la anacoresis.",
            "La unión de dos gérmenes dentarios es una anomalía de desarrollo denominada fusión o geminación dental embrionaria.",
            "",
            "La regeneración celular no se denomina anacoresis; la anacoresis es una vía hematógena de infección microbiana tisular."
        ],
        explicacion="En las líneas dos mil cuatrocientos veinticuatro a dos mil cuatrocientos cuarenta y dos, el profesor explicó textualmente el concepto de anacoresis: «La anacoresis es una migración de bacterias a través del torrente sanguíneo. Pacientes que tenían una enfermedad sistémica o bacteriemia transitoria terminaron con necrosis pulpar sin causas aparentes externas, porque los dientes estaban clínicamente sanos sin caries». Cuando un diente sufre un microtrauma previo o una inflamación subclínica, los vasos pulpares presentan aumento de permeabilidad vascular y marginación leucocitaria; si en ese momento ocurre una bacteriemia transitoria en el organismo, las bacterias circulantes se adhieren al endotelio lesionado de la pulpa, colonizan el tejido pulpar y desencadenan una infección bacteriana con necrosis en un órgano dental con corona intacta.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Causas de patología pulpar: concepto de anacoresis",
        que="Definir el fenómeno de anacoresis como la llegada de bacterias a la pulpa por vía hematógena en dientes sin caries.",
        clave="La anacoresis es la migración bacteriana a través de la sangre hacia una pulpa previamente inflamada provocando necrosis sin caries visible.",
        pistas=[
            "Recuerda la definición textual del profesor: bacterias que viajan por el torrente sanguíneo hasta el diente.",
            "Ten en cuenta cómo puede necrosarse un diente completamente sano sin caries ni fractura externa aparente."
        ],
        plan=[
            "Reconocer las vías clásicas de infección pulpar: coronaria directa, periodontal retrógrada y hematógena.",
            "Definir el concepto específico de anacoresis pulpar según lo expuesto en clase.",
            "Comprender la fijación bacteriana sobre endotelio inflamado durante episodios de bacteriemia."
        ],
        marcas_data=[
            ("destaca un fenómeno biológico denominado «anacoresis»", "clave", "Fenómeno biológico en estudio", "Apunta a vía hematógena de infección pulpar"),
            ("¿Cómo define el profesor la anacoresis pulpar en la clase?", "pide", "Definición textual del profesor", "Demanda asociar bacterias por sangre hacia pulpa inflamada en diente sano")
        ],
        steps_ideas=[
            ("idea", "Infección sin caries", "Un paciente con dientes sanos puede presentar necrosis si las bacterias llegaron por la sangre."),
            ("idea", "Definición del docente", "El profesor dijo textualmente: 'la anacoresis es una migración de bacterias a través del torrente sanguíneo'."),
            ("idea", "Atracción por inflamación", "Las bacterias circulantes se anclan en la pulpa si esta sufrió un microtrauma o inflamación previa."),
            ("check", "Comprobación clínica", "Confirmamos anacoresis como migración bacteriana sanguínea hacia la pulpa dental.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta vía de infección bacteriana explicada por el profesor en la Clase dos."),
            ("m:destaca un fenómeno biológico denominado «anacoresis»", "Observa este término científico que el docente definió de manera muy clara."),
            ("leer", "El docente explicó que a veces un paciente llega con una muela muerta pero sin ninguna caries ni empaste."),
            ("leer", "La explicación es la anacoresis: bacterias que viajaban en la sangre se fijan en la pulpa si esta tenía una inflamación previa."),
            ("leer", "Por lo tanto, la opción que describe la migración de bacterias a través del torrente sanguíneo es la respuesta correcta.")
        ]
    ))

    # 48 (Key D = 3) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-048", nivel=2,
        enunciado="Durante la revisión de las causas iatrogénicas de inflamación y necrosis pulpar (líneas mil cuarenta y uno a mil noventa), el docente analiza los errores operatorios en odontología restauradora y ortodoncia. ¿Cuáles son los principales factores iatrogénicos capaces de inducir daño pulpar irreversible durante los procedimientos dentales?",
        opciones=[
            "El uso de agua potable purificada en la jeringa triple y el secado de la cavidad con gasa estéril durante tres segundos continuos.",
            "La colocación de rollos de algodón en el vestíbulo inferior para realizar una profilaxis con pasta fluorada de consistencia suave.",
            "La toma de impresiones dentales con alginato a temperatura ambiente en dientes con esmalte sano y encía marginal normal.",
            "El tallado cavitario sin abundante refrigeración con agua, el uso de fresas desgastadas que generan calor friccional excesivo, y la aplicación de fuerzas ortodónticas continuas excesivas que colapsan la microcirculación apical."
        ],
        correcta=3,
        distractores=[
            "El lavado con agua purificada y el secado suave con gasa son maniobras operatorias fisiológicas seguras que no dañan la pulpa.",
            "El aislamiento relativo para profilaxis no genera ningún tipo de daño iatrogénico en el tejido pulpar cameral.",
            "La toma de impresiones con alginato es un procedimiento diagnóstico inocuo para la vitalidad pulpar de dientes íntegros.",
            ""
        ],
        explicacion="El docente recalcó que no todas las patologías pulpares son producidas por caries: los procedimientos dentales mal ejecutados representan una causa iatrogénica mayor de necrosis. Los factores determinantes son: 1) Calor friccional: tallar esmalte o dentina con pieza de mano de alta velocidad sin irrigación constante de agua o con fresas desgastadas genera temperaturas que superan ampliamente los cinco grados de aumento intrapulpar, quemando la capa de odontoblastos y desnaturalizando las proteínas pulpares; 2) Desecación dentinaria agresiva con chorros continuos de aire comprimido deshidrata los túbulos y aspira los núcleos odontoblásticos hacia el interior de la dentina; 3) Fuerzas ortodónticas pesadas o descontroladas comprimen el paquete vasculonervioso en el foramen apical, provocando isquemia tisular prolongada, trombosis vascular y necrosis pulpar aséptica.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Causas iatrogénicas de patología pulpar: calor friccional y ortodoncia",
        que="Reconocer los factores iatrogénicos operatorios (fresas sin corte, falta de refrigeración) y ortodónticos de daño pulpar.",
        clave="El tallado sin agua, las fresas desgastadas con calor friccional y las fuerzas ortodónticas excesivas inducen necrosis iatrogénica.",
        pistas=[
            "Recuerda la advertencia del profesor sobre qué le pasa a la pulpa si tallas una muela sin buen chorro de agua fría.",
            "Ten en cuenta cómo las fuerzas pesadas de ortodoncia estrangulan el paquete vascular en el ápice."
        ],
        plan=[
            "Identificar el calor friccional por turbina sin refrigeración acuosa como causa mayor de necrosis iatrogénica.",
            "Evaluar el daño celular por uso de fresas gastadas y desecación dentinaria descontrolada.",
            "Comprender el efecto isquémico periapical de fuerzas ortodónticas continuas sobre los vasos apicales."
        ],
        marcas_data=[
            ("errores operatorios en odontología restauradora y ortodoncia", "clave", "Iatrogenia dental sobre la pulpa", "Apunta a calor friccional sin agua y sobrecarga ortodóntica"),
            ("¿Cuáles son los principales factores iatrogénicos capaces de inducir daño pulpar irreversible durante los procedimientos dentales?", "pide", "Factores iatrogénicos", "Demanda identificar tallado sin agua, fresas viejas y fuerzas pesadas")
        ],
        steps_ideas=[
            ("idea", "Calor friccional", "Tallar sin agua quema la pulpa; si la temperatura sube cinco grados se destruyen los odontoblastos."),
            ("idea", "Fresas viejas", "Una fresa sin corte no corta sino que fricciona y genera un calor abrasivo extremo."),
            ("idea", "Fuerzas de ortodoncia", "Apretar los brackets con fuerzas excesivas aplasta los vasos del ápice causando necrosis por isquemia."),
            ("check", "Comprobación clínica", "Confirmamos falta de agua, fresas desgastadas y fuerzas ortodónticas excesivas como causas iatrogénicas.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta advertencia clínica del profesor sobre los daños que el propio odontólogo puede causar a la pulpa."),
            ("m:errores operatorios en odontología restauradora y ortodoncia", "Observa que no solo las bacterias enferman a la pulpa: una mala técnica odontológica también la mata."),
            ("leer", "El docente enseñó que tallar dientes sin suficiente agua fría o con fresas desgastadas quema la pulpa viva."),
            ("leer", "También advirtió que aplicar fuerzas de ortodoncia demasiado fuertes ahoga el paquete de vasos del ápice."),
            ("leer", "Por lo tanto, la opción que describe el tallado sin agua, fresas desgastadas y fuerzas ortodónticas es la correcta.")
        ]
    ))

    # 49 (Key A = 0) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-049", nivel=2,
        enunciado="En el manejo de los traumatismos dentoalveolares en la Clase 2 (líneas mil ciento treinta y cuatro a mil ciento cincuenta), el docente enfatiza que las complicaciones pulpares y periodontales no siempre son inmediatas. ¿Cuál es el protocolo estricto de controles clínicos y radiográficos que debe seguirse tras un trauma para detectar secuelas a tiempo?",
        opciones=[
            "Realizar control clínico y radiográfico el día del accidente (día cero), a los quince días, un mes, tres meses, seis meses, doce meses y anualmente durante seis años.",
            "Realizar un único control a los diez años del traumatismo si el paciente nota dolor insoportable espontáneo en la arcada dental.",
            "Citar al paciente cada semana durante doce años consecutivos tomando radiografías oclusales cada cuarenta y ocho horas en el consultorio.",
            "No realizar ningún control posterior si el diente no presenta fractura de corona visible a simple vista el primer día de la consulta."
        ],
        correcta=0,
        distractores=[
            "",
            "Esperar diez años sin controles periódicos permite que reabsorciones radiculares silenciosas destruyan la raíz por completo.",
            "Citar semanalmente durante doce años con radiografías cada dos días expone al paciente a radiación innecesaria y no sigue ningún protocolo científico.",
            "Un diente con corona intacta tras un golpe puede sufrir necrosis o reabsorción interna; suspender controles es una mala práctica."
        ],
        explicacion="En las líneas mil ciento treinta y cuatro a mil ciento cincuenta del texto fuente, el profesor explicó que las secuelas postraumáticas (necrosis aséptica, obliteración o calcificación del conducto, reabsorción radicular externa inflamatoria o anquilosis por reemplazo) pueden tardar meses e incluso hasta seis años en evidenciarse clínica o radiográficamente. Por este motivo, el protocolo científico de seguimiento postraumatismo exige evaluaciones periódicas: 1) Día del accidente (registro basal con pruebas de sensibilidad y radiografía inicial); 2) A los quince días; 3) Al mes; 4) A los tres meses; 5) A los seis meses; 6) A los doce meses; y 7) Un control anual hasta completar seis años de evolución postraumática.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Traumatología dental: protocolo de controles postraumáticos hasta seis años",
        que="Conocer el calendario exacto de controles clínicos y radiográficos postraumatismo (día cero, quince días, uno, tres, seis, doce meses y hasta seis años).",
        clave="El calendario postrauma exige controles a día cero, quince días, un mes, tres, seis, doce meses y anualmente hasta seis años.",
        pistas=[
            "Recuerda la cifra de años máxima hasta la cual el profesor advirtió que pueden aparecer las secuelas de un golpe.",
            "Ten en cuenta los intervalos progresivos de control: quince días, un mes, tres, seis y doce meses."
        ],
        plan=[
            "Comprender la cronología tardía de las complicaciones postraumáticas pulpares y periodontales.",
            "Memorizar el calendario escalonado de controles clínicos y radiográficos estandarizado.",
            "Establecer la vigilancia anual obligatoria hasta completar el sexto año postraumatismo."
        ],
        marcas_data=[
            ("las complicaciones pulpares y periodontales no siempre son inmediatas", "clave", "Secuelas tardías de trauma", "Demanda el esquema temporal progresivo de día cero a seis años"),
            ("¿Cuál es el protocolo estricto de controles clínicos y radiográficos que debe seguirse tras un trauma para detectar secuelas a tiempo?", "pide", "Calendario de citas", "Demanda identificar la secuencia temporal exacta de la clase")
        ],
        steps_ideas=[
            ("idea", "Secuelas tardías", "El profesor enseñó que las secuelas de un trauma dental pueden tardar hasta seis años en aparecer."),
            ("idea", "Primer año de control", "Se cita a día cero, quince días, un mes, tres meses, seis meses y un año."),
            ("idea", "Controles a largo plazo", "Luego de un año, se hace una cita anual de control clínico y radiográfico hasta cumplir seis años."),
            ("check", "Comprobación del protocolo", "Confirmamos el protocolo de día cero, quince días, un mes, tres, seis, doce meses y anual a seis años.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos con cuidado este protocolo de traumatología dental enseñado por el profesor en la Clase dos."),
            ("m:las complicaciones pulpares y periodontales no siempre son inmediatas", "Observa que un golpe en un diente no se despacha en una sola cita y ya."),
            ("leer", "El docente explicó que el daño del golpe puede tardar hasta seis años en verse en la radiografía."),
            ("leer", "Por eso enseñó este calendario estricto: día cero, quince días, un mes, tres meses, seis meses, doce meses..."),
            ("leer", "...y luego una cita cada año hasta completar seis años de seguimiento riguroso.")
        ]
    ))

    # 50 (Key B = 1) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-050", nivel=3,
        enunciado="Un paciente de 8 años sufre una fractura no complicada de esmalte y dentina en un incisivo central superior permanente con exposición pulpar pequeña en un diente con ápice radicular inmaduro ampliamente abierto (foramen en trabuco o embudo). La pulpa está vital y responde positivamente a las pruebas térmicas. De acuerdo con lo explicado por el profesor (líneas dos mil ciento catorce a dos mil ciento sesenta), ¿cuál es el tratamiento biológico de elección y su objetivo fundamental?",
        opciones=[
            "Apexificación con hidróxido de calcio y tapón de gutapercha caliente para inducir la momificación del conducto radicular.",
            "Apexogénesis mediante pulpotomía cameral con biocerámico (Biodentine o MTA); su objetivo es mantener la pulpa radicular vital para que culmine el desarrollo fisiológico en longitud y grosor radicular y el cierre apical.",
            "Exodoncia inmediata del diente permanente y colocación de una prótesis fija definitiva con desgaste de dientes vecinos sanos.",
            "Obturación convencional de conductos con cono único de gutapercha y cemento sellador eugenolado en una sola sesión de trabajo."
        ],
        correcta=1,
        distractores=[
            "La apexificación está indicada cuando la pulpa está necrótica (muerta), no cuando la pulpa está vital y en crecimiento.",
            "",
            "La exodoncia de un diente permanente joven con pulpa vital es una mutilación clínica totalmente contraindicada.",
            "Obturar con gutapercha convencional un ápice abierto en trabuco extruye el material al hueso y no permite que la raíz madure."
        ],
        explicacion="En las líneas dos mil ciento catorce a dos mil ciento sesenta, el profesor abordó minuciosamente la disyuntiva en dientes jóvenes con ápices abiertos en función de la vitalidad pulpar: si la pulpa está VITAL, el procedimiento indicado es la APEXOGÉNESIS (terapia pulpar vital). Consiste en remover la pulpa cameral inflamada (pulpotomía cameral superficial o cervical), lograr hemostasia con suero frío en menos de cinco minutos y colocar un silicato de calcio biocerámico (Biodentine o MTA) sobre el muñón radicular vital. El objetivo biológico supremo de la apexogénesis es preservar la vitalidad de la pulpa radicular para que los odontoblastos continúen depositando dentina radicular fisiológica, permitiendo que la raíz alcance su longitud completa, engrose sus paredes para no fracturarse y cierre naturalmente el foramen apical.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Terapéutica en ápice abierto: apexogénesis en pulpa vital",
        que="Indicar la apexogénesis con biocerámicos para preservar la pulpa radicular vital y lograr el desarrollo radicular completo.",
        clave="La apexogénesis se realiza con pulpa vital para que la raíz termine de formarse en longitud, grosor y cierre apical.",
        pistas=[
            "Fíjate en las dos condiciones clave: el ápice está inmaduro abierto y la pulpa está VITAL.",
            "Recuerda la regla del profesor: vital es apexogénesis para que siga creciendo la raíz; muerta es apexificación."
        ],
        plan=[
            "Constatar la vitalidad de la pulpa radicular en un diente permanente inmaduro.",
            "Seleccionar la apexogénesis mediante pulpotomía y biocerámico biocompatible.",
            "Definir el objetivo biológico de desarrollo fisiológico del grosor y longitud radicular."
        ],
        marcas_data=[
            ("ápice radicular inmaduro ampliamente abierto", "dato", "Condición anatómica de inmadurez", "Apunta a foramen divergente en formación"),
            ("La pulpa está vital y responde positivamente a las pruebas térmicas", "clave", "Vitalidad pulpar conservada", "Apunta a indicación estricta de apexogénesis"),
            ("¿cuál es el tratamiento biológico de elección y su objetivo fundamental?", "pide", "Tratamiento y objetivo biológico", "Demanda formular apexogénesis y maduración radicular completa")
        ],
        steps_ideas=[
            ("idea", "Regla de oro del profesor", "El docente enseñó: si la pulpa está viva en ápice abierto, se hace apexogénesis."),
            ("idea", "Pulpotomía con biocerámico", "Se quita solo la parte de arriba de la pulpa y se sella con Biodentine o MTA."),
            ("idea", "Objetivo biológico", "La pulpa de la raíz queda viva para que termine de cerrar el ápice y engrose las paredes."),
            ("check", "Comprobación clínica", "Confirmamos apexogénesis con pulpotomía y biocerámico para culminar el desarrollo radicular.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta decisión terapéutica trascendental en odontopediatría y endodoncia."),
            ("m:ápice radicular inmaduro ampliamente abierto", "Observa que la raíz está a medio camino, abierta como un embudo en el ápice."),
            ("m:La pulpa está vital y responde positivamente a las pruebas térmicas", "Mira este dato fundamental: la pulpa está totalmente viva."),
            ("leer", "El profesor enseñó una regla clarísima: pulpa viva en diente con ápice abierto es igual a APEXOGÉNESIS."),
            ("leer", "Se hace pulpotomía con Biodentine o MTA para que la pulpa viva de la raíz termine de formar el diente y cierre el ápice.")
        ]
    ))

    # 51 (Key C = 2) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-051", nivel=3,
        enunciado="En contraste con el caso anterior, una niña de 9 años presenta un incisivo central superior con antecedente de golpe hace un año. El diente tiene el foramen radicular apical ampliamente abierto (inmaduro), pero la pulpa está completamente desvitalizada (necrosis pulpar con prueba de frío negativa y radiolucidez apical). De acuerdo con la clase (líneas dos mil ciento catorce a dos mil ciento sesenta), ¿cuál es el procedimiento indicado ante este diente no vital con foramen abierto y en qué consiste?",
        opciones=[
            "Apexogénesis directa con pulpotomía cameral dejando la pulpa necrótica en el tercio radicular para que cicatrice sola.",
            "Resección quirúrgica del ápice radicular con curetaje periapical y relleno con amalgama de plata sin desinfectar el conducto.",
            "Apexificación; desinfección química del conducto y colocación de un tapón apical artificial de biocerámico (MTA o Biodentine) de cuatro milímetros (o hidróxido de calcio) para sellar el foramen antes de obturar con gutapercha.",
            "Cierre de la cavidad con cemento de fosfato de zinc sin instrumentar ni irrigar el conducto radicular."
        ],
        correcta=2,
        distractores=[
            "La apexogénesis exige pulpa vital; dejar tejido necrótico infectado sin limpiar perpetúa la infección periapical destructiva.",
            "La cirugía periapical con corte radicular mutila una raíz que ya de por sí es corta y frágil en un niño de nueve años.",
            "",
            "Tapar sin instrumentar ni desinfectar un conducto necrótico produce un absceso agudo doloroso en pocos días."
        ],
        explicacion="En las líneas dos mil ciento catorce a dos mil ciento sesenta, el profesor estableció con total claridad la diferencia: cuando el diente con ápice abierto tiene la pulpa MUERTA (necrosis pulpar), ya no existen células vivas que puedan continuar formando raíz, por lo que está contraindicada la apexogénesis y el tratamiento obligatorio es la APEXIFICACIÓN. La apexificación consiste en desinfectar minuciosamente el conducto radicular con hipoclorito de sodio e hidróxido de calcio, y crear una barrera o tapón apical artificial en el extremo de la raíz mediante la condensación de un tapón de silicato biocerámico (MTA o Biodentine) de cuatro milímetros de espesor (o mediante el recambio periódico de hidróxido de calcio para inducir un tope calcificado duro), lo que permite condensar posteriormente la gutapercha sin que el material de obturación se salga al periápice.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Terapéutica en ápice abierto: apexificación en pulpa necrótica",
        que="Indicar la apexificación con tapón de biocerámico de cuatro milímetros en dientes necróticos con ápice abierto.",
        clave="La apexificación se realiza en pulpa necrótica desinfectando el conducto y colocando un tapón apical de biocerámico de cuatro milímetros.",
        pistas=[
            "Observa que el ápice está inmaduro abierto pero la pulpa está MUERTA (necrosis con prueba de frío negativa).",
            "Recuerda la técnica moderna enseñada por el profesor: tapón apical artificial de MTA o Biodentine de cuatro milímetros."
        ],
        plan=[
            "Reconocer la necrosis pulpar en diente con foramen radicular divergente inmaduro.",
            "Indicar la apexificación mediante desinfección profunda con hipoclorito e hidróxido de calcio.",
            "Crear un tapón apical artificial con cuatro milímetros de biocerámico para sellar antes de la gutapercha."
        ],
        marcas_data=[
            ("foramen radicular apical ampliamente abierto (inmaduro)", "dato", "Anatomía de foramen abierto", "Apunta a imposibilidad de obturación convencional con tope natural"),
            ("pulpa está completamente desvitalizada (necrosis pulpar con prueba de frío negativa", "clave", "Muerte pulpar confirmada", "Apunta a indicación estricta de apexificación"),
            ("¿cuál es el procedimiento indicado ante este diente no vital con foramen abierto y en qué consiste?", "pide", "Tratamiento y técnica", "Demanda formular apexificación y tapón apical biocerámico")
        ],
        steps_ideas=[
            ("idea", "Pulpa muerta en ápice abierto", "Como ya no hay pulpa viva, la raíz ya no va a crecer más de forma natural."),
            ("idea", "Concepto de apexificación", "El profesor explicó que se debe crear un tope o tapón duro artificial para poder tapar el hueco."),
            ("idea", "Tapón de biocerámico", "Se desinfecta y se coloca un tapón de MTA o Biodentine de cuatro milímetros en la punta del ápice."),
            ("check", "Comprobación clínica", "Confirmamos apexificación con desinfección y tapón apical artificial de biocerámico.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos la contraparte del caso anterior: ¿qué pasa cuando la pulpa en el ápice abierto se murió?"),
            ("m:pulpa está completamente desvitalizada (necrosis pulpar con prueba de frío negativa", "Observa que la prueba de frío dio negativa: la pulpa está muerta por el golpe."),
            ("m:foramen radicular apical ampliamente abierto (inmaduro)", "Y la raíz está abierta como un embudo, por lo que no se puede condensar gutapercha normal."),
            ("leer", "El docente enseñó la regla: pulpa muerta en ápice abierto es APEXIFICACIÓN."),
            ("leer", "Consiste en limpiar todo muy bien y poner un tapón apical duro de cuatro milímetros de MTA o Biodentine para poder sellar.")
        ]
    ))

    # 52 (Key D = 3) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-052", nivel=3,
        enunciado="Al tratar un molar con necrosis pulpar y una lesión periapical radiolúcida evidente, el docente discute en clase si se debe o no obturar los conductos en la primera sesión de trabajo (líneas mil seiscientos setenta y nueve a mil setecientos diez). ¿Cuál es la regla clínica obligatoria expuesta por el profesor respecto al número de citas y la medicación intraconducto?",
        opciones=[
            "Siempre se debe obturar en la primera cita en menos de diez minutos para ahorrar tiempo en la clínica dental.",
            "Se debe dejar el diente destapado sin medicación ni curación temporal durante un mes completo para que drene la saliva.",
            "Solo se obtura en dos citas si el paciente presenta caries en el diente contralateral de la arcada opuesta.",
            "No se debe obturar en una sola cita ante lesión periapical bacteriana; se realiza preparación biomecánica y medicación intraconducto con hidróxido de calcio durante ocho a diez días para desinfectar."
        ],
        correcta=3,
        distractores=[
            "Obturar de forma apresurada en una cita un conducto con lesión periapical infectada encierra bacterias y predispone a fracaso agudo.",
            "Dejar el diente destapado al medio bucal contamina el sistema de conductos con flora salival multirresistente grave.",
            "La decisión de citas depende del diagnóstico microbiológico periapical del diente afectado, no del estado de otros cuadrantes.",
            ""
        ],
        explicacion="En las líneas mil seiscientos setenta y nueve a mil setecientos diez del texto fuente, el profesor explicó la conducta clínica estricta: mientras que en una pulpitis irreversible sintomática sin lesión periapical el tratamiento se puede culminar perfectamente en una sola cita (si no hay sangrado persistente ni exudado), en presencia de NECROSIS PULPAR CON LESIÓN PERIAPICAL radiolúcida está contraindicado obturar en una sola sesión. La razón biológica es que la masa bacteriana coloniza los túbulos dentinarios profundos y las ramificaciones apicales; se debe realizar la instrumentación biomecánica completa y colocar una pasta de hidróxido de calcio intraconducto durante ocho a diez días. El hidróxido de calcio ejerce una potente acción antimicrobiana por su elevado pH básico de doce punto cuatro, hidroliza las endotoxinas bacterianas y seca el exudado periapical, garantizando un ambiente aséptico antes de la obturación definitiva.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Criterios de obturación: contraindicación de una cita en lesiones periapicales",
        que="Fundamentar por qué no se obtura en una sola cita un diente con lesión periapical y exigir hidróxido de calcio por ocho a diez días.",
        clave="En necrosis con lesión periapical está contraindicado obturar en una cita; se requiere medicación con hidróxido de calcio por ocho a diez días.",
        pistas=[
            "Recuerda la regla estricta del profesor sobre cuándo se puede hacer en una cita y cuándo NO.",
            "Ten en cuenta el tiempo de acción del hidróxido de calcio para eliminar bacterias intratubulares antes de obturar."
        ],
        plan=[
            "Diferenciar la microbiología de la pulpa vital frente a la necrosis con periodontitis apical.",
            "Fundamentar la necesidad biológica de la medicación intraconducto con hidróxido de calcio.",
            "Establecer el protocolo de dos sesiones con intervalo de ocho a diez días de desinfección."
        ],
        marcas_data=[
            ("molar con necrosis pulpar y una lesión periapical radiolúcida evidente", "dato", "Infección periapical bacteriana crónica", "Apunta a túbulos dentinarios infectados con biofilm"),
            ("¿Cuál es la regla clínica obligatoria expuesta por el profesor respecto al número de citas y la medicación intraconducto?", "clave", "Regla de citas del profesor", "Demanda formular la contraindicación de una cita y el uso de hidróxido de calcio")
        ],
        steps_ideas=[
            ("idea", "Una cita vs dos citas", "En pulpitis vital se puede en una cita; con lesión periapical bacteriana el profesor exige dos citas."),
            ("idea", "Acción del hidróxido de calcio", "El hidróxido de calcio necesita de ocho a diez días para matar las bacterias de los túbulos y neutralizar endotoxinas."),
            ("idea", "Éxito clínico", "Obturar solo cuando el conducto esté completamente seco, asintomático y desinfectado."),
            ("check", "Comprobación clínica", "Confirmamos la regla de no obturar en una cita con lesión periapical y medicar con hidróxido de calcio ocho a diez días.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos este debate clásico sobre si hacer la endodoncia en una o en dos sesiones."),
            ("m:molar con necrosis pulpar y una lesión periapical radiolúcida evidente", "Observa que aquí hay necrosis pulpar con una lesión ósea periapical llena de bacterias."),
            ("leer", "El docente fue muy claro en clase: si hay lesión en el hueso, NO se debe tapar en una sola cita."),
            ("leer", "Se debe limpiar muy bien el conducto y colocar hidróxido de calcio por ocho a diez días."),
            ("leer", "Ese tiempo permite que el hidróxido de calcio desinfecte los túbulos y seque el líquido periapical antes de obturar.")
        ]
    ))

    # 53 (Key A = 0) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-053", nivel=3,
        enunciado="En el manejo farmacológico del Absceso Apical Agudo en la Clase 2 (líneas mil setecientos doce a mil ochocientos dieciocho), el docente aclara cuándo se justifica la prescripción de antibióticos sistémicos y cuál es la pauta antibiótica de elección y alternativa para alérgicos. ¿Cuál es el criterio y régimen terapéutico enseñado en clase?",
        opciones=[
            "Se prescribe antibiótico únicamente si hay compromiso sistémico (fiebre, celulitis facial difusa, trismus o astenia); primera elección amoxicilina quinientos miligramos cada ocho horas por siete días; en alérgicos a penicilinas, clindamicina trescientos miligramos cada seis horas.",
            "Se prescribe antibiótico a todos los pacientes con dolor dental leve independientemente de que haya o no infección bacteriana periapical.",
            "Se indica tetraciclina en jarabe durante tres semanas continuas a niños menores de cinco años para blanquear el esmalte dental.",
            "Se prescribe ciprofloxacino en colirio ocular tres veces al día sin realizar apertura ni drenaje del diente causal."
        ],
        correcta=0,
        distractores=[
            "",
            "Prescribir antibióticos para dolores pulpares leves o localizados genera resistencia bacteriana masiva y no resuelve el dolor pulpar.",
            "Las tetraciclinas están contraindicadas en niños menores de ocho años porque se quelan con el calcio y manchan permanentemente los dientes.",
            "Los colirios oculares no tienen ninguna absorción ni efecto farmacológico sobre los abscesos óseos periapicales odontogénicos."
        ],
        explicacion="En las líneas mil setecientos doce a mil ochocientos dieciocho, el profesor recalcó las pautas de uso racional de antibióticos en endodoncia: 1) Los antibióticos NO sustituyen al tratamiento mecánico; si el absceso está localizado y no hay síntomas sistémicos, el drenaje por conducto y la biomecánica son suficientes sin necesidad de antibióticos; 2) La indicación de antibiótico sistémico es mandatoria cuando la infección se disemina generando celulitis facial difusa con borramiento de planos, trismus (limitación de apertura), fiebre, malestar general o linfoadenopatía regional; 3) El antibiótico de primera elección es la amoxicilina (quinientos miligramos cada ocho horas vía oral durante siete días consecutivos); 4) En pacientes alérgicos a los betalactámicos o penicilinas, la alternativa de elección en endodoncia es la clindamicina (trescientos miligramos cada seis horas durante siete días) por su excelente penetración en tejido óseo y cobertura contra flora anaerobia oral.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Farmacología en endodoncia: antibióticos en absceso agudo",
        que="Identificar los criterios de indicación de antibióticos en endodoncia y formular amoxicilina o clindamicina con posología.",
        clave="Los antibióticos se indican ante compromiso sistémico o trismus: amoxicilina quinientos miligramos c/ocho horas (o clindamicina trescientos miligramos en alérgicos).",
        pistas=[
            "Recuerda que el dolor local sin fiebre ni hinchazón difusa no requiere antibióticos.",
            "Ten presente la combinación de fármacos de la clase: amoxicilina para primera línea y clindamicina para alérgicos a penicilinas."
        ],
        plan=[
            "Establecer los criterios clínicos estrictos para prescribir antibióticos sistémicos en endodoncia.",
            "Formular el antibiótico de primera elección con dosis y frecuencia horaria en español.",
            "Seleccionar la clindamicina como alternativa en pacientes alérgicos a los betalactámicos."
        ],
        marcas_data=[
            ("cuándo se justifica la prescripción de antibióticos sistémicos y cuál es la pauta antibiótica de elección y alternativa para alérgicos", "clave", "Criterios y pautas de prescripción", "Demanda identificar celulitis/trismus, amoxicilina y clindamicina"),
            ("¿Cuál es el criterio y régimen terapéutico enseñado en clase?", "pide", "Régimen terapéutico", "Demanda seleccionar las dosis y tiempos correctos en palabras")
        ],
        steps_ideas=[
            ("idea", "Uso racional de antibióticos", "El antibiótico no es para el dolor: es solo para cuando la infección se regó y hay fiebre o trismus."),
            ("idea", "Primera elección", "El docente enseñó amoxicilina quinientos miligramos cada ocho horas por siete días."),
            ("idea", "Alternativa en alérgicos", "Si el paciente es alérgico a la penicilina, la opción es clindamicina trescientos miligramos cada seis horas."),
            ("check", "Comprobación farmacológica", "Confirmamos antibiótico solo con compromiso sistémico: amoxicilina o clindamicina en alérgicos.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención las pautas de farmacología racional enseñadas por el profesor en la Clase dos."),
            ("m:cuándo se justifica la prescripción de antibióticos sistémicos y cuál es la pauta antibiótica de elección y alternativa para alérgicos", "Fíjate en las dos partes: cuándo se da antibiótico y cuáles son las pastillas adecuadas."),
            ("leer", "El docente enseñó que si no hay fiebre, trismus o hinchazón en la cara, no se debe formular antibiótico."),
            ("leer", "Pero si hay celulitis o trismus, se manda amoxicilina quinientos miligramos cada ocho horas por siete días."),
            ("leer", "Y si el paciente es alérgico a la penicilina, se formula clindamicina trescientos miligramos cada seis horas.")
        ]
    ))

    # 54 (Key B = 1) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-054", nivel=3,
        enunciado="Durante la atención de urgencia de un paciente con un absceso apical agudo con drenaje abundante de pus a través de la cavidad cameral, el operador se plantea cómo dejar el diente al finalizar la sesión. ¿Cuál es la advertencia enfática del profesor en clase (líneas mil setecientos doce a mil ochocientos dieciocho) sobre el sellado de la cavidad?",
        opciones=[
            "Se debe dejar el diente destapado y abierto al medio bucal durante cinco días para que el paciente continúe succionando el pus con la comida.",
            "Nunca se debe dejar el diente abierto a la cavidad oral; se irriga profusamente, se seca el conducto, se coloca una mota de algodón estéril en la cámara y se sella herméticamente con material temporal.",
            "Se debe rellenar la cavidad cameral con cera de pegar caliente y enviar al paciente a su casa sin anestesia.",
            "Se debe obturar inmediatamente con perno de fibra de vidrio y composite definitivo mientras continúa saliendo pus por el conducto."
        ],
        correcta=1,
        distractores=[
            "Dejar el diente abierto permite que entren bacterias de la saliva y comida al conducto, empeorando gravemente la infección.",
            "",
            "La cera caliente no proporciona un sellado hermético bacteriano temporal y quema los tejidos camerales.",
            "Obturar con perno definitivo mientras existe exudado purulento activo atrapa la infección y genera una reagudización explosiva."
        ],
        explicacion="El profesor fue categórico al respecto en las líneas mil setecientos doce a mil ochocientos dieciocho: NUNCA, bajo ninguna circunstancia, se debe dejar un diente abierto a la cavidad bucal. Dejar el diente destapado con la idea errónea de «que siga drenando» permite la entrada masiva de flora microbiana mixta de la saliva, restos alimenticios y levaduras dentro del sistema de conductos, transformando una infección monomicrobiana controlable en una sobreinfección multirresistente mucho más grave y refractaria. El procedimiento correcto es: irrigar abundantemente con hipoclorito de sodio hasta que el exudado ceda, secar el exceso de líquido con conos de papel, colocar una torunda de algodón estéril en la cámara cameral para que actúe como colchón colector y sellar herméticamente la cavidad con un material de obturación provisional denso (como Cavit o ionómero de vidrio), citando al paciente a las cuarenta y ocho horas para continuar la desinfección.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Manejo de urgencia del absceso agudo: nunca dejar el diente abierto",
        que="Fundamentar la prohibición absoluta de dejar dientes abiertos y aplicar el protocolo de sellado con algodón estéril.",
        clave="Nunca se deja el diente abierto a la saliva; se irriga profusamente, se coloca algodón estéril y se sella con material temporal.",
        pistas=[
            "Recuerda la advertencia tajante del profesor en clase: jamás mandar al paciente con la muela abierta.",
            "Ten en cuenta cómo la saliva y la comida infectan el conducto si no se sella con algodón estéril y curación temporal."
        ],
        plan=[
            "Reconocer el grave error clínico de dejar conductos abiertos a la microflora salival.",
            "Comprender la sobreinfección bacteriana multirresistente inducida por la saliva.",
            "Aplicar el protocolo de irrigación, torunda de algodón estéril y sellado provisional denso."
        ],
        marcas_data=[
            ("¿Cuál es la advertencia enfática del profesor en clase (líneas mil setecientos doce a mil ochocientos dieciocho) sobre el sellado de la cavidad?", "clave", "Regla de sellado cameral", "Demanda formular la prohibición de dejar abierto y exigir algodón estéril con temporal")
        ],
        steps_ideas=[
            ("idea", "Prohibición de dejar abierto", "El profesor insistió: jamás se deja un diente destapado para que 'respire' o drene pus en la boca."),
            ("idea", "Contaminación salival", "Si se deja abierto, entran millones de bacterias de la comida y la saliva al interior del conducto."),
            ("idea", "Protocolo de sellado", "Se lava con hipoclorito, se seca, se pone una mota de algodón estéril adentro y se tapa bien."),
            ("check", "Comprobación clínica", "Confirmamos la regla de nunca dejar el diente abierto, sellando con algodón estéril y temporal.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta regla clínica de oro que el profesor repitió varias veces en la clase de patologías."),
            ("m:¿Cuál es la advertencia enfática del profesor en clase (líneas mil setecientos doce a mil ochocientos dieciocho) sobre el sellado de la cavidad?", "Observa qué se debe hacer al terminar de drenar un absceso agudo por el conducto."),
            ("leer", "Un error muy viejo era dejar el diente destapado con una mota para que siguiera botando pus."),
            ("leer", "El docente prohibió tajantemente esa práctica: la saliva entra y llena la raíz de bacterias multirresistentes."),
            ("leer", "La conducta correcta es lavar muy bien, secar, poner una torunda de algodón estéril y sellar con cemento temporal.")
        ]
    ))

    # 55 (Key C = 2) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-055", nivel=2,
        enunciado="Al abordar el tratamiento del Absceso Apical Crónico con fístula en la Clase 2 (líneas mil ochocientos veinte a mil novecientos uno), el docente detalla la técnica de instrumentación química con hidróxido de calcio y el uso del léntulo. ¿Cuál es la técnica correcta enseñada por el profesor para empacar la medicación intraconducto y cuál es el tiempo esperado de cierre de la fístula?",
        opciones=[
            "Se debe girar el léntulo en sentido horario a máxima velocidad para forzar a que la pasta salga masivamente al periápice.",
            "Se prescriben tres tipos distintos de antibióticos sistémicos y se espera seis meses sin tocar el diente en absoluto.",
            "Se mezcla el hidróxido de calcio puro con vehículo acuoso y se lleva al conducto con léntulo girando en sentido antihorario o con limas y conos de papel; no requiere antibióticos y la fístula cierra en unos ocho días.",
            "Se cauteriza la fístula en la encía con bisturí eléctrico sin limpiar el interior de las raíces dentales."
        ],
        correcta=2,
        distractores=[
            "Girar el léntulo en sentido horario empuja violentamente el material fuera del foramen apical pudiendo irritar el periápice.",
            "El absceso crónico con fístula no requiere antibioticoterapia sistémica y dejarlo seis meses sin limpiar agrava la lesión ósea.",
            "",
            "Quemar la fístula externamente con electrobisturí no elimina las bacterias dentro del conducto radicular que la originan."
        ],
        explicacion="En las líneas mil ochocientos veinte a mil novecientos uno, el profesor describió con detalle clínico el manejo del absceso apical crónico: 1) No requiere antibioticoterapia sistémica porque el proceso está drenando continuamente a través del estoma; 2) Se realiza la preparación biomecánica completa y se coloca hidróxido de calcio químicamente puro mezclado con anestésico, suero fisiológico o agua destilada; 3) Para llevar la pasta al conducto sin impulsarla violentamente más allá del foramen apical, se utiliza el léntulo montado en micromotor en rotación inversa (sentido antihorario) o se empaca manualmente con una lima o con una punta de papel invertida; 4) Al sellar el conducto con hidróxido de calcio, la fuente bacteriana se neutraliza y el trayecto fistuloso cicatriza por segunda intención cerrándose por completo en aproximadamente ocho a diez días.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Manejo del absceso crónico: técnica del léntulo antihorario e hidróxido de calcio",
        que="Describir la técnica de medicación intraconducto con léntulo antihorario y el tiempo de cierre de la fístula en ocho días.",
        clave="El hidróxido de calcio se empaca con léntulo en sentido antihorario o puntas de papel; no requiere antibióticos y la fístula cierra en ocho días.",
        pistas=[
            "Recuerda la técnica del léntulo invertido para que la pasta entre al conducto sin dispararse afuera.",
            "Ten en cuenta el tiempo de cicatrización del estoma fistuloso tras colocar la medicación: aproximadamente ocho días."
        ],
        plan=[
            "Comprender la innecesariedad de antibióticos sistémicos en presencia de fístula activa.",
            "Aplicar la técnica de empaquetamiento del hidróxido de calcio con léntulo antihorario o conos.",
            "Monitorear la remisión y cicatrización completa de la fístula en un plazo de ocho a diez días."
        ],
        marcas_data=[
            ("técnica de instrumentación química con hidróxido de calcio y el uso del léntulo", "clave", "Técnica de colocación de medicación", "Demanda rotación antihoraria del léntulo o uso de puntas de papel"),
            ("¿Cuál es la técnica correcta enseñada por el profesor para empacar la medicación intraconducto y cuál es el tiempo esperado de cierre de la fístula?", "pide", "Técnica y tiempo de cicatrización", "Demanda especificar léntulo antihorario y cierre en ocho días")
        ],
        steps_ideas=[
            ("idea", "Sin antibióticos", "El docente enseñó que el absceso crónico con fístula no se medica con antibióticos."),
            ("idea", "Léntulo antihorario", "Para llevar el hidróxido de calcio al fondo sin extruirlo, se gira el léntulo al revés (sentido antihorario)."),
            ("idea", "Cierre en ocho días", "Al neutralizar los microbios con el hidróxido de calcio, la fístula se seca y cierra sola en unos ocho días."),
            ("check", "Comprobación técnica", "Confirmamos colocación con léntulo antihorario o conos y cierre de fístula en ocho días sin antibióticos.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos este procedimiento práctico de colocación de hidróxido de calcio explicado por el docente."),
            ("m:técnica de instrumentación química con hidróxido de calcio y el uso del léntulo", "Observa cómo enseñó el docente a llevar la pasta de hidróxido de calcio al interior del conducto."),
            ("leer", "El docente explicó que no se dan antibióticos porque el grano ya está drenando."),
            ("leer", "Para empacar la pasta, se hace girar el léntulo en sentido antihorario o se empuja con una punta de papel invertida."),
            ("leer", "Al quedar bien colocado, a los ocho días el paciente ya no tiene fístula y el tejido ha cicatrizado.")
        ]
    ))

    # 56 (Key D = 3) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-056", nivel=2,
        enunciado="Durante el debate sobre la terminología de las lesiones periapicales radiolúcidas (líneas mil novecientos tres a mil novecientos dieciocho), un estudiante afirma que en la radiografía periapical se observa con claridad un «quiste radicular» y no un «granuloma periapical». ¿Cuál es la corrección tajante que realiza el docente ante esta afirmación?",
        opciones=[
            "Que los quistes siempre tienen forma triangular y los granulomas son perfectamente pentagonales en la radiografía periapical.",
            "Que los granulomas se tratan con antibióticos sistémicos y los quistes con enjuagues de bicarbonato sódico.",
            "Que la presencia de dolor pulsátil confirma que se trata de un quiste y la ausencia de dolor que es un granuloma.",
            "Que no es posible diferenciar radiográficamente un granuloma de un quiste; ambos se ven como radiolucideces periapicales y solo el estudio histopatológico al microscopio permite distinguirlos, por lo que no es una clasificación clínica."
        ],
        correcta=3,
        distractores=[
            "Las lesiones periapicales inflamatorias no adoptan geometrías triangulares ni pentagonales fijas en hueso.",
            "Ni los granulomas se resuelven con antibióticos ni los quistes radiculares epiteliales con enjuagues de bicarbonato.",
            "Tanto el granuloma como el quiste son lesiones periapicales crónicas habitualmente asintomáticas sin dolor pulsátil.",
            ""
        ],
        explicacion="En las líneas mil novecientos tres a mil novecientos dieciocho del texto fuente, el profesor corrigió rotundamente esta confusión conceptual muy arraigada: clínicamente y radiográficamente es imposible discernir si una radiolucidez periapical corresponde a un granuloma (tejido de granulación inflamatorio crónico) o a un quiste radicular (cavidad patológica revestida por epitelio). Ambas entidades se manifiestan como una imagen radiolúcida periapical redondeada u oval con reabsorción ósea. La única forma científica de distinguirlos es mediante la biopsia y el examen histopatológico bajo el microscopio; por consiguiente, la clasificación clínica estandarizada de la AAE utiliza el término unificado de «Periodontitis apical asintomática», y la conducta clínica inicial no varía, consistiendo en la preparación biomecánica y medicación intraconducto para promover la cicatrización ósea.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Diagnóstico diferencial histopatológico: granuloma vs quiste radicular",
        que="Comprender la imposibilidad de diferenciar radiográficamente un granuloma de un quiste sin estudio histopatológico.",
        clave="Granuloma y quiste no son diagnósticos radiográficos clínicos; solo la biopsia histológica los distingue, clasificándose clínicamente como periodontitis apical asintomática.",
        pistas=[
            "Recuerda la corrección enérgica del profesor cuando un estudiante intentó diagnosticar un quiste solo con la radiografía.",
            "Ten en cuenta que para ver el epitelio de un quiste se necesita obligatoriamente un microscopio y una biopsia."
        ],
        plan=[
            "Reconocer la apariencia radiográfica idéntica de granulomas y quistes como imágenes radiolúcidas periapicales.",
            "Comprender la limitación diagnóstica que exige confirmación histológica mediante biopsia.",
            "Aplicar la terminología clínica unificada de periodontitis apical asintomática de la AAE."
        ],
        marcas_data=[
            ("estudiante afirma que en la radiografía periapical se observa con claridad un «quiste radicular» y no un «granuloma periapical»", "clave", "Error conceptual del estudiante", "Apunta a pretensión de diagnosticar histología en radiografía"),
            ("¿Cuál es la corrección tajante que realiza el docente ante esta afirmación?", "pide", "Corrección del profesor", "Demanda afirmar que solo la histología los distingue y no es clasificación clínica")
        ],
        steps_ideas=[
            ("idea", "Limitación radiográfica", "En la radiografía ambos se ven iguales: una mancha negra radiolúcida en la punta de la raíz."),
            ("idea", "Examen histopatológico", "El docente enseñó: solo con biopsia al microscopio se puede saber si tiene epitelio de quiste o tejido de granuloma."),
            ("idea", "Clasificación clínica", "Por eso la clasificación clínica no usa quiste ni granuloma, sino periodontitis apical asintomática."),
            ("check", "Comprobación conceptual", "Confirmamos que solo el examen histopatológico distingue el granuloma del quiste.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta corrección conceptual clave que el profesor hizo a un expositor en la Clase dos."),
            ("m:estudiante afirma que en la radiografía periapical se observa con claridad un «quiste radicular» y no un «granuloma periapical»", "Observa que el alumno intentó decir que en la radiografía se veía claramente un quiste."),
            ("leer", "El docente lo interrumpió de inmediato: radiográficamente es imposible saber si es quiste o granuloma."),
            ("leer", "Ambos se ven exactamente igual como una mancha radiolúcida, y la única forma de saberlo es mandar la muestra a patología."),
            ("leer", "Por lo tanto, la opción que aclara que solo la histología al microscopio los distingue es la respuesta correcta.")
        ]
    ))

    # 57 (Key A = 0) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-057", nivel=3,
        enunciado="En la sección de diagnóstico diferencial de lesiones radiopacas periapicales (líneas mil novecientos veinte a dos mil cuarenta), el profesor contrasta la osteítis condensante con la displasia cementaria periapical (cementoma en estadios osteolítico, mixto y radiopaco). ¿Cuál es la prueba semiológica determinante que evita realizar una endodoncia innecesaria en una displasia cementaria periapical?",
        opciones=[
            "La prueba de sensibilidad pulpar con frío: en la displasia cementaria periapical la pulpa está vital y sana (frío positivo normal) por lo que no se realiza endodoncia; en la osteítis condensante la pulpa está inflamada o necrótica.",
            "La prueba de movilidad con pinza algodonera, ya que los cementomas presentan movilidad grado tres espontánea en todos los casos.",
            "La prueba de masticación con cera blanda, que produce dolor insoportable en todos los cementomas en fase osteolítica.",
            "El examen de los ganglios linfáticos axilares mediante ecografía de alta resolución sin tocar la cavidad bucal."
        ],
        correcta=0,
        distractores=[
            "",
            "La displasia cementaria está integrada al hueso y los dientes conservan soporte periodontal normal sin movilidad patológica grado tres.",
            "La displasia cementaria periapical es totalmente asintomática y no genera dolor ante la masticación funcional de cera.",
            "Los ganglios axilares no drenan la región dentaria mandibular ni tienen ninguna utilidad en el diagnóstico pulpar."
        ],
        explicacion="En las líneas mil novecientos veinte a dos mil cuarenta, el profesor hizo una advertencia clínica crucial para no cometer iatrogenias: la displasia cementaria periapical (antiguamente llamada cementoma) es una alteración fibro-ósea benigna que ocurre con frecuencia en incisivos inferiores de mujeres de mediana edad. En su estadio radiopaco final, se observa una masa radiopaca densa alrededor de los ápices que puede confundirse con osteítis condensante. La prueba semiológica determinante es la prueba de sensibilidad pulpar térmica con frío: en la displasia cementaria la pulpa dental está completamente SANA y VITAL (responde al frío en uno a dos segundos y cesa de inmediato); el profesor recalcó enfáticamente que si la prueba térmica es positiva normal, está TOTALMENTE CONTRAINDICADO realizar endodoncia o perforar el diente, ya que es un proceso periapical no infeccioso que solo requiere observación periódica.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Diagnóstico diferencial: osteítis condensante vs displasia cementaria",
        que="Utilizar la prueba de frío para diferenciar la displasia cementaria (pulpa vital) de la osteítis condensante y evitar endodoncias.",
        clave="En la displasia cementaria la pulpa está vital (frío positivo normal) y no se hace endodoncia; en la osteítis condensante hay inflamación o necrosis.",
        pistas=[
            "Recuerda la regla de oro del profesor: si la prueba de frío da positiva normal, NO se toca el diente con endodoncia.",
            "Ten en cuenta que la displasia cementaria es una alteración fibro-ósea asintomática con dientes completamente vivos."
        ],
        plan=[
            "Diferenciar radiográficamente las radiopacidades periapicales inflamatorias frente a las fibro-óseas.",
            "Aplicar la prueba térmica de frío como discriminador biológico de vitalidad pulpar.",
            "Contraindicar el tratamiento de conductos en dientes con pulpa vital y displasia cementaria periapical."
        ],
        marcas_data=[
            ("contrasta la osteítis condensante con la displasia cementaria periapical (cementoma", "clave", "Dilema de radiopacidades periapicales", "Apunta a diferenciar osteoesclerosis reactiva de displasia ósea"),
            ("¿Cuál es la prueba semiológica determinante que evita realizar una endodoncia innecesaria en una displasia cementaria periapical?", "pide", "Prueba semiológica determinante", "Demanda identificar prueba de frío positiva que contraindica endodoncia")
        ],
        steps_ideas=[
            ("idea", "Confusión radiográfica", "Ambas se ven como masas radiopacas densas cerca del ápice en molares o incisivos inferiores."),
            ("idea", "Prueba de frío determinante", "El docente enseñó: si haces prueba de frío y el diente responde normal, es un cementoma y la pulpa está sana."),
            ("idea", "No tocar el diente", "Si la prueba térmica es positiva normal, está totalmente prohibido hacer endodoncia: solo se controla."),
            ("check", "Comprobación semiológica", "Confirmamos que la prueba de frío positiva normal en displasia cementaria evita endodoncias innecesarias.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta advertencia del profesor para no cometer una iatrogenia en dientes anteriores."),
            ("m:contrasta la osteítis condensante con la displasia cementaria periapical (cementoma", "Observa que una displasia cementaria se ve muy parecida a una osteítis condensante blanca en la radiografía."),
            ("leer", "El docente explicó que muchos dentistas ven la mancha blanca y abren el diente pensando que es infección."),
            ("leer", "La prueba que te salva es el frío: en la displasia cementaria la pulpa está completamente viva y responde perfecto."),
            ("leer", "Por lo tanto, si la prueba de frío da positiva normal, se comprueba que el diente está sano y no se hace endodoncia.")
        ]
    ))

    # 58 (Key B = 1) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-058", nivel=3,
        enunciado="Al evaluar la radiografía periapical de un molar con tratamiento de conductos previo que presenta dolor moderado a la masticación y una bolsa periodontal estrecha aislada de ocho milímetros en la raíz mesial, el docente señala una imagen radiolúcida característica que rodea lateralmente la superficie radicular en forma de «J invertida» o halo peri-radicular (líneas mil seiscientos veintitrés a mil seiscientos setenta y cinco). ¿Qué sospecha diagnóstica grave indica este hallazgo y qué examen tridimensional se debe solicitar?",
        opciones=[
            "Sospecha de sobreobturación de gutapercha benigna; se debe prescribir analgésicos narcóticos durante dos años sin tomar más imágenes.",
            "Sospecha de fractura radicular vertical incompleta o completa; se debe solicitar una tomografía computarizada de haz cónico (CBCT) para confirmar la línea de fractura.",
            "Sospecha de fluorosis dental radicular benigna; se indica blanqueamiento dental interno con peróxido de carbamida.",
            "Sospecha de amelogénesis imperfecta radicular; se debe realizar desgaste oclusal generalizado en toda la boca."
        ],
        correcta=1,
        distractores=[
            "Una sobreobturación muestra gutapercha extruida en el ápice, no un halo radiolúcido en forma de J invertida a lo largo de la raíz lateral.",
            "",
            "La fluorosis es una hipomineralización del esmalte coronal, no produce lesiones radiolúcidas óseas en forma de J en la raíz.",
            "La amelogénesis afecta exclusivamente al esmalte dental en coronas, no origina bolsas periodontales estrechas con halos perirradiculares."
        ],
        explicacion="En las líneas mil seiscientos veintitrés a mil seiscientos setenta y cinco del texto fuente, el profesor enseñó a identificar los signos radiográficos de la fractura radicular vertical: la imagen en «J invertida» (o imagen en halo que bordea la raíz lateralmente desde el tercio medio hasta el ápice) es patognomónica de una fractura radicular vertical longitudinal. Las bacterias proliferan a lo largo de la línea de fisura ósea destruyendo la inserción del ligamento periodontal. Como la radiografía periapical bidimensional solo muestra la fractura si el rayo incide exactamente en el mismo plano de la línea de ruptura, la conducta diagnóstica de elección consiste en solicitar una Tomografía Computarizada de Haz Cónico (CBCT de alta resolución), la cual permite visualizar tridimensionalmente el trazo de fractura y confirmar el pronóstico para evitar retratamientos inviables.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Diagnóstico de fracturas: imagen en J invertida y tomografía CBCT",
        que="Reconocer la imagen en J invertida como signo patognomónico de fractura radicular vertical y solicitar tomografía CBCT.",
        clave="La imagen en J invertida con bolsa estrecha es patognomónica de fractura radicular vertical y se confirma con tomografía CBCT.",
        pistas=[
            "Observa la forma de letra J invertida que contornea lateralmente la raíz del diente con endodoncia previa.",
            "Recuerda el examen radiográfico avanzado en tres dimensiones que el docente recomendó cuando se sospecha fractura de raíz."
        ],
        plan=[
            "Identificar el patrón radiográfico característico en J invertida o halo peri-radicular.",
            "Correlacionar la radiolucidez lateral con la presencia de bolsa periodontal estrecha.",
            "Solicitar tomografía computarizada de haz cónico (CBCT) para confirmar la fractura vertical."
        ],
        marcas_data=[
            ("imagen radiolúcida característica que rodea lateralmente la superficie radicular en forma de «J invertida»", "clave", "Signo radiográfico en J invertida", "Apunta a fractura radicular vertical longitudinal"),
            ("¿Qué sospecha diagnóstica grave indica este hallazgo y qué examen tridimensional se debe solicitar?", "pide", "Sospecha y examen tridimensional", "Demanda formular fractura radicular vertical y tomografía CBCT")
        ],
        steps_ideas=[
            ("idea", "Halo en J invertida", "La imagen en J invertida dibuja la línea donde la raíz se partió y el hueso se desprendió."),
            ("idea", "Fractura radicular vertical", "Es una de las complicaciones más frustrantes en dientes previamente tratados con pernos."),
            ("idea", "Tomografía CBCT", "El docente enseñó que la radiografía simple puede no mostrar el trazo; se pide una tomografía CBCT tridimensional."),
            ("check", "Comprobación diagnóstica", "Confirmamos sospecha de fractura radicular vertical y solicitud de tomografía de haz cónico.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este signo radiográfico clásico explicado por el profesor en la Clase dos."),
            ("m:imagen radiolúcida característica que rodea lateralmente la superficie radicular en forma de «J invertida»", "Observa esa sombra oscura que rodea la raíz como una letra J al revés."),
            ("leer", "El docente enseñó que la imagen en J invertida acompañada de una bolsa profunda en un punto es típica de fractura de raíz."),
            ("leer", "Como la radiografía común solo tiene dos dimensiones, muchas veces la raya de la fractura queda escondida."),
            ("leer", "Por lo tanto, la conducta diagnóstica indicada por el profesor es pedir una tomografía computarizada CBCT para confirmarla.")
        ]
    ))

    # 59 (Key C = 2) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-059", nivel=2,
        enunciado="En la patología de reabsorción dental en la Clase 2 (líneas dos mil doscientos diecinueve a dos mil trescientos treinta y seis), el profesor diferencia la reabsorción radicular interna de la reabsorción externa. ¿Cuáles son las características radiográficas y clínicas cardinales de una reabsorción radicular interna no perforante de origen pulpar y cuál es su tratamiento?",
        opciones=[
            "Se observa una lesión radiopaca difusa en la corona y se trata exclusivamente con enjuagues de bicarbonato sódico.",
            "Se presenta como un defecto óseo en el cuello del diente con encía hiperplásica y se cura espontáneamente sin tocar la pulpa.",
            "Se observa un ensanchamiento radiolúcido simétrico y redondeado en forma de balón o ampolla dentro de los límites del conducto pulpar; el tratamiento es la endodoncia completa con hidróxido de calcio para detener el avance de las células clásticas.",
            "Ocurre exclusivamente en dientes con endodoncias terminadas hace veinte años y exige la amputación quirúrgica de la raíz."
        ],
        correcta=2,
        distractores=[
            "La reabsorción interna es un defecto lítico radiolúcido (destructivo) y no una radiopacidad que se cure con enjuagues.",
            "El defecto óseo en cuello con tejido invasivo corresponde a la reabsorción cervical externa invasiva, no a la interna.",
            "",
            "La reabsorción interna requiere pulpa vital vascularizada con células clásticas activas; no se origina en dientes con conductos ya obturados."
        ],
        explicacion="En las líneas dos mil doscientos diecinueve a dos mil trescientos treinta y seis, el profesor expuso la reabsorción radicular interna: es un proceso patológico de origen pulpar en el cual las células mesenquimales de una pulpa crónicamente inflamada se transforman en odontoclastos que fagocitan la dentina desde el interior de la cavidad pulpar hacia la periferia. Radiográficamente se aprecia un ensanchamiento ovalado, uniforme y simétrico del conducto radicular que recuerda la silueta de un balón o ampolla («ensanchamiento en ampolla»), donde las paredes del conducto se expanden hacia afuera conservando sus contornos continuos. El tratamiento de elección consiste en realizar la biopulpectomía completa de inmediato para eliminar el tejido pulpar vital vascularizado que alimenta a los clastos; se empaca hidróxido de calcio intraconducto para disolver restos tisulares necróticos y se obtura con gutapercha termoplastificada.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Patología pulpar: reabsorción radicular interna",
        que="Reconocer la reabsorción radicular interna en balón y formular su tratamiento endodóntico con hidróxido de calcio.",
        clave="La reabsorción interna ensancha el conducto en forma de balón o ampolla y se detiene mediante endodoncia con hidróxido de calcio.",
        pistas=[
            "Recuerda la imagen que el docente describió como un balón o ampolla ensanchando el conducto desde adentro.",
            "Ten en cuenta que para detener la reabsorción interna se debe extirpar la pulpa que nutre a las células clásticas."
        ],
        plan=[
            "Identificar el ensanchamiento radiolúcido uniforme en balón dentro del espacio pulpar.",
            "Diferenciar el origen pulpar de la reabsorción interna frente a las agresiones periodontales externas.",
            "Indicar la biopulpectomía completa con hidróxido de calcio para eliminar la actividad osteoclástica."
        ],
        marcas_data=[
            ("reabsorción radicular interna no perforante de origen pulpar", "clave", "Entidad patológica pulpar", "Apunta a acción odontoclástica desde adentro del conducto"),
            ("cuál es su tratamiento?", "pide", "Signos radiográficos y tratamiento", "Demanda identificar ensanchamiento en balón y endodoncia con hidróxido de calcio")
        ],
        steps_ideas=[
            ("idea", "Imagen en balón", "El conducto se ensancha como una ampolla redonda u ovalada con bordes lisos continuos."),
            ("idea", "Origen pulpar", "Las células de la pulpa inflamada se volvieron clásticas y se están comiendo la dentina por dentro."),
            ("idea", "Tratamiento endodóntico", "Al hacer la endodoncia y quitar la pulpa con hidróxido de calcio, los clastos se mueren y la reabsorción se frena."),
            ("check", "Comprobación clínica", "Confirmamos ensanchamiento en balón dentro del conducto tratado con biopulpectomía e hidróxido de calcio.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta patología pulpar destructiva explicada por el profesor en la Clase dos."),
            ("m:reabsorción radicular interna no perforante de origen pulpar", "Observa que se trata de una reabsorción que viene desde adentro del conducto."),
            ("leer", "El docente explicó que en la radiografía el conducto se ve ensanchado de forma simétrica como un balón o una ampolla."),
            ("leer", "Son células de la propia pulpa inflamada que se pusieron a destruir la dentina por dentro."),
            ("leer", "El tratamiento consiste en hacer la endodoncia completa y medicar con hidróxido de calcio para matar los clastos y frenar la lesión.")
        ]
    ))

    # 60 (Key D = 3) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-060", nivel=3,
        enunciado="Respecto a las reabsorciones radiculares externas (líneas dos mil doscientos diecinueve a dos mil trescientos treinta y seis), el profesor clasifica sus tres variedades principales: superficial, inflamatoria y por reemplazo (anquilosis). ¿Cuál es la causa típica de la reabsorción externa por reemplazo y qué hallazgo clínico la distingue?",
        opciones=[
            "Es causada por masticar hielo y se distingue porque el diente se mueve como un péndulo con sangrado constante en encía libre.",
            "Es originada por fluorosis dental y se distingue porque el esmalte se torna transparente en las cúspides de premolares.",
            "Es producida por la ingesta de cítricos y se caracteriza por la pérdida del borde incisal con dolor leve al dulce.",
            "Ocurre típicamente tras un traumatismo severo con avulsión y desecación del ligamento periodontal; las células osteogénicas sustituyen la raíz por hueso alveolar, provocando anquilosis con sonido metálico seco a la percusión y pérdida de movilidad fisiológica."
        ],
        correcta=3,
        distractores=[
            "Masticar hielo puede causar fracturas de esmalte, pero no la anquilosis por reemplazo de la raíz en el alvéolo.",
            "La fluorosis es una anomalía de desarrollo del esmalte durante la amelogénesis, no una reabsorción ósea radicular por trauma.",
            "La ingesta de cítricos produce erosión química ácida extrínseca de coronas, no reabsorciones óseas radiculares.",
            ""
        ],
        explicacion="En las líneas dos mil doscientos diecinueve a dos mil trescientos treinta y seis del texto fuente, el profesor detalló la reabsorción radicular externa por reemplazo (también llamada anquilosis dentoalveolar): ocurre clásicamente tras una avulsión dental donde el diente permaneció fuera del alvéolo en seco durante un tiempo prolongado, muriendo las células del ligamento periodontal. Durante la cicatrización, el organismo reacciona reconociendo la raíz desvitalizada como hueso propio: los osteoclastos y osteoblastos reabsorben progresivamente la dentina y la sustituyen directamente por trabéculas de hueso alveolar sin que exista espacio de ligamento periodontal. Clínicamente, el diente anquilosado pierde por completo su movilidad fisiológica elástica y al ser percutido emite un sonido sordo, agudo y metálico característico («sonido de campana o de porcelana»).",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Patología periapical: reabsorción externa por reemplazo (anquilosis)",
        que="Reconocer la reabsorción por reemplazo post-avulsión como anquilosis ósea con sonido metálico y pérdida de movilidad.",
        clave="La reabsorción por reemplazo ocurre tras avulsión y muerte del ligamento; el hueso sustituye la raíz provocando anquilosis con sonido metálico.",
        pistas=[
            "Recuerda qué pasa cuando un diente se cae al piso (avulsión) y se seca antes de reimplantarlo.",
            "Ten en cuenta los dos signos clínicos cardinales: pérdida total de movilidad y sonido metálico seco como campana al percutir."
        ],
        plan=[
            "Asociar el tiempo extraalveolar prolongado en seco con la necrosis del ligamento periodontal.",
            "Comprender el mecanismo de sustitución progresiva de dentina por tejido óseo trabecular.",
            "Identificar el sonido metálico patognomónico a la percusión y la ausencia de movilidad fisiológica."
        ],
        marcas_data=[
            ("por reemplazo (anquilosis)", "clave", "Entidad patológica periodontal/radicular", "Apunta a unión directa entre dentina y hueso alveolar"),
            ("¿Cuál es la causa típica de la reabsorción externa por reemplazo y qué hallazgo clínico la distingue?", "pide", "Causa y signos clínicos", "Demanda identificar avulsión previa, sonido metálico y falta de movilidad")
        ],
        steps_ideas=[
            ("idea", "Muerte del ligamento", "Si el diente avulsionado se seca afuera de la boca, las células del ligamento mueren."),
            ("idea", "Sustitución por hueso", "Al reimplantarlo, el cuerpo confunde la raíz con hueso y la reemplaza por hueso trabecular."),
            ("idea", "Sonido metálico", "El diente queda soldado al hueso (anquilosado); al percutirlo suena seco y metálico como una porcelana."),
            ("check", "Comprobación clínica", "Confirmamos reabsorción por reemplazo post-avulsión con anquilosis y sonido metálico a la percusión.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos este cuadro clínico traumático explicado por el profesor en la sección de reabsorciones externas."),
            ("m:por reemplazo (anquilosis)", "Observa que se habla de la reabsorción por reemplazo, también llamada anquilosis."),
            ("leer", "El docente explicó que ocurre típicamente cuando un diente se sale de la boca por un golpe y pasa mucho tiempo seco."),
            ("leer", "Al reimplantarlo sin ligamento vivo, el hueso se pega directo a la raíz y se va comiendo la dentina para poner hueso."),
            ("leer", "El diente queda soldado: pierde toda su movilidad elástica y al golpearlo con el espejo suena metálico como una campana.")
        ]
    ))

    # 61 (Key A = 0) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-061", nivel=3,
        enunciado="En el cierre de la Clase 2 sobre consideraciones médicas sistémicas y profilaxis antibiótica (líneas dos mil cuatrocientos cuarenta y tres a dos mil cuatrocientos sesenta), el profesor explica el protocolo farmacológico de prevención de la endocarditis infecciosa en pacientes de alto riesgo cardiovascular antes de procedimientos endodónticos que involucren manipulación periapical o sangrado. ¿Cuál es el régimen antibiótico profiláctico estándar según las guías clínicas y la clase?",
        opciones=[
            "Amoxicilina dos gramos vía oral administrados en una dosis única una hora antes del procedimiento; en pacientes alérgicos a penicilinas, clindamicina seiscientos miligramos (o azitromicina quinientos miligramos) vía oral una hora antes.",
            "Prescribir penicilina benzatínica intramuscular cada doce horas durante quince días consecutivos tras la cita odontológica en el consultorio.",
            "Tomar una tableta de ampicilina de quinientos miligramos al día siguiente de la cita dental si el paciente presenta fiebre o dolor.",
            "Indicar colutorios de clorhexidina al cero punto doce por ciento sin administrar ningún tipo de antibiótico sistémico previo en el paciente."
        ],
        correcta=0,
        distractores=[
            "",
            "La profilaxis antibiótica exige altas dosis orales inmediatas antes del acto quirúrgico, no tratamientos intramusculares prolongados de semanas.",
            "Tomar antibiótico al día siguiente no previene la bacteriemia transitoria que ocurre durante la instrumentación radicular inicial.",
            "Los colutorios de clorhexidina reducen la carga bacteriana salival superficial pero no evitan la bacteriemia intravascular profunda hacia el corazón."
        ],
        explicacion="En las líneas dos mil cuatrocientos cuarenta y tres a dos mil cuatrocientos sesenta del texto, el profesor expuso las normas de profilaxis antibiótica en odontología de acuerdo con la Asociación Americana del Corazón (AHA): está indicada en pacientes con condiciones cardíacas de alto riesgo (prótesis valvulares cardíacas, antecedentes de endocarditis bacteriana infecciosa previa, cardiopatías congénitas cianóticas no reparadas) que van a ser sometidos a procedimientos endodónticos donde se manipulan tejidos periapicales infectados o hay perforación de la mucosa. El régimen farmacológico estándar de elección es: Amoxicilina dos gramos (cuatro cápsulas de quinientos miligramos) por vía oral en dosis única administrada una hora antes del inicio del procedimiento en el consultorio. En pacientes con alergia confirmada a las penicilinas o betalactámicos, la alternativa profiláctica es Clindamicina seiscientos miligramos (o Azitromicina quinientos miligramos) por vía oral en dosis única una hora antes de la cita.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Consideraciones médicas: profilaxis antibiótica de endocarditis",
        que="Formular el protocolo de profilaxis antibiótica estándar para endocarditis con amoxicilina o clindamicina una hora antes.",
        clave="La profilaxis de endocarditis exige amoxicilina dos gramos vía oral una hora antes (o clindamicina seiscientos miligramos en alérgicos).",
        pistas=[
            "Recuerda la dosis alta en gramos administrada una hora antes de sentar al paciente en el sillón dental.",
            "Ten en cuenta las dos opciones: dos gramos de amoxicilina para pacientes comunes, o seiscientos miligramos de clindamicina si es alérgico."
        ],
        plan=[
            "Identificar las condiciones cardiovasculares de alto riesgo que demandan profilaxis antibiótica.",
            "Establecer el momento farmacocinético óptimo de administración una hora previa a la bacteriemia.",
            "Dosificar amoxicilina dos gramos vía oral o clindamicina seiscientos miligramos en alérgicos."
        ],
        marcas_data=[
            ("prevención de la endocarditis infecciosa en pacientes de alto riesgo cardiovascular antes de procedimientos endodónticos", "clave", "Indicación de profilaxis antibiótica", "Apunta a protección de válvulas cardíacas ante bacteriemia transitoria"),
            ("¿Cuál es el régimen antibiótico profiláctico estándar según las guías clínicas y la clase?", "pide", "Régimen profiláctico exacto", "Demanda amoxicilina dos gramos o clindamicina seiscientos miligramos una hora antes")
        ],
        steps_ideas=[
            ("idea", "Prevención de endocarditis", "Manipular conductos con bacterias puede mandar microbios al corazón si el paciente tiene válvulas artificiales."),
            ("idea", "Dosis de amoxicilina", "Se administran dos gramos de amoxicilina por vía oral exactamente una hora antes de empezar el procedimiento."),
            ("idea", "Alternativa en alérgicos", "Si el paciente es alérgico a la penicilina, se mandan seiscientos miligramos de clindamicina una hora antes."),
            ("check", "Comprobación farmacológica", "Confirmamos amoxicilina dos gramos (o clindamicina seiscientos miligramos) una hora antes del tratamiento.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos este protocolo médico fundamental enseñado por el profesor al final de la Clase dos."),
            ("m:prevención de la endocarditis infecciosa en pacientes de alto riesgo cardiovascular antes de procedimientos endodónticos", "Observa que si el paciente tiene una válvula artificial en el corazón, las bacterias de la boca pueden infectarla."),
            ("leer", "El docente enseñó la pauta estandarizada internacional de profilaxis antibiótica."),
            ("leer", "Se formula amoxicilina dos gramos por vía oral una hora antes de tocar el diente."),
            ("leer", "Y si el paciente tiene alergia confirmada a la penicilina, se toman seiscientos miligramos de clindamicina una hora antes.")
        ]
    ))

    # 62 (Key B = 1) - NUEVA CLASE 2
    qs.append(make_q(
        qid="odo-062", nivel=3,
        enunciado="Al discutir el pronóstico a largo plazo entre salvar un diente natural mediante endodoncia y rehabilitación frente a la exodoncia con implante dental (líneas dos mil sesenta y ocho a dos mil ochenta y ocho), el docente analiza el concepto biomecánico del «efecto férula» (ferrule effect). ¿Qué es el efecto férula y cuál es el requisito anatómico indispensable para garantizar el éxito restaurador y evitar la fractura radicular?",
        opciones=[
            "Es la colocación de un alambre de acero trenzado alrededor de los caninos para inmovilizar los premolares antes de la endodoncia.",
            "Es la presencia de al menos dos milímetros de altura de dentina coronal sana por encima del margen gingival en los trescientos sesenta grados del muñón, lo cual disipa las fuerzas de palanca y evita la fractura de la raíz.",
            "Es el uso de coronas provisionales de acrílico durante tres años continuos antes de tomar la impresión definitiva con silicona pesada.",
            "Es la remoción completa de todo el esmalte interproximal para que la grapa de aislamiento descanse directamente sobre la encía libre."
        ],
        correcta=1,
        distractores=[
            "La ferulización con alambre ortodóntico es para dientes luxados o con trauma periodontal, no el concepto protésico del efecto férula.",
            "",
            "Usar coronas temporales por tres años fatiga el cemento provisional y permite filtraciones marginales bacterianas destructivas.",
            "Desgastar esmalte para apoyar grapas en encía lacera los tejidos periodontales y no guarda relación con el efecto férula."
        ],
        explicacion="En las líneas dos mil sesenta y ocho a dos mil ochenta y ocho del texto fuente, el profesor analizó la toma de decisiones clínicas entre conservar el diente natural o realizar la extracción para un implante. El factor biomecánico determinante para la supervivencia del diente endodonciado rehabilitado con perno y corona es el EFECTO FÉRULA (ferrule effect): consiste en una banda circunferencial de dentina sana de al menos dos milímetros de altura coronal por encima del margen gingival y con un espesor mínimo de un milímetro en los trescientos sesenta grados del remanente. Esta abrazadera de dentina natural es abrazada por la corona protésica definitiva, disipando las fuerzas de torsión y palanca transmitidas por el poste hacia el hueso alveolar; si no existe este remanente de dos milímetros (lo que puede requerir alargamiento coronal quirúrgico previo), la raíz se fractura verticalmente bajo la carga masticatoria.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Pronóstico y rehabilitación: efecto férula vs implante dental",
        que="Definir el efecto férula (dos milímetros de dentina sana circunferencial) como factor determinante para evitar fracturas radiculares.",
        clave="El efecto férula exige al menos dos milímetros de dentina sana supragingival en trescientos sesenta grados para abrazar la corona y evitar fracturas.",
        pistas=[
            "Recuerda la altura mínima en milímetros de dentina sana que el profesor exigió por encima de la encía para poner una corona.",
            "Ten en cuenta que esta abrazadera circunferencial de trescientos sesenta grados disipa la fuerza de palanca del perno."
        ],
        plan=[
            "Comprender la biomecánica de distribución de cargas oclusales en dientes tratados endodónticamente.",
            "Definir los requisitos dimensionales del efecto férula: dos milímetros de altura coronal en trescientos sesenta grados.",
            "Valorar la necesidad de alargamiento coronal quirúrgico para lograr férula antes de optar por la exodoncia."
        ],
        marcas_data=[
            ("concepto biomecánico del «efecto férula» (ferrule effect)", "clave", "Principio biomecánico de rehabilitación", "Apunta a abrazadera dentinaria para retención y disipación de fuerzas"),
            ("¿Qué es el efecto férula y cuál es el requisito anatómico indispensable para garantizar el éxito restaurador y evitar la fractura radicular?", "pide", "Definición y requisito dimensional", "Demanda identificar dos milímetros de dentina sana en trescientos sesenta grados")
        ],
        steps_ideas=[
            ("idea", "Salvar diente vs implante", "El profesor enseñó que siempre se lucha por salvar el diente si este tiene suficiente remanente."),
            ("idea", "Efecto férula", "Es el collar o abrazadera de dentina natural sana que la corona abraza como un zuncho alrededor del diente."),
            ("idea", "Requisito de dos milímetros", "Se necesitan mínimo dos milímetros de altura de dentina sana por encima de la encía en toda la vuelta (trescientos sesenta grados)."),
            ("check", "Comprobación biomecánica", "Confirmamos efecto férula como dos milímetros de dentina sana en trescientos sesenta grados para evitar fracturas.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta lección magistral del profesor sobre cómo decidir si un diente se puede salvar o si toca sacarlo."),
            ("m:concepto biomecánico del «efecto férula» (ferrule effect)", "Observa este concepto biomecánico clave: el efecto férula o collar de dentina."),
            ("leer", "El docente explicó que cuando ponemos un perno y una corona, las fuerzas de masticación tratan de partir la raíz."),
            ("leer", "Para que no se parta, la corona debe abrazar al menos dos milímetros de dentina sana en toda la vuelta del muñón."),
            ("leer", "Por lo tanto, la opción que describe dos milímetros de altura de dentina en los trescientos sesenta grados es la correcta.")
        ]
    ))

    return qs
