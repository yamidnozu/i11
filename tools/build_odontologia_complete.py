"""Generador del banco completo de Odontología (Endodoncia) con 30 casos y preguntas.
Fuente: docs/fuentes/endodoncia-clase1-3corte.txt
"""
import json

LETTERS = ['A', 'B', 'C', 'D']

def make_q(qid, nivel, enunciado, opciones, correcta, distractores, explicacion, tema, que, clave, pistas, marcas_data, steps_ideas):
    marcas = [{"frag": m[0], "rol": m[1], "campo": m[2], "nota": m[2]} for m in marcas_data]
    pasos = [
        {"k": "idea", "titulo": steps_ideas[0][0], "texto": steps_ideas[0][1]},
        {"k": "idea", "titulo": steps_ideas[1][0], "texto": steps_ideas[1][1]},
        {"k": "check", "texto": steps_ideas[2][1]}
    ]
    no_items = []
    for i, d in enumerate(distractores):
        if i != correcta and d:
            no_items.append({"t": f"Opción {LETTERS[i]}", "p": f"Pero {d[0].lower() + d[1:]}"})
    correct_letter = LETTERS[correcta]
    lvl2 = [
        {"a": "leer", "t": "Revisemos con atención por qué se descartan las alternativas incorrectas."}
    ]
    for i, d in enumerate(distractores):
        if i != correcta:
            lvl2.append({"a": f"o:{LETTERS[i]}:no", "k": "err", "t": f"La opción {LETTERS[i]} no corresponde: {d}"})
    lvl2.append({"a": f"o:{correct_letter}:ok", "t": f"Por descarte clínico y confirmación de signos, la opción {correct_letter} es la adecuada."})
    lvl1 = [
        {"a": "leer", "t": "Analicemos los datos principales del cuadro clínico presentado."},
        {"a": f"m:{marcas_data[0][0]}", "t": f"Fíjate en el hallazgo clave: {marcas_data[0][0]}."},
        {"a": f"o:{correct_letter}:ok", "t": f"La respuesta correcta corresponde a la opción {correct_letter}: {opciones[correcta]}."}
    ]
    lvl3 = [
        {"a": "p:0", "k": "ana", "t": "Integramos el motivo de consulta con las pruebas de sensibilidad y el examen periapical."},
        {"a": "p:1", "k": "por", "t": clave},
        {"a": f"o:{correct_letter}:ok", "t": f"Concluimos con certeza que la opción correcta es {correct_letter}."}
    ]
    hoja = {
        "modo": "concepto",
        "marcas": marcas,
        "pasos": pasos,
        "enfoque": {
            "tema": tema,
            "que": que,
            "clave": clave,
            "pistas": pistas,
            "plan": [
                {"t": "Identificar los síntomas cardinales y la historia del dolor en la anamnesis."},
                {"t": "Evaluar la respuesta pulpar frente a las pruebas térmicas y mecánicas."},
                {"t": "Correlacionar los hallazgos para establecer el diagnóstico y plan de tratamiento."}
            ],
            "no": no_items
        },
        "guion": {
            "1": lvl1,
            "2": lvl2,
            "3": lvl3
        }
    }
    return {
        "id": qid,
        "area": "odontologia",
        "nivel": nivel,
        "tipo": "multiple",
        "origen": "propio",
        "enunciado": enunciado,
        "opciones": opciones,
        "correcta": correcta,
        "distractores": distractores,
        "explicacion": explicacion,
        "hoja": hoja
    }

questions = []

# 01 (Key 0: A)
questions.append(make_q(
    qid="odo-001", nivel=2,
    enunciado="Un paciente de 28 años consulta por dolor agudo y punzante en el primer molar inferior izquierdo. Relata que el dolor se desencadena con bebidas frías y persiste durante varios minutos tras retirar el vaso, además de presentarse de forma espontánea por las noches al acostarse. Al examen clínico no hay dolor a la percusión ni a la palpación apical, y la prueba térmica con frío genera un dolor intenso que permanece por más de treinta segundos. ¿Cuál es el diagnóstico pulpar más probable?",
    opciones=[
        "Pulpitis irreversible sintomática.",
        "Pulpitis reversible.",
        "Necrosis pulpar.",
        "Periodontitis apical sintomática."
    ],
    correcta=0,
    distractores=[
        "",
        "En la pulpitis reversible el dolor provocado cesa de inmediato a los pocos segundos de retirar el estímulo y nunca se presenta de forma espontánea ni nocturna.",
        "La necrosis pulpar cursa con muerte del tejido pulpar y por tanto presenta ausencia total de respuesta a las pruebas de sensibilidad térmica con frío.",
        "La periodontitis apical sintomática es una patología de los tejidos periapicales que se manifiesta con dolor agudo a la percusión y a la masticación, ausentes en este cuadro."
    ],
    explicacion="El cuadro clínico combina dolor provocado que perdura en el tiempo tras cesar el estímulo (más de treinta segundos), dolor espontáneo y dolor nocturno en posición decúbito. Estos signos cardinales reflejan inflamación pulpar avanzada irreversible con incremento de la presión intrapulpar, lo que define una pulpitis irreversible sintomática.",
    tema="Diagnóstico pulpar: pulpitis irreversible sintomática",
    que="Determinar el diagnóstico pulpar a partir de la respuesta prolongada al frío y dolor nocturno.",
    clave="La persistencia del dolor tras retirar el estímulo y la presencia de dolor nocturno definen la pulpitis irreversible sintomática.",
    pistas=[
        "Evalúa cuánto tiempo perdura la molestia una vez que retiras el frío del diente.",
        "Ten presente que el dolor que despierta al paciente en la noche traduce inflamación pulpar severa."
    ],
    marcas_data=[
        ("persiste durante varios minutos tras retirar el vaso", "clave", "Dolor prolongado tras estímulo"),
        ("espontánea por las noches al acostarse", "dato", "Dolor nocturno por decúbito"),
        ("¿Cuál es el diagnóstico pulpar más probable?", "pide", "Determinar diagnóstico pulpar")
    ],
    steps_ideas=[
        ("Análisis del dolor", "El dolor térmico que perdura tras retirar el estímulo indica daño irreversible en el tejido pulpar."),
        ("Signo de decúbito", "El dolor nocturno ocurre por el aumento de presión cefálica que distiende las paredes rígidas de la cámara pulpar."),
        ("Comprobación diagnóstica", "Confirmamos que la persistencia del dolor al frío y la espontaneidad corresponden a pulpitis irreversible sintomática.")
    ]
))

# 02 (Key 1: B)
questions.append(make_q(
    qid="odo-002", nivel=2,
    enunciado="Durante la explicación de la fisiología del dolor pulpar en clase, el profesor profundiza en las diferencias entre las fibras nerviosas que inervan la pulpa dental. Respecto a las fibras C amielínicas, ¿cuál de las siguientes afirmaciones describe con precisión sus características clínicas y fisiológicas?",
    opciones=[
        "Son mielinizadas de conducción rápida y transmiten un dolor agudo, punzante y bien localizado ante estímulos fríos leves.",
        "Son amielínicas, poseen un umbral de excitación alto, resisten mejor la hipoxia y transmiten un dolor sordo, urente y mal localizado.",
        "Se ubican predominantemente en la unión amelodentinaria y responden exclusivamente a la deformación hidrodinámica de los túbulos.",
        "Inervan el ligamento periodontal y se encargan de la propiocepción y localización exacta del diente afectado a la percusión."
    ],
    correcta=1,
    distractores=[
        "La descripción de fibras mielinizadas de conducción rápida y dolor punzante y agudo al frío corresponde a las fibras A-delta.",
        "",
        "La ubicación en la unión amelodentinaria asociada a la teoría hidrodinámica corresponde a las terminaciones de las fibras A-delta, no a las fibras C.",
        "Las fibras propioceptivas y mecanorreceptoras corresponden a la inervación periapical y periodontal, no a las fibras C del estoma pulpar interno."
    ],
    explicacion="Las fibras C son fibras amielínicas situadas en el estroma profundo de la pulpa. Requieren estímulos de mayor intensidad (umbral alto), toleran mejor la hipoxia y su activación traduce inflamación tisular avanzada con dolor difuso, sordo, pulsátil o urente, a diferencia de las fibras A-delta que son mielínicas y de respuesta rápida y punzante.",
    tema="Inervación pulpar: fibras A-delta y fibras C",
    que="Diferenciar las propiedades fisiológicas y clínicas de las fibras C pulpares.",
    clave="Las fibras C son amielínicas, de conducción lenta y umbral alto, y producen dolor sordo y mal localizado.",
    pistas=[
        "Recuerda que las fibras amielínicas se localizan en el núcleo pulpar y toleran mejor la hipoxia.",
        "Ten en cuenta que el dolor urente y pulsátil continuo es transmitido por las fibras C."
    ],
    marcas_data=[
        ("fibras C amielínicas", "clave", "Estructura nerviosa objeto de la pregunta"),
        ("¿cuál de las siguientes afirmaciones describe con precisión sus características clínicas y fisiológicas?", "pide", "Identificar propiedades de fibras C")
    ],
    steps_ideas=[
        ("Fibras A-delta frente a fibras C", "Las fibras A-delta son mielínicas periféricas y rápidas; las fibras C son amielínicas centrales y lentas."),
        ("Expresión clínica", "El dolor mediado por fibras C es sordo, pulsátil y traduce daño tisular profundo en la pulpa."),
        ("Comprobación diagnóstica", "Verificamos que las fibras C son amielínicas, de umbral alto y responsables del dolor sordo y difuso.")
    ]
))

# 03 (Key 2: C)
questions.append(make_q(
    qid="odo-003", nivel=2,
    enunciado="Un paciente de 35 años acude a consulta refiriendo dolor agudo y breve en un premolar superior al consumir bebidas muy frías. El dolor aparece únicamente cuando el líquido entra en contacto con el diente y desaparece por completo dos segundos después de tragarlo. No refiere dolor espontáneo ni molestias nocturnas. Al examen clínico se observa una restauración de resina con desadaptación marginal leve, sin dolor a la percusión ni cambios periapicales radiográficos. ¿Cuál es el diagnóstico pulpar y la conducta clínica adecuada?",
    opciones=[
        "Pulpitis irreversible sintomática; requiere biopulpectomía de urgencia.",
        "Necrosis pulpar; requiere tratamiento de conductos y medicación intraconducto.",
        "Pulpitis reversible; requiere retirar la restauración desadaptada y realizar protección dentinopulpar.",
        "Periodontitis apical sintomática; requiere ajuste oclusal y ferulización inmediata."
    ],
    correcta=2,
    distractores=[
        "La pulpitis irreversible sintomática presenta dolor persistente por minutos tras retirar el estímulo y suele cursar con dolor espontáneo nocturno.",
        "La necrosis pulpar presenta ausencia total de respuesta al frío por desvitalización del tejido pulpar.",
        "",
        "La periodontitis apical sintomática se caracteriza por dolor notable a la percusión vertical y masticación, los cuales son negativos en este paciente."
    ],
    explicacion="Una respuesta dolorosa al frío que cesa de inmediato (uno a dos segundos) tras retirar el estímulo, en ausencia de dolor espontáneo o nocturno, define una pulpitis reversible. La pulpa conserva su capacidad de reparación una vez eliminado el factor irritante local (la filtración marginal de la resina) mediante una nueva restauración con adecuada protección dentinopulpar.",
    tema="Diagnóstico pulpar: pulpitis reversible",
    que="Identificar el cuadro de pulpitis reversible y su tratamiento conservador.",
    clave="El dolor provocado que desaparece casi de inmediato sin dolor espontáneo caracteriza a la pulpitis reversible.",
    pistas=[
        "Observa que el dolor no perdura una vez que el estímulo frío se retira.",
        "Recuerda que una pulpa reversible tiene capacidad biológica de recuperarse si eliminas la filtración."
    ],
    marcas_data=[
        ("desaparece por completo dos segundos después de tragarlo", "clave", "Cese inmediato del dolor"),
        ("No refiere dolor espontáneo ni molestias nocturnas", "dato", "Ausencia de signos irreversibles"),
        ("¿Cuál es el diagnóstico pulpar y la conducta clínica adecuada?", "pide", "Diagnóstico y conducta")
    ],
    steps_ideas=[
        ("Tiempo de respuesta", "El dolor térmico que se detiene en un lapso de dos segundos indica que el tejido pulpar no está irreversiblemente dañado."),
        ("Manejo conservador", "Al eliminar la causa mecánica o microbiana y proteger la dentina, la pulpa cicatriza sin necesidad de endodoncia."),
        ("Comprobación diagnóstica", "Verificamos que el cuadro clínico corresponde a pulpitis reversible con manejo restaurador conservador.")
    ]
))

