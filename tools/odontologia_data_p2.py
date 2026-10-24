"""Datos de las preguntas 21 a 40 de Odontología (Endodoncia).
Alineadas con la Clase 1 y Clase 2, corregidas y enriquecidas.
"""

def get_questions_21_to_40(make_q):
    qs = []

    # 21 (Key A = 0) - CORRECCIÓN EDAD Y DIFERENCIAL
    qs.append(make_q(
        qid="odo-021", nivel=2,
        enunciado="Una niña de ocho años es traída por su madre a consulta odontológica. Al examen clínico se observa una caries masiva en el primer molar permanente inferior (diente con ápice radicular inmaduro abierto) con una masa de tejido rojizo carnoso e indoloro que brota del interior de la cavidad pulpar hacia la boca y sangra al masticar. De acuerdo con lo explicado por el profesor en clase (líneas dos mil ciento catorce a dos mil doscientos diecisiete), ¿cuál es el diagnóstico, cómo se diferencia de la hiperplasia gingival y qué conducta clínica procede según el tejido remanente?",
        opciones=[
            "Pulpitis irreversible asintomática con pulpitis hiperplásica (pólipo pulpar); se pasa una sonda para verificar que nace del interior de la cámara y no de la encía; si perdió más del sesenta por ciento requerirá endodoncia, si conserva estructura permite pulpotomía con biocerámico.",
            "Absceso apical agudo extenso con celulitis facial difusa y compromiso sistémico; se realiza drenaje con incisión en encía adherida y antibioticoterapia por vía parenteral inmediata.",
            "Necrosis pulpar séptica con periodontitis apical sintomática y reabsorción externa; se procede con exodoncia forzada al no existir posibilidad de tratamiento conservador.",
            "Granuloma periférico de células gigantes del hueso alveolar con eritema gingival; se realiza resección en bloque de la apófisis alveolar mandibular."
        ],
        correcta=0,
        distractores=[
            "",
            "El absceso agudo es una colección purulenta dolorosa con tumefacción fluctuante en fondo de surco, no un pólipo fibrovascular dentro de la cavidad cariosa.",
            "En el pólipo pulpar la pulpa radicular está vital y ricamente vascularizada, lo cual descarta la necrosis pulpar séptica.",
            "El granuloma periférico de células gigantes se origina en el periostio o ligamento periodontal externo, no es una proliferación del tejido pulpar cameral."
        ],
        explicacion="En las líneas dos mil ciento catorce a dos mil doscientos diecisiete, el docente expuso este cuadro clásico: ocurre en niños y adolescentes jóvenes (ocho a nueve años para el primer molar permanente) con dientes de ápices abiertos y rica vascularización pulpar donde una caries masiva permite la proliferación de tejido de granulación hacia la cavidad bucal (pólipo pulpar o pulpitis irreversible asintomática hiperplásica). El profesor enseñó que debe diferenciarse de la hiperplasia gingival pasando suavemente una sonda por el contorno: si la sonda penetra entre la masa y la encía demostrando que el tallo brota de la cámara pulpar, es pólipo pulpar; si está anclado a la papila gingival interdental, es hiperplasia gingival. La conducta terapéutica depende de la destrucción coronaria: si conserva suficiente estructura y el ápice está abierto, se puede realizar una pulpotomía cameral con biocerámico para inducir apexogénesis; si se perdió más del sesenta por ciento de la estructura dental, requerirá endodoncia completa, perno colado o núcleo y corona de cobertura total.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Diagnóstico pulpar: pulpitis hiperplásica (pólipo pulpar)",
        que="Diagnosticar el pólipo pulpar en diente joven con ápice abierto, diferenciarlo con sonda y definir la conducta según remanente.",
        clave="El pólipo pulpar ocurre en dientes jóvenes con ápice abierto; se diferencia de la encía con una sonda y se trata con pulpotomía o endodoncia con corona según remanente.",
        pistas=[
            "Ten en cuenta que el molar de una niña de ocho años tiene la raíz en formación con el foramen apical abierto.",
            "Recuerda la técnica de la sonda explicada por el profesor para comprobar que la masa nace de la cámara pulpar y no de la papila gingival."
        ],
        plan=[
            "Reconocer la proliferación carnosa de granulación en diente joven como pulpitis hiperplásica.",
            "Aplicar la sonda periodontal para delimitar el origen pulpar frente a una hiperplasia gingival.",
            "Determinar el tratamiento según la pérdida coronaria mayor o menor al sesenta por ciento."
        ],
        marcas_data=[
            ("niña de ocho años", "dato", "Edad y ápice inmaduro abierto", "Apunta a paciente joven con foramen radicular en formación"),
            ("masa de tejido rojizo carnoso e indoloro que brota del interior de la cavidad pulpar", "clave", "Signo clínico de pólipo pulpar", "Apunta a pulpitis hiperplásica proliferativa"),
            ("¿cuál es el diagnóstico, cómo se diferencia de la hiperplasia gingival y qué conducta clínica procede según el tejido remanente?", "pide", "Diagnóstico, diferencial y tratamiento", "Demanda integrar diagnóstico, maniobra semiológica y plan terapéutico")
        ],
        steps_ideas=[
            ("idea", "Pólipo pulpar", "Ocurre en dientes jóvenes con abundante aporte vascular donde la pulpa prolifera como tejido de granulación."),
            ("idea", "Diferencial con sonda", "El profesor enseñó a pasar una sonda: si rodea el tallo dentro del diente es pulpar; si viene de la encía es gingival."),
            ("idea", "Criterio del sesenta por ciento", "Si se perdió más del sesenta por ciento requiere endodoncia, núcleo y corona; si no, pulpotomía con biocerámico."),
            ("check", "Comprobación clínica", "Confirmamos pulpitis hiperplásica en diente inmaduro con diferenciación mediante sonda y tratamiento según remanente.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este caso característico de odontopediatría y endodoncia."),
            ("m:niña de ocho años", "Observa que a los ocho años el primer molar permanente todavía tiene el ápice de la raíz abierto en formación."),
            ("m:masa de tejido rojizo carnoso e indoloro que brota del interior de la cavidad pulpar", "Mira esa masa de tejido rojizo que sale de la pulpa: es una pulpitis irreversible hiperplásica o pólipo pulpar."),
            ("leer", "El docente explicó que para no confundirlo con la encía vecina, se pasa una sonda alrededor confirmando que sale de la cámara."),
            ("leer", "Si la corona se destruyó más del sesenta por ciento se hace endodoncia con núcleo y corona; si no, pulpotomía con biocerámico.")
        ]
    ))

    # 22 (Key B = 1)
    qs.append(make_q(
        qid="odo-022", nivel=2,
        enunciado="Durante el diagnóstico diferencial entre lesiones endodónticas y periodontales, el docente interroga sobre cómo distinguir con certeza clínica un absceso periapical de un absceso periodontal en un diente con tumefacción vestibular. ¿Cuáles son los criterios semiológicos cardinales enseñados por el profesor respecto a la vitalidad pulpar y el examen con cono de gutapercha?",
        opciones=[
            "El absceso periodontal siempre produce cefalea hemicraneal intensa y náuseas reflejas, mientras que las infecciones periapicales de origen pulpar se circunscriben de forma estricta a la cresta ósea alveolar sin generar dolor local.",
            "El absceso periapical habitualmente cursa con pulpa desvitalizada (necrosis con prueba de frío negativa) y el cono llega al ápice; el absceso periodontal suele presentar pulpa vital (frío positivo) y el cono queda a mitad de raíz con bolsa profunda.",
            "El absceso periapical se cura espontáneamente tras el uso de colutorios de clorhexidina al cero punto doce por ciento sin requerir desbridamiento mecánico ni desinfección del conducto radicular.",
            "En el absceso periodontal el diente pierde por completo la totalidad del ligamento periodontal en todas sus superficies radiculares convirtiéndose en un diente no rehabilitable."
        ],
        correcta=1,
        distractores=[
            "La cefalea hemicraneal y náuseas no son criterios semiológicos diferenciales de patología periodontal frente a periapical.",
            "",
            "Un absceso periapical con necrosis intraconducto jamás se cura con enjuagues de clorhexidina, requiere biomecánica completa.",
            "La pérdida de inserción en el absceso periodontal es localizada en la zona de la bolsa, no implica desprendimiento total inmediato del diente."
        ],
        explicacion="El docente destacó las diferencias fundamentales entre ambas entidades: 1) Vitalidad pulpar: el absceso periapical es de origen endodóntico bacteriano, por lo que la pulpa está desvitalizada (necrosis pulpar con prueba de frío negativa absoluto); en cambio, el absceso periodontal es de origen marginal en el periodonto de inserción y la pulpa habitualmente se conserva vital y sensible al frío; 2) Fistulografía y sondaje: al introducir un cono de gutapercha radiopaco por la fístula, en el absceso periapical el cono se proyecta hasta el foramen apical, mientras que en el absceso periodontal el cono se detiene lateralmente a mitad de la superficie radicular donde se ubica la bolsa periodontal profunda.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Diagnóstico diferencial: absceso periapical frente a periodontal",
        que="Diferenciar el absceso periapical del periodontal según vitalidad pulpar y trayectoria del cono de gutapercha.",
        clave="El absceso periapical tiene pulpa necrótica y el cono alcanza el ápice; el periodontal tiene pulpa vital y el cono se detiene a mitad de raíz.",
        pistas=[
            "Recuerda que la causa del absceso periapical es la necrosis pulpar dentro del conducto.",
            "Ten en cuenta que en la fistulografía el cono llega al periápice en lesiones pulpares y se queda en la raíz lateral en periodontales."
        ],
        plan=[
            "Evaluar el estado de vitalidad pulpar mediante pruebas térmicas con frío.",
            "Realizar el sondaje periodontal circunferencial en busca de bolsas profundas.",
            "Trazar el trayecto fistuloso con cono de gutapercha para confirmar el ápice o tercio medio radicular."
        ],
        marcas_data=[
            ("distinguir con certeza clínica un absceso periapical de un absceso periodontal", "clave", "Dilema diagnóstico diferencial", "Demanda contrastar signos endodónticos y periodontales"),
            ("respecto a la vitalidad pulpar y el examen con cono de gutapercha", "pide", "Criterios semiológicos evaluados", "Demanda identificar frío negativo/cono apical vs frío positivo/cono medio")
        ],
        steps_ideas=[
            ("idea", "Vitalidad pulpar", "El absceso periapical viene de adentro del diente (necrosis); el periodontal viene de la encía (pulpa vital)."),
            ("idea", "Rastreo con cono", "El cono de gutapercha señala el sitio exacto: si va a la punta de la raíz es periapical; si se queda en la mitad es periodontal."),
            ("check", "Comprobación diferencial", "Confirmamos que frío negativo con cono apical define absceso periapical, y frío positivo con cono a media raíz define periodontal.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta diferenciación diagnóstica fundamental entre dos patologías con hinchazón."),
            ("m:distinguir con certeza clínica un absceso periapical de un absceso periodontal", "Fíjate en las dos preguntas que hace el profesor: ¿cómo está la pulpa y adónde llega el cono?"),
            ("leer", "El docente explicó que el absceso periapical nace de una pulpa muerta, por lo que la prueba de frío da negativa."),
            ("leer", "En cambio, en el absceso periodontal la pulpa suele estar viva y responde al frío con normalidad."),
            ("leer", "Además, en la radiografía el cono de gutapercha llega al ápice en el periapical, y queda a mitad de raíz en el periodontal.")
        ]
    ))

    # 23 (Key C = 2)
    qs.append(make_q(
        qid="odo-023", nivel=3,
        enunciado="Al realizar la inspección del examen extraoral en un paciente que consulta por una infección odontogénica severa originada en un molar inferior, el clínico observa signos de alarma que indican diseminación bacteriana fascial profunda. ¿Cuál de los siguientes grupos de signos clínicos configura una sospecha inminente de Angina de Ludwig que exige remisión hospitalaria urgente?",
        opciones=[
            "Desgaste incisal leve generalizado, facetas de atrición moderadas en bordes caninos superiores e inferiores y ausencia de dolor o hipertrofia en músculos masticatorios.",
            "Torsión de la punta nasal hacia la izquierda, presencia de efélides solares en pómulos malares y agudeza auditiva conservada en la evaluación otorrinolaringológica básica.",
            "Asimetría facial con edema indurado submandibular difuso, trismus severo con limitación de apertura bucal, elevación del piso de la boca y dificultad respiratoria o disfagia.",
            "Pigmentación melánica fisiológica difusa en la encía adherida anterior, ausencia de sangrado al sondaje y respiración nasal perfectamente coordinada."
        ],
        correcta=2,
        distractores=[
            "El desgaste incisal y facetas de atrición corresponden a parafunción oclusal por bruxismo sin compromiso infeccioso.",
            "Las características nasales y cutáneas descritas son variantes estéticas normales no asociadas a sepsis odontogénica.",
            "",
            "La pigmentación melánica y respiración nasal normal son hallazgos fisiológicos de salud en mucosas bucales."
        ],
        explicacion="La presencia de tumefacción indurada bilateral en los espacios submandibular, sublingual y submentoniano, con elevación lingual, trismus severo, disfagia y compromiso de la vía aérea (disnea) define la Angina de Ludwig, complicación infecciosa odontogénica grave originada comúnmente en molares inferiores. El docente subrayó que estos signos representan una emergencia médica que compromete la vida por asfixia inminente; no se maneja en el consultorio dental convencional, sino que requiere traslado inmediato en ambulancia a un centro hospitalario con servicio de cirugía maxilofacial y cuidados intensivos para asegurar la vía aérea y administrar antibióticos intravenosos combinados con desbridamiento quirúrgico.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Examen extraoral: signos de alarma de infección odontogénica",
        que="Reconocer los signos clínicos de alarma de la Angina de Ludwig y ordenar la remisión hospitalaria inmediata.",
        clave="El edema indurado submandibular con trismus, elevación del piso de boca y dificultad respiratoria configura Angina de Ludwig y exige remisión hospitalaria.",
        pistas=[
            "Busca la combinación de hinchazón en cuello y mandíbula con problemas para tragar o respirar.",
            "Recuerda que cuando una infección dental pasa a piso de boca y cuello se convierte en una urgencia hospitalaria de vida o muerte."
        ],
        plan=[
            "Identificar el compromiso de espacios anatómicos profundos submandibulares y sublinguales.",
            "Detectar los signos clínicos críticos de trismus, elevación del piso de boca y disfagia.",
            "Ordenar la remisión inmediata a urgencias hospitalarias para protección de la vía aérea."
        ],
        marcas_data=[
            ("signos de alarma que indican diseminación bacteriana fascial profunda", "clave", "Signos de sepsis odontogénica grave", "Apunta a compromiso de espacios del cuello"),
            ("sospecha inminente de Angina de Ludwig que exige remisión hospitalaria urgente", "pide", "Diagnóstico de alarma y conducta", "Demanda identificar la tríada de edema, trismus y disnea")
        ],
        steps_ideas=[
            ("idea", "Diseminación fascial", "Las bacterias de molares inferiores pueden perforar la cortical lingual y caer a los espacios del cuello."),
            ("idea", "Angina de Ludwig", "La infección bilateral submandibular y sublingual eleva la lengua y cierra la faringe provocando asfixia."),
            ("idea", "Remisión hospitalaria", "El profesor enseñó que esto no se atiende en el sillón dental: se remite de inmediato a urgencias de hospital."),
            ("check", "Comprobación clínica", "Confirmamos edema submandibular, trismus y dificultad respiratoria como signos de Angina de Ludwig.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con máxima atención estos signos de alarma vital explicados por el profesor."),
            ("m:signos de alarma que indican diseminación bacteriana fascial profunda", "Observa que se trata de una infección de molares que se escapó del diente y bajó al cuello."),
            ("leer", "El docente enseñó que cuando el piso de la boca se levanta, se endurece la mandíbula y el paciente no puede tragar ni respirar, estamos ante la Angina de Ludwig."),
            ("leer", "Esta complicación pone en riesgo inmediato la vida del paciente por asfixia."),
            ("leer", "Por lo tanto, la respuesta correcta describe este cuadro de edema submandibular indurado con trismus y disnea.")
        ]
    ))

    # 24 (Key D = 3)
    qs.append(make_q(
        qid="odo-024", nivel=2,
        enunciado="En el análisis del formato de historia clínica exigido en la universidad, el docente hace hincapié en la forma adecuada de redactar la descripción de las caries y las superficies dentarias afectadas (oclusal, mesial, distal) antes de proceder con el aislamiento absoluto. ¿Cuál es la justificación biomecánica y médico-legal enfatizada por el profesor en clase?",
        opciones=[
            "«El diente presenta bacterias cariogénicas vivas infiltradas en el esmalte coronal» para prescribir pastas dentales alcalinas.",
            "«El diente tiene una fractura microscópica que requiere corona total inmediata» para cobrar el procedimiento en la primera consulta.",
            "«El diente se encuentra desmineralizado en un ochenta por ciento de su volumen» para evitar que el paciente mastique chicle.",
            "Por implicaciones biomecánicas y legales: si la caries destruye más del sesenta por ciento del diente, la fuerza de la grapa de aislamiento puede fracturar la raíz si no se reconstruye previamente."
        ],
        correcta=3,
        distractores=[
            "La mención genérica de bacterias vivas en esmalte no aporta datos anatómicos ni biomecánicos sobre el riesgo de fractura con la grapa.",
            "Diagnosticar fractura microscópica sin prueba oclusal selectiva ni justificación clínica constituye una mala práctica profesional.",
            "Estimar desmineralización porcentual arbitraria no guarda relación con la técnica de reconstrucción de paredes ni con el aislamiento.",
            ""
        ],
        explicacion="El docente recalcó en clase que la historia clínica es un documento médico-legal riguroso. Al describir una lesión cariosa es obligatorio detallar las caras afectadas (oclusomesial, distooclusal, etc.) porque ello determina el remanente coronario. Si la caries ha destruido más del sesenta por ciento del volumen dental, las paredes están debilitadas; colocar directamente una grapa metálica de aislamiento absoluto sobre una corona socavada puede fracturarla verticalmente hacia la raíz durante el procedimiento, lo que tiene graves consecuencias legales si no fue advertido y reconstruido previamente con ionómero de vidrio o resina antes de aislar.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Semiología radiográfica: terminología y redacción de hallazgos",
        que="Fundamentar la descripción rigurosa de superficies cariadas y el riesgo de fractura por grapa de aislamiento.",
        clave="Si la destrucción por caries supera el sesenta por ciento, la fuerza de la grapa puede fracturar el diente si no se reconstruye previamente.",
        pistas=[
            "Recuerda la advertencia del docente sobre la fuerza elástica de las grapas metálicas al colocarlas en dientes muy cariados.",
            "Ten en cuenta que el documento de la historia clínica respalda legalmente al operador ante posibles fracturas coronales."
        ],
        plan=[
            "Reconocer la importancia médico-legal de especificar las superficies anatómicas destruidas.",
            "Evaluar el riesgo biomecánico de fractura radicular por tensión de la grapa en dientes con pérdida mayor al sesenta por ciento.",
            "Indicar la reconstrucción pre-endodóntica de paredes para asegurar un aislamiento sin riesgos."
        ],
        marcas_data=[
            ("redactar la descripción de las caries y las superficies dentarias afectadas", "clave", "Requisito de la historia clínica", "Apunta a precisión anatómica y médico-legal"),
            ("¿Cuál es la justificación biomecánica y médico-legal enfatizada por el profesor en clase?", "pide", "Fundamento biomecánico y legal", "Demanda identificar el riesgo de fractura con la grapa")
        ],
        steps_ideas=[
            ("idea", "Valor médico-legal", "La historia clínica documenta el estado inicial del diente antes de que el profesional coloque instrumental."),
            ("idea", "Fuerza de la grapa", "Si la caries destruyó más del sesenta por ciento de la corona, la grapa de metal puede quebrar la pared si no se reconstruye."),
            ("check", "Comprobación clínica", "Confirmamos que se detallan las superficies para prevenir y justificar fracturas por grapa de aislamiento.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta exigencia clínica y legal explicada por el docente en el llenado de la historia clínica."),
            ("m:redactar la descripción de las caries y las superficies dentarias afectadas", "Observa que el docente exige anotar con precisión cuáles caras (mesial, oclusal, distal) están dañadas."),
            ("leer", "El docente explicó que si la caries se comió más del sesenta por ciento del diente, las paredes están muy delgadas."),
            ("leer", "Si el estudiante coloca la grapa de metal directamente sobre esa corona débil, la grapa puede partir el diente en dos."),
            ("leer", "Por ello, se debe registrar para justificar la reconstrucción previa de paredes antes de aislar.")
        ]
    ))

    # 25 (Key A = 0)
    qs.append(make_q(
        qid="odo-025", nivel=2,
        enunciado="Un joven de 20 años asiste a consulta estética porque nota que su incisivo central superior derecho ha cambiado a un color grisáceo opaco. Recuerda haber recibido un balonazo en la boca en la escuela hace varios años sin fractura evidente. En las pruebas de frío y electricidad el diente no responde en absoluto (negativo absoluto) y los tejidos periapicales no duelen a la percusión. De acuerdo con las enseñanzas del profesor sobre traumatología y controles (líneas mil ciento treinta y cuatro a mil ciento cincuenta), ¿cuál es el diagnóstico y qué calendario de controles debió aplicarse?",
        opciones=[
            "Necrosis pulpar postraumática asintomática; las secuelas de un trauma pueden manifestarse hasta seis años después, requiriendo controles el día del golpe, quince días, un mes, tres, seis y doce meses y anualmente hasta seis años.",
            "Pulpitis reversible aguda; el cambio de color se debe a manchas alimentarias extrínsecas que desaparecen con profilaxis básica con pasta abrasiva.",
            "Reabsorción interna perforante maligna; requiere exodoncia urgente del incisivo sin intentar tratamiento de conductos.",
            "Pulpa clínicamente normal con hematoma benigno; no requiere ningún tratamiento endodóntico ni controles posteriores."
        ],
        correcta=0,
        distractores=[
            "",
            "La pulpa está completamente desvitalizada (frío negativo) y la pigmentación grisáceo opaca interna no es una mancha superficial de esmalte.",
            "Una reabsorción interna incipiente no es maligna ni exige exodoncia inmediata; se trata con endodoncia completa.",
            "La respuesta negativa al frío descarta la pulpa normal; la necrosis exige tratamiento de conductos para prevenir infección periapical."
        ],
        explicacion="En las líneas mil ciento treinta y cuatro a mil ciento cincuenta del texto fuente, el profesor expuso claramente que las secuelas patológicas de los traumatismos dentoalveolares (necrosis pulpar, calcificaciones masivas, reabsorciones radiculares) pueden manifestarse muchos años después del impacto, incluso hasta seis años más tarde. Por ello, ante un traumatismo se debe establecer un protocolo estricto de controles clínicos y radiográficos: el día del accidente (día cero), a los quince días, al mes, a los tres meses, a los seis meses, a los doce meses y posteriormente un control anual durante seis años. En este paciente, el impacto seccionó o trombosó el paquete vasculonervioso apical generando necrosis pulpar silente con hemólisis y degradación de hemoglobina en los túbulos dentinarios, originando el color grisáceo característico.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Patología pulpar: necrosis pulpar por traumatismo y controles",
        que="Diagnosticar la necrosis pulpar postraumática con discromía y conocer el protocolo de controles hasta seis años.",
        clave="Las secuelas de un trauma pueden aparecer hasta seis años después; la necrosis cursa con discromía grisácea y prueba térmica negativa.",
        pistas=[
            "Observa el antecedente del balonazo y el color grisáceo opaco del diente.",
            "Recuerda la regla del profesor: los controles de un traumatismo deben prolongarse periódicamente hasta los seis años."
        ],
        plan=[
            "Asociar el traumatismo contuso antiguo con la trombosis vascular y necrosis pulpar silente.",
            "Identificar el cambio de coloración como producto de la degradación hemática intratubular.",
            "Reconocer el calendario de controles postraumáticos establecido hasta seis años de evolución."
        ],
        marcas_data=[
            ("ha cambiado a un color grisáceo opaco. Recuerda haber recibido un balonazo", "clave", "Signo clínico postraumático", "Apunta a necrosis pulpar con descomposición de hemoglobina"),
            ("pruebas de frío y electricidad el diente no responde en absoluto (negativo absoluto)", "dato", "Desvitalización pulpar completa", "Apunta a necrosis aséptica previa"),
            ("¿cuál es el diagnóstico y qué calendario de controles debió aplicarse?", "pide", "Diagnóstico y calendario de seguimiento", "Demanda clasificar la necrosis y detallar el calendario de controles")
        ],
        steps_ideas=[
            ("idea", "Secuelas del trauma", "El docente enseñó que los efectos de un golpe en la boca pueden tardar hasta seis años en verse."),
            ("idea", "Coloración grisácea", "La necrosis destruye los eritrocitos; la hemoglobina se degrada y tiñe la dentina desde adentro."),
            ("idea", "Calendario de citas", "El protocolo exige citas a día cero, quince días, un mes, tres, seis, doce meses y anualmente hasta seis años."),
            ("check", "Comprobación clínica", "Confirmamos necrosis postraumática con protocolo de controles extendido hasta seis años.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este caso muy común de cambio de color en un diente anterior."),
            ("m:ha cambiado a un color grisáceo opaco. Recuerda haber recibido un balonazo", "Observa el antecedente del balonazo en la escuela y el tono grisáceo opaco del diente."),
            ("m:pruebas de frío y electricidad el diente no responde en absoluto (negativo absoluto)", "Al aplicar frío y electricidad no hay respuesta: la pulpa se murió por el impacto."),
            ("leer", "El docente explicó en clase que las consecuencias de un golpe pueden demorar hasta seis años en aparecer."),
            ("leer", "Por ello, el protocolo correcto exige controles periódicos hasta cumplir seis años de seguimiento.")
        ]
    ))

    # 26 (Key B = 1)
    qs.append(make_q(
        qid="odo-026", nivel=2,
        enunciado="Un paciente llega al consultorio con un vaso de agua con hielo en la mano, bebiendo pequeños sorbos constantemente. Manifiesta angustiado: «Doctor, si no tengo agua helada en la boca el dolor es insoportable; pero cuando tomo agua caliente o café el dolor me hace llorar». ¿A qué cuadro histopatológico pulpar corresponde este comportamiento térmico característico y cuál es su base biofísica?",
        opciones=[
            "A una pulpa sana y equilibrada que exhibe un mecanismo vasomotor adaptativo perfectamente normal ante fluctuaciones térmicas extremas inducidas.",
            "A una pulpitis irreversible sintomática en fase avanzada, donde el calor expande los gases y líquidos intrapulpares excitando las fibras C y el frío disminuye temporalmente la presión tisular.",
            "A una periodontitis apical asintomática crónica producida por fuerzas mecánicas de atrición y sobrecarga oclusal leve en los molares.",
            "A una hipersensibilidad dentinaria cervical provocada por retracción de la encía marginal y exposición de túbulos dentinarios desobturados."
        ],
        correcta=1,
        distractores=[
            "Una pulpa sana responde al frío con molestia breve que cede en dos segundos y no requiere beber agua helada constante.",
            "",
            "La periodontitis apical asintomática no responde a cambios térmicos porque la pulpa está desvitalizada y no hay dolor espontáneo.",
            "La hipersensibilidad cervical duele con el frío y no se alivia en absoluto manteniendo agua con cubos de hielo en la boca."
        ],
        explicacion="Este signo patognomónico fue destacado con énfasis por el docente: el paciente que no puede separarse de un vaso con agua fría presenta una pulpitis irreversible sintomática en estadio avanzado de descomposición pulpar. En esta fase, la inflamación microbiana genera liberación de mediadores químicos, exudado y gases intrapulpares. El calor expande físicamente el volumen de los gases y líquidos en una cámara inextensible, comprimiendo violentamente las fibras C amielínicas; al aplicar agua helada, los gases y fluidos se contraen por disminución térmica, reduciendo momentáneamente la presión intrapulpar y aliviando el dolor de forma temporal hasta que el calor corporal vuelve a calentarlo.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Fisiopatología del dolor pulpar: alivio con frío y exacerbación con calor",
        que="Explicar la biofísica del alivio con agua fría y exacerbación con calor en pulpitis irreversible avanzada.",
        clave="En pulpitis irreversible avanzada el calor dilata los gases intrapulpares activando fibras C, y el agua helada contrae el volumen aliviando la presión.",
        pistas=[
            "Observa el cuadro clásico del paciente que llega con el vaso de agua helada en la mano.",
            "Recuerda la ley física explicada por el profesor: los gases se expanden con el calor y se contraen con el frío dentro de una cámara cerrada."
        ],
        plan=[
            "Identificar el síntoma clínico cardinal de dolor al calor con alivio temporal con frío.",
            "Analizar la expansión térmica de gases y exudado inflamatorio sobre las fibras C profundas.",
            "Diagnosticar pulpitis irreversible sintomática en estadio de licuefacción avanzada."
        ],
        marcas_data=[
            ("si no tengo agua helada en la boca el dolor es insoportable; pero cuando tomo agua caliente o café el dolor me hace llorar", "clave", "Signo clínico térmico patognomónico", "Apunta a fase de gasificación pulpar irreversible"),
            ("¿A qué cuadro histopatológico pulpar corresponde este comportamiento térmico característico y cuál es su base biofísica?", "pide", "Diagnóstico y base biofísica", "Demanda fundamentar el rol del calor y del frío sobre la presión de gases")
        ],
        steps_ideas=[
            ("idea", "Paciente con vaso de hielo", "El docente describió este caso clásico: el paciente no puede soltar el vaso de agua helada."),
            ("idea", "Expansión de gases", "La descomposición bacteriana produce gases; el calor los dilata aumentando salvajemente la presión intrapulpar."),
            ("idea", "Alivio temporal", "El hielo enfría y contrae los gases reduciendo momentáneamente la presión sobre las fibras C."),
            ("check", "Comprobación biofísica", "Confirmamos pulpitis irreversible sintomática avanzada con compresión de gases dilatados por calor.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este cuadro clínico que el docente describió como inolvidable."),
            ("m:si no tengo agua helada en la boca el dolor es insoportable; pero cuando tomo agua caliente o café el dolor me hace llorar", "Mira este comportamiento: el paciente llega bebiendo agua helada y el calor lo desespera."),
            ("leer", "El docente explicó la física del fenómeno: dentro de la muela hay gases y bacterias acumuladas."),
            ("leer", "Cuando el paciente toma algo caliente, el gas se expande dentro de la cavidad dura y aplasta las fibras nerviosas C."),
            ("leer", "Al tomar agua con hielo, el gas se contrae y la presión baja por unos instantes, aliviando temporalmente el dolor.")
        ]
    ))

    # 27 (Key C = 2) - REEMPLAZO CLASE 1
    qs.append(make_q(
        qid="odo-027", nivel=2,
        enunciado="Al realizar la evaluación clínica de un incisivo que sufrió una subluxación traumática leve hace tres semanas, el odontólogo detecta movilidad horizontal leve y dolor ligero a la percusión vertical. Al realizar el sondaje periodontal circunferencial no encuentra bolsas periodontales y la prueba térmica de frío da una respuesta positiva normal rápida que cede en dos segundos. De acuerdo con lo explicado por el profesor en clase (líneas doscientas veinticuatro a doscientas treinta y siete), ¿cómo se interpreta esta movilidad y cuál es la conducta indicada?",
        opciones=[
            "Grado tres de destrucción alveolar irreparable que exige la exodoncia forzada y colocación de implante dental inmediato.",
            "Periodontitis marginal crónica avanzada que requiere cirugía de colgajo periodontal abierto y raspaje radicular extenso.",
            "Movilidad fisiopatológica por ensanchamiento y edema inflamatorio del ligamento periodontal tras el trauma con pulpa vital; la conducta es aliviar la oclusión y controlar la vitalidad sin hacer endodoncia.",
            "Necrosis pulpar séptica inmediata con desprendimiento radicular que exige desobturar el conducto en la misma cita."
        ],
        correcta=2,
        distractores=[
            "La movilidad leve con pulpa vital y ligamento periodontal recuperable no justifica en absoluto una exodoncia.",
            "No existen bolsas periodontales profundas ni pérdida ósea marginal, descartando periodontitis crónica.",
            "",
            "La prueba de frío positiva normal descarta la necrosis pulpar; desobturar o hacer endodoncia en este momento es una iatrogenia."
        ],
        explicacion="El docente explicó en clase (líneas doscientas veinticuatro a doscientas treinta y siete) que la movilidad dental no debe interpretarse de forma aislada. Cuando ocurre tras un traumatismo y la pulpa conserva su vitalidad (prueba de frío positiva normal) y no existen bolsas periodontales profundas, la movilidad es transitoria y se debe al edema y congestión inflamatoria de las fibras del ligamento periodontal dentro del alvéolo. La conducta clínica adecuada consiste en aliviar cualquier contacto oclusal traumático, brindar reposo masticatorio al diente y realizar seguimiento clínico y radiográfico a los quince días y al mes sin realizar endodoncia invasiva, ya que el ligamento desinflama y el diente recupera su firmeza original.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Semiología de la movilidad y examen periodontal en endodoncia",
        que="Interpretar la movilidad postraumática con pulpa vital y aplicar conducta conservadora sin endodoncia.",
        clave="La movilidad postraumática con frío positivo normal traduce edema del ligamento; se alivia la oclusión y se controla sin hacer endodoncia.",
        pistas=[
            "Fíjate que la prueba de frío es positiva normal y que no hay bolsas periodontales.",
            "Recuerda la enseñanza del profesor: la movilidad por edema inflamatorio se revierte dando reposo al diente si la pulpa está viva."
        ],
        plan=[
            "Evaluar la movilidad dental en conjunto con el sondaje periodontal y las pruebas térmicas.",
            "Identificar el edema del ligamento periodontal como causa reversible de la movilidad postraumática.",
            "Indicar reposo oclusal y seguimiento periódico evitando tratamientos endodónticos innecesarios."
        ],
        marcas_data=[
            ("movilidad horizontal leve y dolor ligero a la percusión vertical", "dato", "Signos periodontales postraumáticos", "Apunta a inflamación del ligamento periodontal"),
            ("sondaje periodontal circunferencial no encuentra bolsas periodontales y la prueba térmica de frío da una respuesta positiva normal", "clave", "Salud pulpar y periodontal de soporte", "Apunta a proceso inflamatorio reversible con pulpa vital"),
            ("¿cómo se interpreta esta movilidad y cuál es la conducta indicada?", "pide", "Interpretación y conducta", "Demanda descartar endodoncia e indicar reposo y control")
        ],
        steps_ideas=[
            ("idea", "Edema del ligamento", "Un golpe reciente ensancha e inflama el ligamento periodontal generando movilidad temporal."),
            ("idea", "Vitalidad pulpar conservada", "Si la prueba de frío da positiva normal, la pulpa está viva y no hay necrosis bacteriana."),
            ("idea", "Conducta conservadora", "El profesor enseñó que se alivia el contacto de la mordida y se observa, sin abrir el conducto."),
            ("check", "Comprobación clínica", "Confirmamos movilidad por edema de ligamento tratada con alivio oclusal y control de vitalidad.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este caso donde el clínico debe decidir si interviene o conserva el diente."),
            ("m:movilidad horizontal leve y dolor ligero a la percusión vertical", "Observa que el diente se mueve un poco y duele ligeramente a la percusión tras el golpe."),
            ("m:sondaje periodontal circunferencial no encuentra bolsas periodontales y la prueba térmica de frío da una respuesta positiva normal", "Mira este dato crucial: no hay bolsas periodontales y la prueba de frío dio positiva normal."),
            ("leer", "El docente explicó que la movilidad se debe simplemente a que el ligamento está hinchado por el trauma."),
            ("leer", "Como la pulpa está viva y sana, la conducta es no hacer endodoncia: se alivia la mordida y se controla.")
        ]
    ))

    # 28 (Key D = 3)
    qs.append(make_q(
        qid="odo-028", nivel=3,
        enunciado="En una intervención restauradora en un molar permanente joven de un paciente de 16 años con pulpa previamente sana, el operador produce accidentalmente una microexposición pulpar mecánica menor a un milímetro. Se lava la cavidad con suero fisiológico estéril durante cinco minutos logrando hemostasia completa de un sangrado rojo brillante. ¿Cuál es el protocolo de recubrimiento pulpar directo con biocerámicos y su seguimiento posterior?",
        opciones=[
            "Colocar ácido fosfórico directamente sobre la pulpa expuesta para cauterizarla y obturar de inmediato con resina compuesta fluida.",
            "Realizar una biopulpectomía completa con limas rotatorias de inmediato asumiendo que toda exposición pulpar es irreversible.",
            "Colocar eugenol puro sobre el tejido pulpar y esperar a que el paciente refiera dolor nocturno para intervenir.",
            "Aplicar silicato de calcio biocerámico (Biodentine o MTA) directamente sobre la exposición, colocar una base intermedia protectora, sellar la cavidad y realizar controles a los quince días, tres, seis y doce meses con pruebas de frío."
        ],
        correcta=3,
        distractores=[
            "El ácido fosfórico desnaturaliza el tejido pulpar y produce necrosis química severa si entra en contacto directo.",
            "Una microexposición mecánica accidental en pulpa sana previa con hemostasia rápida tiene excelente pronóstico conservador con biocerámicos.",
            "El eugenol libre es citotóxico sobre las células pulpares y produce inflamación crónica irreversible si se aplica directamente.",
            ""
        ],
        explicacion="En una exposición pulpar accidental mecánica menor a un milímetro en diente joven con pulpa sana previa y hemostasia espontánea en menos de cinco minutos con suero fisiológico frío, está indicado el recubrimiento pulpar directo con materiales biocerámicos bioactivos (silicato tricálcico como Biodentine o MTA). El docente explicó que estos materiales son biocompatibles, inducen la formación de un puente dentinario mineralizado por los odontoblastos y sellan herméticamente la cavidad. El protocolo exige colocar encima una base protectora (como ionómero de vidrio), restaurar herméticamente y someter al diente a un seguimiento periódico estricto a los quince días, tres meses, seis meses y doce meses evaluando la respuesta positiva al frío; si en algún control el diente se torna negativo o sintomático, se procede a la endodoncia.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Terapéutica pulpar vital: recubrimiento pulpar directo con biocerámicos",
        que="Aplicar el protocolo de recubrimiento pulpar directo con silicato biocerámico y establecer su calendario de controles.",
        clave="En microexposición mecánica con hemostasia se aplica silicato biocerámico (Biodentine/MTA), base intermedia y controles a quince días, tres, seis y doce meses.",
        pistas=[
            "Observa que la exposición fue mecánica accidental, menor a un milímetro y con hemostasia rápida con suero.",
            "Ten presentes los materiales modernos biocerámicos (Biodentine/MTA) y el calendario de controles clínicos exigido."
        ],
        plan=[
            "Verificar las condiciones biológicas favorables: exposición mecánica pequeña, pulpa sana y hemostasia en cinco minutos.",
            "Seleccionar el material bioactivo biocerámico de silicato tricálcico para inducir puente de dentina.",
            "Programar el seguimiento periódico estricto a quince días, tres, seis y doce meses con pruebas térmicas."
        ],
        marcas_data=[
            ("microexposición pulpar mecánica menor a un milímetro", "dato", "Condición anatómica favorable", "Apunta a viabilidad biológica para recubrimiento directo"),
            ("hemostasia completa de un sangrado rojo brillante", "clave", "Signo vascular de pulpa sana", "Apunta a capacidad reparativa intacta"),
            ("¿Cuál es el protocolo de recubrimiento pulpar directo con biocerámicos y su seguimiento posterior?", "pide", "Protocolo clínico y seguimiento", "Demanda detallar material bioactivo y calendario de citas")
        ],
        steps_ideas=[
            ("idea", "Condiciones para recubrimiento", "Debe ser exposición pequeña accidental, sin caries bacteriana y con sangrado que frene con suero."),
            ("idea", "Biocerámicos modernos", "El profesor destacó el uso de Biodentine o MTA: sellan y estimulan a los odontoblastos para formar puente dentinario."),
            ("idea", "Controles obligatorios", "Se debe controlar a los quince días, tres, seis y doce meses; si no duele y responde al frío, fue un éxito."),
            ("check", "Comprobación terapéutica", "Confirmamos aplicación de Biodentine/MTA con base protectora y controles periódicos hasta el año.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos con cuidado este protocolo de preservación pulpar vital explicado por el profesor."),
            ("m:microexposición pulpar mecánica menor a un milímetro", "Nota que fue un accidente mecánico limpio, menor a un milímetro, en un diente con pulpa sana previa."),
            ("m:hemostasia completa de un sangrado rojo brillante", "Al irrigar con suero fisiológico frío cinco minutos, el sangrado frenó perfectamente con color rojo vivo."),
            ("leer", "El docente enseñó que en estos casos se debe aplicar un biocerámico bioactivo como Biodentine o MTA."),
            ("leer", "Se coloca una base intermedia, se restaura y se controla a los quince días, tres, seis y doce meses con pruebas de frío.")
        ]
    ))

    # 29 (Key A = 0)
    qs.append(make_q(
        qid="odo-029", nivel=2,
        enunciado="Un paciente de 38 años asiste a la clínica endodóntica con una restauración provisional de óxido de zinc en el primer premolar superior. Trae una remisión que certifica que le realizaron una apertura cameral y pulpotomía de urgencia en otro centro de salud hace una semana para calmar un dolor insoportable, y que el tratamiento quedó inconcluso. Actualmente el diente está asintomático. De acuerdo con la clasificación estandarizada de la AAE y lo enseñado en clase, ¿cuál es el diagnóstico pulpar y la conducta clínica a seguir?",
        opciones=[
            "Diente con terapia previamente iniciada; la conducta es realizar el tratamiento de conductos radiculares completo definitivo.",
            "Diente previamente tratado con obturación definitiva de conductos terminada; tomar radiografía y dar de alta.",
            "Necrosis pulpar séptica con osteólisis periapical aguda difusa; prescribir antibióticos durante diez días sin retirar la curación.",
            "Pulpitis irreversible sintomática con inflamación periapical secundaria; realizar pulpotomía con óxido de zinc repetida."
        ],
        correcta=0,
        distractores=[
            "",
            "Un diente previamente tratado ya tiene los conductos obturados con gutapercha definitiva, lo cual no ocurre aquí.",
            "No se deben administrar antibióticos en curaciones asintomáticas; la indicación es culminar la instrumentación mecánica.",
            "La pulpa cameral ya fue amputada y el diente está desbridado; repetir pulpotomías no es el tratamiento definitivo en dientes adultos."
        ],
        explicacion="De acuerdo con la clasificación diagnóstica de la Asociación Americana de Endodoncia (AAE) y lo enseñado en clase, la categoría pulpar de «Diente con terapia previamente iniciada» se reserva para aquellos órganos dentales que han sido sometidos a una intervención endodóntica parcial previa (como pulpotomía de urgencia o desbridamiento cameral) sin que se haya culminado la instrumentación y obturación radicular definitiva. Como la cámara pulpar ya fue desbridada y contiene una restauración provisional permeable, la conducta obligatoria consiste en aislar con dique de goma, desinfectar la cavidad, realizar la preparación biomecánica completa de los conductos y obturarlos tridimensionalmente.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Clasificación diagnóstica AAE: terapia previamente iniciada",
        que="Clasificar el diente con desbridamiento previo incompleto y definir la culminación del tratamiento de conductos.",
        clave="El diente con intervención endodóntica parcial previa se clasifica como terapia previamente iniciada y requiere endodoncia completa.",
        pistas=[
            "Observa que el diente ya fue abierto y le hicieron una pulpotomía de urgencia que quedó incompleta.",
            "Recuerda la categoría diagnóstica de la AAE para procedimientos parciales previos sin obturación definitiva."
        ],
        plan=[
            "Identificar el antecedente de intervención endodóntica de urgencia previa.",
            "Asignar la categoría diagnóstica estandarizada de terapia previamente iniciada.",
            "Programar la instrumentación biomecánica y obturación tridimensional definitiva."
        ],
        marcas_data=[
            ("apertura cameral y pulpotomía de urgencia en otro centro de salud hace una semana", "clave", "Intervención endodóntica parcial previa", "Apunta a categoría AAE de terapia previamente iniciada"),
            ("tratamiento quedó inconcluso. Actualmente el diente está asintomático", "dato", "Estado transitorio con sellado provisional", "Apunta a necesidad de culminación definitiva"),
            ("¿cuál es el diagnóstico pulpar y la conducta clínica a seguir?", "pide", "Diagnóstico y conducta terapéutica", "Demanda clasificar bajo norma AAE y ordenar endodoncia completa")
        ],
        steps_ideas=[
            ("idea", "Categoría diagnóstica", "El diente que ya fue abierto y pulpotomizado clasifica como terapia previamente iniciada."),
            ("idea", "Riesgo de filtración", "Las curaciones provisionales se degradan y permiten el paso de bacterias a las pocas semanas."),
            ("idea", "Tratamiento definitivo", "Se debe colocar dique de goma, limpiar los conductos radiculares y obturar con gutapercha."),
            ("check", "Comprobación clínica", "Confirmamos terapia previamente iniciada con indicación de tratamiento de conductos completo.")
        ],
        lvl1_steps=[
            ("leer", "Analicemos esta clasificación estandarizada de la Asociación Americana de Endodoncia explicada en clase."),
            ("m:apertura cameral y pulpotomía de urgencia en otro centro de salud hace una semana", "Observa que el diente ya fue abierto de urgencia para aliviar el dolor, pero no se terminaron los conductos."),
            ("m:tratamiento quedó inconcluso. Actualmente el diente está asintomático", "Tiene una curación provisional y está pendiente de terminar."),
            ("leer", "El docente enseñó que la categoría oficial exacta para este estado es «diente con terapia previamente iniciada»."),
            ("leer", "La conducta clínica no es dejarlo así, sino proceder con la instrumentación biomecánica y obturación definitiva de los conductos.")
        ]
    ))

    # 30 (Key B = 1)
    qs.append(make_q(
        qid="odo-030", nivel=3,
        enunciado="Un paciente consulta por dolor intenso a la percusión y al masticar en el primer molar inferior derecho. En la radiografía periapical se observa que los conductos radiculares fueron obturados con gutapercha hace cuatro años, pero el conducto mesial distal muestra una obturación desadaptada y corta con una radiolucidez periapical persistente. De acuerdo con los criterios del docente sobre el tiempo de cicatrización y conducta (líneas mil cuatrocientos sesenta y uno a mil seiscientos veintiuno), ¿cuál es el diagnóstico integral y el manejo clínico?",
        opciones=[
            "Pulpa clínicamente normal con tejidos periapicales sanos; colocar un perno colado y una corona definitiva sin tocar la gutapercha.",
            "Diente previamente tratado con periodontitis apical sintomática; la lesión debió cicatrizar a partir del tercer mes; al persistir con dolor y falla biomecánica procede el retratamiento de conductos, y si hay sobreobturación irritativa que no responde, cirugía periapical.",
            "Absceso apical agudo primario; prescribir amoxicilina sistémica durante un mes continuo sin desobturar los conductos.",
            "Periodontitis apical por trauma oclusal exclusiva; realizar desgaste cuspídeo masivo y no evaluar la calidad de la obturación previa."
        ],
        correcta=1,
        distractores=[
            "Un diente con conductos obturados no tiene pulpa vital ni tejidos periapicales sanos ante dolor y radiolucidez evidente.",
            "",
            "Los antibióticos por un mes no resuelven la causa mecánica de conductos subobturados y producen toxicidad bacteriana.",
            "El dolor no se debe solo a sobrecarga oclusal sino a la sobreinfección bacteriana del conducto mal obturado con lesión periapical."
        ],
        explicacion="El diagnóstico pulpar es «Diente previamente tratado» porque los conductos radiculares ya contienen material de obturación endodóntica; el diagnóstico periapical es «Periodontitis apical sintomática» debido al dolor manifiesto ante las fuerzas de impacto oclusal y la percusión vertical. En las líneas mil cuatrocientos sesenta y uno a mil seiscientos veintiuno, el profesor explicó la evolución postendodóntica: las lesiones periapicales comienzan su proceso de cicatrización y reducción ósea a partir del tercer mes postratamiento; si tras cuatro años persiste la radiolucidez y hay dolor asociado a una subobturación o desadaptación del sellado, se diagnostica fracaso endodóntico y la primera opción de manejo es el retratamiento endodóntico no quirúrgico (desobturar, desinfectar químicamente y reobturar); si existiera una sobreobturación grosera con cuerpo extraño inaccesible o fracasara el retratamiento, se evalúa la cirugía periapical con apicectomía y obturación retrógrada.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Diagnóstico en retratamiento: diente previamente tratado",
        que="Formular el diagnóstico en un diente obturado con fracaso periapical y definir los criterios de retratamiento o cirugía.",
        clave="Diente con gutapercha previa y dolor periapical es diente previamente tratado con periodontitis sintomática; se indica retratamiento o cirugía.",
        pistas=[
            "Verifica que en la radiografía ya hay material de obturación en las raíces (endodoncia terminada en el pasado).",
            "Ten en cuenta los tiempos de cicatrización enseñados por el profesor: la lesión ósea debe comenzar a sanar desde el tercer mes."
        ],
        plan=[
            "Asignar la categoría pulpar de diente previamente tratado por presencia de gutapercha.",
            "Establecer el diagnóstico periapical de periodontitis apical sintomática por dolor oclusal.",
            "Indicar el retratamiento endodóntico como primera línea, considerando cirugía ante sobreobturación refractaria."
        ],
        marcas_data=[
            ("conductos radiculares fueron obturados con gutapercha hace cuatro años", "clave", "Endodoncia previa terminada", "Apunta a diente previamente tratado"),
            ("obturación desadaptada y corta con una radiolucidez periapical persistente", "dato", "Falla biomecánica de sellado", "Apunta a persistencia de infección bacteriana"),
            ("¿cuál es el diagnóstico integral y el manejo clínico?", "pide", "Diagnóstico integral y manejo", "Demanda integrar diagnóstico pulpar/periapical y pauta de retratamiento")
        ],
        steps_ideas=[
            ("idea", "Clasificación en retratamiento", "Al tener material de obturación en las raíces, clasifica como diente previamente tratado."),
            ("idea", "Tiempos de cicatrización", "El docente explicó que el periápice debe cicatrizar desde el tercer mes; a los cuatro años con lesión es fracaso."),
            ("idea", "Retratamiento vs cirugía", "La conducta es desobturar y rehacer la endodoncia; si hay sobreobturación irritativa que no cura, se hace cirugía."),
            ("check", "Comprobación clínica", "Confirmamos diente previamente tratado con periodontitis apical sintomática manejado con retratamiento.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este caso clínico sobre evaluación de tratamientos de conductos antiguos."),
            ("m:conductos radiculares fueron obturados con gutapercha hace cuatro años", "Observa que el diente ya tiene endodoncia terminada con gutapercha desde hace cuatro años."),
            ("m:obturación desadaptada y corta con una radiolucidez periapical persistente", "Sin embargo, el conducto quedó corto, la lesión ósea sigue ahí y el paciente tiene dolor al masticar."),
            ("leer", "El docente enseñó que las lesiones periapicales deben cicatrizar a partir del tercer mes; si tras años persiste, es un fracaso."),
            ("leer", "El diagnóstico es diente previamente tratado con periodontitis sintomática, y la conducta es el retratamiento (o cirugía si no responde).")
        ]
    ))

    # 31 (Key C = 2) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-031", nivel=2,
        enunciado="En la sección inicial de la historia clínica en endodoncia, el profesor profundiza sobre el motivo de consulta y enumera diversas causas por las que un paciente acude al especialista (líneas siete a once). ¿Cuál de las siguientes situaciones representa un motivo de consulta frecuente en endodoncia donde el paciente suele acudir completamente asintomático sin percibir dolor alguno?",
        opciones=[
            "Dolor insoportable continuo que se incrementa violentamente en posición decúbito por las noches al acostarse.",
            "Dolor pulsátil agudo a la masticación con tumefacción facial difusa y trismus severo que deforma el ángulo mandibular.",
            "Hallazgo radiográfico incidental de una lesión periapical durante un chequeo de rutina, o remisión preprotésica antes de tallar una corona.",
            "Dolor urente difuso provocado por alimentos dulces que no cede con analgésicos narcóticos sistémicos."
        ],
        correcta=2,
        distractores=[
            "El dolor nocturno continuo es un motivo de consulta agudo muy sintomático propio de la pulpitis irreversible.",
            "La tumefacción facial con trismus y dolor masticatorio corresponde a un absceso agudo doloroso que no pasa desapercibido.",
            "",
            "El dolor urente que no cede con analgésicos representa un cuadro inflamatorio sintomático florido, no una consulta asintomática."
        ],
        explicacion="El profesor explicó que el motivo de consulta debe anotarse entre comillas con las palabras textuales del paciente, y no siempre involucra dolor. Un motivo de consulta muy frecuente en endodoncia es el hallazgo radiográfico de rutina donde el paciente acude completamente asintomático («el doctor me vio una mancha negra en la radiografía»), el cambio de coloración estética de un diente tras un trauma antiguo («se me puso el diente oscuro»), o la remisión de rehabilitación oral para tratamiento de conductos previo a la colocación de un perno o corona.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Historia clínica: motivos de consulta asintomáticos en endodoncia",
        que="Reconocer los motivos de consulta asintomáticos frecuentes en endodoncia como hallazgos radiográficos o remisiones preprotésicas.",
        clave="El hallazgo radiográfico incidental y la remisión preprotésica son motivos de consulta frecuentes donde el paciente está asintomático.",
        pistas=[
            "Recuerda la advertencia del docente: no todos los pacientes llegan a la consulta con dolor de muelas.",
            "Ten en cuenta las remisiones de rehabilitación o los descubrimientos fortuitos en radiografías de rutina."
        ],
        plan=[
            "Comprender la variedad de motivos de consulta en la práctica endodóntica.",
            "Identificar las situaciones clínicas silentes donde la patología periapical es asintomática.",
            "Reconocer las indicaciones de tratamiento de conductos con fines protésicos."
        ],
        marcas_data=[
            ("motivo de consulta frecuente en endodoncia donde el paciente suele acudir completamente asintomático", "clave", "Consulta endodóntica asintomática", "Apunta a hallazgo incidental o fin preprotésico"),
            ("profesor profundiza sobre el motivo de consulta y enumera diversas causas", "pide", "Pregunta de anamnesis clínica", "Demanda seleccionar el escenario asintomático de la clase")
        ],
        steps_ideas=[
            ("idea", "Motivo de consulta", "El paciente no siempre llega con dolor; muchas veces llega remitido o por hallazgo casual."),
            ("idea", "Lesiones silentes", "Una necrosis con periodontitis apical asintomática puede pasar años sin dar síntomas."),
            ("idea", "Fin protésico", "En rehabilitación se requiere endodoncia previa para colocar pernos o retenedores intrarradiculares."),
            ("check", "Comprobación clínica", "Confirmamos hallazgo radiográfico incidental y remisión preprotésica como motivos asintomáticos.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos este aspecto de la historia clínica enseñado por el profesor en las primeras líneas de la clase."),
            ("m:motivo de consulta frecuente en endodoncia donde el paciente suele acudir completamente asintomático", "Observa que la pregunta indaga por una consulta en la cual el paciente no siente dolor."),
            ("leer", "El docente explicó que muchos pacientes llegan diciendo «yo no siento nada, pero mi odontólogo me vio una mancha»."),
            ("leer", "Otro motivo frecuente es la remisión de prótesis para hacer endodoncia antes de tallar una corona o perno."),
            ("leer", "Por lo tanto, la opción que describe el hallazgo radiográfico incidental y la remisión preprotésica es la correcta.")
        ]
    ))

    # 32 (Key D = 3) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-032", nivel=2,
        enunciado="Al indagar sobre la enfermedad o problema actual del paciente con dolor dental, el profesor enumera ocho datos esenciales que deben registrarse minuciosamente en la anamnesis (líneas trece a cuarenta y dos). ¿Cuáles son estos ocho parámetros semiológicos que permiten caracterizar con exactitud el dolor del paciente?",
        opciones=[
            "Nombre del paciente, documento de identidad, número de teléfono, ocupación, estado civil, estrato socioeconómico y tipo de afiliación al seguro.",
            "Marca del cepillo dental utilizado, número de limpiezas al año, tipo de enjuague bucal y presencia de manchas de café en los dientes.",
            "Calibre de la aguja de anestesia, marca del dique de goma, tipo de lámpara de fotocurado y fecha de vencimiento del ionómero.",
            "Momento de inicio, localización anatómica, intensidad en escala analógica de cero a diez, duración del episodio, frecuencia, estímulos desencadenantes, factores que lo alivian y espontaneidad o nocturnidad."
        ],
        correcta=3,
        distractores=[
            "Estos datos corresponden a la ficha de filiación o datos demográficos generales, no al análisis semiológico del dolor actual.",
            "Los hábitos de higiene oral pertenecen al examen de prevención y antecedentes odontológicos, no a los parámetros del dolor agudo.",
            "Los materiales y calibres corresponden al inventario clínico o protocolo de procedimiento, no a la anamnesis del paciente.",
            ""
        ],
        explicacion="En las líneas trece a cuarenta y dos del texto fuente, el profesor detalló con gran precisión los ocho parámetros semiológicos que componen la descripción del problema actual en endodoncia: 1) Inicio o cronología (¿cuándo comenzó?), 2) Localización (¿dónde duele?), 3) Intensidad cuantitativa (escala analógica visual de cero a diez), 4) Duración (¿cuánto tiempo dura cuando aparece?), 5) Frecuencia (¿cuántas veces al día o semana?), 6) Factores desencadenantes (¿con qué le da: frío, calor, dulce, masticación?), 7) Factores de alivio (¿con qué se le calma?), y 8) Espontaneidad y decúbito (¿le da solo sin estímulo, le duele al acostarse por las noches?).",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Historia clínica: los ocho datos esenciales del problema actual",
        que="Identificar los ocho parámetros semiológicos cardinales para el análisis del dolor dental en la anamnesis.",
        clave="Los ocho datos del problema actual son inicio, localización, intensidad (cero a diez), duración, frecuencia, estímulos, alivio y espontaneidad.",
        pistas=[
            "Recuerda la lista metódica que el docente hizo en el tablero para interrogar el dolor del paciente.",
            "Ten en cuenta los elementos esenciales: intensidad de cero a diez, qué lo despierta, qué lo calma y cuánto dura."
        ],
        plan=[
            "Revisar el protocolo sistemático de interrogatorio del dolor en la historia clínica.",
            "Identificar los ocho parámetros clínicos cuantitativos y cualitativos del síntoma.",
            "Diferenciar los datos del dolor frente a la información demográfica o de filiación."
        ],
        marcas_data=[
            ("profesor enumera ocho datos esenciales que deben registrarse minuciosamente en la anamnesis", "clave", "Los ocho parámetros del dolor", "Apunta a metodología de interrogatorio de la enfermedad actual"),
            ("¿Cuáles son estos ocho parámetros semiológicos que permiten caracterizar con exactitud el dolor del paciente?", "pide", "Lista de parámetros", "Demanda identificar la lista completa de inicio a nocturnidad")
        ],
        steps_ideas=[
            ("idea", "Interrogatorio sistemático", "El profesor enseñó que no basta con decir 'le duele la muela': hay que caracterizar ocho aspectos."),
            ("idea", "Parámetros del dolor", "Inicio, sitio, escala cero a diez, duración, frecuencia, qué lo causa, qué lo calma y si da en la noche."),
            ("check", "Comprobación clínica", "Confirmamos los ocho parámetros semiológicos cardinales del problema actual.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos con cuidado esta enseñanza metodológica del docente sobre la historia clínica."),
            ("m:profesor enumera ocho datos esenciales que deben registrarse minuciosamente en la anamnesis", "Observa que el docente exige anotar ocho datos indispensables para entender el dolor del paciente."),
            ("leer", "El docente explicó: cuándo empezó, dónde le duele, de cero a diez cuánto le duele y cuánto le dura el dolor."),
            ("leer", "Además: cada cuánto le da, con qué le da (frío, calor), con qué se le calma y si le duele solo en la noche."),
            ("leer", "Por lo tanto, la opción que recopila estos ocho parámetros semiológicos exactos es la correcta.")
        ]
    ))

    # 33 (Key A = 0) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-033", nivel=2,
        enunciado="Un paciente asiste manifestando que al comer chocolates o postres dulces siente una punzada aguda y breve en un molar, la cual se detiene por completo tan pronto como se enjuaga la boca con agua tibia. No hay dolor espontáneo. De acuerdo con la regla clínica explícita enseñada por el profesor (líneas trescientos doce a trescientos catorce), ¿a qué diagnóstico apunta este signo específico y cuál es su causa biofísica?",
        opciones=[
            "Pulpitis reversible; el docente enseñó que «dolor con dulce es pulpitis reversible», originado por la tracción osmótica que deshidrata los túbulos dentinarios expuestos estimulando fibras A-delta.",
            "Necrosis pulpar séptica; las bacterias sacarolíticas metabolizan el azúcar dentro del foramen apical liberando toxinas que destruyen el periápice.",
            "Periodontitis apical aguda; el azúcar penetra en el ligamento periodontal provocando reabsorción ósea externa inmediata.",
            "Angina de Ludwig incipiente; la ingesta de sacarosa produce vasodilatación masiva de los vasos submandibulares con compromiso de la vía aérea."
        ],
        correcta=0,
        distractores=[
            "",
            "La necrosis pulpar cursa con muerte del tejido sensorial y no responde a estímulos osmóticos breves de dulce en esmalte.",
            "El azúcar en la boca no penetra físicamente al ligamento periodontal profundo para causar reabsorción ósea inmediata.",
            "La Angina de Ludwig es una celulitis facial infecciosa grave diseminada en cuello, no un dolor dental breve provocado por dulce."
        ],
        explicacion="En las líneas trescientos doce a trescientos catorce, el profesor compartió una de sus reglas mnemotécnicas más contundentes: «dolor con dulce es igual a pulpitis reversible». El mecanismo biofísico se explica por la teoría hidrodinámica de Brännström: la alta concentración de azúcar genera un gradiente osmótico rápido que extrae fluido del interior de los túbulos dentinarios desprotegidos hacia el medio bucal; ese movimiento violento de fluido deforma físicamente los odontoblastos y estimula las terminaciones nerviosas de las fibras A-delta mielínicas periféricas, produciendo un dolor breve que cesa al lavarse la boca y no requiere endodoncia si se sella la dentina.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Diagnóstico pulpar: dolor con dulce y pulpitis reversible",
        que="Reconocer el dolor con dulce como signo cardinal de pulpitis reversible y comprender su base osmótica hidrodinámica.",
        clave="La regla clínica del profesor establece que «dolor con dulce es igual a pulpitis reversible» por gradiente osmótico en túbulos dentinarios.",
        pistas=[
            "Recuerda la frase textual del docente en clase sobre qué significa cuando el dolor aparece al comer chocolates o postres.",
            "Ten en cuenta que el dolor cesa de inmediato al enjuagar el dulce (respuesta reversible provocada)."
        ],
        plan=[
            "Identificar el desencadenante osmótico dulce como estímulo reversible característico.",
            "Aplicar la regla mnemotécnica enseñada por el profesor en clase.",
            "Comprender el mecanismo hidrodinámico de deformación tubular sobre fibras A-delta."
        ],
        marcas_data=[
            ("al comer chocolates o postres dulces siente una punzada aguda y breve en un molar, la cual se detiene por completo tan pronto como se enjuaga", "clave", "Dolor osmótico provocado reversible", "Apunta a gradiente osmótico sobre túbulos expuestos"),
            ("regla clínica explícita enseñada por el profesor (líneas trescientos doce a trescientos catorce)", "dato", "Referencia a la regla del profesor", "Apunta a «dolor con dulce = pulpitis reversible»"),
            ("¿a qué diagnóstico apunta este signo específico y cuál es su causa biofísica?", "pide", "Diagnóstico y causa biofísica", "Demanda formular pulpitis reversible y mecanismo hidrodinámico")
        ],
        steps_ideas=[
            ("idea", "Regla del profesor", "El profesor fue categórico: 'dolor con dulce es pulpitis reversible'."),
            ("idea", "Mecanismo osmótico", "El azúcar deshidrata y jala el fluido de los túbulos dentinarios estimulando las fibras A-delta."),
            ("idea", "Cese con lavado", "Al enjuagarse con agua, el dulce se lava, el fluido se estabiliza y el dolor desaparece de inmediato."),
            ("check", "Comprobación clínica", "Confirmamos pulpitis reversible originada por tracción osmótica en túbulos dentinarios.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención esta regla práctica que el docente enseñó para el examen parcial."),
            ("m:al comer chocolates o postres dulces siente una punzada aguda y breve en un molar, la cual se detiene por completo tan pronto como se enjuaga", "Observa este detalle característico: el dolor da con chocolates o dulce y se quita al lavarse la boca."),
            ("leer", "El docente repitió en clase una regla de oro: «dolor con dulce es igual a pulpitis reversible»."),
            ("leer", "La base biológica es que el azúcar crea un gradiente osmótico que jala el líquido de los túbulos dentinarios."),
            ("leer", "Por lo tanto, la pulpa está viva y reversible, requiriendo únicamente proteger y sellar la dentina.")
        ]
    ))

    # 34 (Key B = 1) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-034", nivel=2,
        enunciado="Durante el examen extraoral de una paciente que consulta por una lesión supurativa en la piel del mentón que no cicatriza tras múltiples tratamientos dermatológicos, el odontólogo sospecha un origen odontogénico. Al revisar la arcada inferior encuentra el incisivo central con caries profunda y prueba de frío negativa. ¿Cuál es el mecanismo fisiopatológico explicado por el docente (líneas sesenta y cuatro a noventa y dos) sobre las fístulas cutáneas extraorales?",
        opciones=[
            "La infección pulpar viaja exclusivamente por los conductos linfáticos parotídeos hacia la epidermis sin perforar el hueso mandibular.",
            "El pus busca la vía de menor resistencia ósea: si el ápice se encuentra por debajo de la inserción muscular del mentoniano, el trayecto perfora la cortical hacia la piel originando una fístula extraoral.",
            "Las fístulas extraorales son de origen vírico por herpes zóster y no guardan ninguna relación con la necrosis de los dientes vecinos.",
            "El exudado purulento se genera en la saliva y migra a través de los poros de la piel sin comprometer el tejido periapical."
        ],
        correcta=1,
        distractores=[
            "Los vasos linfáticos parotídeos drenan la región lateral superior, no explican trayectos fistulosos directos en el mentón óseo.",
            "",
            "Las fístulas odontogénicas son de etiología bacteriana purulenta por necrosis pulpar periapical, no por reactivación herpética.",
            "La saliva no atraviesa los poros cutáneos para formar fístulas purulentas crónicas en el mentón."
        ],
        explicacion="En las líneas sesenta y cuatro a noventa y dos del texto, el profesor explicó por qué es obligatorio inspeccionar tanto la cara externa como la cavidad oral en busca de fístulas. El exudado purulento de un absceso periapical por necrosis destruye el hueso trabecular buscando el camino de menor resistencia anatómica. Si el ápice radicular del diente causal se sitúa por debajo de las inserciones musculares faciales (como el músculo mentoniano en incisivos inferiores o el buccinador en molares), la fístula no drena en el fondo de surco intraoral sino que drena hacia la piel externa de la cara o el cuello, confundiéndose con lesiones dermatológicas hasta que se realiza la endodoncia del diente causal.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Examen clínico: fístulas extraorales de origen odontogénico",
        que="Explicar el trayecto de las fístulas cutáneas extraorales en relación con las inserciones musculares anatómicas.",
        clave="El pus busca menor resistencia; si el ápice está más allá de la inserción muscular (mentoniano/buccinador) drena a la piel de la cara.",
        pistas=[
            "Recuerda la explicación anatómica del profesor sobre la relación entre el ápice del diente y la inserción de los músculos faciales.",
            "Ten en cuenta que el pus busca la vía de menor resistencia ósea y perfora hacia afuera si la raíz sobrepasa el músculo."
        ],
        plan=[
            "Analizar la anatomía topográfica de los ápices radiculares respecto a los músculos faciales.",
            "Comprender el mecanismo de drenaje óseo por la vía de menor resistencia anatómica.",
            "Relacionar la lesión cutánea refractaria con la necrosis pulpar del diente causal."
        ],
        marcas_data=[
            ("lesión supurativa en la piel del mentón que no cicatriza tras múltiples tratamientos dermatológicos", "dato", "Fístula extraoral crónica", "Apunta a sospecha de patología periapical oculta"),
            ("incisivo central con caries profunda y prueba de frío negativa", "clave", "Diente causal desvitalizado", "Apunta a necrosis pulpar como origen bacteriano"),
            ("¿Cuál es el mecanismo fisiopatológico explicado por el docente (líneas sesenta y cuatro a noventa y dos) sobre las fístulas cutáneas extraorales?", "pide", "Mecanismo anatómico y fisiopatológico", "Demanda fundamentar la relación con la inserción muscular")
        ],
        steps_ideas=[
            ("idea", "Fístula en piel", "Muchas lesiones cutáneas en barbilla o cuello son fístulas dentales que los médicos confunden con problemas de piel."),
            ("idea", "Inserción muscular", "El docente explicó que si la raíz termina por debajo de la inserción del músculo, el pus sale hacia la piel."),
            ("idea", "Vía de menor resistencia", "El pus no sube al fondo de surco si el músculo le cierra el paso; perfora la cortical hacia afuera."),
            ("check", "Comprobación anatómica", "Confirmamos que el pus drena a la piel si el ápice se ubica más allá de la inserción muscular.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos con cuidado este motivo de consulta interdisciplinario entre dermatología y endodoncia."),
            ("m:lesión supurativa en la piel del mentón que no cicatriza tras múltiples tratamientos dermatológicos", "Observa que la paciente tiene un granito con pus en la barbilla que ningún tratamiento de piel ha curado."),
            ("m:incisivo central con caries profunda y prueba de frío negativa", "Al revisar la boca, el odontólogo encuentra que el incisivo central inferior tiene la pulpa muerta."),
            ("leer", "El docente explicó en clase por qué la fístula sale en la piel de la cara: el pus busca la menor resistencia ósea."),
            ("leer", "Como el ápice del incisivo está por debajo del músculo mentoniano, el drenaje se desvía hacia la piel del mentón.")
        ]
    ))

    # 35 (Key C = 2) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-035", nivel=2,
        enunciado="El profesor detalla la «tríada de la prueba de frío» y la conducta clínica asociada a cada resultado (líneas ciento veintiséis a ciento cuarenta y tres). ¿Cuál de las siguientes asociaciones resume de manera integral esta correlación diagnóstica y terapéutica enseñada en clase?",
        opciones=[
            "Dolor ausente = pulpa sana (conducta preventiva); dolor que cesa en dos segundos = endodoncia obligatoria; dolor de más de treinta segundos = profilaxis dental.",
            "Dolor que perdura minutos = tratamiento conservador con resina; dolor que cesa rápido = biopulpectomía de urgencia; dolor ausente = colocación de corona.",
            "Dolor que cesa en uno o dos segundos = pulpa sana o reversible (conducta conservadora); dolor que perdura más de treinta segundos = pulpitis irreversible (endodoncia); sin respuesta = necrosis (desinfección intraconducto).",
            "Toda respuesta al frío exige la prescripción de antibióticos por vía oral durante siete días independientemente de la duración."
        ],
        correcta=2,
        distractores=[
            "La ausencia de dolor traduce necrosis y no salud pulpar; un dolor que cesa en dos segundos jamás requiere endodoncia.",
            "Invertir la conducta realizando endodoncia al dolor rápido y resina al dolor prolongado constituye una negligencia diagnóstica.",
            "",
            "Las pruebas de frío evalúan la respuesta pulpar y no determinan el uso indiscriminado de antibióticos sistémicos."
        ],
        explicacion="En las líneas ciento veintiséis a ciento cuarenta y tres del texto fuente, el docente sintetizó la tríada clínica de la prueba térmica con frío en tres escenarios cardinales: 1) El paciente siente frío o molestia leve que desaparece en uno a dos segundos tras retirar el algodón: pulpa sana o con pulpitis reversible, cuya conducta es conservadora (mantener o proteger con ionómero sin endodoncia); 2) El paciente experimenta dolor severo que permanece por más de treinta segundos tras retirar el estímulo: pulpitis irreversible sintomática, cuya conducta obligatoria es la endodoncia (biopulpectomía); 3) El paciente no percibe ninguna sensación térmica en absoluto: necrosis pulpar, cuya conducta es el tratamiento de conductos enfocado en la desinfección química y biomecánica bacteriana.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Semiología pulpar: tríada diagnóstica del frío y conducta",
        que="Integrar la tríada diagnóstica de la prueba de frío con la conducta terapéutica conservadora o invasiva.",
        clave="La tríada del frío establece: cede en dos segundos es sana/reversible, persiste más de treinta segundos es irreversible (endodoncia), y no siente es necrosis.",
        pistas=[
            "Recuerda el esquema de tres salidas que el profesor enseñó para tomar decisiones en el sillón dental.",
            "Asocia el tiempo de dolor: dos segundos es conservador, treinta segundos es endodoncia, nada es necrosis."
        ],
        plan=[
            "Categorizar las tres respuestas posibles ante la aplicación de frío en la superficie dental.",
            "Vincular el tiempo de persistencia del dolor con la capacidad biológica de recuperación pulpar.",
            "Definir la conducta terapéutica adecuada para cada uno de los tres estados pulpares."
        ],
        marcas_data=[
            ("«tríada de la prueba de frío» y la conducta clínica asociada a cada resultado", "clave", "Tríada diagnóstica y terapéutica", "Demanda correlacionar tiempo de respuesta con tratamiento"),
            ("¿Cuál de las siguientes asociaciones resume de manera integral esta correlación diagnóstica y terapéutica", "pide", "Asociación completa", "Demanda seleccionar la tríada exacta enseñada en clase")
        ],
        steps_ideas=[
            ("idea", "Respuesta breve", "Dolor que se va en uno o dos segundos indica pulpa sana o reversible; se cuida y no se hace endodoncia."),
            ("idea", "Respuesta prolongada", "Dolor que sigue doliendo más de treinta segundos indica pulpitis irreversible; requiere endodoncia."),
            ("idea", "Sin respuesta", "Si no siente nada en absoluto la pulpa está necrótica; requiere desinfección del conducto."),
            ("check", "Comprobación clínica", "Confirmamos la tríada del frío y sus tres conductas clínicas correspondientes.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta tríada de decisiones clínicas que el docente enseñó para resolver cualquier caso en consulta."),
            ("m:«tríada de la prueba de frío» y la conducta clínica asociada a cada resultado", "Fíjate en las tres posibilidades de tiempo al aplicar el frío con el algodón."),
            ("leer", "Si el paciente siente frío pero se le pasa en uno o dos segundos: pulpa sana o reversible (tratamiento conservador)."),
            ("leer", "Si el dolor se queda pegado doliendo por más de treinta segundos: pulpitis irreversible (hacer endodoncia)."),
            ("leer", "Si el paciente no siente absolutamente nada de frío: necrosis pulpar (hacer conductos con desinfección).")
        ]
    ))

    # 36 (Key D = 3) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-036", nivel=3,
        enunciado="Respecto a la prueba térmica con calor en endodoncia, el profesor explica que actualmente se usa poco debido a sus riesgos biológicos, detallando el protocolo con barra de gutapercha caliente y vaselina (líneas ciento sesenta y cuatro a ciento setenta y ocho, y dos mil cuatrocientos quince a dos mil cuatrocientos veintidós). ¿Qué riesgo biológico existe si no se controla la temperatura y qué indica el dolor severo al calor que se calma con frío?",
        opciones=[
            "Si la temperatura sube más de un grado se fractura el esmalte dental; el dolor al calor indica que el paciente padece bruxismo nocturno severo.",
            "El calor genera calcificación pulpar acelerada en segundos; la calma con frío traduce presencia de caries en esmalte superficial.",
            "La gutapercha caliente disuelve la amalgama palatina; el alivio con frío traduce presencia de una corona desadaptada sin inflamación.",
            "Si la temperatura intrapulpar se incrementa más de cinco grados centígrados se induce necrosis irreversible; y el dolor provocado por calor que se alivia con frío traduce necrosis pulpar en curso con gasificación."
        ],
        correcta=3,
        distractores=[
            "El esmalte soporta cambios térmicos moderados sin fracturarse; el dolor al calor no diagnostica bruxismo.",
            "La calcificación pulpar es un proceso celular que tarda meses o años y no ocurre en segundos durante una prueba térmica.",
            "La gutapercha no disuelve amalgamas dentales metálicas y la calma con frío no se relaciona con desadaptación coronaria simple.",
            ""
        ],
        explicacion="El docente destacó dos principios biológicos sobre la prueba de calor: 1) Siempre se debe aplicar una capa fina de vaselina sobre el esmalte para evitar que la gutapercha caliente se adhiera y queme el diente, teniendo presente que un incremento de apenas cinco grados centígrados en la temperatura intrapulpar es suficiente para producir daño vascular irreversible y necrosis térmica del tejido pulpar; 2) Cuando un paciente relata que los alimentos calientes desencadenan un dolor pulsátil lacerante pero que se alivia temporalmente al beber agua fría, indica un estadio de necrosis pulpar con licuefacción donde los gases acumulados se expanden con el calor y se contraen con el frío.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Semiología pulpar: prueba térmica de calor y umbral térmico",
        que="Reconocer el riesgo de lesión térmica por encima de cinco grados y asociar el dolor al calor con necrosis en gasificación.",
        clave="El calor que sube más de cinco grados necrosa la pulpa; el dolor provocado por calor que se calma con frío indica necrosis en marcha con gases.",
        pistas=[
            "Recuerda la cifra de aumento de temperatura en grados que el profesor advirtió como peligrosa para la pulpa.",
            "Ten en cuenta qué fenómeno físico ocurre cuando el calor despierta dolor y el frío lo apaga en una cámara cerrada."
        ],
        plan=[
            "Comprender el protocolo de protección con vaselina y gutapercha tibia.",
            "Evaluar el umbral biológico crítico de elevación térmica intrapulpar de cinco grados centígrados.",
            "Interpretar la biofísica del dolor inducido por calor y calmado por frío como descomposición gaseosa."
        ],
        marcas_data=[
            ("detallando el protocolo con barra de gutapercha caliente y vaselina", "dato", "Protocolo de prueba de calor", "Apunta a protección con vaselina sobre esmalte"),
            ("¿Qué riesgo biológico existe si no se controla la temperatura y qué indica el dolor severo al calor que se calma con frío?", "clave", "Riesgo térmico y signo clínico", "Demanda identificar el aumento de cinco grados y la necrosis con gases")
        ],
        steps_ideas=[
            ("idea", "Riesgo de cinco grados", "El profesor advirtió que subir apenas cinco grados centígrados la temperatura dentro del diente puede matar la pulpa."),
            ("idea", "Protección con vaselina", "Se coloca vaselina previa para que la gutapercha no se pegue ni transmita calor descontrolado."),
            ("idea", "Dolor al calor y calma con frío", "Si el café caliente duele y el agua fría lo calma, hay descomposición y gasificación de la pulpa."),
            ("check", "Comprobación biológica", "Confirmamos el riesgo de cinco grados de aumento y la necrosis con gasificación ante dolor al calor.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta advertencia biológica que el profesor dio sobre las pruebas térmicas con calor."),
            ("m:detallando el protocolo con barra de gutapercha caliente y vaselina", "Observa que hoy en día casi no se hace prueba de calor porque puede dañar la pulpa si no se cuida."),
            ("leer", "El docente enseñó que con solo subir cinco grados la temperatura interna de la pulpa, los vasos se queman y el tejido se muere."),
            ("leer", "Por eso se usa vaselina para proteger el diente y no dejar la gutapercha pegada."),
            ("leer", "Además, el docente destacó que si el calor desata el dolor y el frío lo calma, la pulpa se está pudriendo con gases acumulados.")
        ]
    ))

    # 37 (Key A = 0) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-037", nivel=2,
        enunciado="Al discutir las pruebas pulpares eléctricas mediante el vitalómetro, el docente aclara qué mide realmente este instrumento en la fisiología pulpar (líneas ciento ochenta a ciento ochenta y siete). ¿Cuál es la interpretación clínica exacta de la prueba eléctrica pulpar?",
        opciones=[
            "Mide exclusivamente la respuesta sensorial y excitabilidad de las fibras nerviosas mielínicas intrapulpares, pero no determina la vitalidad vascular ni el flujo sanguíneo del tejido.",
            "Muestra de forma cuantitativa el porcentaje exacto de necrosis bacteriana existente en el conducto radicular mediante una escala numérica.",
            "Sustituye a las radiografías periapicales porque detecta con precisión matemática si existe una lesión ósea en el periápice.",
            "Evalúa el tono muscular del ligamento periodontal y determina si el diente requiere ajuste oclusal inmediato."
        ],
        correcta=0,
        distractores=[
            "",
            "El vitalómetro produce un estímulo eléctrico graduado, pero sus números no indican porcentajes de bacterias ni de tejido necrótico.",
            "La prueba eléctrica no interactúa con el tejido óseo periapical y jamás sustituye al examen radiográfico.",
            "El ligamento periodontal contiene mecanorreceptores periodontales que no son evaluados por la corriente coronal del vitalómetro."
        ],
        explicacion="En las líneas ciento ochenta a ciento ochenta y siete, el profesor enfatizó que el vitalómetro o prueba eléctrica es una prueba exclusivamente neurosensorial. El paso de la corriente a través del esmalte despolariza las fibras A-delta provocando una sensación de cosquilleo o punzada breve. Sin embargo, la verdadera vitalidad pulpar es de naturaleza vascular (presencia de perfusión sanguínea y microcirculación intacta). Por ello, un diente puede tener flujo sanguíneo comprometido y dar respuesta nerviosa sensorial residual, o viceversa, tener pulpa vital con cámara calcificada y dar una lectura negativa al vitalómetro.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Semiología pulpar: límites del vitalómetro eléctrico",
        que="Diferenciar la respuesta sensorial nerviosa del vitalómetro frente a la verdadera vitalidad vascular de la pulpa.",
        clave="El vitalómetro solo evalúa la excitabilidad nerviosa sensorial de fibras A-delta, no la perfusión sanguínea ni la vascularización pulpar.",
        pistas=[
            "Recuerda que la verdadera vitalidad de un tejido depende de su sangre y vasos, no solo de sus nervios.",
            "Ten presente la distinción hecha por el profesor: el vitalómetro mide conducción nerviosa, no salud vascular."
        ],
        plan=[
            "Comprender el mecanismo bioeléctrico de estimulación del vitalómetro sobre las fibras A-delta.",
            "Distinguir el concepto de sensibilidad nerviosa frente a vitalidad microvascular.",
            "Reconocer las limitaciones diagnósticas de los vitalómetros en dientes con trauma o calcificación."
        ],
        marcas_data=[
            ("docente aclara qué mide realmente este instrumento en la fisiología pulpar", "clave", "Objeto de evaluación del vitalómetro", "Apunta a respuesta sensorial nerviosa y no vascular"),
            ("¿Cuál es la interpretación clínica exacta de la prueba eléctrica pulpar?", "pide", "Interpretación fisiológica", "Demanda diferenciar inervación sensorial de perfusión sanguínea")
        ],
        steps_ideas=[
            ("idea", "Respuesta neurosensorial", "La corriente eléctrica estimula las fibras nerviosas A-delta produciendo cosquilleo o dolor breve."),
            ("idea", "Vitalidad vascular", "El profesor aclaró que vitalidad es sangre circulando; el vitalómetro no mide si hay flujo sanguíneo."),
            ("idea", "Falsos diagnósticos", "Un diente puede estar perdiendo riego sanguíneo y todavía responder a la electricidad."),
            ("check", "Comprobación clínica", "Confirmamos que el vitalómetro evalúa respuesta nerviosa sensorial pero no el flujo vascular.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta aclaración fisiológica fundamental explicada por el profesor sobre el vitalómetro."),
            ("m:docente aclara qué mide realmente este instrumento en la fisiología pulpar", "Observa qué mide el aparato cuando le ponemos corriente eléctrica al diente."),
            ("leer", "El docente explicó que la electricidad solo estimula a los nervios para ver si transmiten un cosquilleo."),
            ("leer", "Pero la verdadera vida de la pulpa depende de sus vasos sanguíneos y de su circulación."),
            ("leer", "Por lo tanto, la prueba eléctrica solo mide respuesta sensorial nerviosa y no puede medir el flujo sanguíneo.")
        ]
    ))

    # 38 (Key B = 1) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-038", nivel=3,
        enunciado="Durante el examen periodontal aplicado a la endodoncia, el odontólogo introduce una sonda periodontal milimetrada alrededor de un diente desvitalizado. Encuentra un surco gingival de dos milímetros en casi toda la circunferencia, excepto en un punto vestibular estrecho y aislado donde la sonda se profundiza bruscamente hasta nueve milímetros cerca del ápice. De acuerdo con lo enseñado en clase (líneas doscientas veinticuatro a doscientas treinta y siete), ¿qué patología debe sospecharse ante esta bolsa periodontal estrecha y solitaria?",
        opciones=[
            "Periodontitis marginal crónica generalizada por placa bacteriana y sarro subgingival difuso en toda la arcada.",
            "Drenaje de una fístula intrasulcular de origen periapical o una fractura radicular vertical incompleta en ese plano radicular.",
            "Gingivitis descamativa autoinmune asociada a estrés psicológico sin afección del tejido dentario ni periodontal de soporte.",
            "Abrasión por cepillado dental con exfoliación fisiológica acelerada de la raíz en dientes adultos mayores."
        ],
        correcta=1,
        distractores=[
            "Una periodontitis marginal cursa con bolsas anchas en múltiples dientes y superficies, no con un defecto estrecho aislado en un solo punto.",
            "",
            "La gingivitis descamativa afecta a la superficie del epitelio gingival sin formar bolsas estrechas profundas de nueve milímetros al ápice.",
            "El cepillado traumático provoca recesión gingival y pérdida de cuellos en esmalte, no una bolsa estrecha profunda intraligamentosa."
        ],
        explicacion="En las líneas doscientas veinticuatro a doscientas treinta y siete, el docente enseñó a diferenciar el sondeo periodontal: una periodontitis periodontal pura presenta bolsas anchas en múltiples dientes y superficies; por el contrario, cuando un diente tiene encía adherida sana con sondeo normal de dos milímetros pero en un solo punto milimétrico la sonda penetra de forma profunda y vertical hasta el periápice, se trata de una bolsa periodontal estrecha de origen endodóntico (un trayecto fistuloso que drena por el ligamento periodontal hacia el surco gingival) o de una fractura radicular vertical que ha destruido la inserción ósea a lo largo de la línea de fisura.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Examen periodontal en endodoncia: bolsa periodontal estrecha",
        que="Identificar la bolsa periodontal estrecha aislada como signo de trayecto fistuloso intrasulcular o fractura vertical.",
        clave="Una bolsa periodontal estrecha profunda en un solo punto de un diente con surco sano orienta a fístula intrasulcular o fractura radicular.",
        pistas=[
            "Observa que el sondeo es de dos milímetros en toda la muela y solo en un puntito estrecho se hunde hasta nueve milímetros.",
            "Recuerda la enseñanza del profesor: una bolsa solitaria como una hendidura apunta a fístula por ligamento o fractura vertical."
        ],
        plan=[
            "Diferenciar las bolsas periodontales anchas generalizadas de las bolsas estrechas solitarias.",
            "Sospechar drenaje intrasulcular periapical en dientes con necrosis pulpar.",
            "Evaluar el riesgo de fractura radicular vertical longitudinal a lo largo del defecto óseo."
        ],
        marcas_data=[
            ("surco gingival de dos milímetros en casi toda la circunferencia, excepto en un punto vestibular estrecho y aislado donde la sonda se profundiza bruscamente hasta nueve milímetros", "clave", "Signo semiológico de bolsa estrecha solitaria", "Apunta a trayecto fistuloso por ligamento o fisura radicular"),
            ("¿qué patología debe sospecharse ante esta bolsa periodontal estrecha y solitaria?", "pide", "Sospecha diagnóstica", "Demanda identificar fístula intrasulcular o fractura vertical")
        ],
        steps_ideas=[
            ("idea", "Bolsa ancha vs estrecha", "La periodontitis da bolsas anchas en forma de copa; el problema endodóntico da una hendidura estrecha en un solo punto."),
            ("idea", "Fístula intrasulcular", "El pus del ápice puede buscar el ligamento periodontal y salir por la encía simulando una bolsa."),
            ("idea", "Fractura radicular", "Una fisura vertical en la raíz rompe el hueso exactamente en esa línea permitiendo que la sonda caiga."),
            ("check", "Comprobación clínica", "Confirmamos sospecha de fístula intrasulcular periapical o fractura radicular vertical.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos con atención este hallazgo del examen periodontal enseñado por el docente."),
            ("m:surco gingival de dos milímetros en casi toda la circunferencia, excepto en un punto vestibular estrecho y aislado donde la sonda se profundiza bruscamente hasta nueve milímetros", "Observa que la encía está sana en casi todo el contorno y solo en un punto milimétrico la sonda baja hasta nueve milímetros."),
            ("leer", "El docente enseñó que esto no es una periodontitis común, sino una bolsa estrecha aislada."),
            ("leer", "Este signo traduce que un absceso periapical está drenando por el ligamento (fístula intrasulcular), o que la raíz está partida verticalmente."),
            ("leer", "Por lo tanto, la opción que señala la fístula intrasulcular o fractura radicular es la correcta.")
        ]
    ))

    # 39 (Key C = 2) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-039", nivel=2,
        enunciado="En la lectura e interpretación radiográfica sistemática en endodoncia, el profesor enumera los elementos anatómicos perirradiculares que deben evaluarse metódicamente (líneas doscientos treinta y nueve a doscientos cuarenta y siete). ¿Cuál es la estructura radiopaca delgada y continua que rodea inmediatamente la raíz dentaria y qué traduce clínicamente su pérdida o discontinuidad en la zona apical?",
        opciones=[
            "El cemento radicular acelular; su pérdida traduce exfoliación dental fisiológica acelerada en pacientes adultos.",
            "La cámara pulpar cameral; su discontinuidad indica presencia de un pólipo pulpar benigno en la corona.",
            "La lámina dura (cortical alveolar cribiforme); su pérdida o ensanchamiento periapical traduce desmineralización ósea activa por proceso inflamatorio o infeccioso.",
            "La encía queratinizada vestibular; su ruptura indica fractura del esmalte dental en la corona clínica."
        ],
        correcta=2,
        distractores=[
            "El cemento radicular es una capa microscópica íntimamente adherida a la dentina radicular, no la cortical ósea alveolar visible.",
            "La cámara pulpar se encuentra dentro de la corona del diente, no rodeando el exterior de la raíz en el periápice.",
            "",
            "La encía queratinizada es un tejido blando que no se visualiza como línea radiopaca ósea en radiografías periapicales."
        ],
        explicacion="En las líneas doscientos treinta y nueve a doscientos cuarenta y siete, el docente explicó que en la radiografía periapical se debe observar minuciosamente la lámina dura (la fina línea blanca radiopaca que corresponde al hueso alveolar cortical que delimita el alvéolo) y el espacio radiolúcido uniforme del ligamento periodontal. La pérdida de continuidad, engrosamiento o reabsorción de la lámina dura en la zona periapical es el primer signo radiográfico de que los mediadores inflamatorios o toxinas bacterianas provenientes del conducto radicular están destruyendo activamente el hueso alveolar circundante.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Semiología radiográfica: análisis de la lámina dura",
        que="Identificar la lámina dura radiográfica y comprender el significado patológico de su pérdida de continuidad apical.",
        clave="La lámina dura es la línea radiopaca que bordea el alvéolo; su pérdida periapical es el primer signo de reabsorción ósea por infección.",
        pistas=[
            "Busca la línea delgada blanca que contornea la raíz por fuera del espacio negro del ligamento.",
            "Ten en cuenta que cuando las bacterias salen del ápice, lo primero que destruyen es esta cortical blanca."
        ],
        plan=[
            "Identificar las estructuras perirradiculares normales en la radiografía periapical.",
            "Reconocer la lámina dura como la cortical interna del alvéolo óseo.",
            "Interpretar la discontinuidad o rotura de la lámina dura como signo precoz de periodontitis apical."
        ],
        marcas_data=[
            ("estructura radiopaca delgada y continua que rodea inmediatamente la raíz dentaria", "clave", "Estructura anatómica radiográfica", "Apunta a lámina dura o cortical alveolar"),
            ("qué traduce clínicamente su pérdida o discontinuidad en la zona apical?", "pide", "Significado clínico patológico", "Demanda asociar la ruptura con desmineralización e inflamación ósea")
        ],
        steps_ideas=[
            ("idea", "Lámina dura", "Es la línea blanca radiopaca que dibuja el contorno del alvéolo óseo alrededor del diente."),
            ("idea", "Espacio del ligamento", "Entre la raíz y la lámina dura corre el espacio radiolúcido oscuro del ligamento periodontal."),
            ("idea", "Pérdida de continuidad", "Si la línea blanca se borra o se rompe en el ápice, el hueso se está desmineralizando por infección pulpar."),
            ("check", "Comprobación radiográfica", "Confirmamos la lámina dura y su reabsorción apical como signo de periodontitis activa.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta estructura anatómica esencial en la lectura de cualquier radiografía periapical."),
            ("m:estructura radiopaca delgada y continua que rodea inmediatamente la raíz dentaria", "Observa esa línea blanca finita y continua que rodea toda la raíz del diente en el hueso."),
            ("leer", "El docente enseñó que esa línea blanca se llama lámina dura o cortical alveolar."),
            ("leer", "Si las bacterias salen del conducto, los ácidos y mediadores inflamatorios la rompen y la borran."),
            ("leer", "Por lo tanto, la pérdida de la lámina dura en el ápice es el primer aviso de que hay una infección periapical activa.")
        ]
    ))

    # 40 (Key D = 3) - NUEVA CLASE 1
    qs.append(make_q(
        qid="odo-040", nivel=2,
        enunciado="El docente insiste con gran firmeza en que «la toma de la radiografía inicial periapical previa a cualquier instrumentación o tratamiento de conductos es obligatoria e intransigible, teniendo además un valor médico-legal determinante» (líneas cuatrocientos noventa y ocho a quinientos ocho). ¿Cuál de las siguientes razones clínicas y legales fundamenta esta exigencia antes de introducir cualquier instrumento en el conducto?",
        opciones=[
            "Permite facturar automáticamente el costo del dique de goma a la aseguradora antes de iniciar el tratamiento.",
            "Evita que el paciente deba cepillarse los dientes en los tres días posteriores a la cita dental en el consultorio.",
            "Sirve para esterilizar químicamente el conducto radicular mediante los fotones de radiación ionizante emitidos.",
            "Permite documentar la anatomía previa, curvaturas radiculares, calcificaciones, reabsorciones o la presencia de instrumentos fracturados por operadores anteriores antes de tocar el diente."
        ],
        correcta=3,
        distractores=[
            "Los trámites administrativos de facturación no constituyen el fundamento biológico ni la exigencia médico-legal clínica.",
            "La toma radiográfica diagnóstica no suspende en ningún momento las medidas básicas de higiene oral del paciente.",
            "La dosis diagnóstica de rayos X dentales no posee ningún efecto esterilizante ni bactericida sobre el biofilm intraconducto.",
            ""
        ],
        explicacion="En las líneas cuatrocientos noventa y ocho a quinientos ocho, el profesor explicó la enorme trascendencia médica y legal de la radiografía inicial o de diagnóstico. Si el clínico comienza a instrumentar sin una radiografía previa de calidad, no podrá advertir curvaturas severas en bayoneta, dilaceraciones o conductos atrésicos que predisponen a perforaciones. Más aún en el terreno legal: si el diente ya tenía una lima fracturada abandonada por un odontólogo anterior o una reabsorción perforante y el clínico no tomó radiografía inicial previa, legalmente se asumirá que la complicación iatrogénica fue causada por él durante la consulta.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Radiología endodóntica: valor diagnóstico y médico-legal de la radiografía inicial",
        que="Fundamentar el valor diagnóstico y la protección médico-legal de la radiografía periapical previa a la instrumentación.",
        clave="La radiografía inicial obligatoria documenta anatomía, curvaturas complejas o limas fracturadas previas protegiendo legalmente al operador.",
        pistas=[
            "Recuerda la advertencia del docente: si encuentras una lima partida adentro y no tomaste radiografía antes, la culpa legal es tuya.",
            "Ten en cuenta que planificar la instrumentación requiere conocer previamente curvaturas y conductos calcificados."
        ],
        plan=[
            "Comprender la función diagnóstica de la radiografía inicial en la detección de variaciones anatómicas complejas.",
            "Reconocer el valor médico-legal como registro documental previo a la intervención del operador.",
            "Establecer la obligatoriedad de la radiografía previa antes de introducir instrumental en el conducto."
        ],
        marcas_data=[
            ("la toma de la radiografía inicial periapical previa a cualquier instrumentación o tratamiento de conductos es obligatoria e intransigible", "clave", "Norma clínica obligatoria", "Apunta a estándar de cuidado y protección legal"),
            ("¿Cuál de las siguientes razones clínicas y legales fundamenta esta exigencia antes de introducir cualquier instrumento en el conducto?", "pide", "Fundamento clínico y legal", "Demanda identificar anatomía previa y antecedentes de limas fracturadas")
        ],
        steps_ideas=[
            ("idea", "Planificación anatómica", "La radiografía muestra si el conducto es curvo, calcificado o si tiene varias raíces."),
            ("idea", "Protección médico-legal", "Si otro dentista dejó una lima rota y tú no tomaste radiografía inicial, legalmente asumen que fuiste tú quien la rompió."),
            ("check", "Comprobación legal y clínica", "Confirmamos que la radiografía inicial documenta anatomía previa y limas fracturadas antes de tocar el diente.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta norma fundamental de la práctica odontológica explicada por el profesor."),
            ("m:la toma de la radiografía inicial periapical previa a cualquier instrumentación o tratamiento de conductos es obligatoria e intransigible", "Observa que el docente no permite tocar ningún diente sin tener la radiografía inicial."),
            ("leer", "Clínicamente, la radiografía te avisa si la raíz está torcida, si el conducto está tapado o si tiene raíces extras."),
            ("leer", "Y legalmente es tu seguro de vida: si había una lima rota de un tratamiento viejo y no tomaste foto previa, la responsabilidad recae sobre ti."),
            ("leer", "Por lo tanto, la opción que describe la anatomía previa y los instrumentos fracturados anteriores es la respuesta correcta.")
        ]
    ))

    return qs
