"""Datos de las preguntas 1 a 20 de Odontología (Endodoncia).
Completamente alineadas con la Clase 1 y Clase 2, corregidas y enriquecidas.
"""

def get_questions_1_to_20(make_q):
    qs = []

    # 01 (Key B = 1)
    qs.append(make_q(
        qid="odo-001", nivel=2,
        enunciado="Un paciente de 28 años consulta por dolor agudo y punzante en el primer molar inferior izquierdo. Relata que el dolor se desencadena con bebidas frías y persiste durante varios minutos tras retirar el vaso, además de presentarse de forma espontánea por las noches al acostarse. Al examen clínico no hay dolor a la percusión ni a la palpación apical, y la prueba térmica con frío genera un dolor intenso que permanece por más de treinta segundos. ¿Cuál es el diagnóstico pulpar y la conducta clínica adecuada?",
        opciones=[
            "Pulpitis reversible con hiperemia pulpar localizada; requiere retirar la causa y colocar protección dentinopulpar.",
            "Pulpitis irreversible sintomática; requiere biopulpectomía en una sola sesión o pulpotomía de urgencia en decúbito.",
            "Necrosis pulpar séptica con periodontitis apical asintomática crónica; requiere medicación con hidróxido de calcio.",
            "Periodontitis apical sintomática originada exclusivamente por sobrecarga oclusal; requiere ajuste con papel de articular."
        ],
        correcta=1,
        distractores=[
            "En la pulpitis reversible el dolor provocado cesa de inmediato a los dos segundos de retirar el estímulo y no despierta al paciente en la noche.",
            "",
            "La necrosis pulpar cursa con muerte tisular y por ende presenta ausencia total de respuesta a las pruebas de frío.",
            "La periodontitis apical sintomática se manifiesta por dolor exquisito a la percusión vertical y masticación, ausentes en este cuadro."
        ],
        explicacion="El cuadro clínico combina dolor provocado prolongado que perdura más de treinta segundos tras retirar el frío y dolor espontáneo nocturno en decúbito. Estos signos cardinales reflejan inflamación pulpar avanzada irreversible con incremento de la presión intrapulpar, lo que define una pulpitis irreversible sintomática. Conducta clínica enseñada por el profesor: biopulpectomía completa (tratamiento de conductos); al no existir compromiso periapical ni exudado purulento se puede terminar en una sola cita. En urgencias nocturnas, la pulpotomía cameral con hemostasia alivia inmediatamente la presión.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Diagnóstico pulpar: pulpitis irreversible sintomática",
        que="Determinar el diagnóstico pulpar y la conducta clínica a partir de la respuesta prolongada al frío y dolor nocturno.",
        clave="La persistencia del dolor tras retirar el estímulo térmico y la presencia de dolor nocturno definen la pulpitis irreversible sintomática.",
        pistas=[
            "Evalúa que la molestia permanece por más de treinta segundos tras retirar el vaso.",
            "Ten presente que el dolor que despierta al paciente en la noche traduce inflamación pulpar severa en una cámara cerrada."
        ],
        plan=[
            "Comprobar el tiempo que permanece el dolor una vez retirado el estímulo térmico.",
            "Analizar el componente postural decúbito que incrementa la presión cefálica intrapulpar.",
            "Establecer la conducta de biopulpectomía o pulpotomía de urgencia según el estado pulpar."
        ],
        marcas_data=[
            ("persiste durante varios minutos tras retirar el vaso", "clave", "Dolor prolongado tras estímulo", "Apunta a daño irreversible del tejido pulpar"),
            ("espontánea por las noches al acostarse", "dato", "Dolor nocturno por decúbito", "Apunta a incremento de presión hidrostática cefálica"),
            ("¿Cuál es el diagnóstico pulpar y la conducta clínica adecuada?", "pide", "Determinar diagnóstico y plan", "Solicita formulación integral de diagnóstico y conducta")
        ],
        steps_ideas=[
            ("idea", "Cronología del dolor", "El dolor térmico que perdura tras retirar el estímulo indica daño irreversible en el tejido pulpar."),
            ("idea", "Mecanismo del decúbito", "El dolor nocturno ocurre por el aumento de presión cefálica que distiende las paredes rígidas de la cámara pulpar."),
            ("idea", "Conducta clínica", "Al no existir lesión periapical bacteriana crónica, el tratamiento endodóntico se puede realizar en una sola sesión."),
            ("check", "Comprobación diagnóstica", "Confirmamos que la persistencia al frío y la espontaneidad nocturna corresponden a pulpitis irreversible sintomática.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención los síntomas principales relatados por el paciente en la consulta."),
            ("m:persiste durante varios minutos tras retirar el vaso", "Observa que el dolor no se detiene al retirar el frío, sino que perdura varios minutos."),
            ("leer", "El docente enseñó que cuando el dolor continúa más de treinta segundos, la pulpa no tiene capacidad de recuperarse."),
            ("m:espontánea por las noches al acostarse", "Fíjate además en el dolor nocturno al acostarse, signo típico de inflamación pulpar severa."),
            ("leer", "Por lo tanto, descartamos las opciones reversibles o periapicales puras y confirmamos la pulpitis irreversible.")
        ]
    ))

    # 02 (Key C = 2)
    qs.append(make_q(
        qid="odo-002", nivel=2,
        enunciado="Durante la explicación de la neurofisiología del dolor pulpar en clase, el profesor profundiza en las diferencias entre las fibras nerviosas que inervan el estroma de la pulpa dental. Respecto a las fibras C amielínicas, ¿cuál de las siguientes afirmaciones describe con precisión sus características biológicas y clínicas?",
        opciones=[
            "Son mielinizadas periféricas de conducción rápida y transmiten un dolor agudo, punzante y bien localizado ante estímulos fríos leves.",
            "Se ubican predominantemente en la unión amelodentinaria y responden exclusivamente a la deformación hidrodinámica de los túbulos.",
            "Son amielínicas, poseen un umbral de excitación alto, resisten mejor la hipoxia y transmiten un dolor sordo, urente y mal localizado.",
            "Inervan el ligamento periodontal y se encargan de la propiocepción y localización exacta del diente afectado a la percusión."
        ],
        correcta=2,
        distractores=[
            "La descripción de fibras mielinizadas de conducción rápida y dolor punzante y agudo al frío corresponde a las fibras A-delta periféricas.",
            "La ubicación en la unión amelodentinaria asociada a la teoría hidrodinámica corresponde a las terminaciones de las fibras A-delta, no a las fibras C.",
            "",
            "Las fibras propioceptivas y mecanorreceptoras corresponden a la inervación periapical y periodontal, no a las fibras C del estroma pulpar interno."
        ],
        explicacion="Las fibras C son fibras amielínicas situadas en el estroma profundo de la pulpa dental. Requieren estímulos de mayor intensidad (umbral alto), toleran mejor la hipoxia y su activación traduce inflamación tisular avanzada con dolor difuso, sordo, pulsátil o urente. En contraste, las fibras A-delta son mielínicas, periféricas, de conducción rápida y generan dolor agudo y punzante bien localizado.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Inervación pulpar: fibras A-delta y fibras C",
        que="Diferenciar las propiedades fisiológicas y clínicas de las fibras C amielínicas del estroma pulpar.",
        clave="Las fibras C son amielínicas, de conducción lenta y umbral alto, y producen dolor sordo y mal localizado.",
        pistas=[
            "Recuerda que las fibras amielínicas se localizan en el núcleo pulpar y toleran mejor la hipoxia.",
            "Ten en cuenta que el dolor urente y sordo continuo es transmitido por las fibras C."
        ],
        plan=[
            "Reconocer las diferencias estructurales entre fibras mielínicas y amielínicas.",
            "Asociar el dolor sordo y urente con la despolarización de las fibras C en el estroma.",
            "Contrastar la localización pulpar frente a los mecanorreceptores periodontales."
        ],
        marcas_data=[
            ("fibras C amielínicas", "clave", "Estructura nerviosa objeto de la pregunta", "Apunta a inervación sensorial profunda del estroma"),
            ("¿cuál de las siguientes afirmaciones describe con precisión sus características biológicas y clínicas?", "pide", "Identificar propiedades de fibras C", "Demanda identificar umbral, conducción y tipo de dolor")
        ],
        steps_ideas=[
            ("idea", "Fibras A-delta frente a fibras C", "Las fibras A-delta son mielínicas periféricas y rápidas; las fibras C son amielínicas centrales y lentas."),
            ("idea", "Expresión clínica del dolor", "El dolor mediado por fibras C es sordo, pulsátil y traduce daño tisular profundo en el estroma pulpar."),
            ("check", "Comprobación fisiológica", "Verificamos que las fibras C son amielínicas, de umbral alto y responsables del dolor sordo y difuso.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos la pregunta teórica sobre los dos tipos de fibras sensitivas que inervan la pulpa dental."),
            ("m:fibras C amielínicas", "Identifica que se pregunta de forma específica por las fibras C amielínicas del estroma interno."),
            ("leer", "El profesor enseñó que las fibras A-delta dan dolor agudo y punzante, mientras que las fibras C dan dolor sordo y urente."),
            ("leer", "Además, las fibras C tienen un umbral de excitación más elevado y soportan mejor los ambientes con hipoxia."),
            ("leer", "Por descarte de las opciones mielinizadas o periodontales, seleccionamos la alternativa exacta.")
        ]
    ))

    # 03 (Key A = 0)
    qs.append(make_q(
        qid="odo-003", nivel=2,
        enunciado="Un paciente de 35 años acude a consulta refiriendo dolor agudo y breve en un premolar superior al consumir bebidas frías o dulces. El dolor aparece únicamente cuando el estímulo entra en contacto con el diente y desaparece por completo dos segundos después de retirarlo o tragarlo. No refiere dolor espontáneo ni molestias nocturnas. Al examen clínico se observa una restauración de resina con desadaptación marginal leve, sin dolor a la percusión ni cambios periapicales radiográficos. ¿Cuál es el diagnóstico pulpar y la conducta clínica adecuada?",
        opciones=[
            "Pulpitis reversible; retirar la resina filtrada, colocar protección dentinopulpar con ionómero o silicato cálcico y restaurar; la pulpa seguirá vital.",
            "Pulpitis irreversible sintomática; realizar biopulpectomía cameral y radicular en dos citas separadas con hidróxido de calcio.",
            "Necrosis pulpar por desvitalización microbiana; requiere tratamiento de conductos y medicación intraconducto.",
            "Periodontitis apical sintomática con ensanchamiento periapical; requiere ajuste oclusal y ferulización inmediata."
        ],
        correcta=0,
        distractores=[
            "",
            "La pulpitis irreversible sintomática presenta dolor persistente por minutos tras retirar el estímulo y suele cursar con dolor espontáneo nocturno.",
            "La necrosis pulpar presenta ausencia total de respuesta al frío por desvitalización completa del tejido pulpar.",
            "La periodontitis apical sintomática se caracteriza por dolor notable a la percusión vertical y masticación, los cuales son negativos en este paciente."
        ],
        explicacion="Una respuesta dolorosa al frío o al dulce que cesa de inmediato (uno a dos segundos) tras retirar el estímulo, en ausencia de dolor espontáneo o nocturno, define una pulpitis reversible. El profesor destacó la regla: «dolor con dulce es igual a pulpitis reversible». La pulpa conserva intacta su capacidad de reparación si se elimina el factor irritante local (la filtración marginal de la resina) mediante una nueva restauración con adecuada protección dentinopulpar (ionómero de vidrio o silicato cálcico). Tras la restauración, la prueba de frío debe seguir positiva normal, confirmando la vitalidad.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Diagnóstico pulpar: pulpitis reversible",
        que="Identificar el cuadro de pulpitis reversible y su tratamiento conservador preservando la vitalidad pulpar.",
        clave="El dolor provocado que desaparece casi de inmediato sin dolor espontáneo caracteriza a la pulpitis reversible.",
        pistas=[
            "Observa que el dolor no perdura una vez que el estímulo frío o dulce se retira.",
            "Recuerda que una pulpa reversible tiene capacidad biológica de recuperarse si eliminas la filtración."
        ],
        plan=[
            "Evaluar el tiempo de desaparición del dolor al cesar el contacto con el frío o dulce.",
            "Constatar la ausencia de dolor espontáneo nocturno y la integridad periapical.",
            "Seleccionar la conducta restauradora conservadora con base intermedia protectora."
        ],
        marcas_data=[
            ("desaparece por completo dos segundos después de retirarlo", "clave", "Cese inmediato del dolor", "Apunta a capacidad reparativa pulpar conservada"),
            ("No refiere dolor espontáneo ni molestias nocturnas", "dato", "Ausencia de signos irreversibles", "Descarta pulpitis irreversible"),
            ("¿Cuál es el diagnóstico pulpar y la conducta clínica adecuada?", "pide", "Diagnóstico y conducta", "Demanda integrar patología pulpar y plan terapéutico")
        ],
        steps_ideas=[
            ("idea", "Tiempo de respuesta", "El dolor térmico que se detiene en un lapso de dos segundos indica que el tejido pulpar no está irreversiblemente dañado."),
            ("idea", "Regla clínica del dulce", "El profesor enseñó que el dolor con dulce traduce permeabilidad dentinaria y clasifica como pulpitis reversible."),
            ("idea", "Manejo conservador", "Al eliminar la causa mecánica o microbiana y proteger la dentina con ionómero, la pulpa cicatriza sin endodoncia."),
            ("check", "Comprobación diagnóstica", "Verificamos que el cuadro clínico corresponde a pulpitis reversible con manejo restaurador conservador.")
        ],
        lvl1_steps=[
            ("leer", "Analicemos los datos principales aportados por el paciente sobre su molestia dental."),
            ("m:desaparece por completo dos segundos después de retirarlo", "Fíjate en este dato clave: el dolor dura apenas dos segundos y desaparece."),
            ("leer", "El docente enseñó que cuando el dolor cede de inmediato y aparece con dulce, la pulpa está viva y es reversible."),
            ("m:No refiere dolor espontáneo ni molestias nocturnas", "Además, confirma que no hay dolor en la noche ni de forma espontánea."),
            ("leer", "Por lo tanto, la conducta es totalmente conservadora: retirar la resina, proteger con ionómero y restaurar.")
        ]
    ))

    # 04 (Key D = 3)
    qs.append(make_q(
        qid="odo-004", nivel=3,
        enunciado="Al realizar el examen intraoral de un paciente, el odontólogo detecta un estoma fistuloso activo con salida de exudado purulento ubicado en la encía vestibular entre el segundo premolar y el primer molar superior derecho. Ambos dientes presentan restauraciones coronales extensas y el paciente no recuerda cuál presentó dolor previo. De acuerdo con las enseñanzas del docente en clase sobre el examen clínico, ¿cuál es el procedimiento indicado para identificar con certeza el diente causal?",
        opciones=[
            "Iniciar la apertura coronal de ambos dientes de forma simultánea con fresa redonda para explorar visualmente si existe drenaje cameral purulento.",
            "Realizar una biopsia por escisión del estoma fistuloso vestibular bajo anestesia infiltrativa y enviar la muestra a estudio anatomopatológico.",
            "Prescribir antibióticos sistémicos de amplio espectro durante siete días consecutivos y esperar a que la fístula desaparezca espontáneamente sin intervenir.",
            "Introducir con suavidad un cono de gutapercha radiopaco por el estoma fistuloso y tomar una radiografía periapical para seguir el trayecto hasta el ápice del diente causal."
        ],
        correcta=3,
        distractores=[
            "Abrir ambos dientes de manera invasiva sin diagnóstico causal vulnera la integridad de un diente que podría estar vital y sano.",
            "La biopsia de la fístula no está indicada en primera instancia ante una lesión de claro origen odontogénico bacteriano.",
            "Los antibióticos no resuelven la causa infecciosa necrótica intraconducto y no permiten identificar qué diente origina la fístula.",
            ""
        ],
        explicacion="La fistulografía es la prueba clínica indicada cuando una fístula se encuentra en una posición intermedia o dudosa. Consiste en insertar suavemente un cono de gutapercha (habitualmente calibre treinta o treinta y cinco) a través del trayecto fistuloso hasta topar resistencia y tomar una radiografía periapical. El profesor explicó que si el cono radiopaco llega hasta el ápice radicular confirma el origen periapical del diente causal; si el cono queda a la mitad de la raíz, señala un origen periodontal.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Procedimientos diagnósticos: fistulografía",
        que="Identificar el diente causal de una fístula mediante fistulografía con cono de gutapercha.",
        clave="La inserción de un cono de gutapercha radiopaco por el trayecto fistuloso señala el diente origen en la radiografía.",
        pistas=[
            "Recuerda la técnica comentada por el profesor para no tener que adivinar entre dos dientes vecinos.",
            "Aprovecha las propiedades radiopacas y flexibles de la gutapercha para el rastreo en la radiografía."
        ],
        plan=[
            "Identificar la presencia de un estoma fistuloso en una zona intermedia dudosa.",
            "Seleccionar la técnica semiológica de fistulografía con cono de gutapercha radiopaco.",
            "Interpretar la llegada del cono al ápice (origen pulpar) o a media raíz (periodontal)."
        ],
        marcas_data=[
            ("estoma fistuloso activo con salida de exudado purulento", "dato", "Presencia de fístula", "Apunta a proceso infeccioso crónico que drena"),
            ("entre el segundo premolar y el primer molar superior derecho", "clave", "Ubicación intermedia entre dos dientes", "Genera duda diagnóstica sobre el diente causal"),
            ("¿cuál es el procedimiento indicado para identificar con certeza el diente causal?", "pide", "Procedimiento de localización", "Demanda seleccionar la técnica diagnóstica adecuada")
        ],
        steps_ideas=[
            ("idea", "Rastreo fistuloso", "El trayecto de una fístula puede recorrer distancias considerables antes de perforar la cortical ósea."),
            ("idea", "Fistulografía con gutapercha", "La gutapercha es flexible y radiopaca, lo que permite trazar el trayecto exacto en la radiografía sin traumatizar."),
            ("idea", "Criterio de ubicación", "Si el cono llega al ápice es periapical; si se queda a la mitad de la raíz es periodontal."),
            ("check", "Comprobación diagnóstica", "Confirmamos que la fistulografía con cono de gutapercha es el procedimiento estándar enseñado en clase.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos la situación clínica: hay dos dientes vecinos restaurados y una fístula en el medio."),
            ("m:entre el segundo premolar y el primer molar superior derecho", "Observa que no podemos adivinar cuál de los dos dientes está infectado."),
            ("leer", "El docente explicó que abrir los dos dientes a ciegas o dar antibióticos es un grave error profesional."),
            ("leer", "La técnica enseñada consiste en introducir un cono de gutapercha calibre treinta por el estoma."),
            ("leer", "Al tomar la radiografía periapical, el cono radiopaco nos guiará directamente al ápice del diente causal.")
        ]
    ))

    # 05 (Key B = 1)
    qs.append(make_q(
        qid="odo-005", nivel=2,
        enunciado="Un paciente de 42 años asiste a control odontológico de rutina completamente asintomático. En la radiografía periapical se observa de forma casual una zona radiolúcida periapical circunscrita y redondeada alrededor del ápice del incisivo central superior derecho. En las pruebas de sensibilidad pulpar con frío el diente no responde (negativo absoluto), y a la percusión y palpación no manifiesta molestia alguna. De acuerdo con los criterios del docente, ¿cuál es el diagnóstico pulpar y periapical correcto y la pauta de tratamiento?",
        opciones=[
            "Pulpitis reversible con periodontitis apical sintomática; requiere protección indirecta y ajuste oclusal.",
            "Necrosis pulpar con periodontitis apical asintomática; requiere preparación biomecánica y medicación con hidróxido de calcio por ocho a diez días, no en una sola cita.",
            "Pulpitis irreversible sintomática con tejidos periapicales normales; requiere biopulpectomía de urgencia en una sola sesión.",
            "Diente previamente tratado con absceso apical agudo; requiere prescripción de antibióticos por vía oral durante siete días."
        ],
        correcta=1,
        distractores=[
            "En la pulpitis reversible la pulpa está vital y responde al frío, y la periodontitis sintomática duele intensamente a la percusión.",
            "",
            "La pulpitis irreversible sintomática presenta respuesta térmica positiva exagerada y dolor continuo, ausentes en un diente desvitalizado.",
            "El diente no ha recibido tratamiento de conductos previo y el absceso agudo cursa con dolor pulsátil y tumefacción evidente."
        ],
        explicacion="La falta absoluta de respuesta al frío confirma la necrosis pulpar (muerte del tejido pulpar). La presencia de una zona radiolúcida periapical sin dolor a la masticación ni a la percusión corresponde a una periodontitis apical asintomática. El profesor recalcó que no se debe utilizar la terminología de «granuloma o quiste» en el diagnóstico clínico, pues solo el estudio histopatológico puede diferenciarlos. Plan de tratamiento: al haber infección bacteriana periapical crónica, NO se debe obturar en una sola cita; se realiza instrumentación biomecánica completa y medicación intraconducto con hidróxido de calcio durante ocho a diez días para desinfectar antes de obturar.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Diagnóstico pulpar y periapical: necrosis y periodontitis apical asintomática",
        que="Integrar la necrosis pulpar con el hallazgo radiográfico periapical asintomático y definir el tratamiento.",
        clave="La respuesta negativa a pruebas térmicas con lesión radiolúcida indolora define necrosis pulpar con periodontitis apical asintomática y medicación con hidróxido de calcio.",
        pistas=[
            "Evalúa que la ausencia de respuesta térmica indica desvitalización pulpar completa.",
            "Ten en cuenta que la lesión periapical sin dolor a la percusión clasifica como asintomática y requiere dos citas con hidróxido de calcio."
        ],
        plan=[
            "Confirmar la desvitalización pulpar mediante la prueba de frío negativa.",
            "Clasificar la lesión ósea periapical asintomática evitando términos histológicos.",
            "Indicar el protocolo de dos citas con medicación intraconducto de hidróxido de calcio."
        ],
        marcas_data=[
            ("diente no responde (negativo absoluto)", "clave", "Signo de necrosis pulpar", "Apunta a muerte del tejido vasculonervioso"),
            ("zona radiolúcida periapical circunscrita y redondeada", "dato", "Lesión ósea periapical", "Apunta a pérdida de densidad ósea crónica"),
            ("¿cuál es el diagnóstico pulpar y periapical correcto y la pauta de tratamiento?", "pide", "Diagnóstico integrado y conducta", "Demanda clasificar y establecer número de citas")
        ],
        steps_ideas=[
            ("idea", "Evaluación pulpar", "La falta de respuesta a las pruebas térmicas indica necrosis pulpar."),
            ("idea", "Evaluación periapical", "La radiolucidez periapical sin dolor a la percusión define la periodontitis apical asintomática."),
            ("idea", "Regla de las citas del profesor", "El profesor enseñó que con lesión periapical no se obtura en una cita: se medica con hidróxido de calcio ocho a diez días."),
            ("check", "Comprobación diagnóstica", "Verificamos que corresponde a necrosis con periodontitis apical asintomática tratada en dos sesiones.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con calma los hallazgos clínicos y radiográficos de este paciente asintomático."),
            ("m:diente no responde (negativo absoluto)", "Observa que la prueba térmica de frío dio totalmente negativa, lo cual significa necrosis pulpar."),
            ("m:zona radiolúcida periapical circunscrita y redondeada", "En la radiografía hay una lesión ósea, pero el paciente no tiene dolor a la percusión."),
            ("leer", "El docente aclaró que esto es periodontitis apical asintomática (no se diagnostica quiste ni granuloma clínicamente)."),
            ("leer", "Además, el docente exige no obturar en una sola cita: se debe colocar hidróxido de calcio durante ocho a diez días.")
        ]
    ))

    # 06 (Key C = 2)
    qs.append(make_q(
        qid="odo-006", nivel=2,
        enunciado="Durante la práctica clínica, el docente le pide a un estudiante palpar un abultamiento ubicado en el fondo de surco vestibular sobre el ápice de un diente que presentó una fístula en el pasado. El estudiante realiza la palpación y describe que la consistencia es completamente dura como hueso, no fluctuante y no genera dolor. El diente tiene un tratamiento de conductos terminado hace un año y la mucosa es normal. ¿Qué significado clínico tiene este hallazgo según la clase?",
        opciones=[
            "Que se trata de un flemón activo en fase serosa que aún no ha perforado el periostio ni generado necrosis licuefactiva en los tejidos circundantes.",
            "Que existe acumulación purulenta en los tejidos submucosos formando un absceso que ya está maduro y listo para ser desbridado o drenado quirúrgicamente.",
            "Que corresponde a una cicatriz ósea o fibrosa dura en la cortical alveolar tras la resolución de la fístula previa, lo cual no indica patología activa.",
            "Que el ligamento periodontal presenta anquilosis alveolar completa imposibilitando cualquier respuesta inflamatoria transmucosa local."
        ],
        correcta=2,
        distractores=[
            "Un flemón es una inflamación difusa con dolor severo y tumefacción blanda en tejidos blandos.",
            "La acumulación purulenta se manifiesta como una masa fluctuante y blanda, no dura como hueso.",
            "",
            "La anquilosis afecta la interfase entre la raíz y el hueso dentro del alvéolo, no se diagnostica por abultamiento duro en surco."
        ],
        explicacion="El docente enseñó expresamente en la clase la interpretación semiológica de la palpación: si al palpar la mucosa se siente blanda o fluctuante, indica exudado purulento que requiere incisión o drenaje; pero si la consistencia es dura como hueso o tejido cicatrizal consolidado en un diente asintomático con endodoncia previa, corresponde a una cicatriz ósea o defecto cortical fibroso curado. No representa infección activa ni requiere retratamiento.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Examen clínico: palpación y cicatriz de fístula",
        que="Interpretar la consistencia dura a la palpación apical como cicatriz ósea y no como patología activa.",
        clave="La palpación dura e indolora en la zona de una fístula previa corresponde a una cicatriz ósea y no a una lesión activa.",
        pistas=[
            "Recuerda la distinción hecha por el profesor entre una consistencia blanda fluctuante y una consistencia dura.",
            "Ten en cuenta que el hueso o tejido fibroso cicatrizal se palpa duro y no representa infección activa."
        ],
        plan=[
            "Evaluar las características semiológicas de dureza y ausencia de fluctuación a la palpación.",
            "Correlacionar con el antecedente de fístula previa resuelta y endodoncia terminada.",
            "Diferenciar una cicatriz reparativa de un absceso purulento activo."
        ],
        marcas_data=[
            ("consistencia es completamente dura como hueso", "clave", "Signo semiológico de palpación", "Apunta a tejido mineralizado cicatrizal"),
            ("no fluctuante y no genera dolor", "dato", "Ausencia de signos agudos", "Descarta proceso purulento activo"),
            ("¿Qué significado clínico tiene este hallazgo según la clase?", "pide", "Interpretación diagnóstica", "Demanda reconocer cicatriz ósea post-fístula")
        ],
        steps_ideas=[
            ("idea", "Semiología de la palpación", "La palpación blanda o fluctuante indica pus; la palpación dura indica hueso o cicatriz."),
            ("idea", "Antecedente de fístula", "El orificio por donde drenó la fístula puede reparar con tejido fibroso o reborde óseo endurecido."),
            ("check", "Comprobación clínica", "Verificamos que se trata de una cicatriz ósea o fibrosa que no amerita reapertura ni tratamiento.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos con cuidado la descripción semiológica de la palpación realizada por el estudiante."),
            ("m:consistencia es completamente dura como hueso", "Nota que el tejido se palpa duro como hueso, totalmente opuesto a una masa blanda con pus."),
            ("m:no fluctuante y no genera dolor", "Además no hay dolor ni fluctuación en un diente que ya tiene endodoncia terminada."),
            ("leer", "El docente enseñó que cuando una fístula cura, el defecto óseo puede cerrar con una cicatriz ósea o fibrosa dura."),
            ("leer", "Por consiguiente, esto no es infección activa sino una cicatriz alveolar normal.")
        ]
    ))

    # 07 (Key D = 3)
    qs.append(make_q(
        qid="odo-007", nivel=2,
        enunciado="Un paciente de 50 años asiste muy angustiado al consultorio refiriendo dolor severo al masticar en el segundo premolar inferior, donde le colocaron una restauración de resina hace dos días. Manifiesta que siente el diente «más alto, como una piedra en el zapato». Al examen clínico, la percusión vertical y la palpación oclusal son extremadamente dolorosas, pero la prueba térmica de frío es positiva normal y cesa en dos segundos. La radiografía periapical muestra ligamento periodontal íntegro sin radiolucidez. ¿Cuál es el diagnóstico y la conducta clínica indicada?",
        opciones=[
            "Pulpitis irreversible sintomática; realizar de inmediato una biopulpectomía de urgencia.",
            "Necrosis pulpar por trauma; prescribir antibióticos durante ocho días y citar para conductos.",
            "Absceso apical agudo en evolución; colocar pasta de hidróxido de calcio intraconducto para inducir desinfección.",
            "Periodontitis apical sintomática por trauma oclusal con pulpa vital; realizar un ajuste oclusal selectivo con papel de articular sin endodoncia."
        ],
        correcta=3,
        distractores=[
            "En la pulpitis irreversible el dolor térmico al frío perdura intensamente por más de treinta segundos, lo cual no ocurre aquí.",
            "La necrosis pulpar cursa con prueba de frío negativa absoluto por desvitalización del tejido pulpar.",
            "El absceso apical agudo se asocia a necrosis pulpar y tumefacción fluctuante evidente, ausentes en este diente vital.",
            ""
        ],
        explicacion="La presencia de dolor agudo al masticar tras una restauración alta reciente («piedra en el zapato»), con prueba de frío positiva normal que cede en dos segundos (pulpa sana), define una periodontitis apical sintomática de etiología mecánica traumática. El docente recalcó que el tratamiento NO es hacer endodoncia: consiste en realizar un ajuste oclusal selectivo desgastando el punto prematuro con papel de articular para desinflamar el ligamento periodontal, con lo cual el dolor desaparece.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Diagnóstico diferencial: periodontitis apical por trauma oclusal",
        que="Diferenciar la periodontitis apical mecánica por contacto prematuro frente a una infección bacteriana.",
        clave="El dolor periapical tras restauración reciente con prueba térmica normal corresponde a trauma oclusal y se resuelve con ajuste oclusal.",
        pistas=[
            "Fíjate que la prueba de frío es positiva normal (la pulpa está completamente sana).",
            "Ten en cuenta la metáfora de la «piedra en el zapato» que describe el trauma oclusal agudo por punto prematuro."
        ],
        plan=[
            "Identificar la correlación temporal entre la colocación de la resina y el dolor al masticar.",
            "Verificar la vitalidad pulpar intacta con la respuesta normal y breve al frío.",
            "Indicar el ajuste oclusal selectivo sin tocar innecesariamente el tejido pulpar sano."
        ],
        marcas_data=[
            ("siente el diente «más alto, como una piedra en el zapato»", "clave", "Signo de sobrecarga oclusal", "Apunta a contacto prematuro reciente"),
            ("prueba térmica de frío es positiva normal y cesa en dos segundos", "dato", "Vitalidad pulpar conservada", "Descarta necrosis o pulpitis irreversible"),
            ("¿Cuál es el diagnóstico y la conducta clínica indicada?", "pide", "Diagnóstico y conducta", "Demanda establecer diagnóstico mecánico y manejo conservador")
        ],
        steps_ideas=[
            ("idea", "Vitalidad pulpar conservada", "La pulpa responde al frío con normalidad; el problema reside en el ligamento periodontal."),
            ("idea", "Causa oclusal", "Una restauración alta comprime el ligamento periodontal en cada masticación inflamándolo intensamente."),
            ("idea", "Conducta conservadora", "El profesor enseñó que jamás se debe hacer endodoncia a una pulpa sana por un punto alto: se realiza ajuste oclusal."),
            ("check", "Comprobación clínica", "Confirmamos periodontitis apical sintomática por trauma oclusal tratada con desgaste oclusal.")
        ],
        lvl1_steps=[
            ("leer", "Analicemos este caso clásico de dolor agudo posterior a un procedimiento restaurador."),
            ("m:siente el diente «más alto, como una piedra en el zapato»", "Observa esta expresión típica: el paciente siente el diente alto al morder."),
            ("m:prueba térmica de frío es positiva normal y cesa en dos segundos", "Mira la prueba de frío: la pulpa está viva y sana, no tiene pulpitis irreversible."),
            ("leer", "El docente fue enfático: si la pulpa está viva, el dolor a la percusión se debe al golpe constante de la mordida alta."),
            ("leer", "Por lo tanto, la conducta es ajustar la oclusión con papel de articular y no hacer endodoncia.")
        ]
    ))

    # 08 (Key A = 0)
    qs.append(make_q(
        qid="odo-008", nivel=3,
        enunciado="Al evaluar un diente pilar con corona completa metalocerámica en el que el paciente refiere dolor sordo difuso, el odontólogo intenta realizar la prueba de sensibilidad con frío pero no obtiene ninguna respuesta del paciente. De acuerdo con las pautas del docente en clase sobre dientes pilares con prótesis fijas, ¿cuál es la razón de esta falta de respuesta y qué consideración semiológica debe aplicarse?",
        opciones=[
            "La porcelana es un aislante térmico que no conduce el frío; se debe buscar un margen cervical accesible o fricción, sabiendo que si duele al calor indica necrosis en curso.",
            "Prescindir de las pruebas de sensibilidad y diagnosticar necrosis pulpar basándose únicamente en el hecho de que el diente posee una corona de recubrimiento total.",
            "Realizar la prueba eléctrica colocando el electrodo del vitalómetro directamente sobre la porcelana seca de la superficie vestibular de la corona protésica.",
            "Perforar inmediatamente la corona con fresa de diamante para aplicar calor directo mediante un instrumento metálico al rojo vivo sobre la dentina coronal."
        ],
        correcta=0,
        distractores=[
            "",
            "Tener una corona no significa que el diente esté necrótico; muchos dientes pilares conservan pulpa vital sana bajo la corona.",
            "La porcelana no conduce la corriente eléctrica del vitalómetro produciendo lecturas erróneas de falso negativo.",
            "Perforar la corona sin verificar márgenes o realizar pruebas especiales es una conducta destructiva e injustificada."
        ],
        explicacion="La porcelana y el metal son excelentes aislantes térmicos que impiden que el frío llegue a la dentina y a la pulpa, originando falsos negativos. El profesor explicó que se debe buscar un margen cervical accesible de estructura dentaria natural para aplicar el refrigerante o recurrir a pruebas térmicas con calor o fricción. Asimismo, el docente resaltó una regla fundamental: si un diente con corona duele al estímulo caliente y se alivia con líquidos fríos, indica un proceso de necrosis pulpar y gasificación en evolución dentro de la cámara.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Pruebas de sensibilidad especiales: dientes con coronas",
        que="Explicar las limitaciones térmicas de las coronas protésicas y la conducta diagnóstica alternativa.",
        clave="La porcelana aísla térmicamente la pulpa; se debe evaluar el margen cervical o aplicar calor sabiendo que el dolor al calor indica necrosis en curso.",
        pistas=[
            "Recuerda que los materiales protésicos como la cerámica no transmiten el frío adecuadamente.",
            "Ten en cuenta la regla del profesor: dolor provocado por calor en un diente coronado traduce necrosis en curso."
        ],
        plan=[
            "Comprender el efecto aislante térmico y eléctrico de las coronas completas de porcelana.",
            "Identificar las zonas alternativas de evaluación como el margen cervical expuesto.",
            "Reconocer el valor semiológico del dolor al calor como indicador de necrosis pulpar."
        ],
        marcas_data=[
            ("corona completa metalocerámica", "dato", "Restauración protésica presente", "Apunta a barrera física aislante"),
            ("intenta realizar la prueba de sensibilidad con frío pero no obtiene ninguna respuesta", "clave", "Falso negativo por aislamiento", "Apunta a limitación de la prueba convencional de frío"),
            ("¿cuál es la razón de esta falta de respuesta y qué consideración semiológica debe aplicarse?", "pide", "Razón biofísica y conducta", "Demanda fundamentar el aislamiento y la alternativa diagnóstica")
        ],
        steps_ideas=[
            ("idea", "Aislamiento protésico", "La porcelana actúa como aislante térmico y eléctrico; el frío no alcanza la pulpa."),
            ("idea", "Evaluación en cuello", "El clínico debe buscar márgenes radiculares o cervicales expuestos para realizar la prueba."),
            ("idea", "Regla del calor", "El docente enseñó que si un diente con corona responde dolorosamente al calor, está en proceso de necrosis."),
            ("check", "Comprobación diagnóstica", "Verificamos que la porcelana aísla el frío y que el calor orienta hacia necrosis en marcha.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos esta dificultad clínica frecuente al examinar dientes con coronas completas."),
            ("m:corona completa metalocerámica", "Observa que el diente está cubierto totalmente por una capa de metal y porcelana."),
            ("m:intenta realizar la prueba de sensibilidad con frío pero no obtiene ninguna respuesta", "El frío no produce respuesta porque la porcelana no conduce la temperatura."),
            ("leer", "El docente explicó que no se puede asumir necrosis solo por esto; hay que buscar el margen en el cuello."),
            ("leer", "Además, el docente destacó que si este diente duele con calor, se sospecha necrosis en evolución.")
        ]
    ))

    # 09 (Key B = 1)
    qs.append(make_q(
        qid="odo-009", nivel=2,
        enunciado="Una paciente de 19 años es remitida por el servicio de odontología restauradora tras detectar una lesión cariosa profunda en el primer molar inferior. La paciente no ha tenido dolor espontáneo. Al remover la dentina cariada profunda con aislamiento absoluto, se produce una exposición pulpar de dos milímetros de diámetro con tejido pulpar rojizo que sangra activamente. De acuerdo con los criterios de la clase sobre el manejo pulpar vital y sangrado, ¿cuál es el diagnóstico pulpar y la conducta a evaluar?",
        opciones=[
            "Pulpitis reversible con hiperemia leve; colocar óxido de zinc eugenol directamente sobre la pulpa sin evaluar el sangrado.",
            "Pulpitis irreversible asintomática por exposición cariosa; evaluar el sangrado cameral con suero frío: si cohíbe en menos de cinco minutos permite pulpotomía con biocerámico, si no, biopulpectomía.",
            "Necrosis pulpar séptica con lesión periapical circunscrita; requiere instrumentación con limas de grueso calibre de inmediato.",
            "Pulpa clínicamente normal con respuesta biológica conservada; obturar definitivamente con amalgama de plata condensada con fuerza."
        ],
        correcta=1,
        distractores=[
            "Una exposición pulpar directa por caries profunda ya no clasifica como pulpitis reversible, y el eugenol directo es citotóxico sobre la pulpa expuesta.",
            "",
            "La pulpa sangra activamente y estaba vital, lo cual descarta de plano la necrosis pulpar.",
            "Al haber invasión bacteriana y exposición pulpar por caries, la pulpa no puede clasificarse como clínicamente normal."
        ],
        explicacion="La exposición pulpar directa como resultado del avance de una caries profunda en un diente asintomático clasifica como pulpitis irreversible asintomática. El docente enseñó que la conducta depende de la respuesta biológica y la hemostasia: al irrigar con suero fisiológico frío durante cinco minutos, si el sangrado es rojo rutilante y cohíbe rápidamente, la pulpa radicular está sana y se puede realizar terapia pulpar vital (pulpotomía cameral con biocerámico tipo Biodentine o MTA); si el sangrado es oscuro, profuso e incontrolable, indica inflamación irreversible de toda la pulpa y se debe proceder a la biopulpectomía completa.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Diagnóstico pulpar: pulpitis irreversible asintomática",
        que="Identificar la pulpitis irreversible asintomática por caries y evaluar la conducta terapéutica según el sangrado.",
        clave="La exposición pulpar por caries es pulpitis irreversible asintomática; la viabilidad de la terapia pulpar vital depende del control del sangrado en cinco minutos.",
        pistas=[
            "Ten en cuenta que la exposición pulpar causada por caries profunda ya no es reversible.",
            "Recuerda la regla del profesor: la calidad y el tiempo de coagulación del sangrado con suero frío determinan si se preserva la pulpa radicular."
        ],
        plan=[
            "Clasificar la exposición pulpar cariosa como pulpitis irreversible asintomática.",
            "Evaluar el tiempo de hemostasia y aspecto del sangrado con irrigación de suero frío.",
            "Seleccionar entre pulpotomía con biocerámico o biopulpectomía según la respuesta vascular."
        ],
        marcas_data=[
            ("exposición pulpar de dos milímetros de diámetro con tejido pulpar rojizo que sangra", "clave", "Signo de exposición cariosa vital", "Apunta a comunicación pulpar directa por caries"),
            ("La paciente no ha tenido dolor espontáneo", "dato", "Carácter asintomático del cuadro", "Apunta a pulpitis irreversible asintomática"),
            ("¿cuál es el diagnóstico pulpar y la conducta a evaluar?", "pide", "Diagnóstico y conducta terapéutica", "Demanda integrar diagnóstico y criterio de hemostasia")
        ],
        steps_ideas=[
            ("idea", "Clasificación diagnóstica", "La exposición por caries en diente asintomático es pulpitis irreversible asintomática."),
            ("idea", "Prueba de hemostasia", "Se irriga con suero frío cinco minutos: si el sangrado cohíbe y es rojo claro, la pulpa radicular es viable."),
            ("idea", "Terapia vital vs biopulpectomía", "Si cohíbe se hace pulpotomía con biocerámico; si el sangrado no frena se realiza endodoncia completa."),
            ("check", "Comprobación terapéutica", "Confirmamos que se trata de pulpitis irreversible asintomática con conducta sujeta a hemostasia.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención lo ocurrido durante la remoción de caries en este molar joven."),
            ("m:La paciente no ha tenido dolor espontáneo", "Nota que la paciente no tenía dolor espontáneo previo a la consulta."),
            ("m:exposición pulpar de dos milímetros de diámetro con tejido pulpar rojizo que sangra", "Sin embargo, al remover la caries profunda hubo exposición directa de la pulpa."),
            ("leer", "El docente explicó que esto clasifica como pulpitis irreversible asintomática."),
            ("leer", "La conducta enseñada consiste en evaluar el sangrado con suero frío para decidir entre pulpotomía con biocerámico o endodoncia completa.")
        ]
    ))

    # 10 (Key C = 2)
    qs.append(make_q(
        qid="odo-010", nivel=2,
        enunciado="En la sección de semiología clínica y pruebas periapicales, el profesor interroga a los estudiantes sobre la técnica correcta para realizar la percusión dental y su justificación biofísica. ¿Cuál de las siguientes afirmaciones describe la técnica enseñada en clase y su fundamento?",
        opciones=[
            "Utilizando la punta afilada del explorador dental presionando fuertemente el surco oclusal del diente sospechoso con movimientos de torsión mecánica lateral.",
            "Golpeando exclusivamente en sentido lateral con el mango metálico de la pinza algodonera sin evaluar previamente los dientes contralaterales sanos.",
            "Utilizando la parte roma y gruesa del mango del espejo dental, realizando golpecitos muy leves y evaluando primero un diente de control sano, porque un ligamento inflamado duele con mínima fuerza.",
            "Pidiéndole al paciente que mastique con fuerza una barra de cera dura o un rollo de algodón para reproducir el dolor periapical a la carga funcional."
        ],
        correcta=2,
        distractores=[
            "El explorador evalúa anatomía y cavidades cariadas, no la condición del ligamento periodontal a la percusión.",
            "Percutir con violencia o sin comparar con un diente de control asusta al paciente e invalida la prueba semiológica.",
            "",
            "Morder rollos de algodón o cuñas evalúa fracturas o fisuras dentales, no la prueba estándar de percusión vertical."
        ],
        explicacion="El docente recalcó que la percusión debe ser sumamente suave y delicada, realizada con la parte roma y metálica del mango del espejo. El motivo es biofísico: cuando el ligamento periodontal está inflamado (periodontitis apical), los mecanorreceptores y nociceptores están sensibilizados al máximo y un impacto leve es suficiente para provocar dolor intenso. Asimismo, siempre se debe percutir primero un diente de control sano para calibrar la respuesta del paciente y no comenzar asustándolo en el diente sospechoso.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Semiología periapical: técnica de percusión dental",
        que="Explicar la técnica adecuada de percusión con mango de espejo y su fundamento biológico.",
        clave="La percusión debe ser muy suave con el mango del espejo evaluando primero un diente sano para calibrar la respuesta.",
        pistas=[
            "Recuerda que un ligamento periodontal inflamado duele intensamente ante la fuerza más mínima.",
            "Ten presente la regla del profesor: siempre se evalúa primero un diente de control sano para comparar."
        ],
        plan=[
            "Identificar el instrumento idóneo (mango romo del espejo) para la percusión dental.",
            "Comprender la hipersensibilidad de los mecanorreceptores periodontales ante la inflamación.",
            "Aplicar el protocolo de evaluación previa en un diente de control sano."
        ],
        marcas_data=[
            ("técnica correcta para realizar la percusión dental y su justificación biofísica", "clave", "Objeto de la evaluación semiológica", "Demanda describir instrumento, fuerza y control"),
            ("¿Cuál de las siguientes afirmaciones describe la técnica enseñada en clase y su fundamento?", "pide", "Pregunta de semiología clínica", "Solicita seleccionar la afirmación precisa de la técnica")
        ],
        steps_ideas=[
            ("idea", "Instrumento adecuado", "Se utiliza el mango del espejo dental por su parte roma y lisa."),
            ("idea", "Sensibilidad periodontal", "El ligamento periodontal inflamado no requiere golpes fuertes: duele con toques leves."),
            ("idea", "Control contralateral", "Siempre se percute primero un diente sano para que el paciente conozca la sensación basal."),
            ("check", "Comprobación semiológica", "Confirmamos que se usan toques leves con mango de espejo iniciando por el diente de control.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos la técnica semiológica de percusión explicada detalladamente por el profesor."),
            ("m:técnica correcta para realizar la percusión dental y su justificación biofísica", "Fíjate en los dos elementos: cómo se realiza el golpe y por qué debe ser suave."),
            ("leer", "El docente corrigió a los alumnos que golpeaban con fuerza: el ligamento inflamado duele con el roce más leve."),
            ("leer", "Además, el docente exigió evaluar primero un diente de control sano para que el paciente no se asuste."),
            ("leer", "Por lo tanto, la opción correcta describe el golpeteo leve con el mango del espejo iniciando en el diente sano.")
        ]
    ))

    # 11 (Key A = 0)
    qs.append(make_q(
        qid="odo-011", nivel=3,
        enunciado="Un paciente de 32 años acude a urgencias por dolor pulsátil espontáneo e insoportable en el primer molar inferior derecho. Al examen intraoral se observa tumefacción marcada en fondo de surco vestibular que borra el pliegue mucolabial, dolor exquisito al menor contacto o percusión, y ligera limitación de apertura bucal (trismus leve). La prueba térmica con frío es negativa absoluto. De acuerdo con lo enseñado por el profesor sobre el manejo de urgencia del Absceso Apical Agudo, ¿cuál es el diagnóstico y la conducta inmediata en el consultorio?",
        opciones=[
            "Absceso apical agudo; realizar descompresión y drenaje inmediato por conducto o incisión, colocar algodón estéril y temporal sin dejar abierto, y prescribir antibiótico por el trismus y celulitis.",
            "Pulpitis reversible aguda; realizar protección dentinopulpar indirecta y colocar restauración definitiva de ionómero en la misma cita.",
            "Periodontitis apical asintomática; obturar los conductos con gutapercha en una sola sesión y citar a control en un año.",
            "Osteítis condensante; aplicar flúor barniz en el margen gingival y no realizar ningún tratamiento biomecánico intraconducto."
        ],
        correcta=0,
        distractores=[
            "",
            "La pulpitis reversible presenta pulpa vital sin tumefacción vestibular ni dolor severo a la percusión.",
            "La periodontitis apical asintomática cursa sin dolor y está totalmente contraindicado obturar con pus o tumefacción activa.",
            "La osteítis condensante es una reacción ósea asintomática sin tumefacción submucosa ni dolor pulsátil agudo."
        ],
        explicacion="El cuadro de dolor pulsátil severo, tumefacción vestibular que deforma el fondo de surco, dolor exquisito al tacto y pulpa necrótica (frío negativo) corresponde a un Absceso apical agudo. El manejo de urgencia según el profesor comprende: 1) Apertura cameral y descompresión con drenaje a través del conducto (o incisión intraoral si hay fluctuación submucosa evidente); 2) Irrigación profusa con hipoclorito de sodio; 3) Colocar una mota de algodón estéril en la cámara y sellar con material temporal denso; el profesor enfatizó que NUNCA se debe dejar el diente destapado al medio bucal porque se sobreinfecta con flora oral; 4) Al existir celulitis con trismus o compromiso de espacios, se prescribe antibiótico sistémico (amoxicilina quinientos miligramos cada ocho horas durante siete días, o clindamicina trescientos miligramos en alérgicos).",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Diagnóstico periapical: absceso apical agudo",
        que="Reconocer el absceso apical agudo y aplicar el protocolo de urgencia con drenaje, sellado temporal y antibiótico por celulitis.",
        clave="El absceso apical agudo requiere drenaje inmediato, sellado hermético con algodón estéril (nunca dejar abierto) y antibiótico si hay trismus o celulitis.",
        pistas=[
            "Evalúa la combinación de pulpa necrótica con dolor exquisito y tumefacción vestibular difusa.",
            "Recuerda la regla estricta del profesor: jamás dejar el diente abierto a la saliva y medicar antibiótico ante trismus o celulitis."
        ],
        plan=[
            "Diagnosticar el absceso apical agudo correlacionando la necrosis y la tumefacción activa.",
            "Ejecutar la apertura cameral para drenaje y descompresión inmediata del pus.",
            "Sellar con algodón estéril y temporal, e indicar antibiótico por compromiso sistémico y trismus."
        ],
        marcas_data=[
            ("tumefacción marcada en fondo de surco vestibular que borra el pliegue mucolabial", "clave", "Signo cardinal de absceso agudo", "Apunta a colección purulenta submucosa"),
            ("ligera limitación de apertura bucal (trismus leve)", "dato", "Signo de alarma / diseminación", "Apunta a indicación precisa de antibioticoterapia"),
            ("¿cuál es el diagnóstico y la conducta inmediata en el consultorio?", "pide", "Diagnóstico y manejo de urgencia", "Demanda establecer protocolo completo de drenaje y medicación")
        ],
        steps_ideas=[
            ("idea", "Diagnóstico agudo", "La tumefacción vestibular con dolor pulsátil y necrosis pulpar define el absceso apical agudo."),
            ("idea", "Drenaje y sellado", "Se debe drenar por conducto; el profesor recalcó que nunca se deja el diente abierto, se sella con algodón estéril."),
            ("idea", "Antibióticos sistémicos", "Al haber trismus y celulitis se prescribe amoxicilina quinientos miligramos (o clindamicina en alérgicos)."),
            ("check", "Comprobación clínica", "Confirmamos absceso apical agudo manejado con drenaje, sellado temporal y antibiótico.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este caso de urgencia odontológica con dolor pulsátil intenso."),
            ("m:tumefacción marcada en fondo de surco vestibular que borra el pliegue mucolabial", "Observa la tumefacción vestibular que borra el surco y el dolor al menor tacto."),
            ("m:ligera limitación de apertura bucal (trismus leve)", "Fíjate que el paciente tiene además trismus y dificultad para abrir la boca."),
            ("leer", "El docente enseñó que el absceso apical agudo exige drenaje inmediato pero jamás dejar el diente abierto al medio bucal."),
            ("leer", "Al existir trismus y celulitis, la conducta incluye antibióticos sistémicos además del drenaje y sellado temporal.")
        ]
    ))

    # 12 (Key D = 3)
    qs.append(make_q(
        qid="odo-012", nivel=2,
        enunciado="En repetidas ocasiones a lo largo de la clase, el docente enfatiza a los estudiantes que «la radiografía periapical es una ayuda diagnóstica complementaria y nunca un medio de diagnóstico exclusivo». ¿Cuál de los siguientes ejemplos clínicos citados por el profesor en clase sustenta esta afirmación?",
        opciones=[
            "La radiografía periapical muestra con total exactitud si las bacterias intraconducto están vivas o muertas mediante la densidad de la película.",
            "Las radiografías periapicales digitales sustituyen por completo a las pruebas térmicas de frío y calor en cualquier diagnóstico pulpar.",
            "Una radiolucidez periapical solo aparece si el paciente refiere dolor espontáneo nocturno de más de diez días de evolución.",
            "Es una imagen bidimensional de algo tridimensional; una amalgama palatina puede parecer dentro de la cámara o un cono parecer salido por el trabeculado óseo sin estarlo."
        ],
        correcta=3,
        distractores=[
            "Las radiografías muestran sombras radiopacas y radiolúcidas de densidad mineral, no la viabilidad biológica microscópica bacteriana.",
            "La radiografía no evalúa vitalidad vascular ni sensorial de la pulpa; las pruebas térmicas son insustituibles.",
            "Muchas radiolucideces periapicales son completamente asintomáticas y se descubren de forma incidental.",
            ""
        ],
        explicacion="El profesor explicó que la radiografía aplana una estructura anatómica tridimensional en dos dimensiones. Como consecuencia de la superposición de planos, una restauración de amalgama en palatino puede proyectarse sobre la cámara pulpar pareciendo una invasión profunda sin serlo, o el trabeculado óseo denso puede dar la falsa ilusión de un cono pasado de ápice o un ápice aparente. Por ello, la radiografía nunca determina la vitalidad pulpar por sí sola y debe correlacionarse obligatoriamente con el examen clínico y las pruebas de sensibilidad.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Semiología radiográfica: rol de la radiografía periapical",
        que="Reconocer a la radiografía como examen complementario bidimensional sujeto a superposiciones anatómicas.",
        clave="La radiografía es una ayuda complementaria bidimensional donde la superposición de planos puede simular perforaciones o conos salidos.",
        pistas=[
            "Recuerda que la radiografía aplana un objeto tridimensional en un plano bidimensional.",
            "Ten presentes los ejemplos de la clase: amalgama palatina que parece dentro de la pulpa o conos que parecen pasados."
        ],
        plan=[
            "Comprender la naturaleza bidimensional de la proyección radiográfica periapical.",
            "Analizar los fenómenos de superposición anatómica de restauraciones y trabeculado.",
            "Concluir la necesidad de correlacionar siempre la imagen con las pruebas clínicas y térmicas."
        ],
        marcas_data=[
            ("«la radiografía periapical es una ayuda diagnóstica complementaria y nunca un medio de diagnóstico exclusivo»", "clave", "Axioma clínico del docente", "Apunta al carácter complementario y no absoluto de la imagen"),
            ("¿Cuál de los siguientes ejemplos clínicos citados por el profesor en clase sustenta esta afirmación?", "pide", "Ejemplo clínico de la clase", "Demanda identificar la limitación geométrica bidimensional")
        ],
        steps_ideas=[
            ("idea", "Limitación geométrica", "Una radiografía aplana estructuras tridimensionales en dos dimensiones."),
            ("idea", "Superposición de planos", "Una restauración palatina puede proyectarse sobre la cámara sin estar tocando la pulpa."),
            ("idea", "Trabeculado y ápice", "El trabeculado óseo puede dar la impresión de un ápice aparente o sobreobturación inexistente."),
            ("check", "Comprobación conceptual", "Verificamos que la radiografía es una ayuda complementaria sujeta a ilusiones ópticas por superposición.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos este principio fundamental de la semiología radiográfica repetido por el profesor."),
            ("m:«la radiografía periapical es una ayuda diagnóstica complementaria y nunca un medio de diagnóstico exclusivo»", "Nota que el docente insiste en que no se puede diagnosticar solo con una radiografía."),
            ("leer", "El docente recordó que la radiografía toma una estructura con tres dimensiones y la convierte en dos."),
            ("leer", "Por eso, una amalgama en palatino puede parecer dentro de la cámara, o un cono parecer salido sin estarlo."),
            ("leer", "Por lo tanto, la opción correcta describe con fidelidad esta limitación bidimensional enseñada en clase.")
        ]
    ))

    # 13 (Key B = 1)
    qs.append(make_q(
        qid="odo-013", nivel=2,
        enunciado="Un paciente de 24 años consulta porque notó un pequeño granito en la encía superior que ocasionalmente supura un líquido salado y luego se desinflama sin dolor. Al examen clínico no hay dolor a la percusión, la prueba térmica con frío es negativa absoluto y en la radiografía se observa una lesión radiolúcida periapical. ¿Cuál es el diagnóstico periapical y la conducta respecto al uso de antibióticos y medicación intraconducto?",
        opciones=[
            "Absceso apical agudo; prescribir antibióticos intravenosos por diez días y realizar incisión quirúrgica amplia de inmediato.",
            "Absceso apical crónico; no requiere antibióticos sistémicos; se realiza preparación biomecánica y medicación con hidróxido de calcio; la fístula cerrará en unos ocho días.",
            "Quiste periodontal lateral; no realizar endodoncia y derivar al periodoncista para raspaje y alisado radicular a campo abierto.",
            "Periodontitis apical sintomática por trauma oclusal; prescribir analgésicos narcóticos y mantener el diente sin aislamiento absoluto."
        ],
        correcta=1,
        distractores=[
            "El absceso agudo no tiene fístula de descompresión y cursa con tumefacción severa y dolor insoportable pulsátil.",
            "",
            "La lesión radiolúcida y la fístula se originan en el periápice por necrosis pulpar confirmada con frío negativo, no en el periodonto lateral.",
            "El trauma oclusal cursa con dolor agudo a la masticación y pulpa vital positiva al frío, sin fístula mucosa purulenta."
        ],
        explicacion="La presencia de un estoma fistuloso que drena de forma intermitente indolora asociado a necrosis pulpar (frío negativo) y radiolucidez periapical define un Absceso apical crónico. El docente enfatizó dos conceptos terapéuticos clave: 1) NO se medica con antibióticos, porque la fístula actúa como vía de drenaje natural evitando la acumulación de presión y diseminación sistémica; 2) El tratamiento es la instrumentación biomecánica del conducto con colocación de hidróxido de calcio llevado con léntulo en sentido antihorario o lima; al eliminar la fuente bacteriana del conducto, la fístula cicatriza y cierra espontáneamente en aproximadamente ocho días.",
        competencia="Terapéutica y Resolución de Casos Clínicos",
        afirmacion="Selecciona la conducta clínica apropiada, medidas de urgencia y protocolos biológicos de preservación o intervención pulpar.",
        tema="Diagnóstico periapical: absceso apical crónico",
        que="Identificar el absceso apical crónico con fístula y aplicar el tratamiento con hidróxido de calcio sin antibióticos.",
        clave="El absceso apical crónico drena por fístula, no requiere antibióticos sistémicos y la fístula cierra en ocho días con hidróxido de calcio.",
        pistas=[
            "Observa que el granito supura líquido salado y no duele (drenaje fistuloso continuo).",
            "Recuerda que si el proceso drena por fístula no se medican antibióticos y se coloca hidróxido de calcio."
        ],
        plan=[
            "Diagnosticar absceso apical crónico por presencia de estoma fistuloso y necrosis pulpar.",
            "Descartar la prescripción innecesaria de antibióticos sistémicos al existir drenaje activo.",
            "Indicar medicación con hidróxido de calcio y verificar el cierre fistuloso en ocho días."
        ],
        marcas_data=[
            ("pequeño granito en la encía superior que ocasionalmente supura un líquido salado", "clave", "Signo clínico de estoma fistuloso", "Apunta a drenaje crónico periapical"),
            ("frío es negativa absoluto y en la radiografía se observa una lesión radiolúcida", "dato", "Necrosis pulpar con lesión periapical", "Apunta a etiología bacteriana endodóntica"),
            ("¿Cuál es el diagnóstico periapical y la conducta respecto al uso de antibióticos y medicación intraconducto?", "pide", "Diagnóstico y conducta terapéutica", "Demanda establecer diagnóstico crónico y pauta sin antibióticos")
        ],
        steps_ideas=[
            ("idea", "Drenaje por fístula", "La fístula es una vía de escape que descomprime el pus, por lo que no hay dolor agudo."),
            ("idea", "No a los antibióticos", "El profesor enseñó expresamente que no se medica antibiótico en el absceso crónico fistulizado."),
            ("idea", "Hidróxido de calcio", "Al desinfectar el conducto con hidróxido de calcio, la fístula cierra por sí sola en unos ocho días."),
            ("check", "Comprobación clínica", "Verificamos absceso apical crónico tratado con hidróxido de calcio sin antibióticos.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este motivo de consulta muy frecuente en endodoncia."),
            ("m:pequeño granito en la encía superior que ocasionalmente supura un líquido salado", "Observa este detalle: un granito que bota pus salado de forma intermitente sin dolor."),
            ("m:frío es negativa absoluto y en la radiografía se observa una lesión radiolúcida", "La prueba de frío negativa y la mancha radiográfica confirman necrosis pulpar con fístula."),
            ("leer", "El docente enseñó que esto es un absceso apical crónico y que no necesita antibióticos porque ya está drenando."),
            ("leer", "El tratamiento es limpiar el conducto y colocar hidróxido de calcio, con lo cual la fístula cerrará en unos ocho días.")
        ]
    ))

    # 14 (Key A = 0) - REEMPLAZO CLASE 1
    qs.append(make_q(
        qid="odo-014", nivel=2,
        enunciado="Al tomar una radiografía periapical ortorradial convencional de un primer molar inferior con anatomía compleja, los dos conductos de la raíz mesial aparecen completamente superpuestos en la película radiográfica, simulando un conducto único. De acuerdo con lo explicado por el profesor en la clase (líneas novecientas seis a novecientas doce), ¿qué técnica radiográfica debe aplicar el clínico para disociar las raíces y conductos superpuestos y evitar iatrogenias?",
        opciones=[
            "Variar la angulación horizontal del tubo de rayos X tomando una proyección mesiorradial o distorradial para disociar las estructuras anatómicas superpuestas.",
            "Aumentar el tiempo de exposición al doble manteniendo la misma angulación ortorradial para que los conductos se transparenten en la película.",
            "Tomar una radiografía oclusal panorámica general asumiendo que los conductos convergen en un foramen común sin explorar.",
            "Iniciar la instrumentación con limas de grueso calibre a ciegas sin verificar la presencia de raíces o conductos accesorios."
        ],
        correcta=0,
        distractores=[
            "",
            "Aumentar el tiempo de exposición sobreexpone la película y la oscurece, sin separar geométricamente las raíces superpuestas.",
            "Una radiografía oclusal o panorámica no tiene la resolución espacial periapical necesaria para disociar conductos radiculares finos.",
            "Instrumentar a ciegas sin disociar conductos superpuestos provoca desvíos apicales, escalones y perforaciones radiculares graves."
        ],
        explicacion="El docente destacó en clase (líneas novecientas seis a novecientas doce) que cuando dos raíces o conductos se encuentran en el mismo plano bucolingual (como los conductos mesiovestibular y mesiolingual de los molares inferiores), la proyección ortorradial los superpone ocultando la anatomía real. La solución clínica consiste en angular el haz de rayos X en sentido horizontal (proyección mesioangulada o distoangulada); esto separa las sombras de las dos raíces o conductos en la imagen resultante, permitiendo identificar conductos curvos o raíces adicionales y evitando perforaciones o conductos no tratados.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Técnicas radiográficas: angulación horizontal para disociar raíces",
        que="Aplicar la variación de angulación horizontal de rayos X para separar raíces y conductos superpuestos.",
        clave="La angulación horizontal mesioangulada o distoangulada disocia conductos superpuestos en el plano bucolingual evitando perforaciones.",
        pistas=[
            "Recuerda la explicación del docente sobre cómo una raíz oculta a la otra si el rayo incide recto.",
            "Ten en cuenta que variar la angulación horizontal proyecta las dos raíces en posiciones separadas sobre la película."
        ],
        plan=[
            "Reconocer la limitación de la radiografía ortorradial ante raíces en el mismo plano bucolingual.",
            "Aplicar la angulación horizontal mesiorradial o distorradial para disociar las sombras radiográficas.",
            "Verificar la trayectoria anatómica individual de cada conducto para evitar iatrogenias."
        ],
        marcas_data=[
            ("dos conductos de la raíz mesial aparecen completamente superpuestos en la película radiográfica", "clave", "Superposición anatómica bucolingual", "Apunta a necesidad de disociación radiográfica"),
            ("¿qué técnica radiográfica debe aplicar el clínico para disociar las raíces y conductos superpuestos y evitar iatrogenias?", "pide", "Técnica de angulación radiográfica", "Demanda seleccionar la modificación de angulación horizontal")
        ],
        steps_ideas=[
            ("idea", "Superposición de conductos", "En proyección ortorradial los conductos vestibulares y linguales caen en el mismo rayo y se tapan."),
            ("idea", "Angulación horizontal", "El docente enseñó a variar el ángulo horizontal (mesiorradial o distorradial) para desfasar las raíces."),
            ("check", "Comprobación radiográfica", "Verificamos que la angulación horizontal mesio o distoangulada disocia los conductos superpuestos.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta situación anatómica cotidiana en la endodoncia de molares inferiores."),
            ("m:dos conductos de la raíz mesial aparecen completamente superpuestos en la película radiográfica", "Observa que al incidir el rayo de forma perpendicular recta, un conducto tapa al otro."),
            ("leer", "El docente explicó en clase que si nos quedamos con esa sola imagen podemos perforar o dejar un conducto sin limpiar."),
            ("leer", "La solución enseñada por el profesor es angular el cono de rayos X en sentido mesial o distal."),
            ("leer", "Al angular horizontalmente el tubo, las dos raíces se separan en la radiografía y se ve la anatomía real.")
        ]
    ))

    # 15 (Key C = 2)
    qs.append(make_q(
        qid="odo-015", nivel=3,
        enunciado="Un paciente adulto mayor presenta un incisivo central superior con antecedente de trauma antiguo. El diente exhibe una coloración café amarillenta por aposición de dentina terciaria y cámara pulpar retraída. En las pruebas de frío y electricidad no hay respuesta, pero radiográficamente no se observa ninguna zona radiolúcida periapical y los tejidos periapicales son normales. De acuerdo con el caso clínico enseñado por el profesor, ¿cuál es la prueba diagnóstica indicada antes de decidir el tratamiento?",
        opciones=[
            "Prueba de percusión vertical forzada empleando un percutor quirúrgico de impacto para valorar la estabilidad biomecánica de la corona.",
            "Prueba de tinción intragingival con solución de azul de metileno al dos por ciento sin aislamiento absoluto para detectar fisuras invisibles.",
            "Prueba de cavidad, que consiste en realizar un fresado superficial en esmalte y dentina sin anestesia local: si percibe dolor la pulpa está vital y se obtura con base intermedia.",
            "Prueba de aspiración transmucosa periapical con aguja hipodérmica de calibre grueso para verificar la presencia de exudado inflamatorio celular."
        ],
        correcta=2,
        distractores=[
            "La percusión forzada violenta no evalúa vitalidad pulpar y puede fracturar la raíz en un paciente mayor.",
            "La tinción de azul de metileno se usa en fisuras coronales expuestas, no para comprobar vitalidad pulpar en cámara calcificada.",
            "",
            "La aspiración transmucosa solo se realiza ante tumefacciones fluctuantes de abscesos agudos, no en tejidos periapicales normales."
        ],
        explicacion="El docente presentó este caso exacto en clase: en pacientes mayores con dientes que sufrieron trauma antiguo o envejecimiento fisiológico, la aposición de dentina reactiva calcifica y retrae la cámara pulpar. Como el grosor de dentina es masivo, el frío y la corriente eléctrica no logran estimular a las fibras pulpares produciendo un falso negativo, pero no hay lesión periapical. La prueba final enseñada por el profesor es la «prueba de cavidad»: se fresa el esmalte y la dentina superficial sin anestesia local; si el paciente manifiesta dolor o sensibilidad aguda, se confirma que la pulpa está vital y sana, por lo que se detiene el fresado, se coloca una base protectora intermedia y se sella la cavidad sin realizar endodoncia.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Pruebas especiales: test de cavidad en cámaras calcificadas",
        que="Aplicar la prueba de cavidad sin anestesia para confirmar la vitalidad pulpar en dientes calcificados con falso negativo térmico.",
        clave="La prueba de cavidad sin anestesia confirma la vitalidad pulpar en dientes con cámara retraída evitando endodoncias innecesarias.",
        pistas=[
            "Ten en cuenta que el gran grosor de dentina calcificada impide que el frío llegue a la pulpa.",
            "Recuerda el caso del profesor en paciente mayor: si al fresar sin anestesia siente dolor, la pulpa está viva y se sella."
        ],
        plan=[
            "Identificar el fenómeno de falso negativo térmico por obliteración y calcificación de la cámara.",
            "Seleccionar la prueba de cavidad como último recurso diagnóstico sin anestésico.",
            "Preservar la vitalidad pulpar colocando una base intermedia protectora si el paciente siente dolor."
        ],
        marcas_data=[
            ("coloración café amarillenta por aposición de dentina terciaria y cámara pulpar retraída", "dato", "Signo de calcificación dentinaria", "Apunta a barrera física que aísla térmicamente la pulpa"),
            ("frío y electricidad no hay respuesta, pero radiográficamente no se observa ninguna zona radiolúcida", "clave", "Sospecha de falso negativo", "Apunta a pulpa vital con respuesta térmica amortiguada"),
            ("¿cuál es la prueba diagnóstica indicada antes de decidir el tratamiento?", "pide", "Prueba diagnóstica especial", "Demanda seleccionar el test de cavidad")
        ],
        steps_ideas=[
            ("idea", "Falso negativo por dentina", "La dentina gruesa no deja pasar el frío ni la electricidad, simulando una necrosis inexistente."),
            ("idea", "Prueba de cavidad", "Se fresa suavemente la dentina sin anestesiar: si hay dolor, los túbulos y la pulpa están vitales."),
            ("idea", "Conducta conservadora", "Al confirmar dolor, se suspende la apertura de conductos, se coloca ionómero y se sella."),
            ("check", "Comprobación clínica", "Confirmamos la prueba de cavidad como método definitivo para verificar vitalidad en dientes calcificados.")
        ],
        lvl1_steps=[
            ("leer", "Analicemos este interesante caso clínico presentado por el profesor sobre un paciente adulto mayor."),
            ("m:coloración café amarillenta por aposición de dentina terciaria y cámara pulpar retraída", "Observa que el diente se puso café amarillento porque la cámara se llenó de dentina calcificada."),
            ("m:frío y electricidad no hay respuesta, pero radiográficamente no se observa ninguna zona radiolúcida", "Las pruebas térmicas dieron negativas pero no hay ninguna mancha ni infección en el periápice."),
            ("leer", "El docente explicó que la dentina gruesa aísla la pulpa y produce un falso negativo."),
            ("leer", "La prueba indicada por el profesor es fresar un poquito sin anestesia (prueba de cavidad): si siente dolor, la pulpa vive y se tapa.")
        ]
    ))

    # 16 (Key A = 0) - CORRECCIÓN CLAVE A
    qs.append(make_q(
        qid="odo-016", nivel=3,
        enunciado="Una paciente acude a la clínica manifestando un dolor agudo y difuso de gran intensidad que le abarca todo el lado derecho de la cara. Refiere angustiada que no logra identificar si el dolor proviene de un molar del maxilar superior o de la mandíbula. Las pruebas de sensibilidad son dudosas y no hay lesiones periapicales evidentes. De acuerdo con la técnica exacta enseñada por el profesor en clase (líneas seiscientas catorce a seiscientas veintinueve), ¿cuál es el procedimiento de anestesia selectiva indicado para localizar el origen del dolor?",
        opciones=[
            "Realizar un bloqueo del nervio dentario inferior: al anestesiar toda la mandíbula con una punción, si el dolor desaparece el origen era inferior; si persiste, el origen es superior.",
            "Iniciar aplicando anestesia infiltrativa en cada diente superior de forma individualizada de mesial a distal hasta que el paciente deje de sentir dolor facial.",
            "Anestesiar de manera simultánea los cuadrantes superior e inferior afectados con técnica infiltrativa y troncular combinada para suprimir el dolor en una sola sesión de trabajo.",
            "Proceder con la inducción de sedación intravenosa o anestesia general hospitalaria para anular toda respuesta nociceptiva del paciente y poder explorar ambos maxilares a la vez."
        ],
        correcta=0,
        distractores=[
            "",
            "La infiltración diente por diente en el maxilar superior es engorrosa y el anestésico difunde a dientes vecinos generando confusión diagnóstica antes de descartar la mandíbula.",
            "Anestesiar ambos maxilares a la vez suprime todo el dolor pero impide por completo saber de cuál de los dos maxilares procedía el problema.",
            "La anestesia general hospitalaria está totalmente desproporcionada y contraindicada para un diagnóstico diferencial odontológico de rutina."
        ],
        explicacion="En las líneas seiscientas catorce a seiscientas veintinueve de la clase, el docente corrigió a los estudiantes y enseñó la regla clínica precisa: cuando hay dolor difuso referido entre ambos maxilares, se debe bloquear primero el NERVIO DENTARIO INFERIOR. La razón biomecánica es que con una sola punción troncular se anestesia toda la hemiarcada mandibular de ese lado. Tras comprobar que el labio y la media lengua están dormidos: si el dolor del paciente desaparece por completo, se confirma con certeza que el diente causal era inferior; si el dolor persiste inalterado, se descarta la mandíbula y se procede a evaluar el maxilar superior diente por diente con técnica infiltrativa.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Procedimientos diagnósticos: anestesia selectiva",
        que="Aplicar la técnica de anestesia selectiva bloqueando primero el dentario inferior para dirimir dolor referido entre maxilares.",
        clave="La anestesia selectiva se inicia bloqueando el dentario inferior: si el dolor cesa era abajo, si persiste era arriba.",
        pistas=[
            "Recuerda la corrección del profesor en clase: con una sola punción duermes toda la mandíbula de ese lado.",
            "Ten en cuenta la comprobación clínica obligatoria: verificar que el labio y media lengua queden dormidos."
        ],
        plan=[
            "Identificar el cuadro de dolor difuso referido entre maxilar superior e inferior.",
            "Ejecutar la técnica de anestesia selectiva bloqueando en primer lugar el nervio dentario inferior.",
            "Interpretar la desaparición del dolor (origen mandibular) o su persistencia (origen maxilar)."
        ],
        marcas_data=[
            ("no logra identificar si el dolor proviene de un molar del maxilar superior o de la mandíbula", "clave", "Dolor referido entre arcos dentarios", "Apunta a necesidad de anestesia selectiva"),
            ("técnica exacta enseñada por el profesor en clase (líneas seiscientas catorce a seiscientas veintinueve)", "dato", "Referencia obligatoria a la clase", "Apunta a iniciar por bloqueo troncular mandibular"),
            ("¿cuál es el procedimiento de anestesia selectiva indicado para localizar el origen del dolor?", "pide", "Procedimiento de localización", "Demanda seleccionar el bloqueo del dentario inferior")
        ],
        steps_ideas=[
            ("idea", "Dolor referido", "La inervación sensitiva del trigémino puede referir dolor entre ramas mandibulares y maxilares."),
            ("idea", "Bloqueo mandibular inicial", "El profesor enseñó que se bloquea primero el dentario inferior con una sola punción troncular."),
            ("idea", "Interpretación de respuesta", "Si el dolor se quita era mandibular; si sigue doliendo era maxilar y se busca arriba."),
            ("check", "Comprobación clínica", "Confirmamos que se bloquea primero el dentario inferior comprobando labio y media lengua dormidos.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta pregunta clave de la clase donde el docente corrigió expresamente a los alumnos."),
            ("m:no logra identificar si el dolor proviene de un molar del maxilar superior o de la mandíbula", "Nota que el paciente no sabe si el diente enfermo está arriba o está abajo."),
            ("leer", "Un estudiante propuso anestesiar arriba primero, pero el docente lo corrigió: se anestesia primero abajo."),
            ("leer", "La razón del profesor es contundente: una sola inyección duerme toda la mandíbula inferior derecha."),
            ("leer", "Si el dolor se le quita al paciente, el diente era de abajo; si el dolor sigue, el diente era de arriba.")
        ]
    ))

    # 17 (Key D = 3)
    qs.append(make_q(
        qid="odo-017", nivel=2,
        enunciado="Un paciente de 40 años refiere dolor agudo punzante al masticar alimentos duros o granos en el primer premolar superior. El dolor aparece súbitamente al morder y cesa de inmediato al abrir la boca y liberar la presión oclusal. No refiere dolor espontáneo y las pruebas térmicas con frío son normales. De acuerdo con las explicaciones del profesor en clase, ¿cuál es el diagnóstico y la prueba clínica realizada cúspide por cúspide?",
        opciones=[
            "Absceso apical agudo con tumefacción intraoral fluctuante; prueba de fluctuación mucosa con sonda periodontal en fondo de saco.",
            "Necrosis pulpar total con fístula vestibular activa crónica; prueba de cavidad con fresado rotatorio sin anestesia en el surco central.",
            "Pulpitis irreversible asintomática con reabsorción interna; toma radiográfica con duplicación del tiempo de exposición en ortorradial.",
            "Síndrome del diente fisurado (fractura cuspídea incompleta); prueba de mordida selectiva con cuña de madera de operatoria cúspide por cúspide."
        ],
        correcta=3,
        distractores=[
            "El absceso apical cursa con tumefacción purulenta, dolor pulsátil continuo y necrosis pulpar, ausentes en este cuadro.",
            "La necrosis pulpar cursa con prueba de frío negativa absoluto y no produce dolor selectivo al liberar la mordida en cúspides aisladas.",
            "La reabsorción interna es un hallazgo radiográfico pulpar indoloro en estadios iniciales que no genera dolor al masticar granos duros.",
            ""
        ],
        explicacion="El dolor agudo y punzante que se desencadena típicamente con la masticación de consistencias duras y se intensifica al liberar la fuerza oclusal corresponde al síndrome del diente fisurado (fractura cuspídea incompleta). El docente explicó que para diagnosticarlo en el consultorio se utiliza una cuña de madera de operatoria (o instrumento similar) colocándola sobre cada cúspide individualmente e indicando al paciente que muerda; cuando la cúspide fisurada se flexiona bajo la carga, se reproduce el dolor agudo característico.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Patología dentaria: síndrome del diente fisurado",
        que="Identificar el síndrome del diente fisurado mediante la prueba de mordida con cuña de madera cúspide por cúspide.",
        clave="El dolor agudo al morder y soltar alimentos duros en un diente con pulpa vital corresponde a diente fisurado evaluado con cuña de madera.",
        pistas=[
            "Fíjate en el dolor punzante breve al morder granos duros que cesa al abrir la boca.",
            "Recuerda la técnica sencilla del profesor con la cuña de madera de operatoria probando cúspide por cúspide."
        ],
        plan=[
            "Correlacionar el dolor masticatorio selectivo con la flexión micromecánica de una cúspide fisurada.",
            "Verificar la vitalidad pulpar conservada en las pruebas térmicas basales.",
            "Aplicar la prueba de mordida con cuña de madera cúspide por cúspide para localizar la fractura incompleta."
        ],
        marcas_data=[
            ("dolor agudo punzante al masticar alimentos duros o granos", "dato", "Síntoma cardinal mecánico", "Apunta a fractura cuspídea incompleta"),
            ("aparece súbitamente al morder y cesa de inmediato al abrir la boca", "clave", "Dolor al liberar la carga", "Apunta a flexión elástica de la fisura"),
            ("¿cuál es el diagnóstico y la prueba clínica realizada cúspide por cúspide?", "pide", "Diagnóstico y prueba clínica", "Demanda identificar diente fisurado y cuña de madera")
        ],
        steps_ideas=[
            ("idea", "Mecánica de la fisura", "Al morder sobre una cúspide fisurada, los segmentos se separan estimulando bruscamente los túbulos."),
            ("idea", "Prueba de la cuña", "El docente enseñó a usar una cuña de madera de operatoria sobre cada cúspide para identificar la fracturada."),
            ("check", "Comprobación diagnóstica", "Confirmamos diente fisurado evaluado con mordida selectiva con cuña de madera.")
        ],
        lvl1_steps=[
            ("leer", "Revisemos con atención este motivo de consulta clásico por dolor agudo al masticar."),
            ("m:dolor agudo punzante al masticar alimentos duros o granos", "Observa que el dolor aparece específicamente al morder algo duro como un grano o cereal."),
            ("m:aparece súbitamente al morder y cesa de inmediato al abrir la boca", "Fíjate que al soltar la mordida la molestia se detiene y la pulpa está viva."),
            ("leer", "El docente explicó que esto corresponde al síndrome del diente fisurado."),
            ("leer", "Para confirmarlo, el docente enseñó a colocar una cuña de madera sobre cada cúspide hasta encontrar la que duele.")
        ]
    ))

    # 18 (Key B = 1) - CORRECCIÓN DIFUSA
    qs.append(make_q(
        qid="odo-018", nivel=2,
        enunciado="En la radiografía periapical de un primer molar inferior con una caries extensa y antecedentes de pulpitis sintomática previa, se observa una radiopacidad ósea difusa alrededor del ápice de la raíz mesial sin bordes circunscritos netos, conservando la línea del ligamento periodontal. La prueba de frío genera dolor que persiste varios segundos. De acuerdo con lo enseñado por el profesor en clase (líneas mil novecientas veinte a dos mil cuarenta), ¿cuál es el diagnóstico periapical y qué característica evolutiva tiene esta lesión?",
        opciones=[
            "Absceso apical agudo con celulitis facial difusa y compromiso sistémico; se resuelve con antibióticos en tres días.",
            "Osteítis condensante; reacción ósea radiopaca difusa que no desaparece tras el tratamiento endodóntico y requiere diferencial con cementomas si es circunscrita.",
            "Periodontitis apical asintomática con osteólisis destructiva aguda; requiere curetaje quirúrgico periapical inmediato.",
            "Displasia cementaria periapical en fase osteolítica inicial; no requiere ningún tipo de control posterior."
        ],
        correcta=1,
        distractores=[
            "El absceso agudo es una colección purulenta con dolor pulsátil y tumefacción, no una zona radiopaca asintomática densa.",
            "",
            "La periodontitis apical destructiva se manifiesta como una zona radiolúcida de pérdida ósea, no como una radiopacidad densa.",
            "La fase osteolítica de la displasia cementaria es radiolúcida (oscura), no radiopaca, y ocurre comúnmente en incisivos con pulpa sana."
        ],
        explicacion="En las líneas mil novecientas veinte a dos mil cuarenta del texto fuente, el profesor explicó detalladamente la osteítis condensante (osteoesclerosis periapical): es una reacción ósea proliferativa densa y radiopaca en respuesta a una irritación pulpar crónica de baja intensidad en pacientes jóvenes con buen potencial defensivo. El profesor recalcó dos conceptos fundamentales: 1) Es una imagen radiopaca DIFUSA alrededor del ápice, no circunscrita ni delimitada; si fuera muy redondeada y nítida se debe sospechar otra patología como hipercementosis o cementoma (displasia cementaria periapical); 2) La osteítis condensante NO desaparece tras la endodoncia; el hueso esclerótico permanece como cicatriz ósea asintomática a lo largo de los años.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Diagnóstico periapical: osteítis condensante difusa",
        que="Identificar la osteítis condensante como radiopacidad difusa periapical y comprender que no desaparece tras la endodoncia.",
        clave="La osteítis condensante es una radiopacidad periapical difusa (no circunscrita) que persiste como cicatriz ósea tras la endodoncia.",
        pistas=[
            "Ten en cuenta que se observa hueso radiopaco más blanco y denso alrededor del ápice.",
            "Recuerda la insistencia del profesor: la osteítis condensante es difusa y no desaparece con el tratamiento de conductos."
        ],
        plan=[
            "Reconocer la imagen radiopaca periapical asociada a irritación pulpar crónica.",
            "Distinguir el contorno difuso de la osteítis frente a las lesiones circunscritas como cementomas.",
            "Comprender la persistencia del hueso denso tras la culminación de la endodoncia."
        ],
        marcas_data=[
            ("radiopacidad ósea difusa alrededor del ápice de la raíz mesial sin bordes circunscritos", "clave", "Signo radiográfico cardinal", "Apunta a osteoesclerosis proliferativa reactiva"),
            ("antecedentes de pulpitis sintomática previa", "dato", "Estímulo inflamatorio crónico", "Apunta a respuesta del hueso ante toxinas pulpares"),
            ("¿cuál es el diagnóstico periapical y qué característica evolutiva tiene esta lesión?", "pide", "Diagnóstico y evolución", "Demanda identificar osteítis condensante difusa y su permanencia")
        ],
        steps_ideas=[
            ("idea", "Respuesta ósea proliferativa", "Ante toxinas de baja intensidad, el hueso periapical reacciona engrosando las trabéculas en vez de destruirse."),
            ("idea", "Carácter difuso", "El profesor insistió en que es radiopaca DIFUSA; si fuera muy circunscrita se sospecha cementoma."),
            ("idea", "Persistencia post-tratamiento", "La osteítis condensante no desaparece tras el tratamiento endodóntico, queda como cicatriz ósea."),
            ("check", "Comprobación diagnóstica", "Confirmamos osteítis condensante difusa que permanece en el hueso alveolar.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos con cuidado este hallazgo radiográfico en un molar con pulpitis crónica previa."),
            ("m:radiopacidad ósea difusa alrededor del ápice de la raíz mesial sin bordes circunscritos", "Observa que alrededor del ápice se ve una zona blanca radiopaca y DIFUSA."),
            ("leer", "El docente enseñó que cuando el hueso se pone más blanco y denso de forma difusa, es osteítis condensante."),
            ("leer", "Si los bordes fueran muy circunscritos y nítidos habría que pensar en cementoma o hipercementosis."),
            ("leer", "Además, el docente destacó que este hueso denso no desaparece después de hacer la endodoncia.")
        ]
    ))

    # 19 (Key C = 2)
    qs.append(make_q(
        qid="odo-019", nivel=2,
        enunciado="Al inicio de la clase, el profesor llama la atención sobre un dato fundamental que debe indagarse siempre en el interrogatorio del dolor dental: «¿El dolor le aumenta por las noches al acostarse?». ¿Cuál es el mecanismo fisiopatológico exacto que explica la exacerbación del dolor pulpar nocturno en posición decúbito?",
        opciones=[
            "Durante las horas de sueño descienden bruscamente los niveles séricos de cortisol endógeno, lo cual desactiva los mecanismos compensatorios de analgesia tisular periférica en el diente.",
            "El esmalte dental se contrae térmicamente por el enfriamiento del aire nocturno en la habitación generando tensiones mecánicas y microfracturas sobre la cámara pulpar.",
            "Al adoptar la posición horizontal en decúbito supino, aumenta la presión hidrostática y sanguínea cefálica, lo que incrementa la presión intrapulpar en una cámara inextensible y comprime las fibras nerviosas.",
            "Las bacterias orales anaerobias facultativas experimentan una proliferación exponencial durante la fase de menor salivación nocturna estimulando químicamente a los nociceptores periodontales."
        ],
        correcta=2,
        distractores=[
            "El ciclo circadiano del cortisol modula la inflamación general pero no explica el aumento mecánico inmediato de presión al acostarse en la cama.",
            "Las variaciones térmicas del dormitorio no son suficientes para contraer el esmalte ni comprimir mecánicamente la pulpa interna.",
            "",
            "La proliferación bacteriana en saliva no genera picos instantáneos de dolor al adoptar la postura horizontal."
        ],
        explicacion="En posición de pie o sentado, la gravedad favorece el drenaje venoso cefálico. Al pasar a la posición horizontal de decúbito supino para dormir, la presión hidrostática sanguínea en la cabeza aumenta considerablemente. En una pulpa con pulpitis irreversible donde ya existe vasodilatación y edema inflamatorio severo dentro de una cavidad dentaria rígida e inextensible, este incremento de presión cefálica eleva bruscamente la presión intrapulpar, comprimiendo intensamente las terminaciones nerviosas y despertando al paciente con dolor pulsátil agudo.",
        competencia="Diagnóstico Clínico Endodóntico",
        afirmacion="Determina la condición histopatológica pulpar y periapical correlacionando anamnesis, pruebas térmicas y hallazgos radiográficos.",
        tema="Anamnesis del dolor: mecanismo del dolor nocturno en decúbito",
        que="Explicar el incremento de presión hidrostática cefálica e intrapulpar como causa del dolor nocturno en decúbito.",
        clave="En posición decúbito horizontal aumenta la presión sanguínea cefálica, lo que incrementa la presión intrapulpar en una cavidad cerrada y exacerba el dolor.",
        pistas=[
            "Ten en cuenta el cambio físico gravitacional que ocurre al pasar de estar de pie a acostarse horizontalmente.",
            "Recuerda que la pulpa dental se encuentra encerrada en una cámara de paredes rígidas inextensibles."
        ],
        plan=[
            "Analizar la influencia de la postura corporal sobre la hemodinámica cefálica.",
            "Relacionar el aumento de presión hidrostática con la inextensibilidad de la cámara dentinaria.",
            "Concluir que la compresión de fibras nerviosas en decúbito es signo cardinal de pulpitis irreversible."
        ],
        marcas_data=[
            ("«¿El dolor le aumenta por las noches al acostarse?»", "clave", "Pregunta de anamnesis del dolor", "Apunta a componente postural en decúbito"),
            ("¿Cuál es el mecanismo fisiopatológico exacto que explica la exacerbación del dolor pulpar nocturno en posición decúbito?", "pide", "Mecanismo biofísico", "Demanda fundamentar el aumento de presión cefálica intrapulpar")
        ],
        steps_ideas=[
            ("idea", "Cambio postural", "Al acostarse, la cabeza queda al mismo nivel del corazón aumentando la presión sanguínea cefálica."),
            ("idea", "Cámara inextensible", "La dentina no se estira; cualquier aumento en el volumen vascular eleva de inmediato la presión intrapulpar."),
            ("check", "Comprobación biofísica", "Verificamos que el aumento de presión hidrostática en decúbito comprime las terminaciones nerviosas.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos esta pregunta clásica de la anamnesis resaltada por el profesor en la clase."),
            ("m:«¿El dolor le aumenta por las noches al acostarse?»", "Observa que el paciente refiere que el dolor se desata con fuerza al acostarse en la cama."),
            ("leer", "El docente explicó el motivo fisiológico: al acostarse horizontalmente, la sangre sube con mayor presión a la cabeza."),
            ("leer", "Como la pulpa está encerrada dentro de paredes duras de dentina que no se expanden, la presión interna se dispara."),
            ("leer", "Esa presión aplasta a las fibras nerviosas y desata el dolor pulsátil nocturno.")
        ]
    ))

    # 20 (Key D = 3)
    qs.append(make_q(
        qid="odo-020", nivel=2,
        enunciado="Durante la práctica, un estudiante toma el spray de gas refrigerante para realizar la prueba térmica de sensibilidad pulpar en un paciente. ¿Cuál es el protocolo estricto de aplicación enseñado por el docente y cuál es la tríada diagnóstica que debe registrarse según la respuesta del paciente?",
        opciones=[
            "Se debe rociar el aerosol congelante de manera directa y continua sobre la encía queratinizada y el surco gingival del diente sospechoso para insensibilizar previamente los mecanorreceptores.",
            "Se debe emplear una mota gigante de algodón densamente impregnada que haga contacto simultáneo sobre tres dientes contiguos para acelerar la exploración semiológica en el consultorio.",
            "Se debe sumergir completamente la arcada dental en agua con hielo triturado sin emplear rollos de algodón ni aislar piezas dentales vecinas.",
            "Se debe realizar aislamiento relativo con rollos de algodón, secar el diente con gasa o aire suave y aplicar una pequeña torunda impregnada con el refrigerante exclusivamente en el tercio medio vestibular del diente sano de control antes del diente sospechoso; si cede rápido es normal/reversible, si perdura es irreversible y si no siente es necrosis."
        ],
        correcta=3,
        distractores=[
            "Rociar spray congelante directamente en la mucosa gingival provoca quemaduras térmicas y no evalúa la pulpa del diente.",
            "Tocar varios dientes a la vez impide discriminar cuál diente responde y puede generar falsos positivos.",
            "Sumergir la arcada en agua con hielo enfría todos los dientes y tejidos blandos a la vez imposibilitando el diagnóstico individualizado.",
            ""
        ],
        explicacion="El protocolo estricto enseñado en clase incluye: 1) Aislamiento relativo con rollos de algodón y secado de la superficie dental con gasa o algodón (evitando chorros de aire frío que confundan la respuesta); 2) Rociar el spray en una torunda pequeña de algodón sostenida con la pinza (nunca directo en boca); 3) Aplicar en el tercio medio vestibular, evaluando primero un diente de control sano de la misma arcada o contralateral; 4) Aplicar la tríada diagnóstica: si el dolor cesa en uno o dos segundos la pulpa está sana o reversible; si perdura más de treinta segundos tras retirar el algodón es pulpitis irreversible sintomática; si no hay ninguna respuesta en absoluto es necrosis pulpar.",
        competencia="Semiología y Exámenes Complementarios",
        afirmacion="Aplica e interpreta pruebas diagnósticas especiales, técnicas radiográficas de angulación y examen periodontal en endodoncia.",
        tema="Semiología pulpar: protocolo de la prueba de frío",
        que="Aplicar el protocolo técnico de la prueba de frío y registrar la tríada diagnóstica de la respuesta pulpar.",
        clave="La prueba de frío exige aislamiento, secado, torunda pequeña en tercio medio vestibular, inicio en diente sano y aplicación de la tríada diagnóstica.",
        pistas=[
            "Recuerda que nunca se rocía el spray congelante directo en la boca por riesgo de quemadura.",
            "Ten presente el protocolo: aislamiento relativo, secado, torunda en tercio medio y evaluar primero el diente de control sano."
        ],
        plan=[
            "Establecer las medidas de bioseguridad y aislamiento relativo para la prueba de frío.",
            "Identificar el tercio medio vestibular como la zona óptima de aplicación sobre esmalte limpio.",
            "Correlacionar la respuesta térmica con la tríada clínica de salud, pulpitis irreversible o necrosis."
        ],
        marcas_data=[
            ("protocolo estricto de aplicación enseñado por el docente", "clave", "Metodología semiológica correcta", "Demanda aislamiento, secado, torunda pequeña y diente control"),
            ("cuál es la tríada diagnóstica que debe registrarse según la respuesta del paciente", "pide", "Interpretación de resultados", "Demanda vincular el tiempo de respuesta con el diagnóstico")
        ],
        steps_ideas=[
            ("idea", "Preparación del campo", "Se aísla con rollos de algodón y se seca con gasa para que la humedad no desvíe el frío."),
            ("idea", "Aplicación puntual", "Se impregna una bolita pequeña de algodón con la pinza y se coloca en el tercio medio vestibular."),
            ("idea", "Diente de control y tríada", "Se prueba primero en un diente sano; si el dolor cede rápido es sana/reversible, si perdura es irreversible, si no siente es necrosis."),
            ("check", "Comprobación del protocolo", "Verificamos el protocolo completo con torunda pequeña en tercio medio e inicio en diente de control.")
        ],
        lvl1_steps=[
            ("leer", "Examinemos con cuidado el protocolo estricto que el docente exige para la prueba de frío."),
            ("m:protocolo estricto de aplicación enseñado por el docente", "Observa que no se puede improvisar rociando spray a lo loco en la boca."),
            ("leer", "El docente enseñó a poner rollos de algodón para aislar, secar el diente con una gasa y usar una torunda pequeña."),
            ("leer", "Se aplica en el tercio medio de la corona y siempre se prueba primero un diente sano de control."),
            ("leer", "La tríada enseñada por el profesor es clara: si pasa rápido es sana o reversible, si dura más de treinta segundos es irreversible y si no siente es necrosis.")
        ]
    ))

    return qs