# 04 (Key 3: D)
questions.append(make_q(
    qid="odo-004", nivel=3,
    enunciado="Al realizar el examen intraoral de un paciente, el odontólogo detecta un estoma fistuloso activo con salida de exudado purulento ubicado en la encía vestibular entre el segundo premolar y el primer molar superior derecho. Ambos dientes presentan restauraciones coronales extensas y el paciente no recuerda cuál presentó dolor previo. De acuerdo con las enseñanzas del docente en clase sobre el examen clínico, ¿cuál es el procedimiento indicado para identificar con certeza el diente causal?",
    opciones=[
        "Iniciar la apertura coronal de ambos dientes de forma simultánea para explorar visualmente la cámara pulpar.",
        "Realizar una biopsia por escisión del estoma fistuloso y enviar la muestra a estudio anatomopatológico.",
        "Prescribir antibióticos sistémicos durante siete días y esperar a que la fístula desaparezca espontáneamente.",
        "Introducir con suavidad un cono de gutapercha radiopaco por el estoma fistuloso y tomar una radiografía periapical para seguir el trayecto hasta el ápice del diente causal."
    ],
    correcta=3,
    distractores=[
        "Abrir ambos dientes de manera invasiva sin diagnóstico causal vulnera la integridad de un diente que podría estar vital y sano.",
        "La biopsia de la fístula no está indicada en primera instancia ante una lesión de claro origen odontogénico bacteriano.",
        "Los antibióticos no resuelven la causa infecciosa necrótica intraconducto y no permiten identificar qué diente origina la fístula.",
        ""
    ],
    explicacion="La fistulografía es la prueba clínica indicada cuando una fístula se encuentra en una posición intermedia o dudosa. Consiste en insertar suavemente un cono de gutapercha (habitualmente de calibre intermedio como calibre treinta) a través del trayecto fistuloso hasta topar resistencia y tomar una radiografía periapical. El cono radiopaco señalará con exactitud matemática el ápice radicular del diente responsable de la infección.",
    tema="Procedimientos diagnósticos: fistulografía",
    que="Identificar el diente causal de una fístula mediante fistulografía con cono de gutapercha.",
    clave="La inserción de un cono de gutapercha radiopaco por el trayecto fistuloso señala el diente origen en la radiografía.",
    pistas=[
        "Recuerda la técnica comentada por el profesor para no tener que adivinar entre dos dientes vecinos.",
        "Aprovecha las propiedades radiopacas de la gutapercha para el rastreo en la radiografía."
    ],
    marcas_data=[
        ("estoma fistuloso activo con salida de exudado purulento", "dato", "Presencia de fístula"),
        ("entre el segundo premolar y el primer molar superior derecho", "clave", "Ubicación intermedia entre dos dientes"),
        ("¿cuál es el procedimiento indicado para identificar con certeza el diente causal?", "pide", "Procedimiento de localización")
    ],
    steps_ideas=[
        ("Rastreo fistuloso", "El trayecto de una fístula puede recorrer distancias considerables antes de perforar la cortical ósea."),
        ("Fistulografía con gutapercha", "La gutapercha es flexible y radiopaca, lo que permite trazar el trayecto exacto en la radiografía sin traumatizar."),
        ("Comprobación diagnóstica", "Confirmamos que la fistulografía con cono de gutapercha es el procedimiento estándar enseñado en clase.")
    ]
))

# 05 (Key 0: A)
questions.append(make_q(
    qid="odo-005", nivel=2,
    enunciado="Un paciente de 42 años asiste a control odontológico de rutina completamente asintomático. En la radiografía periapical se observa de forma casual una zona radiolúcida periapical circunscrita y redondeada alrededor del ápice del incisivo central superior derecho. En las pruebas de sensibilidad pulpar con frío y vitalómetro eléctrico el diente no responde (negativo absoluto), y a la percusión y palpación no manifiesta molestia alguna. ¿Cuál es el diagnóstico pulpar y periapical correcto?",
    opciones=[
        "Necrosis pulpar con periodontitis apical asintomática.",
        "Pulpitis reversible con periodontitis apical sintomática.",
        "Pulpitis irreversible sintomática con tejidos periapicales normales.",
        "Diente previamente tratado con absceso apical agudo."
    ],
    correcta=0,
    distractores=[
        "",
        "En la pulpitis reversible la pulpa está vital y responde positivamente al frío, y la periodontitis apical sintomática cursa con dolor notable a la percusión.",
        "La pulpitis irreversible sintomática presenta respuesta térmica positiva exagerada y dolor espontáneo continuo, ausentes en un diente desvitalizado y asintomático.",
        "El diente no ha recibido obturación de conductos previa y el absceso agudo se caracteriza por tumefacción y dolor pulsátil severo."
    ],
    explicacion="La falta absoluta de respuesta a las pruebas de sensibilidad pulpar (frío y electricidad) confirma la necrosis pulpar (muerte del paquete vasculonervioso). La presencia de una zona radiolúcida periapical sin dolor a la masticación ni a la percusión corresponde a una periodontitis apical asintomática (granuloma o quiste periapical de origen inflamatorio crónico).",
    tema="Diagnóstico pulpar y periapical: necrosis y periodontitis apical asintomática",
    que="Integrar la necrosis pulpar con el hallazgo radiográfico periapical asintomático.",
    clave="La respuesta negativa a pruebas térmicas con lesión radiolúcida indolora define necrosis pulpar con periodontitis apical asintomática.",
    pistas=[
        "Evalúa que la ausencia de respuesta térmica indica desvitalización pulpar completa.",
        "Ten en cuenta que la lesión periapical sin dolor a la percusión clasifica como asintomática."
    ],
    marcas_data=[
        ("diente no responde (negativo absoluto)", "clave", "Signo de necrosis pulpar"),
        ("zona radiolúcida periapical circunscrita y redondeada", "dato", "Lesión ósea periapical"),
        ("¿Cuál es el diagnóstico pulpar y periapical correcto?", "pide", "Diagnóstico integrado")
    ],
    steps_ideas=[
        ("Evaluación de la vitalidad", "La falta de respuesta a frío y vitalómetro confirma la muerte pulpar (necrosis)."),
        ("Evaluación del periápice", "La lesión ósea radiolúcida sin dolor clínico define la periodontitis apical asintomática."),
        ("Comprobación diagnóstica", "Verificamos que el diagnóstico integrado es necrosis pulpar con periodontitis apical asintomática.")
    ]
))

# 06 (Key 1: B)
questions.append(make_q(
    qid="odo-006", nivel=2,
    enunciado="Durante la práctica clínica, el docente le pide a un estudiante palpar un abultamiento nodular en la encía adherida sobre la raíz de un diente con endodoncia realizada hace cinco años. El estudiante nota que la lesión es firme, dura, indolora a la presión digital y no drena pus ni líquido. Con base en la discusión clínica de la clase sobre la palpación periapical, ¿cuál es la interpretación correcta de este hallazgo?",
    opciones=[
        "Se trata de un absceso apical agudo en fase inicial de licuefacción que requiere incisión quirúrgica inmediata.",
        "Se trata de una cicatriz fibrosa de una fístula antigua curada, formada por tejido colágeno duro tras el tratamiento de conductos previo.",
        "Corresponde a una perla del esmalte ubicada anatómicamente en el tercio apical de la superficie radicular de cemento.",
        "Representa una reactivación infecciosa activa que exige prescribir amoxicilina de inmediato."
    ],
    correcta=1,
    distractores=[
        "Un absceso apical agudo es sumamente blando, eritematoso, doloroso a la palpación y con contenido líquido fluctuante, no firme ni duro.",
        "",
        "Las perlas del esmalte son anomalías adamantinas de la corona o furca, no estructuras de tejido blando en la encía vestibular apical.",
        "Una masa fibrosa dura e indolora que no drena exudado no es una infección bacteriana activa y no requiere antibioterapia."
    ],
    explicacion="El profesor enfatiza en clase que no todo nódulo gingival representa una fístula activa o pus. Una fístula que drenó por mucho tiempo y luego cicatrizó tras un tratamiento de conductos exitoso deja con frecuencia un nódulo fibroso, duro a la palpación, asintomático y sin secreción purulenta: una cicatriz de fístula.",
    tema="Examen clínico: palpación y cicatriz de fístula",
    que="Diferenciar una fístula activa de una cicatriz fibrosa de fístula mediante palpación.",
    clave="La palpación dura, indolora y sin exudado en una encía con endodoncia antigua corresponde a una cicatriz de fístula.",
    pistas=[
        "Recuerda la anécdota del profesor cuando preguntó qué pasaba si palpaba y la lesión estaba dura y no salía pus.",
        "Distingue la consistencia blanda y fluctuante de la pus frente al tejido fibroso cicatrizal."
    ],
    marcas_data=[
        ("lesión es firme, dura, indolora a la presión digital y no drena pus", "clave", "Características a la palpación"),
        ("¿cuál es la interpretación correcta de este hallazgo?", "pide", "Interpretación de palpación")
    ],
    steps_ideas=[
        ("Consistencia del tejido", "La consistencia dura e indolora descarta la presencia de exudado purulento o absceso activo."),
        ("Antecedente de tratamiento", "El tejido colágeno cicatrizal persiste como un nódulo fibroso asintomático tras el cierre de una fístula crónica."),
        ("Comprobación diagnóstica", "Concluimos que el hallazgo corresponde a una cicatriz fibrosa de una fístula antigua.")
    ]
))

# 07 (Key 2: C)
questions.append(make_q(
    qid="odo-007", nivel=2,
    enunciado="Un paciente de 50 años asiste muy angustiado al consultorio refiriendo dolor severo al masticar en el segundo premolar inferior derecho, donde le cementaron una corona metalocerámica hace dos días. Describe que al cerrar la boca siente que ese diente choca antes que todos los demás y se le desencadena una molestia insoportable. Al examen clínico, la percusión vertical y la masticación con papel de articular generan dolor intenso y marcan un contacto prematuro marcado, pero la prueba de frío muestra una respuesta térmica normal que desaparece a los dos segundos. ¿Cuál es el diagnóstico y la conducta de elección?",
    opciones=[
        "Necrosis pulpar; realizar apertura coronal y biopulpectomía de inmediato.",
        "Pulpitis irreversible sintomática; remover la corona y desvitalizar el diente.",
        "Periodontitis apical por trauma oclusal secundaria a contacto prematuro; realizar ajuste oclusal desgastando el punto alto sin endodoncia.",
        "Fractura radicular vertical completa; proceder a la exodoncia quirúrgica inmediata."
    ],
    correcta=2,
    distractores=[
        "La necrosis pulpar cursa con prueba térmica negativa, mientras que este diente tiene vitalidad pulpar completamente sana.",
        "La pulpitis irreversible sintomática se caracteriza por dolor prolongado al frío de minutos de duración y dolor nocturno, ausentes aquí.",
        "",
        "El cuadro se inició inmediatamente tras la cementación de una restauración alta sin antecedentes de traumatismo ni líneas de fractura al sondaje."
    ],
    explicacion="El profesor explica la analogía de la piedra en el zapato: una restauración con un contacto oclusal prematuro somete al ligamento periodontal a una sobrecarga traumática continua, generando periodontitis apical por trauma oclusal. Dado que la pulpa responde con normalidad al frío (vitalidad conservada), el tratamiento no es endodóntico, sino mecánico: alivio oclusal mediante desgaste selectivo del punto prematuro.",
    tema="Diagnóstico diferencial: periodontitis apical por trauma oclusal",
    que="Reconocer la periodontitis apical por sobrecarga oclusal en un diente con pulpa vital.",
    clave="Un contacto oclusal prematuro produce dolor agudo a la masticación con pulpa vital sana; se trata únicamente con ajuste oclusal.",
    pistas=[
        "Observa que la prueba térmica con frío en el diente es completamente normal.",
        "Recuerda la analogía del profesor sobre la piedra en el zapato que inflama el ligamento periodontal."
    ],
    marcas_data=[
        ("siente que ese diente choca antes que todos los demás", "dato", "Contacto prematuro"),
        ("prueba de frío muestra una respuesta térmica normal que desaparece a los dos segundos", "clave", "Pulpa vital y sana"),
        ("¿Cuál es el diagnóstico y la conducta de elección?", "pide", "Diagnóstico y conducta")
    ],
    steps_ideas=[
        ("Evaluación de la pulpa", "La respuesta normal al frío demuestra que la pulpa no está infectada ni necrosada."),
        ("Mecanismo lesional", "El ligamento periodontal está inflamado agudamente por trauma mecánico de oclusión (punto alto)."),
        ("Comprobación diagnóstica", "El diagnóstico es periodontitis apical por trauma oclusal y se resuelve con ajuste oclusal.")
    ]
))

# 08 (Key 3: D)
questions.append(make_q(
    qid="odo-008", nivel=3,
    enunciado="Al evaluar un diente pilar con corona completa metalocerámica en el que el paciente refiere molestias difusas al masticar, el estudiante intenta realizar la prueba de sensibilidad con frío aplicando Endo-Ice sobre la superficie vestibular de la porcelana, pero no obtiene respuesta alguna. En la clase sobre pruebas térmicas especiales, ¿qué explicó el profesor sobre la limitación de la prueba de frío en dientes con coronas y cuál alternativa técnica mencionó?",
    opciones=[
        "El frío desintegra químicamente la porcelana dental, por lo que está contraindicado aplicar Endo-Ice sobre coronas fijas.",
        "La prueba de frío es completamente infalible en coronas si se empapa un hisopo gigante abarcando tres dientes continuos.",
        "Las coronas metalocerámicas conducen el frío con mayor rapidez que el esmalte natural, por lo que la ausencia de dolor confirma necrosis.",
        "La cofia metálica de la corona actúa como aislante térmico impidiendo la transmisión del frío; se puede generar calor por fricción mediante una copa de caucho a baja velocidad."
    ],
    correcta=3,
    distractores=[
        "El refrigerante químico no altera ni disuelve la estructura inorgánica de la porcelana dental.",
        "Abarcar varios dientes con un hisopo gigante es un error técnico grave que genera falsos positivos al enfriar los dientes vecinos.",
        "El metal y la cerámica bajo la corona no aumentan la conducción al diente, sino que actúan como barrera aislante que atenúa el estímulo.",
        ""
    ],
    explicacion="El profesor destaca que las coronas completas (especialmente las que tienen subestructura metálica) actúan como aislantes térmicos, haciendo que el frío del Endo-Ice no alcance la dentina ni estimule los odontoblastos. Una alternativa clínica para evaluar la vitalidad sin perforar la corona consiste en generar calor por fricción mediante una copa de caucho profiláctica en pieza de mano a baja velocidad sobre la restauración.",
    tema="Pruebas de sensibilidad especiales: dientes con coronas",
    que="Comprender el efecto aislante de las coronas protésicas y la técnica de calor por fricción.",
    clave="Las coronas metálicas aíslan el frío; se puede aplicar calor por fricción con copa de caucho a baja velocidad para evaluar vitalidad.",
    pistas=[
        "Recuerda la advertencia del docente sobre el costo de quitar una corona solo para probar sensibilidad.",
        "Ten en cuenta cómo la copa de profilaxis genera calor por fricción controlada en la pieza de baja velocidad."
    ],
    marcas_data=[
        ("corona completa metalocerámica", "dato", "Presencia de restauración protésica"),
        ("¿qué explicó el profesor sobre la limitación de la prueba de frío en dientes con coronas y cuál alternativa técnica mencionó?", "pide", "Limitación y técnica alternativa")
    ],
    steps_ideas=[
        ("Aislamiento térmico protésico", "La estructura protésica impide que la temperatura bajo cero del frío alcance la cámara pulpar."),
        ("Prueba de fricción", "La fricción controlada con goma rotatoria genera calor capaz de atravesar la restauración e inducir respuesta."),
        ("Comprobación diagnóstica", "Verificamos que la corona actúa como aislante y que la prueba de fricción es la alternativa técnica descrita.")
    ]
))

# 09 (Key 0: A)
questions.append(make_q(
    qid="odo-009", nivel=2,
    enunciado="Una paciente de 19 años es remitida por el servicio de odontología restauradora tras iniciar la remoción de una lesión de caries oclusal profunda en el segundo molar inferior. Durante la excavación dentinaria se produce una exposición pulpar franca de dos milímetros, observándose tejido pulpar rojo brillante y sangrado activo controlable. La paciente afirma que el diente nunca le había dolido antes y que no tiene dolor espontáneo ni nocturno. De acuerdo con el consenso diagnóstico de la Asociación Americana de Endodoncia discutido en clase, ¿cuál es el diagnóstico pulpar?",
    opciones=[
        "Pulpitis irreversible asintomática.",
        "Pulpitis irreversible sintomática.",
        "Necrosis pulpar.",
        "Pulpa clínicamente normal."
    ],
    correcta=0,
    distractores=[
        "",
        "La pulpitis irreversible sintomática exige la presencia de dolor espontáneo, pulsátil, exacerbación térmica prolongada o dolor nocturno.",
        "La presencia de sangrado activo rojo rutilante confirma que la pulpa está vital y no necrosada.",
        "Una pulpa clínicamente normal no presenta exposición directa a la cavidad oral por avance destructivo de caries profunda."
    ],
    explicacion="Cuando una caries profunda compromete y expone la pulpa dental vital sin que el paciente haya experimentado sintomatología dolorosa espontánea previa, la pulpa se encuentra irreversiblemente inflamada y colonizada por bacterias, clasificándose como pulpitis irreversible asintomática.",
    tema="Diagnóstico pulpar: pulpitis irreversible asintomática",
    que="Identificar la pulpitis irreversible asintomática ante exposición pulpar indolora por caries profunda.",
    clave="La exposición pulpar por caries profunda en un diente vital sin antecedentes de dolor espontáneo define la pulpitis irreversible asintomática.",
    pistas=[
        "Observa que la pulpa está vital y sangra, lo que descarta necrosis.",
        "Ten en cuenta que no hay dolor espontáneo, lo que descarta la variante sintomática."
    ],
    marcas_data=[
        ("exposición pulpar franca de dos milímetros, observándose tejido pulpar rojo brillante", "clave", "Exposición pulpar vital"),
        ("nunca le había dolido antes y que no tiene dolor espontáneo ni nocturno", "dato", "Ausencia de síntomas dolorosos"),
        ("¿cuál es el diagnóstico pulpar?", "pide", "Determinar diagnóstico")
    ],
    steps_ideas=[
        ("Vitalidad presente", "El sangrado rutilante comprueba que el tejido pulpar conserva circulación sanguínea activa."),
        ("Irreversibilidad biológica", "La invasión bacteriana masiva por caries profunda impide la cicatrización espontánea de la pulpa coronal."),
        ("Comprobación diagnóstica", "El diagnóstico clínico exacto es pulpitis irreversible asintomática.")
    ]
))

# 10 (Key 1: B)
questions.append(make_q(
    qid="odo-010", nivel=2,
    enunciado="En la sección de semiología clínica y pruebas periapicales, el profesor interroga a los estudiantes sobre la técnica correcta para realizar la prueba de percusión dental. Según las directrices explicadas enfáticamente por el docente, ¿cómo debe ejecutarse adecuadamente esta prueba?",
    opciones=[
        "Utilizando la punta afilada del explorador dental presionando fuertemente el surco oclusal del diente sospechoso.",
        "Utilizando la parte roma y gruesa del mango del espejo dental, realizando golpecitos suaves y evaluando primero un diente de control sano.",
        "Pidiéndole al paciente que mastique con fuerza una barra de cera dura para reproducir el dolor periapical.",
        "Golpeando exclusivamente en sentido lateral con el mango de la pinza algodonera sin evaluar dientes adyacentes."
    ],
    correcta=1,
    distractores=[
        "El profesor prohibió explícitamente usar instrumental punzante o la punta del explorador para percutir porque puede fracturar esmalte o traumatizar al paciente.",
        "",
        "Masticar cera no constituye la prueba de percusión diagnóstica y no permite aislar el vector de impacto vertical ni horizontal.",
        "Evaluar dientes de control sanos previos es obligatorio para calibrar el umbral y respuesta propioceptiva normal del paciente."
    ],
    explicacion="El profesor recalca en el audio que la prueba de percusión se debe realizar con la parte roma del instrumental (el mango del espejo dental, nunca con puntas afiladas de exploradores). Se debe evaluar primero un diente de control contralateral o adyacente sano para que el paciente distinga el sonido y tacto normal frente a la inflamación periapical.",
    tema="Semiología periapical: técnica de percusión dental",
    que="Reconocer el instrumental y la técnica adecuada para la prueba de percusión.",
    clave="La percusión se realiza con el mango romo del espejo bucal de forma suave y evaluando previamente un diente testigo sano.",
    pistas=[
        "Recuerda las palabras textuales del profesor prohibiendo usar exploradores de punta para percutir.",
        "Ten presente la necesidad obligatoria de evaluar un diente testigo de referencia."
    ],
    marcas_data=[
        ("técnica correcta para realizar la prueba de percusión dental", "clave", "Objeto de la prueba"),
        ("¿cómo debe ejecutarse adecuadamente esta prueba?", "pide", "Técnica de ejecución")
    ],
    steps_ideas=[
        ("Instrumental adecuado", "Se emplea el mango romo del espejo dental para evitar microfracturas o sensaciones punzantes confusas."),
        ("Protocolo comparativo", "Siempre se percute primero un diente sano para establecer el parámetro de comparación en el paciente."),
        ("Comprobación diagnóstica", "Verificamos que el uso del mango romo con diente de control es el método indicado.")
    ]
))

# 11 (Key 2: C)
questions.append(make_q(
    qid="odo-011", nivel=2,
    enunciado="Un paciente de 32 años acude a urgencias por dolor pulsátil espontáneo e insoportable en el primer premolar superior. Al examen extraoral e intraoral presenta una tumefacción visible, indurada y eritematosa en el fondo de surco vestibular sobre el ápice del diente, la cual es dolorosa y fluctuante a la palpación. El diente presenta dolor extremo a la percusión vertical y horizontal con sensación de diente extruido o crecido, y las pruebas térmicas con frío son negativas (sin respuesta). No se observa ningún estoma fistuloso en la encía. ¿Cuál es el diagnóstico periapical?",
    opciones=[
        "Periodontitis apical asintomática.",
        "Absceso apical crónico.",
        "Absceso apical agudo.",
        "Osteítis condensante."
    ],
    correcta=2,
    distractores=[
        "La periodontitis apical asintomática cursa sin tumefacción ni dolor a la palpación o percusión, presentándose solo como radiolucidez apical indolora.",
        "El absceso apical crónico se caracteriza por la presencia de una fístula activa drenante y suele ser casi indoloro al estar descomprimido.",
        "",
        "La osteítis condensante es una reacción ósea proliferativa radiopaca crónica sin tumefacción fluctuante ni absceso agudo."
    ],
    explicacion="El absceso apical agudo se caracteriza por un inicio rápido, dolor pulsátil severo espontáneo, dolor extremo a la percusión, tumefacción fluctuante en tejidos blandos por acumulación de pus no drenado, y necrosis pulpar previa. La ausencia de fístula diferencia la fase aguda de la crónica.",
    tema="Diagnóstico periapical: absceso apical agudo",
    que="Diferenciar el absceso apical agudo del crónico y de la periodontitis apical.",
    clave="Tumefacción dolorosa fluctuante, dolor pulsátil severo y falta de fístula en diente desvitalizado definen el absceso apical agudo.",
    pistas=[
        "Fíjate en la presencia de hinchazón fluctuante sin ninguna fístula por donde drene el pus.",
        "Observa la sensación típica de diente crecido y el dolor pulsátil severo."
    ],
    marcas_data=[
        ("tumefacción visible, indurada y eritematosa en el fondo de surco vestibular", "clave", "Edema fluctuante"),
        ("No se observa ningún estoma fistuloso en la encía", "dato", "Ausencia de drenaje espontáneo"),
        ("¿Cuál es el diagnóstico periapical?", "pide", "Diagnóstico periapical")
    ],
    steps_ideas=[
        ("Presión tisular purulenta", "La acumulación de pus dentro del periápice sin salida genera tumefacción dolorosa y extrusión dental."),
        ("Diferenciación con fístula", "Al no existir fístula, el proceso es cerrado y agudo con alta sintomatología sistémica y local."),
        ("Comprobación diagnóstica", "El cuadro clínico corresponde con certeza a un absceso apical agudo.")
    ]
))

# 12 (Key 3: D)
questions.append(make_q(
    qid="odo-012", nivel=1,
    enunciado="En repetidas ocasiones a lo largo de la grabación, el docente corrige a los estudiantes cuando intentan emitir un diagnóstico definitivo mirando únicamente una imagen periapical. ¿Cuál es el postulado central que enseñó el profesor respecto al rol de la radiografía en endodoncia?",
    opciones=[
        "La radiografía periapical es un medio diagnóstico autosuficiente que reemplaza por completo a las pruebas clínicas de palpación y percusión.",
        "Las radiografías solo son necesarias cuando se sospecha una fractura de corona visible a simple vista.",
        "Una radiografía digital siempre muestra de forma fidedigna la vitalidad histológica del tejido pulpar interno.",
        "La radiografía es una ayuda diagnóstica complementaria y nunca un medio de diagnóstico exclusivo, pues debe correlacionarse siempre con los hallazgos clínicos y pruebas de sensibilidad."
    ],
    correcta=3,
    distractores=[
        "El profesor afirmó enfáticamente que la radiografía sola no da el diagnóstico y no puede reemplazar el examen clínico directo.",
        "El estudio radiográfico es fundamental en todas las fases endodónticas y no solo en fracturas coronales superficiales.",
        "La radiografía muestra sombras y densidades minerales de tejidos duros; no puede mostrar si el tejido celular pulpar interno está vivo o necrótico.",
        ""
    ],
    explicacion="El profesor recalca que la radiografía es una ayuda diagnóstica y no un medio diagnóstico autosuficiente. Una pulpa en estado de pulpitis irreversible puede tener un periápice radiográficamente sano, y superposiciones anatómicas pueden simular lesiones o tapar raíces. Siempre debe integrarse con anamnesis y pruebas de vitalidad.",
    tema="Semiología radiográfica: rol de la radiografía periapical",
    que="Reconocer el valor complementario de la radiografía frente a las pruebas clínicas.",
    clave="La radiografía es una ayuda complementaria que nunca debe sustituir a la evaluación clínica y pruebas de vitalidad.",
    pistas=[
        "Recuerda las palabras del profesor insistiendo en que no se puede diagnosticar solo con la radiografía.",
        "Ten presente que los rayos X no revelan la condición histológica vital de la pulpa dental."
    ],
    marcas_data=[
        ("docente corrige a los estudiantes cuando intentan emitir un diagnóstico definitivo mirando únicamente una imagen", "clave", "Principio semiológico"),
        ("¿Cuál es el postulado central que enseñó el profesor respecto al rol de la radiografía en endodoncia?", "pide", "Rol de la radiografía")
    ],
    steps_ideas=[
        ("Limitación de la imagen bidimensional", "La radiografía es una proyección plana de estructuras tridimensionales que puede falsear información anatómica."),
        ("Complementariedad clínica", "El diagnóstico en endodoncia se fundamenta en la tríada: síntomas, pruebas de sensibilidad y radiografía."),
        ("Comprobación diagnóstica", "Verificamos que la radiografía es una ayuda diagnóstica complementaria.")
    ]
))

# 13 (Key 0: A)
questions.append(make_q(
    qid="odo-013", nivel=2,
    enunciado="Un paciente de 24 años consulta porque notó un pequeño granito en la encía superior que de forma periódica drena pus y luego se desinflama, sin causarle mayor dolor. Al examen intraoral se observa un estoma fistuloso activo con supuración en la mucosa adherida del incisivo lateral superior izquierdo. El diente no responde a la prueba de frío ni eléctrica, la percusión es negativa y la radiografía revela una zona radiolúcida periapical evidente. ¿Cuál es el diagnóstico pulpar y periapical?",
    opciones=[
        "Necrosis pulpar con absceso apical crónico.",
        "Pulpitis irreversible sintomática con periodontitis apical sintomática.",
        "Pulpitis reversible con absceso apical agudo.",
        "Pulpa normal con osteítis condensante."
    ],
    correcta=0,
    distractores=[
        "",
        "La pulpitis irreversible sintomática cursa con respuesta positiva prolongada al frío y dolor continuo severo, incompatibles con una pulpa desvitalizada e indolora.",
        "En la pulpitis reversible la pulpa responde vitalmente al frío y el absceso agudo se caracteriza por ausencia de fístula y gran tumefacción dolorosa.",
        "Una pulpa normal respondería a las pruebas térmicas y la osteítis condensante se manifiesta como radiopacidad apical, no con fístula ni radiolucidez."
    ],
    explicacion="La presencia de una fístula activa (tracto sinuoso) que drena secreción purulenta en un diente desvitalizado (negativo al frío y electricidad) con radiolucidez periapical define con precisión una necrosis pulpar asociada a un absceso apical crónico.",
    tema="Diagnóstico periapical: absceso apical crónico",
    que="Identificar el absceso apical crónico por la presencia de fístula activa en diente necrótico.",
    clave="Un estoma fistuloso activo con drenaje de pus en un diente desvitalizado caracteriza al absceso apical crónico.",
    pistas=[
        "Observa la presencia de fístula que drena pus de manera intermitente sin dolor intenso.",
        "Nota que la prueba de sensibilidad pulpar es completamente negativa."
    ],
    marcas_data=[
        ("estoma fistuloso activo con supuración en la mucosa adherida", "clave", "Presencia de fístula"),
        ("diente no responde a la prueba de frío ni eléctrica", "dato", "Necrosis pulpar"),
        ("¿Cuál es el diagnóstico pulpar y periapical?", "pide", "Diagnóstico integrado")
    ],
    steps_ideas=[
        ("Vía de descompresión", "La fístula actúa como válvula de escape del exudado purulento, aliviando la presión y evitando el dolor agudo."),
        ("Origen necrótico", "La muerte pulpar es el reservorio microbiano que mantiene activo el drenaje crónico periapical."),
        ("Comprobación diagnóstica", "El diagnóstico definitivo es necrosis pulpar con absceso apical crónico.")
    ]
))

# 14 (Key 1: B)
questions.append(make_q(
    qid="odo-014", nivel=3,
    enunciado="Al tomar una radiografía periapical ortorradial de un primer molar inferior, los dos conductos de la raíz mesial (mesiovestibular y mesiolingual) aparecen totalmente superpuestos en la misma línea visual. Para poder disociar ambos conductos e identificar la posición de cada instrumento endodóntico, el clínico aplica la técnica de Clark (regla del objeto lingual o SLOB). Si el cono de rayos X se angula hacia mesial (mesiorradial), ¿hacia dónde se proyectará la imagen del conducto mesiolingual en la radiografía resultante?",
    opciones=[
        "Se proyectará hacia distal, porque los objetos más profundos siempre se mueven en sentido contrario a la angulación del tubo.",
        "Se proyectará hacia mesial, porque el objeto lingual siempre se desplaza en la misma dirección hacia la que se orienta la angulación del tubo de rayos X.",
        "Permanecerá estático en el centro exacto de la raíz sin sufrir ningún tipo de desplazamiento geométrico.",
        "Desaparecerá de la película radiográfica debido a la refracción tangencial del haz de radiación."
    ],
    correcta=1,
    distractores=[
        "El objeto que se proyecta en sentido contrario (hacia distal) es el conducto vestibular (Opposite Buccal), no el lingual.",
        "",
        "Cualquier modificación de la angulación horizontal produce inevitablemente la disociación y desplazamiento relativo de ambos conductos.",
        "La radiación ionizante no sufre refracción óptica en el diente que haga desaparecer conductos radiculares anatómicos."
    ],
    explicacion="La regla de Clark (regla del objeto lingual o regla SLOB: Same Lingual, Opposite Buccal) establece que cuando el tubo de rayos X se angula horizontalmente, el conducto situado por lingual se proyecta en la misma dirección hacia la que se dirigió el tubo (si se anguló a mesial, se mueve a mesial), mientras que el conducto vestibular se proyecta en dirección opuesta (hacia distal).",
    tema="Técnicas radiográficas: regla de Clark (SLOB)",
    que="Aplicar la técnica de Clark para disociar conductos radiculares superpuestos.",
    clave="Según la regla SLOB, al angular el tubo hacia mesial, el conducto lingual se desplaza hacia mesial (misma dirección).",
    pistas=[
        "Acuérdate de la sigla SLOB: Same Lingual, Opposite Buccal.",
        "Si el rayo apunta hacia mesial, el objeto lingual viaja hacia mesial."
    ],
    marcas_data=[
        ("técnica de Clark (regla del objeto lingual o SLOB)", "clave", "Principio geométrico radiográfico"),
        ("Si el cono de rayos X se angula hacia mesial (mesiorradial)", "dato", "Dirección de angulación"),
        ("¿hacia dónde se proyectará la imagen del conducto mesiolingual en la radiografía resultante?", "pide", "Proyección resultante")
    ],
    steps_ideas=[
        ("Principio de paralaje", "Al desplazar el foco emisor, las estructuras más cercanas al detector (linguales) se proyectan en la dirección del haz."),
        ("Regla mnemotécnica SLOB", "Same Lingual (lingual se mueve igual que el cono), Opposite Buccal (vestibular se mueve al lado opuesto)."),
        ("Comprobación diagnóstica", "Al angular a mesial, el conducto lingual se proyecta hacia mesial.")
    ]
))

# 15 (Key 2: C)
questions.append(make_q(
    qid="odo-015", nivel=3,
    enunciado="Un paciente adulto mayor presenta un incisivo central superior con antecedente de traumatismo antiguo, el cual muestra un cambio de color amarillento oscuro y cámara pulpar con marcada calcificación y retracción radiográfica. Las pruebas térmicas con frío y calor resultan negativas, pero el diente no presenta lesiones periapicales ni movilidad ni dolor alguno. Ante la duda de si el diente está vital o necrótico, el docente describe en clase una prueba especial de último recurso antes de abrirlo. ¿Cuál es dicha prueba y en qué consiste?",
    opciones=[
        "Prueba de percusión forzada con martillo quirúrgico de impacto.",
        "Prueba de tinción con azul de metileno intragingival sin aislamiento.",
        "Prueba de cavidad, que consiste en realizar un fresado superficial en esmalte y dentina sin anestesia local para verificar si existe respuesta dolorosa.",
        "Prueba de aspiración periapical transmucosa con aguja de calibre grueso."
    ],
    correcta=2,
    distractores=[
        "El traumatismo violento con instrumentos quirúrgicos está totalmente proscrito en semiología dental.",
        "La tinción con azul de metileno se emplea para buscar líneas de fractura coronal, no para determinar vitalidad en cámaras calcificadas.",
        "",
        "La punción transmucosa no evalúa sensibilidad pulpar y solo se emplea para descomprimir abscesos fluctuantes en tejidos blandos."
    ],
    explicacion="El test de cavidad (prueba de cavidad) es el último recurso semiológico cuando las pruebas térmicas y eléctricas no son concluyentes debido a metamorfosis cálcica o recubrimiento de dentina terciaria densa. Consiste en desgastar con fresa pequeña a baja o alta velocidad sin anestesia a través del esmalte hasta tocar dentina: si el paciente siente sensibilidad aguda inmediata, se confirma vitalidad y se detiene el fresado; si no siente nada al alcanzar dentina profunda, se confirma necrosis.",
    tema="Pruebas especiales: test de cavidad",
    que="Conocer la indicación y ejecución de la prueba de cavidad en dientes calcificados.",
    clave="El test de cavidad consiste en fresar dentina sin anestesia para constatar vitalidad cuando las pruebas térmicas no son viables.",
    pistas=[
        "Recuerda la anécdota del profesor sobre pacientes mayores con cámara retraída donde el frío no alcanza a estimular.",
        "Ten en cuenta que esta prueba se realiza sin anestesiar para evaluar la respuesta sensitiva del paciente."
    ],
    marcas_data=[
        ("cámara pulpar con marcada calcificación y retracción radiográfica", "dato", "Dificultad de estímulo térmico"),
        ("prueba especial de último recurso antes de abrirlo", "clave", "Prueba diagnóstica extrema"),
        ("¿Cuál es dicha prueba y en qué consiste?", "pide", "Identificar prueba y método")
    ],
    steps_ideas=[
        ("Barrera de dentina terciaria", "La aposición masiva de dentina aísla térmicamente la pulpa restante de los estímulos de superficie."),
        ("Estimulación directa", "El contacto físico de la fresa sobre túbulos dentinarios profundos desata dolor súbito únicamente si hay pulpa viva."),
        ("Comprobación diagnóstica", "La prueba de cavidad sin anestesia es la técnica indicada en estos casos específicos.")
    ]
))

# 16 (Key 3: D)
questions.append(make_q(
    qid="odo-016", nivel=3,
    enunciado="Una paciente acude a la clínica manifestando un dolor agudo y difuso de gran intensidad que le abarca todo el lado derecho del rostro. Afirma no saber si el dolor proviene de un molar superior o de un molar inferior, ya que siente que le duele la mejilla, la sien y la mandíbula simultáneamente. ¿Cuál es el protocolo de anestesia diagnóstica selectiva que recomendó el profesor en clase para dilucidar el arco dentario responsable?",
    opciones=[
        "Realizar de inmediato un bloqueo troncular del nervio dentario inferior, ya que si es el inferior se anestesiará toda la mandíbula.",
        "Inyectar anestesia general en el quirófano para suprimir por completo cualquier percepción dolorosa del paciente.",
        "Anestesiar simultáneamente el maxilar superior y la mandíbula para evitar que el paciente continúe con molestia durante la consulta.",
        "Iniciar aplicando anestesia infiltrativa de forma selectiva en el diente sospechoso del arco superior, ya que no produce bloqueo regional amplio y permite confirmar o descartar el maxilar antes de tocar la mandíbula."
    ],
    correcta=3,
    distractores=[
        "El profesor advirtió que si se bloquea primero el dentario inferior, se anestesia todo el cuadrante mandibular y se pierde la capacidad de discriminar entre dientes inferiores.",
        "La anestesia general no es una herramienta diagnóstica de consultorio para localización dental.",
        "Anestesiar ambos arcos a la vez impide por completo identificar cuál de los dos maxilares era el causante del dolor.",
        ""
    ],
    explicacion="El docente explicó en clase que cuando hay dolor referido entre arcos superior e inferior, la técnica de anestesia selectiva debe comenzar por el arco superior con técnica infiltrativa en el diente sospechoso más posterior. Si el dolor desaparece de inmediato, se confirma que el origen era superior. Si se bloqueara primero el nervio dentario inferior, se insensibilizaría toda la mandíbula a la vez sin poder distinguir entre molares ni premolares inferiores.",
    tema="Procedimientos diagnósticos: anestesia selectiva",
    que="Aplicar la técnica de anestesia selectiva para resolver el dolor referido entre maxilares.",
    clave="Se infiltra primero de forma selectiva el arco superior para no anular en bloque la sensibilidad mandibular.",
    pistas=[
        "Recuerda la advertencia del profesor sobre el gasto innecesario de cartuchos y la pérdida de referencia mandibular.",
        "Considera que la infiltración superior es localizada y reversible en un solo diente."
    ],
    marcas_data=[
        ("no saber si el dolor proviene de un molar superior o de un molar inferior", "dato", "Dolor referido intermaxilar"),
        ("¿Cuál es el protocolo de anestesia diagnóstica selectiva que recomendó el profesor en clase para dilucidar el arco dentario responsable?", "pide", "Técnica de anestesia selectiva")
    ],
    steps_ideas=[
        ("Dolor irradiado por ramas trigeminales", "La convergencia sensitiva de las ramas V2 y V3 en el núcleo espinal del trigémino produce confusión de arco."),
        ("Aislamiento por infiltración", "La anestesia intraligamentosa o infiltrativa superior apaga el diente superior sospechoso sin dormir la mandíbula."),
        ("Comprobación diagnóstica", "El protocolo correcto inicia por infiltración selectiva en el maxilar superior.")
    ]
))

# 17 (Key 0: A)
questions.append(make_q(
    qid="odo-017", nivel=3,
    enunciado="Un paciente de 40 años refiere dolor agudo punzante al masticar alimentos duros (como granos o semillas) en el primer molar inferior derecho. Al examinar el diente no se aprecian caries ni inflamación periapical en la radiografía, y a las pruebas de frío responde de manera normal. Sin embargo, al aplicar la prueba de cuña con un dispositivo mordedor (Tooth Slooth) sobre la cúspide distovestibular, el paciente experimenta un dolor agudo característico en el preciso instante en que libera o suelta la presión de la mordida. ¿Cuál es el diagnóstico más probable?",
    opciones=[
        "Síndrome del diente fisurado (fractura cuspídea incompleta).",
        "Absceso apical agudo.",
        "Necrosis pulpar total.",
        "Pulpitis irreversible asintomática con reabsorción interna."
    ],
    correcta=0,
    distractores=[
        "",
        "El absceso apical agudo presenta tumefacción fluctuante, dolor pulsátil espontáneo y pruebas térmicas negativas.",
        "La necrosis pulpar cursa con desvitalización y ausencia de respuesta al frío.",
        "La reabsorción interna es un hallazgo radiográfico con ensanchamiento redondeado del conducto, habitualmente asintomático en sus etapas iniciales."
    ],
    explicacion="El dolor agudo que aparece o se acentúa en el momento de soltar o liberar la fuerza oclusal (dolor al rebote en la prueba de cuña) es el signo patognomónico del síndrome del diente fisurado. La separación microscópica de las paredes fracturadas moviliza el fluido dentinario activando bruscamente las fibras A-delta.",
    tema="Patología dentaria: síndrome del diente fisurado",
    que="Reconocer el síndrome del diente fisurado mediante la prueba de mordida y dolor a la liberación.",
    clave="El dolor agudo al liberar la fuerza de mordida en la prueba de cuña es típico del diente fisurado.",
    pistas=[
        "Fíjate en el dolor al momento de soltar la mordida en una cúspide aislada.",
        "Observa que la radiografía convencional suele verse completamente normal."
    ],
    marcas_data=[
        ("dolor agudo característico en el preciso instante en que libera o suelta la presión de la mordida", "clave", "Dolor al rebote oclusal"),
        ("prueba de cuña con un dispositivo mordedor (Tooth Slooth)", "dato", "Prueba de cuña"),
        ("¿Cuál es el diagnóstico más probable?", "pide", "Determinar diagnóstico")
    ],
    steps_ideas=[
        ("Mecánica de la fisura", "La masticación abre momentáneamente la fisura estimulando los mecanorreceptores y túbulos dentinarios."),
        ("Dolor a la liberación", "El rebote elástico de la cúspide al soltar la mordida genera un pico súbito de despolarización nerviosa."),
        ("Comprobación diagnóstica", "El cuadro clínico corresponde al síndrome del diente fisurado.")
    ]
))

# 18 (Key 1: B)
questions.append(make_q(
    qid="odo-018", nivel=2,
    enunciado="En la radiografía periapical de un primer molar inferior con una caries extensa y antecedentes de pulpitis sintomática prolongada, se evidencia una zona radiopaca difusa y bien delimitada de hueso trabecular denso y esclerótico alrededor de los ápices radiculares, sin aumento del espacio periodontal ni destrucción cortical. De acuerdo con la clasificación periapical estudiada en clase, ¿cuál es este diagnóstico?",
    opciones=[
        "Absceso apical agudo.",
        "Osteítis condensante.",
        "Periodontitis apical asintomática.",
        "Displasia cementaria periapical en fase osteolítica."
    ],
    correcta=1,
    distractores=[
        "El absceso apical agudo se presenta con tumefacción purulenta, dolor pulsátil severo y posible rarefacción ósea, no con radiopacidad esclerótica.",
        "",
        "La periodontitis apical asintomática se manifiesta como una zona radiolúcida (oscura) por destrucción ósea, no como una zona radiopaca (blanca).",
        "La fase osteolítica de la displasia cementaria es puramente radiolúcida y ocurre en dientes anteriores vitales sin caries."
    ],
    explicacion="La osteítis condensante (también llamada osteoesclerosis periapical) es una reacción ósea proliferativa periapical frente a una irritación pulpar de bajo grado y larga duración. En la radiografía se observa como una masa radiopaca radiodensa circunscrita al ápice radicular.",
    tema="Diagnóstico periapical: osteítis condensante",
    que="Identificar la osteítis condensante como respuesta ósea radiopaca ante irritación pulpar crónica.",
    clave="Una zona radiopaca circunscrita al ápice en respuesta a una irritación pulpar prolongada define la osteítis condensante.",
    pistas=[
        "Observa que la lesión periapical no es oscura (radiolúcida) sino blanca y densa (radiopaca).",
        "Recuerda que representa una reacción de defensa ósea con formación de más trabéculas."
    ],
    marcas_data=[
        ("zona radiopaca difusa y bien delimitada de hueso trabecular denso y esclerótico", "clave", "Signo radiográfico radiopaco"),
        ("¿cuál es este diagnóstico?", "pide", "Diagnóstico periapical")
    ],
    steps_ideas=[
        ("Reacción osteoblástica", "Los estímulos irritativos crónicos de baja intensidad inducen aplanamiento y proliferación de hueso denso periapical."),
        ("Aspecto radiográfico", "Se aprecia un aumento de radiopacidad concéntrica alrededor de los ápices afectados."),
        ("Comprobación diagnóstica", "El diagnóstico periapical corresponde a osteítis condensante.")
    ]
))

# 19 (Key 2: C)
questions.append(make_q(
    qid="odo-019", nivel=2,
    enunciado="Al inicio de la clase, el profesor llama la atención sobre un dato fundamental que no debe omitirse durante la anamnesis del problema actual: la presencia o ausencia de dolor nocturno. ¿Cuál es la razón fisiopatológica por la que el dolor de una pulpitis irreversible sintomática se exacerba notablemente durante la noche cuando el paciente se acuesta?",
    opciones=[
        "Durante la noche descienden los niveles de cortisol en sangre, lo que neutraliza por completo los anestésicos locales residuales.",
        "El esmalte dental se contrae por el enfriamiento ambiental nocturno generando microfracturas en la cámara pulpar.",
        "Al adoptar la posición horizontal en decúbito supino, aumenta la presión hidrostática y sanguínea cefálica, lo que incrementa la presión intrapulpar en una cámara inextensible.",
        "Las bacterias orales anaerobias se multiplican exclusivamente en la oscuridad estimulando de forma intermitente las fibras periapicales."
    ],
    correcta=2,
    distractores=[
        "Los cambios circadianos hormonales no neutralizan anestésicos ni explican el mecanismo hidrodinámico primario de la inflamación pulpar.",
        "El esmalte dental no sufre contracciones térmicas nocturnas capaces de provocar dolor espontáneo severo.",
        "",
        "Las bacterias intraconducto son anaerobias y no dependen de la luz exterior para su metabolismo infeccioso."
    ],
    explicacion="La pulpa dental se encuentra confinada dentro de una cámara rígida de dentina que no se puede expandir (sistema de baja distensibilidad). Al acostarse horizontalmente en decúbito supino, la presión arterial cefálica y el retorno venoso aumentan, incrementando drásticamente la presión intrapulpar sobre las terminaciones nerviosas excitadas.",
    tema="Anamnesis del dolor: mecanismo del dolor nocturno",
    que="Comprender la base fisiopatológica del dolor nocturno en decúbito en la pulpitis irreversible.",
    clave="La postura en decúbito aumenta la presión vascular cefálica elevando la presión intrapulpar en la cámara cerrada.",
    pistas=[
        "Piensa en qué le ocurre a la circulación sanguínea de la cabeza cuando pasas de estar de pie a acostarte horizontal.",
        "Recuerda que la cámara pulpar tiene paredes rígidas que no se pueden estirar."
    ],
    marcas_data=[
        ("presencia o ausencia de dolor nocturno", "clave", "Pregunta de anamnesis"),
        ("¿Cuál es la razón fisiopatológica por la que el dolor de una pulpitis irreversible sintomática se exacerba notablemente durante la noche cuando el paciente se acuesta?", "pide", "Explicación fisiopatológica")
    ],
    steps_ideas=[
        ("Efecto gravitacional circulatorio", "El decúbito supino aumenta el flujo sanguíneo hacia el cráneo e incrementa la congestión capilar pulpar."),
        ("Inextensibilidad de la cámara", "La vasodilatación en un espacio cerrado aumenta la presión tisular comprimiendo directamente las fibras nerviosas."),
        ("Comprobación diagnóstica", "El aumento de presión intrapulpar por decúbito explica el dolor nocturno.")
    ]
))

# 20 (Key 3: D)
questions.append(make_q(
    qid="odo-020", nivel=2,
    enunciado="Durante la práctica, un estudiante toma una torunda grande de algodón, la satura con Endo-Ice (Endofrost) y la coloca abarcando dos dientes simultáneamente sin secar la saliva. El profesor detiene la maniobra de inmediato y explica la técnica correcta para evitar falsos diagnósticos. ¿Cuál de las siguientes afirmaciones describe el protocolo clínico adecuado para realizar la prueba térmica con frío?",
    opciones=[
        "Se debe aplicar el spray congelante directamente sobre la encía libre para anestesiar previamente la zona papilar.",
        "Se debe emplear una mota gigante de algodón impregnada que toque al menos tres dientes contiguos para ahorrar tiempo en la consulta.",
        "Se debe sumergir toda la arcada en agua helada con cubos de hielo sin necesidad de aislar ningún diente.",
        "Se debe realizar aislamiento relativo con rollos de algodón, secar el diente con gasa o aire suave y aplicar una pequeña torunda impregnada con el refrigerante exclusivamente en el tercio medio vestibular del diente de control antes del diente sospechoso."
    ],
    correcta=3,
    distractores=[
        "El refrigerante químico produce quemaduras severas si entra en contacto directo con la encía o tejidos blandos.",
        "Tocar varios dientes contiguos con una mota grande produce falsos positivos, pues se estimulan las fibras de dientes vecinos sanos.",
        "El uso de agua helada generalizada no permite discriminar cuál es el diente causal específico que responde patológicamente.",
        ""
    ],
    explicacion="El protocolo correcto dictado en clase exige: 1. Aislamiento relativo y secado cuidadoso para que la saliva no actúe de puente térmico; 2. Uso de una bolita pequeña de algodón tomada con pinza y rociada con el spray; 3. Aplicación puntual en el tercio medio vestibular (donde el esmalte es más delgado y está más cerca de los cuernos pulpares); 4. Evaluación obligatoria de un diente testigo sano previo.",
    tema="Semiología pulpar: protocolo de la prueba de frío",
    que="Dominar la técnica clínica exacta de aplicación del spray de frío (Endo-Ice).",
    clave="El protocolo exige aislamiento, secado, torunda pequeña puntual en tercio medio y evaluación previa de diente control.",
    pistas=[
        "Recuerda la advertencia del profesor sobre el tamaño de la torunda de algodón.",
        "Ten presente que si la saliva moja dos dientes, el frío se transmite al diente de al lado generando un falso diagnóstico."
    ],
    marcas_data=[
        ("El profesor detiene la maniobra de inmediato y explica la técnica correcta para evitar falsos diagnósticos", "clave", "Corrección de técnica"),
        ("¿Cuál de las siguientes afirmaciones describe el protocolo clínico adecuado para realizar la prueba térmica con frío?", "pide", "Protocolo correcto")
    ],
    steps_ideas=[
        ("Aislamiento del campo", "El secado y los rollos de algodón previenen que la saliva conduzca el frío a los dientes sanos vecinos."),
        ("Aplicación en tercio medio", "El tercio medio vestibular ofrece la vía más rápida y confiable hacia los receptores del plexo pulpar."),
        ("Comprobación diagnóstica", "Verificamos que el uso de torunda pequeña puntual con diente testigo es el estándar clínico.")
    ]
))

# 21 (Key 0: A)
questions.append(make_q(
    qid="odo-021", nivel=2,
    enunciado="Una niña de 14 años es traída por su madre a consulta odontológica. Al examen clínico se observa una caries masiva en el primer molar inferior permanente, el cual presenta ápice radicular inmaduro en la radiografía. Ocupando toda la cavidad oclusal se evidencia una masa de tejido blando, carnoso, de color rosado rojizo, indoloro a la palpación pero que sangra con facilidad al cepillado. La paciente no refiere antecedentes de dolor espontáneo. ¿Cuál es el diagnóstico?",
    opciones=[
        "Pulpitis irreversible asintomática con pulpitis hiperplásica (pólipo pulpar).",
        "Absceso apical agudo con celulitis facial difusa.",
        "Necrosis pulpar con periodontitis apical sintomática.",
        "Granuloma periférico de células gigantes del hueso alveolar."
    ],
    correcta=0,
    distractores=[
        "",
        "El absceso agudo es una tumefacción fluctuante intensamente dolorosa con afectación del estado general, no un tejido carnoso proliferativo intraocular crónico.",
        "En la necrosis pulpar el tejido pulpar muere y se licúa o deseca, sin proliferar en forma de pólipo vital sangrante.",
        "El granuloma periférico de células gigantes es una lesión neoplásica o reactiva de encía o periostio, no una masa que brota desde el interior de la cámara pulpar de un diente joven."
    ],
    explicacion="La pulpitis irreversible asintomática hiperplásica (pólipo pulpar) se presenta típicamente en niños y adolescentes en dientes con cavidades de caries amplias y abundante vascularización pulpar con ápices abiertos. El tejido pulpar inflamado crónicamente prolifera hacia el exterior formando una masa carnosa exofítica e indolora recubierta de epitelio escamoso estratificado.",
    tema="Diagnóstico pulpar: pulpitis hiperplásica (pólipo pulpar)",
    que="Reconocer el pólipo pulpar como manifestación de pulpitis irreversible asintomática en pacientes jóvenes.",
    clave="La proliferación carnosa indolora de tejido pulpar a través de una cavidad cariosa amplia define el pólipo pulpar.",
    pistas=[
        "Observa la edad de la paciente y la masa carnosa que brota desde el interior de la cámara pulpar.",
        "Ten en cuenta que el pólipo no produce dolor espontáneo severo a pesar de su tamaño."
    ],
    marcas_data=[
        ("masa de tejido blando, carnoso, de color rosado rojizo, indoloro a la palpación", "clave", "Signo clínico de pólipo"),
        ("primer molar inferior permanente, el cual presenta ápice radicular inmaduro", "dato", "Diente joven con abundante aporte vascular"),
        ("¿Cuál es el diagnóstico?", "pide", "Diagnóstico clínico")
    ],
    steps_ideas=[
        ("Vascularización en dientes jóvenes", "El foramen apical amplio permite un gran aporte de sangre que favorece la hiperplasia celular en vez de la necrosis rápida."),
        ("Epitelización de la pulpa expuesta", "Las células de la mucosa oral descaman y tapizan la pulpa proliferada confiriéndole aspecto de pólipo indoloro."),
        ("Comprobación diagnóstica", "El cuadro clínico corresponde a pulpitis hiperplásica (pólipo pulpar).")
    ]
))

# 22 (Key 1: B)
questions.append(make_q(
    qid="odo-022", nivel=3,
    enunciado="Durante el diagnóstico diferencial entre lesiones endodónticas y periodontales, el docente explica cómo distinguir un absceso periapical agudo de un absceso periodontal agudo en un diente multirradicular. ¿Cuál de los siguientes criterios clínicos es determinante para diferenciar ambas entidades?",
    opciones=[
        "El absceso periodontal siempre presenta dolor de cabeza severo mientras que el periapical no afecta estructuras craneales.",
        "El absceso periapical habitualmente cursa con pulpa desvitalizada (necrosis con prueba de frío negativa), mientras que el absceso periodontal suele presentar pulpa vital y un defecto de sondaje periodontal profundo a lo largo de la superficie radicular.",
        "El absceso periapical se resuelve espontáneamente con enjuagues de clorhexidina sin necesidad de instrumentación.",
        "En el absceso periodontal el diente no tiene ligamento periodontal en ninguna de sus caras."
    ],
    correcta=1,
    distractores=[
        "La cefalea no es un criterio diagnóstico discriminativo entre patología pulpar y periodontal.",
        "",
        "Ningún absceso de origen bacteriano intraconducto se cura con enjuagues orales superficiales.",
        "El ligamento periodontal está presente en toda la superficie radicular remanente no afectada por la bolsa periodontal."
    ],
    explicacion="La vitalidad pulpar y el sondaje periodontal son los pilares diagnósticos: en un absceso periapical primario, la infección proviene del interior del conducto y por ende la pulpa está necrótica (frío negativo); en el absceso periodontal primario, la infección proviene de la bolsa periodontal en la encía marginal, por lo que la pulpa suele conservar su vitalidad (frío positivo) y el sondaje revela una bolsa profunda.",
    tema="Diagnóstico diferencial: absceso periapical frente a periodontal",
    que="Diferenciar el absceso periapical del absceso periodontal mediante vitalidad y sondaje.",
    clave="El absceso periapical presenta necrosis pulpar (frío negativo); el absceso periodontal cursa con pulpa vital y bolsa periodontal profunda.",
    pistas=[
        "Verifica qué pasa con la prueba de sensibilidad pulpar en cada una de las dos entidades.",
        "Recuerda la importancia del sondaje periodontal con sonda milimetrada."
    ],
    marcas_data=[
        ("distinguir un absceso periapical agudo de un absceso periodontal agudo", "clave", "Diagnóstico diferencial"),
        ("¿Cuál de los siguientes criterios clínicos es determinante para diferenciar ambas entidades?", "pide", "Criterio determinante")
    ],
    steps_ideas=[
        ("Origen de la infección", "El absceso periapical desciende desde el conducto radicular; el periodontal asciende desde la bolsa marginal."),
        ("Pruebas de sensibilidad", "La respuesta positiva al frío orienta hacia causa periodontal primaria con pulpa sana."),
        ("Comprobación diagnóstica", "Verificamos que la prueba de frío y el sondaje determinan la distinción precisa.")
    ]
))

# 23 (Key 2: C)
questions.append(make_q(
    qid="odo-023", nivel=2,
    enunciado="Al realizar la inspección del examen extraoral en un paciente que consulta por una infección odontogénica severa originada en un tercer molar inferior, el odontólogo evalúa la simetría facial y los tejidos cervicales. ¿Cuál de los siguientes grupos de signos clínicos constituye una alarma roja que indica la diseminación de la infección hacia espacios aponeuróticos faciales profundos (como en la angina de Ludwig)?",
    opciones=[
        "Desgaste incisal leve, facetas de atrición en caninos y ausencia de dolor muscular.",
        "Torsión de la punta nasal, presencia de pecas en pómulos y sensibilidad auditiva normal.",
        "Asimetría facial con edema indurado submandibular difuso, trismus severo con limitación de apertura bucal, elevación del piso de la boca y dificultad respiratoria o disfagia.",
        "Pigmentación melánica en encía adherida anterior y respiración exclusivamente nasal."
    ],
    correcta=2,
    distractores=[
        "La atrición incisal y canina son signos biomecánicos de bruxismo o función masticatoria, no de celulitis infecciosa.",
        "Los rasgos morfológicos nasales y efélides en piel no tienen relación con procesos infecciosos odontogénicos.",
        "",
        "Las máculas melánicas en encía son variantes fisiológicas normales de la pigmentación oral en diversas poblaciones."
    ],
    explicacion="El compromiso de espacios fasciales profundos (como el submandibular, sublingual o retrofaríngeo) genera asimetría facial indurada, trismus pronunciado por espasmo muscular masticatorio, elevación de la lengua y disfagia/disnea. Estos signos constituyen una emergencia médica que compromete la vía aérea.",
    tema="Examen extraoral: signos de alarma de infección odontogénica",
    que="Identificar los signos extraorales de diseminación infecciosa hacia espacios fasciales profundos.",
    clave="Edema indurado difuso, trismus severo, elevación del piso de la boca y disfagia señalan compromiso fascial grave.",
    pistas=[
        "Busca signos que pongan en peligro la ventilación y la deglución del paciente.",
        "Observa la limitación extrema para abrir la boca (trismus) y el edema duro que desfigura la mandíbula."
    ],
    marcas_data=[
        ("diseminación de la infección hacia espacios aponeuróticos faciales profundos", "clave", "Condición de alarma clínica"),
        ("¿Cuál de los siguientes grupos de signos clínicos constituye una alarma roja", "pide", "Identificar signos de alarma")
    ],
    steps_ideas=[
        ("Vías de propagación fascial", "Las bacterias anaerobias perforan la cortical lingual mandibular ingresando a los espacios sublingual y submandibular."),
        ("Compromiso de la vía aérea", "La tumefacción masiva empuja la lengua hacia arriba y atrás, amenazando la permeabilidad respiratoria."),
        ("Comprobación diagnóstica", "El conjunto de edema indurado, trismus y disfagia constituye la alarma roja clínica indiscutible.")
    ]
))

# 24 (Key 3: D)
questions.append(make_q(
    qid="odo-024", nivel=2,
    enunciado="En el análisis del formato de historia clínica exigido en la universidad, el docente corrige enérgicamente a un grupo de estudiantes por escribir en el apartado de hallazgos radiográficos la frase: «el diente tiene caries oclusal». De acuerdo con la explicación dada en clase por el profesor, ¿cómo debe redactarse con rigor científico el informe radiográfico coronal?",
    opciones=[
        "«El diente presenta bacterias cariogénicas vivas infiltradas en el esmalte».",
        "«El diente tiene una fractura microscópica que requiere corona total inmediata».",
        "«El diente se encuentra desmineralizado en un ochenta por ciento de su volumen».",
        "«Se observa una imagen radiolúcida compatible con caries que involucra esmalte y dentina en la superficie oclusal»."
    ],
    correcta=3,
    distractores=[
        "Las radiografías no permiten ver bacterias ni microorganismos vivos, solo contrastes de absorción mineral de radiación.",
        "Diagnosticar fractura microscópica basándose en una sombra oclusal es una extrapolación errónea sin base clínica.",
        "El porcentaje cuantitativo de volumen no puede estimarse con precisión en una película periapical bidimensional.",
        ""
    ],
    explicacion="El profesor subraya que la radiografía muestra densidades ópticas (zonas radiolúcidas y radiopacas), por lo que semiológicamente nunca se debe asegurar directamente «hay caries» en el informe radiográfico, sino describirlo como: «zona o imagen radiolúcida compatible con caries que compromete tal superficie coronal».",
    tema="Semiología radiográfica: terminología y redacción de hallazgos",
    que="Redactar adecuadamente los hallazgos radiográficos según la terminología semiológica correcta.",
    clave="En radiología se reporta «imagen radiolúcida compatible con caries que compromete determinadas superficies», no la enfermedad directa.",
    pistas=[
        "Recuerda la corrección del profesor en el audio cuando dijo: «yo no puedo decir caries en un hallazgo radiográfico».",
        "Ten en cuenta los términos físicos básicos: radiolúcido para lo oscuro y radiopaco para lo claro."
    ],
    marcas_data=[
        ("docente corrige enérgicamente a un grupo de estudiantes por escribir en el apartado de hallazgos radiográficos la frase: «el diente tiene caries oclusal»", "clave", "Error semiológico a corregir"),
        ("¿cómo debe redactarse con rigor científico el informe radiográfico coronal?", "pide", "Forma correcta de redacción")
    ],
    steps_ideas=[
        ("Naturaleza del examen radiológico", "Los rayos X registran diferencias de absorción mineral, produciendo imágenes radiolúcidas donde hay pérdida mineral."),
        ("Principio de compatibilidad", "Semiológicamente se describe la imagen y se establece la compatibilidad con el proceso patológico."),
        ("Comprobación diagnóstica", "La redacción científica rigurosa es «imagen radiolúcida compatible con caries que involucra esmalte y dentina».")
    ]
))

# 25 (Key 0: A)
questions.append(make_q(
    qid="odo-025", nivel=2,
    enunciado="Un joven de 20 años asiste a consulta estética porque nota que su incisivo central superior izquierdo ha cambiado gradualmente de color en los últimos dos años, luciendo grisáceo y opaco en comparación con los dientes vecinos. Recuerda haber recibido un golpe jugando fútbol hace tres años, pero como no se fracturó el diente no acudió al dentista. Actualmente no refiere dolor alguno. Al examen clínico no hay respuesta al frío ni a la prueba eléctrica, la percusión es negativa y la radiografía muestra conducto permeable sin cambios periapicales evidentes. ¿Cuál es el diagnóstico pulpar?",
    opciones=[
        "Necrosis pulpar asintomática postraumática.",
        "Pulpitis reversible incipiente.",
        "Pulpitis irreversible sintomática.",
        "Pulpa clínicamente normal con tinción extrínseca por café."
    ],
    correcta=0,
    distractores=[
        "",
        "En la pulpitis reversible la prueba de frío es positiva y el diente conserva su coloración y brillo translúcido natural.",
        "La pulpitis irreversible sintomática se caracteriza por dolor agudo y prolongado al frío, completamente ausentes en este diente insensible.",
        "Las tinciones extrínsecas por alimentos afectan la superficie del esmalte de múltiples dientes y no generan falta de vitalidad pulpar."
    ],
    explicacion="El traumatismo dental contuso produce con frecuencia el desgarro del paquete vasculonervioso a nivel del foramen apical (isquemia pulpar), lo que deriva en necrosis pulpar aséptica. La descomposición de los eritrocitos y la degradación de la hemoglobina liberan hierro que penetra en los túbulos dentinarios, produciendo el cambio característico de color grisáceo y la falta de respuesta térmica.",
    tema="Patología pulpar: necrosis pulpar por traumatismo",
    que="Identificar la necrosis pulpar postraumática evidenciada por cambio de color y falta de vitalidad.",
    clave="El cambio de color coronal grisáceo con falta de respuesta a pruebas de sensibilidad tras un golpe indica necrosis pulpar.",
    pistas=[
        "Relaciona el antecedente del golpe contuso en el fútbol con la pérdida del aporte de sangre a la pulpa.",
        "Observa la falta total de respuesta a las pruebas térmicas y eléctricas."
    ],
    marcas_data=[
        ("cambiado gradualmente de color en los últimos dos años, luciendo grisáceo y opaco", "clave", "Discromía por degradación hemática"),
        ("no hay respuesta al frío ni a la prueba eléctrica", "dato", "Desvitalización pulpar"),
        ("¿Cuál es el diagnóstico pulpar?", "pide", "Determinar diagnóstico")
    ],
    steps_ideas=[
        ("Isquemia por luxación", "El impacto contuso lesiona los vasos apicales interrumpiendo el flujo nutricio y causando necrosis."),
        ("Pigmentación por hemólisis", "Los subproductos de la hemoglobina infiltran la dentina coronal generando el tinte grisáceo opaco."),
        ("Comprobación diagnóstica", "El diagnóstico indiscutible es necrosis pulpar asintomática postraumática.")
    ]
))

# 26 (Key 1: B)
questions.append(make_q(
    qid="odo-026", nivel=3,
    enunciado="Un paciente llega al consultorio con un vaso de agua con hielo en la mano, bebiendo pequeños sorbos constantemente. Refiere que desde anoche presenta un dolor pulsátil intolerable en un molar que empeora desesperadamente con cualquier alimento tibio o caliente, y que la única forma de conseguir un alivio transitorio de pocos segundos es mantener agua helada en la boca. En la discusión de patologías pulpares, ¿a qué estado fisiopatológico corresponde típicamente este fenómeno?",
    opciones=[
        "A una pulpa sana que responde fisiológicamente a las variaciones térmicas habituales.",
        "A una pulpitis irreversible sintomática en fase avanzada, donde el calor expande los gases y líquidos intrapulpares excitando las fibras C y el frío disminuye temporalmente la presión tisular.",
        "A una periodontitis apical asintomática producida por traumatismo oclusal leve.",
        "A una hipersensibilidad dentinaria cervical provocada por retracción gingival."
    ],
    correcta=1,
    distractores=[
        "Una pulpa sana nunca experimenta dolor insoportable que calme con agua helada constante.",
        "",
        "La periodontitis apical asintomática no produce dolor espontáneo severo ni responde con alivio al agua helada.",
        "La hipersensibilidad dentinaria se exacerba con el frío y no se alivia manteniendo agua helada dentro de la boca."
    ],
    explicacion="El paciente con el vaso de agua helada en la mano es un clásico en endodoncia: en las fases avanzadas de la pulpitis irreversible sintomática, las fibras C están altamente excitadas y el calor produce vasodilatación y expansión de los gases intrapulpares aumentando la presión a niveles insoportables; el frío produce vasoconstricción temporal y contracción de volumen, reduciendo la presión intrapulpar durante unos segundos.",
    tema="Fisiopatología del dolor pulpar: alivio con frío y exacerbación con calor",
    que="Comprender el mecanismo de exacerbación por calor y alivio temporal con frío en pulpitis avanzada.",
    clave="El calor expande los fluidos intrapulpares estimulando las fibras C; el agua helada disminuye momentáneamente la presión aliviando el dolor.",
    pistas=[
        "Visualiza al paciente típico que no suelta el vaso de agua helada en la sala de espera.",
        "Considera la ley física de los gases y la presión dentro de la cámara pulpar rígida."
    ],
    marcas_data=[
        ("única forma de conseguir un alivio transitorio de pocos segundos es mantener agua helada en la boca", "clave", "Signo clínico de alivio con frío"),
        ("empeora desesperadamente con cualquier alimento tibio o caliente", "dato", "Exacerbación térmica por calor"),
        ("¿a qué estado fisiopatológico corresponde típicamente este fenómeno?", "pide", "Estado fisiopatológico")
    ],
    steps_ideas=[
        ("Expansión volumétrica por calor", "La temperatura cálida expande el exudado inflamatorio y los gases estimulando intensamente las terminaciones libres."),
        ("Vasoconstricción momentánea", "El agua helada contrae brevemente el lecho vascular disminuyendo la presión sobre las fibras C."),
        ("Comprobación diagnóstica", "El cuadro clínico corresponde a una pulpitis irreversible sintomática avanzada.")
    ]
))

# 27 (Key 2: C)
questions.append(make_q(
    qid="odo-027", nivel=2,
    enunciado="Al realizar el examen clínico de movilidad dental en un incisivo que sufrió una luxación lateral, el clínico utiliza los mangos rígidos de dos instrumentos para evaluar el desplazamiento. De acuerdo con la escala clásica de Miller revisada en semiología endodóntica, ¿cómo se definen los tres grados de movilidad dental?",
    opciones=[
        "Grado uno: el diente se mueve un centímetro; grado dos: dos centímetros; grado tres: tres centímetros de desplazamiento.",
        "Grado uno: movilidad imperceptible a la vista; grado dos: movilidad con sangrado; grado tres: movilidad con dolor.",
        "Grado uno: desplazamiento vestibulolingual horizontal menor a un milímetro; grado dos: desplazamiento horizontal mayor a un milímetro; grado tres: desplazamiento horizontal severo acompañado de intrusión o depresión vertical en el alvéolo.",
        "Grado uno: rotación pura; grado dos: extrusión pura; grado tres: exfoliación espontánea."
    ],
    correcta=2,
    distractores=[
        "Las medidas en centímetros no se aplican a la movilidad dentro del alvéolo dental; se mide en fracciones de milímetro.",
        "El sangrado y el dolor no forman parte de la definición cuantitativa geométrica de los grados de Miller.",
        "",
        "Los grados de Miller no se definen por movimientos ortodóncicos puros ni por pérdida dental inmediata."
    ],
    explicacion="La escala de Miller clasifica la movilidad dental con los mangos de dos espejos: Grado uno: movimiento horizontal menor a un milímetro en sentido vestíbulo-lingual; Grado dos: movimiento horizontal mayor a un milímetro sin intrusión; Grado tres: movimiento horizontal acentuado que se acompaña de desplazamiento en sentido vertical (el diente se puede deprimir dentro del alvéolo).",
    tema="Semiología periodontal: grados de movilidad de Miller",
    que="Conocer la clasificación de movilidad dental de Miller aplicada al examen endodóntico.",
    clave="Miller clasifica: grado uno menor a un milímetro horizontal, grado dos mayor a un milímetro, grado tres con intrusión vertical.",
    pistas=[
        "Recuerda que la movilidad se mide usando dos mangos rígidos, nunca con los dedos.",
        "Ten presente que el grado tres incluye movimiento en sentido vertical hacia el interior del alvéolo."
    ],
    marcas_data=[
        ("escala clásica de Miller revisada en semiología endodóntica", "clave", "Escala de clasificación"),
        ("¿cómo se definen los tres grados de movilidad dental?", "pide", "Definición de grados")
    ],
    steps_ideas=[
        ("Técnica con dos mangos", "Los mangos rígidos de instrumental eliminan la deformación elástica de las yemas de los dedos al medir."),
        ("Criterio milimétrico y vertical", "El compromiso de fibras periodontales apicales permite la depresión vertical característica del grado tres."),
        ("Comprobación diagnóstica", "Verificamos que la definición en milímetros y depresión vertical corresponde a la escala de Miller.")
    ]
))

# 28 (Key 0: A)
questions.append(make_q(
    qid="odo-028", nivel=3,
    enunciado="En una intervención restauradora en un diente joven con pulpa sana, se produce una microexposición pulpar accidental menor a un milímetro por fresado mecánico bajo aislamiento absoluto con dique de goma. El sangrado se cohíbe con facilidad a los dos minutos. El docente explica en clase que actualmente existen materiales biocerámicos de última generación que estimulan la regeneración y la formación de un puente dentinario reparativo. ¿Cuál es el material de elección para este recubrimiento pulpar directo?",
    opciones=[
        "Agregado de trióxido mineral (MTA) o silicato de calcio biocerámico.",
        "Óxido de zinc y eugenol puro en consistencia fluida.",
        "Ácido fosfórico al treinta y siete por ciento aplicado directamente sobre el tejido sangrante.",
        "Formocresol puro con fijación química de la pulpa coronal."
    ],
    correcta=0,
    distractores=[
        "",
        "El eugenol libre en contacto directo con el tejido pulpar genera citotoxicidad y necrosis inflamatoria severa.",
        "El ácido fosfórico desnaturaliza las proteínas pulpares y destruye irreversiblemente la capa odontoblástica expuesta.",
        "El formocresol es un fijador tisular tóxico y mutagénico desaconsejado para preservar la vitalidad en dientes permanentes."
    ],
    explicacion="El agregado de trióxido mineral (MTA) y los silicatos de calcio biocerámicos son los materiales de elección para recubrimiento pulpar directo gracias a su excelente biocompatibilidad, alcalinidad prolongada bactericida, capacidad de sellado hermético e inducción de diferenciación celular para formar puentes de dentina terciaria reparativa.",
    tema="Terapéutica pulpar vital: recubrimiento pulpar directo con biocerámicos",
    que="Seleccionar el material biocerámico indicado para la preservación pulpar directa.",
    clave="El MTA o silicato de calcio biocerámico estimula la formación de puente dentinario con alta biocompatibilidad.",
    pistas=[
        "Recuerda la mención del profesor sobre los biocerámicos y el trióxido mineral agregado en las terapias vitales.",
        "Ten en cuenta qué material promueve el sellado biológico y la dentinogénesis reparativa."
    ],
    marcas_data=[
        ("materiales biocerámicos de última generación que estimulan la regeneración y la formación de un puente dentinario reparativo", "clave", "Propiedades del material buscado"),
        ("¿Cuál es el material de elección para este recubrimiento pulpar directo?", "pide", "Material de elección")
    ],
    steps_ideas=[
        ("Sellado hermético y bioactividad", "Los silicatos de calcio liberan iones de calcio formando hidroxiapatita que sella biológicamente la herida."),
        ("Alcalinidad reparadora", "El pH alcalino inicial desinfecta la superficie y estimula a las células mesenquimales a formar nuevos odontoblastos."),
        ("Comprobación diagnóstica", "El material de elección es el agregado de trióxido mineral (MTA) o silicato de calcio biocerámico.")
    ]
))

# 29 (Key 2: C)
questions.append(make_q(
    qid="odo-029", nivel=2,
    enunciado="Un paciente de 38 años asiste a la clínica endodóntica con una restauración provisional de ionómero de vidrio en el primer molar superior. Relata que hace tres semanas acudió a un centro de urgencias por dolor insoportable, donde le colocaron anestesia, le hicieron una cavidad en el centro del diente para calmar el dolor y le dijeron que debía buscar un endodoncista para terminar el tratamiento. En la radiografía se observa la cámara pulpar abierta y parcialmente despejada sin material de obturación en los conductos. Según el sistema diagnóstico de la AAE, ¿cuál es la categoría diagnóstica pulpar de este diente?",
    opciones=[
        "Diente previamente tratado.",
        "Necrosis pulpar séptica.",
        "Diente con terapia previamente iniciada.",
        "Pulpitis irreversible sintomática."
    ],
    correcta=2,
    distractores=[
        "Diente previamente tratado se reserva exclusivamente para piezas que ya tienen sus conductos radiculares completamente obturados con gutapercha y sellador.",
        "Aunque no hay pulpa vital intacta, la categoría formal estandarizada por haber recibido una intervención de urgencia parcial previa es terapia previamente iniciada.",
        "",
        "El diente ya no tiene tejido pulpar cameral intacto tras la pulpotomía o pulpectomía inicial de urgencia."
    ],
    explicacion="La Asociación Americana de Endodoncia establece la categoría «diente con terapia previamente iniciada» para aquellos casos en los que se realizó una intervención endodóntica parcial de urgencia (como pulpotomía o desbridamiento cameral) pero aún no se ha culminado la preparación y obturación definitiva del sistema de conductos radiculares.",
    tema="Clasificación diagnóstica AAE: terapia previamente iniciada",
    que="Diferenciar un diente previamente tratado de un diente con terapia previamente iniciada.",
    clave="Un diente intervenido de urgencia con apertura cameral pero sin obturación de conductos es un diente con terapia previamente iniciada.",
    pistas=[
        "Observa que el tratamiento se empezó en urgencias pero nunca se terminó ni se obturaron los conductos con gutapercha.",
        "Distingue entre un diente con la endodoncia ya terminada y uno que está a medio camino."
    ],
    marcas_data=[
        ("le hicieron una cavidad en el centro del diente para calmar el dolor y le dijeron que debía buscar un endodoncista para terminar", "clave", "Intervención parcial previa"),
        ("¿cuál es la categoría diagnóstica pulpar de este diente?", "pide", "Categoría diagnóstica AAE")
    ],
    steps_ideas=[
        ("Intervención previa incompleta", "El acto de urgencia desbridó la cámara coronal para descompresión pero los conductos radiculares siguen vacíos."),
        ("Nomenclatura estandarizada", "La categoría oficial de la AAE distingue explícitamente la terapia iniciada frente al tratamiento culminado."),
        ("Comprobación diagnóstica", "El diagnóstico pulpar es diente con terapia previamente iniciada.")
    ]
))

# 30 (Key 1: B)
questions.append(make_q(
    qid="odo-030", nivel=3,
    enunciado="Un paciente consulta por dolor intenso a la percusión y al masticar en el primer molar superior derecho. Al examen radiográfico se observa que los tres conductos radiculares fueron obturados con gutapercha hace cuatro años, pero el conducto mesiovestibular se encuentra subobturado a cuatro milímetros del ápice y se aprecia una radiolucidez periapical evidente alrededor de dicha raíz. A las pruebas de sensibilidad térmica no hay respuesta. De acuerdo con la clasificación diagnóstica formal de la AAE discutida en clase, ¿cuál es el diagnóstico integral?",
    opciones=[
        "Diente con terapia previamente iniciada con absceso apical agudo.",
        "Diente previamente tratado con periodontitis apical sintomática.",
        "Necrosis pulpar con periodontitis apical asintomática.",
        "Pulpitis irreversible sintomática con osteítis condensante."
    ],
    correcta=1,
    distractores=[
        "La terapia previamente iniciada se aplica a dientes sin obturación final, mientras que este molar ya fue completamente obturado con gutapercha en el pasado.",
        "",
        "En un diente con endodoncia previa ya no existe parénquima pulpar que pueda diagnosticarse como necrosis primaria; la categoría pulpar es diente previamente tratado.",
        "La pulpitis irreversible exige la presencia de tejido pulpar vital y la osteítis condensante cursa con radiopacidad periapical densa."
    ],
    explicacion="El diagnóstico pulpar es «diente previamente tratado» porque los conductos ya fueron obturados con material endodóntico (gutapercha). El diagnóstico periapical es «periodontitis apical sintomática» debido al dolor manifiesto ante la percusión y la masticación, acompañado de la radiolucidez apical por persistencia o sobreinfección bacteriana en el conducto subobturado.",
    tema="Diagnóstico en retratamiento: diente previamente tratado",
    que="Formular el diagnóstico integral en un diente con endodoncia previa y fracaso periapical sintomático.",
    clave="Un diente con conductos obturados con gutapercha que presenta dolor a la percusión es un diente previamente tratado con periodontitis apical sintomática.",
    pistas=[
        "Verifica que en la radiografía ya hay material de obturación en las raíces (endodoncia terminada en el pasado).",
        "Considera el dolor severo al percutir y masticar para el diagnóstico periapical."
    ],
    marcas_data=[
        ("conductos radiculares fueron obturados con gutapercha hace cuatro años", "clave", "Endodoncia previa terminada"),
        ("dolor intenso a la percusión y al masticar", "dato", "Síntoma periapical cardinal"),
        ("¿cuál es el diagnóstico integral?", "pide", "Diagnóstico integral AAE")
    ],
    steps_ideas=[
        ("Clasificación pulpar en retratamiento", "Al existir material de obturación intraconducto, la categoría pulpar estandarizada es diente previamente tratado."),
        ("Clasificación periapical sintomática", "El dolor agudo a las fuerzas de impacto oclusal y percusión vertical define la periodontitis apical sintomática."),
        ("Comprobación diagnóstica", "El diagnóstico definitivo es diente previamente tratado con periodontitis apical sintomática.")
    ]
))

with open("content/questions/odontologia.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Generated {len(questions)} questions in content/questions/odontologia.json successfully.")

from collections import Counter
c = Counter([q["correcta"] for q in questions])
print("Distribution of answers:")
for k in range(4):
    print(f"  {LETTERS[k]}: {c[k]}")

if __name__ == "__main__":
    pass
