"""Opciones balanceadas para odontología para eliminar sesgo de longitud.
Asegura que la opción correcta sea la más larga en ~25%-30% de los casos (16-19 de 62),
cumpliendo con la auditoría de calidad (< 50%).
"""

BALANCED_OPTIONS = {
    # 002 (corr=2) -> expand distractor 3
    "odo-002": [
        "Biopulpectomía cameral convencional bajo anestesia local con fresa de diamante y cucharilla afilada.",
        "Tratamiento restaurador atraumático exclusivamente cavitario utilizando ionómero de vidrio autopolimerizable.",
        "Drenaje a través del surco vestibular mediante incisión en el periostio si hay fluctuación palpable, o apertura cameral cuidadosa con irrigación copiosa de hipoclorito sódico y secado sin dejar el diente abierto.",
        "Prescripción de antibióticos sistémicos de amplio espectro en monoterapia por diez días consecutivos con enjuagues calientes de clorhexidina y colocación de compresas calientes extraorales sin intervención física sobre el diente causal."
    ],

    # 003 (corr=0) -> expand distractor 1
    "odo-003": [
        "Pulpitis reversible; el plan de tratamiento consiste en retirar la restauración filtrada o desadaptada, eliminar dentina cariada y colocar una protección dentinopulpar adecuada.",
        "Pulpitis irreversible sintomática con compromiso pulpar difuso; requiere realizar una biopulpectomía cameral y radicular completa con instrumentación biomecánica en la primera sesión clínica.",
        "Necrosis pulpar séptica con afección periapical incipiente; requiere medicación intraconducto prolongada con hidróxido de calcio.",
        "Periodontitis apical sintomática por hiperoclusión o trauma oclusal severo; requiere desgaste selectivo con fresa fina."
    ],

    # 004 (corr=3) -> expand distractor 2
    "odo-004": [
        "Iniciar apertura cameral simultánea de ambos premolares para verificar visualmente de cuál conducto drena exudado.",
        "Prescribir antibióticos sistémicos de amplio espectro por siete días y esperar a que el tracto fistuloso cierre solo.",
        "Realizar una biopsia escisional quirúrgica completa de todo el estoma y trayecto fistuloso mucoso bajo anestesia infiltrativa local profunda y enviarla a estudio patológico para descartar neoplasia mesenquimal benigna.",
        "Introducir cuidadosamente un cono de gutapercha radiopaco por el orificio de la fístula y tomar una radiografía periapical para seguir el trayecto exacto hasta el periápice del diente causal."
    ],

    # 005 (corr=1) -> expand distractor 0
    "odo-005": [
        "Prescribir amoxicilina con ácido clavulánico por catorce días consecutivos y citar a cirugía periapical con apicectomía y obturación retrógrada con ionómero de vidrio sin instrumentar previamente los conductos radiculares infectados.",
        "Tratamiento de conductos en dos sesiones: preparación biomecánica con abundante irrigación de hipoclorito sódico y medicación intraconducto con hidróxido de calcio durante ocho a diez días para desinfectar.",
        "Obturación inmediata en la primera cita para evitar la contaminación cruzada del conducto radicular.",
        "Exodoncia obligatoria del diente seguida de colocación de un implante osteointegrado oseosoportado inmediato."
    ],

    # 007 (corr=3) -> expand distractor 2
    "odo-007": [
        "Un absceso periapical agudo en fase de flemón difuso con celulitis facial hemifacial.",
        "Una necrosis pulpar asintomática con destrucción ósea periapical difusa de pronóstico desfavorable.",
        "Una pulpitis irreversible sintomática de larga evolución en fase supurativa terminal con destrucción radicular acelerada que demanda biopulpectomía inmediata bajo anestesia general intrahospitalaria ambulatoria.",
        "Una pulpitis irreversible hiperplásica (pólipo pulpar), originada por una respuesta proliferativa exuberante del tejido conectivo pulpar expuesto ante la irritación bacteriana continua en un diente joven."
    ],

    # 008 (corr=0) -> expand distractor 1
    "odo-008": [
        "Obturar el conducto radicular únicamente cuando esté asintomático, completamente seco, sin drenaje activo de exudado ni olor fétido y con el conducto instrumentado y desinfectado.",
        "Obturar en la misma sesión diagnóstica independientemente del exudado profuso o hemorragia apical activa, aprovechando el efecto sellador hermético del cemento biocerámico recién preparado.",
        "Mantener el conducto abierto al medio oral durante cinco días para que drene espontáneamente antes de obturar.",
        "Aplicar formocresol como medicación intraconducto durante tres semanas antes de proceder a la obturación final."
    ],

    # 009 (corr=1) -> expand distractor 0
    "odo-009": [
        "Prescribir analgésicos narcóticos mayores y solicitar una tomografía de haz cónico de todo el macizo craneofacial antes de efectuar cualquier exploración táctil o inspección intraoral exploratoria detallada en el consultorio dental.",
        "Realizar palpación apical con la yema del dedo sobre la mucosa vestibular en el fondo de surco, comparando con los dientes vecinos para identificar tumefacción localizada, dolor o fluctuación en el periápice.",
        "Introducir una sonda periodontal milimetrada por el ápice a través de la mucosa móvil con fuerza compresiva moderada.",
        "Aplicar peróxido de hidrógeno caliente sobre la encía insertada para comprobar la respuesta térmica de los tejidos blandos."
    ],

    # 010 (corr=2) -> expand distractor 0
    "odo-010": [
        "Utilizando la punta afilada del explorador dental presionando enérgicamente el surco oclusal con torsión mecánica lateral y percutiendo fuertemente en sentido vertical sin comparar previamente con los dientes de control contralaterales.",
        "Golpeando exclusivamente en sentido lateral con el mango metálico de la pinza algodonera sin evaluar previamente los dientes contralaterales sanos.",
        "Utilizando la parte roma y gruesa del mango del espejo dental, realizando golpecitos muy leves y evaluando primero un diente de control sano, porque un ligamento inflamado duele con mínima fuerza.",
        "Pidiéndole al paciente que mastique con fuerza una barra de cera dura o un rollo de algodón para reproducir el dolor periapical a la carga funcional."
    ],

    # 011 (corr=0) -> expand distractor 1
    "odo-011": [
        "Movilidad grado cero (fisiológica, menor a cero punto dos milímetros); grado uno (movilidad horizontal menor o igual a un milímetro); grado dos (mayor a un milímetro en sentido horizontal); grado tres (horizontal y vertical).",
        "Movilidad grado uno cuando el diente gira sobre su eje longitudinal más de noventa grados en el alvéolo óseo; grado dos cuando se desplaza lateralmente hacia mesial o distal; grado tres cuando se extrude espontáneamente sin soporte periodontal.",
        "Movilidad leve (uno), moderada (dos) y severa (tres) según la fuerza muscular que aplique el paciente al masticar.",
        "Movilidad clase A (reversible) y clase B (irreversible) según la cantidad de placa bacteriana acumulada en el margen."
    ],

    # 012 (corr=3) -> expand distractor 0
    "odo-012": [
        "El diente lingualizado se desplaza exactamente hacia el lado opuesto al que se movió el tubo de rayos X periapical, aplicando la regla matemática del paralelismo perpendicular estricto en el eje horizontal.",
        "El objeto más cercano a la película radiográfica siempre desaparece de la imagen en proyecciones mesiorradiales.",
        "La raíz mesial siempre se proyecta hacia distal independientemente del ángulo horizontal de incidencia del rayo.",
        "«Lo que está por lingual (o palatino) se mueve en la misma dirección hacia donde se desplaza el tubo de rayos X; lo que está por vestibular se desplaza en sentido contrario»."
    ],

    # 013 (corr=1) -> expand distractor 0
    "odo-013": [
        "Infiltrar la solución anestésica únicamente en la mucosa yugal retrocomisural y proceder a abrir la cámara pulpar de inmediato sin verificar ningún tipo de signo clínico subjetivo u objetivo en los tejidos blandos.",
        "Bloquear el nervio alveolar inferior y verificar que el labio inferior y la mitad de la lengua estén completamente anestesiados («adormecidos») antes de comenzar cualquier intervención.",
        "Comenzar la instrumentación del conducto y solo anestesiar si el paciente manifiesta dolor insoportable en el sillón.",
        "Inyectar dos gotas directamente en la encía libre interdental vestibular esperando cinco segundos antes de fresar."
    ],

    # 014 (corr=0) -> expand distractor 1
    "odo-014": [
        "Tomar una proyección radiográfica horizontal angulada (mesioradial o distoradial) aplicando la regla de Clark para separar las raíces superpuestas.",
        "Aumentar el tiempo de exposición radiológica al triple manteniendo la angulación ortoradial estrictamente perpendicular al eje coronal para saturar la densidad de la imagen periapical obtenida en el sensor digital.",
        "Tomar una radiografía oclusal panorámica modificada con haz oblicuo posterior sin variar la posición del colimador.",
        "Indicar inmediatamente una biopsia ósea exploratoria periapical para visualizar anatómicamente las dos raíces."
    ],

    # 015 (corr=2) -> expand distractor 0
    "odo-015": [
        "Diferenciar una pulpitis reversible de una irreversible sintomática aplicando anestesia tópica de benzocaína en spray durante cinco minutos continuos en todo el fondo del vestíbulo dental afectado.",
        "Confirmar el diagnóstico de necrosis pulpar infectada en el incisivo lateral inferior mediante bloqueo troncular.",
        "Identificar cuál diente de una misma hemiarcada es el causante del dolor difuso cuando el paciente no logra precisar el origen, anestesiando de mesial a distal diente por diente.",
        "Comprobar si existe fractura radicular vertical mediante la infiltración del ligamento periodontal interproximal."
    ],

    # 016 (corr=0) -> expand distractor 1
    "odo-016": [
        "Bloquear el nervio alveolar inferior, comprobar el adormecimiento del labio y lengua, y si persiste sensibilidad pulpar al fresar, aplicar técnicas complementarias (intraligamentosa o intrapulpar).",
        "Infiltrar anestésico tópico en gel al diez por ciento sobre el surco vestibular durante quince minutos y fresar directamente la dentina profunda sin administrar ningún tipo de bloqueo regional previo en el paciente.",
        "Iniciar de inmediato la anestesia intrapulpar a presión sin colocar previamente ningún anestésico troncular.",
        "Indicar anestesia general ambulatoria en pabellón quirúrgico para cualquier pulpotomía de premolares inferiores."
    ],

    # 017 (corr=3) -> expand distractor 2
    "odo-017": [
        "Lesión radiolúcida periapical redondeada con borde cortical bien definido en el ápice.",
        "Reabsorción radicular externa apical con borramiento total del conducto pulpar cameral.",
        "Ensanchamiento del espacio del ligamento periodontal mayor a tres milímetros con destrucción de la tabla ósea vestibular y fístula supurativa activa en el fondo de surco.",
        "Estructura ósea radiográfica de apariencia normal o leve ensanchamiento del ligamento periodontal, sin radiolucidez periapical evidente."
    ],

    # 018 (corr=1) -> expand distractor 0
    "odo-018": [
        "Zona radiolúcida ovalada circunscrita con halo esclerótico denso que desaparece por completo a las veinticuatro horas de iniciar la antibioticoterapia oral ambulatoria en el consultorio dental.",
        "Zona radiopaca difusa (no circunscrita) alrededor del ápice de un diente con inflamación pulpar prolongada, que no desaparece tras el tratamiento endodóntico.",
        "Línea radiolúcida fina que bordea exclusivamente el tercio coronal sin alterar el periápice.",
        "Reabsorción ósea vertical en forma de embudo con pérdida total de las corticales alveolares."
    ],

    # 019 (corr=2) -> expand distractor 0
    "odo-019": [
        "La pulpa necrótica no requiere aislamiento ya que las bacterias orales son inocuas para los conductos radiculares y el uso de tela de caucho aumentaría el tiempo de trabajo operatorio de forma innecesaria en la clínica diaria ante citas de urgencia.",
        "El aislamiento absoluto solo se indica durante la obturación final con gutapercha termoplastificada para evitar el vapor salival.",
        "El docente enfatizó que el aislamiento absoluto con tela de caucho y grapa es innegociable e intransigible en todo tratamiento endodóntico, para proteger la vía aérea, evitar deglución o aspiración de instrumental y prevenir contaminación microbiana salival.",
        "Se puede sustituir libremente por rollos de algodón en el vestíbulo si el paciente afirma tener claustrofobia leve."
    ],

    # 020 (corr=3) -> expand distractor 1
    "odo-020": [
        "Realizar pulpotomía cameral con hipoclorito sódico al cinco por ciento y obturar con ionómero de vidrio para diferir la endodoncia definitiva por diez años.",
        "Prescribir dexametasona intramuscular y amoxicilina durante diez días continuos, difiriendo la intervención mecánica sobre el diente hasta que los síntomas remitan completamente y el paciente no refiera dolor espontáneo ni a la masticación en el sillón dental.",
        "Apertura cameral y dejar el diente abierto con una torunda de algodón empapada en formocresol para aliviar la presión.",
        "Tratamiento de conductos (biopulpectomía completa) o pulpotomía de urgencia en caso de no disponer de tiempo para terminar la instrumentación biomecánica completa."
    ],

    # 021 (corr=0) -> expand distractor 1
    "odo-021": [
        "El docente enfatizó diferenciar con sonda si el tejido proviene de la pulpa cameral o de la encía vecina; si es pulpa en ápice abierto, realizar pulpotomía con biocerámico; si hay pérdida coronaria mayor al sesenta por ciento, requerirá poste de fibra de vidrio y corona completa.",
        "Realizar la exodoncia quirúrgica inmediata del molar permanente joven mediante osteotomía alveolar amplia y colocar una prótesis fija metalporcelana con pónticos distales apoyados en los premolares recién erupcionados para preservar el espacio interdental funcional en la arcada dental infantil.",
        "Tratamiento de conductos en una sola cita obturando con gutapercha termoplastificada caliente hasta el ápice inmaduro.",
        "Amputar el pólipo con bisturí eléctrico sin tocar la cámara pulpar y sellar la cavidad con amalgama de plata pulida."
    ],

    # 022 (corr=1) -> expand distractor 0
    "odo-022": [
        "Apertura cameral con fresa redonda de carburo número cuatro a baja velocidad bajo anestesia local troncular, instrumentación de los conductos radiculares con limas manuales tipo K de primera serie y secado con puntas de papel estériles en el sillón.",
        "Toma obligatoria de radiografía periapical inicial de diagnóstico previa a cualquier intervención o instrumentación de conductos, fundamentada en razones clínicas (anatomía, curvaturas, reabsorciones) y médico-legales.",
        "Aislamiento relativo con rollos de algodón y aspirador quirúrgico de alta potencia en la arcada dentaria.",
        "Irrigación de la cámara pulpar con agua oxigenada al diez por ciento y clorhexidina al dos por ciento."
    ],

    # 024 (corr=3) -> expand distractor 1
    "odo-024": [
        "Que el dolor es de origen periodontal exclusivo y no tiene relación con el tejido pulpar cameral.",
        "Que la pulpa se encuentra hiperémica con vasodilatación leve reversible que curará espontáneamente tras colocar barniz fluorado y realizar una sesión de profilaxis con copa de goma en todas las superficies dentarias.",
        "Que el conducto se encuentra calcificado por dentina terciaria reactiva protectora de origen odontoblástico secundario.",
        "Que el tejido pulpar coronario y radicular se encuentra necrótico (desvitalizado), perdiendo su vascularización e inervación sensitiva, lo que impide generar cualquier impulso nociceptivo ante el frío."
    ],

    # 025 (corr=0) -> expand distractor 1
    "odo-025": [
        "Tomar una proyección radiográfica con angulación horizontal (mesioangulada o distoangulada) aplicando la regla de Clark para separar las imágenes de las raíces superpuestas.",
        "Tomar una radiografía oclusal panorámica modificada con haz oblicuo posterior y aumentar el tiempo de exposición al triple para contrastar los contornos radiculares sobre el sensor digital directo.",
        "Aumentar el tiempo de exposición al doble manteniendo la proyección ortoradial perpendicular sin cambios.",
        "Indicar inmediatamente una resonancia magnética nuclear de la articulación temporomandibular bilateral."
    ],

    # 026 (corr=1) -> expand distractor 0
    "odo-026": [
        "Diferenciar un granuloma periapical de un quiste radicular mediante la visualización radiográfica del halo esclerótico perirradicular en la radiografía periapical digital tomada con técnica de paralelismo estricto en el consultorio.",
        "Localizar el trayecto y el diente origen de una fístula mucocutánea mediante la introducción de un cono de gutapercha radiopaco hasta el tope de resistencia seguido de una toma radiográfica periapical.",
        "Evaluar la vitalidad de la microcirculación pulpar en dientes con conductos atrésicos o calcificados.",
        "Medir la densidad trabecular ósea de la mandíbula en pacientes con sospecha de osteoporosis sistémica."
    ],

    # 027 (corr=2) -> expand distractor 0
    "odo-027": [
        "Sondaje periodontal uniforme menor a dos milímetros en todas las caras y movilidad dental grado tres con rotación completa del diente sobre su propio alvéolo dentario en la arcada dental.",
        "Bolsa periodontal ancha generalizada con cálculo subgingival abundante y respuesta pulpar positiva normal al frío.",
        "Movilidad aumentada con percusión positiva intensa y una bolsa periodontal estrecha y solitaria que profundiza súbitamente hasta el ápice, con pulpa necrótica no vital.",
        "Encía marginal engrosada y eritematosa sin movilidad dental y con sangrado espontáneo al cepillado."
    ],

    # 028 (corr=3) -> expand distractor 1
    "odo-028": [
        "Se aplica directamente calor con una barra de gutapercha al rojo vivo sobre la encía libre marginal para estimular la circulación colateral periférica.",
        "Se coloca una fresa de diamante a alta velocidad sin irrigación de agua sobre la cúspide dental durante diez segundos para generar fricción térmica controlada y evaluar si el paciente siente alivio con la vibración mecánica.",
        "Se irriga la mucosa vestibular con alcohol isopropílico al setenta por ciento para deshidratar los túbulos.",
        "Se aplica una torunda de algodón impregnada con spray de gas refrigerante sobre el tercio gingival o medio de la corona del diente sospechoso, comparando con un diente de control contralateral sano."
    ],

    # 030 (corr=1) -> expand distractor 0
    "odo-030": [
        "Prescribir analgésicos opiáceos y citar al paciente para dentro de tres meses para observar si el proceso osteolítico se detiene espontáneamente sin necesidad de intervenir físicamente los conductos radiculares.",
        "Tratamiento de conductos en dos sesiones: preparación biomecánica cuidadosa, abundante irrigación de hipoclorito sódico y medicación intraconducto con hidróxido de calcio entre citas durante ocho a diez días.",
        "Obturación inmediata en la primera cita con gutapercha termoplastificada para sellar el foramen apical.",
        "Exodoncia obligatoria del diente seguida de colocación inmediata de un implante osteointegrado."
    ],

    # 031 (corr=2) -> expand distractor 1
    "odo-031": [
        "Indagar exclusivamente los antecedentes médicos de diabetes e hipertensión de los abuelos.",
        "Calcular inmediatamente el presupuesto protésico de implantes dentales oseointegrados sin interrogar al paciente sobre sus quejas principales ni registrar síntomas.",
        "Identificar y registrar en sus propias palabras el motivo de consulta («lo que el paciente siente y describe»), pues orienta todo el diagnóstico.",
        "Prescribir de inmediato antibióticos sistémicos de amplio espectro antes de conversar con el paciente."
    ],

    # 032 (corr=3) -> expand distractor 0
    "odo-032": [
        "Preguntar únicamente si el paciente posee seguro odontológico privado y programar una profilaxis con pasta profiláctica suave sin examinar la mucosa oral ni interrogar sobre el dolor dental previo ni registrar antecedentes de enfermedades sistémicas.",
        "Prescribir antiinflamatorios no esteroideos y despedir al paciente sin realizar ningún examen clínico.",
        "Tomar impresiones preliminares de ambas arcadas dentales con alginato a temperatura ambiente.",
        "Indagar las ocho dimensiones del dolor: localización, inicio, tipo de dolor, duración, intensidad (escala de cero a diez), factores que lo alivian o empeoran, periodicidad y respuesta a analgésicos."
    ],

    # 033 (corr=0) -> expand distractor 1
    "odo-033": [
        "Pulpitis reversible con dolor provocado de corta duración; se trata eliminando la causa y colocando una restauración adaptada con protección dentinopulpar.",
        "Pulpitis irreversible sintomática de larga data que requiere biopulpectomía cameral y radicular completa en una o dos sesiones clínicas especializadas bajo aislamiento absoluto con tela de caucho.",
        "Necrosis pulpar séptica con afectación ósea periapical incipiente que demanda medicación prolongada con hidróxido de calcio.",
        "Periodontitis apical sintomática traumática que requiere ajuste oclusal selectivo con papel de articular fino."
    ],

    # 034 (corr=1) -> expand distractor 0
    "odo-034": [
        "Realizar una biopsia incisional de la piel facial bajo anestesia local profunda y enviar la muestra a estudio anatomopatológico sospechando un carcinoma de células escamosas metastásico cutáneo.",
        "Realizar examen endodóntico clínico y radiográfico completo de los dientes mandibulares anteriores y premolares para descartar una infección odontogénica crónica fistulizada hacia la piel.",
        "Prescribir cremas antibióticas tópicas con corticosteroides sobre la fístula cutánea durante seis meses.",
        "Extirpar quirúrgicamente la fístula facial sin revisar la cavidad oral ni tomar radiografías dentales."
    ],

    # 035 (corr=2) -> expand distractor 0
    "odo-035": [
        "Aplicar el frío sobre la mucosa vestibular móvil y esperar a que el paciente refiera mareo o sudoración fría sin tocar en ningún momento la superficie del esmalte dental sospechoso en la arcada dentaria, asumiendo que la mucosa refleja la pulpa.",
        "El diente de control contralateral sano no debe evaluarse nunca para no alterar la respuesta biológica del paciente.",
        "El frío se aplica con spray de gas refrigerante en una torunda de algodón sobre el tercio medio o cervical de la corona; evalúa intensidad, tiempo de latencia y tiempo de desaparición, comparando siempre con un diente sano.",
        "Si el paciente no siente frío en los primeros treinta segundos, se debe perforar el esmalte con fresa de diamante."
    ],

    # 036 (corr=3) -> expand distractor 0
    "odo-036": [
        "El calor genera una contracción rápida del líquido dentinario que alivia de inmediato la inflamación de la cámara pulpar mejorando la microcirculación de las fibras nerviosas mielínicas pulpares y estimulando la formación de osteocementoblastos reparativos.",
        "El calor nunca debe usarse en odontología porque destruye el esmalte dental a cualquier temperatura.",
        "El calor solo está indicado en dientes con coronas protésicas metálicas para evaluar la conductividad eléctrica.",
        "Si la temperatura intrapulpar aumenta más de cinco grados centígrados, se produce desnaturalización irreversible de proteínas pulpares y necrosis térmica; por ello se debe proteger el diente con vaselina y retirar el calor al primer aviso."
    ],

    # 037 (corr=0) -> expand distractor 1
    "odo-037": [
        "El test pulpar eléctrico evalúa únicamente la respuesta de las fibras nerviosas sensitivas intactas pero no el flujo sanguíneo vascular pulpar; un diente con flujo vascular íntegro pero sin inervación reactiva puede dar falso negativo.",
        "El test eléctrico mide directamente la saturación de oxígeno de la arteriola pulpar central mediante fotopletismografía óptica infrarroja transmitida a través de la corona clínica del diente analizado, garantizando un registro hemodinámico absoluto.",
        "El test eléctrico siempre es cien por ciento certero y sustituye por completo a las pruebas térmicas con frío.",
        "El test eléctrico se aplica colocando el electrodo sobre restauraciones metálicas de oro o amalgama sin aislante."
    ],

    # 039 (corr=2) -> expand distractor 0
    "odo-039": [
        "El cemento radicular acelular extrínseco; su reabsorción o discontinuidad apical traduce exfoliación dental fisiológica acelerada en pacientes adultos jóvenes con dentición permanente completa y sana.",
        "La cámara pulpar cameral; su discontinuidad indica presencia de un pólipo pulpar benigno en la corona.",
        "La lámina dura (cortical alveolar cribiforme); su pérdida o ensanchamiento periapical traduce desmineralización ósea activa por proceso inflamatorio o infeccioso.",
        "La encía queratinizada vestibular; su ruptura indica fractura del esmalte dental en la corona clínica."
    ],

    # 040 (corr=3) -> expand distractor 0
    "odo-040": [
        "Permite facturar automáticamente el costo del dique de goma y los honorarios profesionales a la empresa aseguradora privada antes de iniciar el tratamiento biomecánico en el consultorio dental.",
        "Evita que el paciente deba cepillarse los dientes en los tres días posteriores a la cita dental en el consultorio.",
        "Sirve para esterilizar químicamente el conducto radicular mediante los fotones de radiación ionizante emitidos.",
        "Permite documentar la anatomía previa, curvaturas radiculares, calcificaciones, reabsorciones o la presencia de instrumentos fracturados por operadores anteriores antes de tocar el diente."
    ],

    # 041 (corr=0) -> expand distractor 1
    "odo-041": [
        "Reconstruir previamente las paredes coronales ausentes con ionómero de vidrio o resina compuesta para permitir el aislamiento absoluto con grapa y crear un reservorio estanco de hipoclorito sódico durante la endodoncia.",
        "Iniciar de inmediato la instrumentación biomecánica sin colocar dique de goma sujetando las paredes cavitarias con rollos de algodón interproximales y gasas estériles impregnadas en clorhexidina para evitar perder tiempo en la sesión.",
        "Colocar un poste metálico colado en el conducto antes de retirar la caries y antes de la biopulpectomía.",
        "Citar a exodoncia quirúrgica inmediata asumiendo que un diente con pérdida mayor al sesenta por ciento es irrecuperable."
    ],

    # 042 (corr=1) -> expand distractor 0
    "odo-042": [
        "Garantizar legalmente al paciente que el tratamiento de conductos tendrá un éxito biológico de por vida del cien por ciento libre de cualquier tipo de dolor, fractura o molestia postoperatoria en el futuro tras firmar un pagaré bancario.",
        "Explicar claramente al paciente los riesgos inherentes al procedimiento (dolor postoperatorio, fractura de instrumental, sobreextensión de irrigante, perforación, necesidad de cirugía o pérdida dental) y obtener su firma.",
        "Cobrar los honorarios profesionales por anticipado antes de realizar la inspección clínica intraoral.",
        "Exonerar al odontólogo de toda responsabilidad penal ante negligencias operatorias graves cometidas en la clínica."
    ],

    # 043 (corr=2) -> expand distractor 0
    "odo-043": [
        "Infiltrar exclusivamente anestésico tópico en crema sobre el fondo de surco vestibular durante veinte minutos continuos y fresar sin aplicar ninguna técnica inyectable en los tejidos orales profundos.",
        "Administrar anestesia infiltrativa subperióstica vestibular en el molar inferior y comenzar a instrumentar.",
        "Realizar el bloqueo troncular del nervio alveolar inferior y lingual; si persiste sensibilidad pulpar al fresar, aplicar anestesia intraligamentosa o intrapulpar directa con presión hidráulica firme.",
        "Indicar anestesia general en quirófano hospitalario para realizar la apertura cameral de cualquier molar inferior."
    ],

    # 044 (corr=3) -> expand distractor 0
    "odo-044": [
        "Zona central vascularizada rica en miofibrillas contráctiles estriadas; capa periférica epitelial queratinizada impermeable a toxinas; membrana basal acelular rígida; estrato córneo protector apical calcificado.",
        "Capa cortical ósea externa; periostio celular interno; endostio medular reticular; capa sinovial periapical.",
        "Zona cementoblástica externa; estrato de fibras de Sharpey; zona cribiforme alveolar; plexo de Ruffini terminal.",
        "Capa de odontoblastos en la periferia pulpar; zona acelular de Weil; zona rica en células (fibroblastos y células mesenquimales indiferenciadas); zona central de la pulpa con vasos sanguíneos y fibras nerviosas."
    ],

    # 045 (corr=0) -> expand distractor 1
    "odo-045": [
        "Formativa (produce dentina continua), nutritiva (aporta nutrientes por capilares), sensitiva (inervación sensorial del dolor), defensiva (reacciona con inflamación y dentina terciaria) e inductora (induce amelogénesis embrionaria).",
        "Masticatoria (tritura alimentos duros en la boca), fonética (modula los sonidos articulados del lenguaje), gustativa (percibe los sabores dulce, salado y ácido en la lengua), deglutoria y salival (segrega saliva serosa y mucosa en los conductos de Stenon).",
        "Osteogénica (forma hueso maxilar), queratinizante (produce estrato córneo), inmunitaria humoral exclusiva y amortiguadora de cargas oclusales pesadas.",
        "Motora (genera contracción muscular pulpar), hemopoyética (produce hematíes en la cámara cameral), linfopoyética y fagocitaria general."
    ],

    # 046 (corr=1) -> expand distractor 0
    "odo-046": [
        "Bloquear completamente el flujo sanguíneo de la mandíbula cuando el paciente abre la boca durante la masticación en el sillón dental mediante un reflejo vagal inhibitorio transmitido a los vasos periapicales.",
        "Amortiguar el impacto mecánico oclusal distribuyendo las fuerzas al hueso alveolar y albergar mecanorreceptores y propioceptores que localizan con exactitud el diente inflamado.",
        "Producir esmalte dental accesorio en la raíz para sellar las cavidades de caries subgingivales en el tercio apical.",
        "Inervar la lengua y los músculos de la mímica facial mediante axones motores eferentes procedentes del ganglio ótico."
    ],

    # 047 (corr=2) -> expand distractor 0
    "odo-047": [
        "La formación de cálculos pulpares (pulpolitos) de fosfato cálcico dentro de la cámara cameral que obstruyen mecánicamente la entrada a los conductos radiculares de molares superiores e inferiores, comprimiendo los filetes nerviosos.",
        "La reabsorción osteoclástica masiva de la corona dental provocada por traumatismo oclusal excéntrico severo.",
        "La fijación y colonización de bacterias circulantes en el torrente sanguíneo hacia un tejido pulpar previamente traumatizado o con inflamación subclínica previa, provocando necrosis e infección sin caries visible.",
        "La perforación iatrogénica de la raíz producida por una fresa de Peeso desalineada durante la desobturación."
    ],

    # 048 (corr=3) -> expand distractor 0
    "odo-048": [
        "El uso de agua potable purificada en la jeringa triple y el secado de la cavidad con gasa estéril durante tres segundos continuos aplicando aire tibio a baja presión sobre la superficie cavitaria para no irritar la dentina.",
        "La colocación de rollos de algodón en el vestíbulo inferior para realizar una profilaxis con pasta fluorada de consistencia suave.",
        "La toma de impresiones dentales con alginato a temperatura ambiente en dientes con esmalte sano y encía marginal normal.",
        "El tallado cavitario sin abundante refrigeración con agua, el uso de fresas desgastadas que generan calor friccional excesivo, y la aplicación de fuerzas ortodónticas continuas excesivas que colapsan la microcirculación apical."
    ],

    # 049 (corr=0) -> expand distractor 1
    "odo-049": [
        "Realizar control clínico y radiográfico el día del accidente (día cero), a los quince días, un mes, tres meses, seis meses, doce meses y anualmente durante seis años.",
        "Realizar un único control a los diez años del traumatismo si el paciente nota dolor insoportable espontáneo en la arcada dental con movilidad extrema o fístula purulenta espontánea que drene hacia el vestíbulo bucal.",
        "Citar al paciente cada semana durante doce años consecutivos tomando radiografías oclusales cada cuarenta y ocho horas en el consultorio.",
        "No realizar ningún control posterior si el diente no presenta fractura de corona visible a simple vista el primer día de la consulta."
    ],

    # 050 (corr=1) -> expand distractor 0
    "odo-050": [
        "Pulpectomía completa con instrumentación biomecánica hasta el ápice inmaduro y obturación inmediata con gutapercha termoplastificada a presión hidráulica caliente para sellar rápidamente el orificio del foramen radicular embudado.",
        "Pulpotomía coronal superficial o profunda preservando la pulpa radicular vital y sellado con biocerámico (MTA o biodentine), promoviendo la apexogénesis para que la raíz termine de formarse en longitud y grosor.",
        "Apicectomía quirúrgica periapical con ostectomía vestibular amplia y colocación de un tapón retrógrado de amalgama de plata sin mercurio residual, difiriendo la endodoncia por cinco años.",
        "Exodoncia obligatoria del diente inmaduro y colocación de una corona protésica fija provisional apoyada en los dientes vecinos."
    ],

    # 051 (corr=2) -> expand distractor 0
    "odo-051": [
        "Apertura cameral y dejar el conducto totalmente abierto al medio oral durante tres semanas consecutivas con citas semanales para realizar lavados orales con clorhexidina al cero punto doce por ciento y agua oxigenada comercial diluida en partes iguales hasta que el exudado desaparezca espontáneamente.",
        "Obturación inmediata con conos de gutapercha y cemento sellador en la primera sesión diagnóstica de urgencia.",
        "Apertura cameral de urgencia, preparación biomecánica copiosa con hipoclorito sódico, colocación de hidróxido de calcio intraconducto, y confección de un tapón apical de cuatro milímetros de material biocerámico (MTA o biodentine) para sellar el foramen abierto.",
        "Tracción ortodóntica rápida con extrusión dental violenta para reducir el diámetro del foramen apical."
    ],

    # 052 (corr=3) -> expand distractor 0
    "odo-052": [
        "El hidróxido de calcio es un antibiótico bactericida derivado de la tetraciclina que tiñe los túbulos dentinarios de color pardo oscuro facilitando la visualización directa del conducto bajo microscopio quirúrgico operatorio y esteriliza los conductos en diez minutos.",
        "El hidróxido de calcio disuelve el cemento sellador y facilita la colocación de postes de fibra de cuarzo.",
        "El hidróxido de calcio se endurece como piedra y sustituye a la gutapercha en la obturación tridimensional final.",
        "Permite que la medicación intraconducto con hidróxido de calcio actúe durante ocho a diez días aprovechando su pH alcalino antibacteriano, disolviendo restos necróticos y neutralizando lipopolisacáridos antes de obturar herméticamente."
    ],

    # 053 (corr=0) -> expand distractor 1
    "odo-053": [
        "Realizar desbridamiento del conducto con abundante irrigación de hipoclorito sódico, lograr drenaje a través del conducto o por incisión mucosa si hay fluctuación, colocar torunda estéril seca y sellado temporal hermético (nunca dejar abierto); prescribir amoxicilina solo si hay síntomas sistémicos.",
        "Abrir la cámara pulpar de par en par con fresa redonda grande y dejar el diente completamente abierto al medio oral durante siete días consecutivos para que los gases purulentos se ventilen libremente en la saliva bucal del paciente antes de medicar con pastas antibióticas.",
        "Prescribir antibióticos sistémicos de amplio espectro en monoterapia sin tocar el diente ni realizar apertura cameral.",
        "Obturar el conducto radicular de forma inmediata con gutapercha termoplastificada para evitar que salgan bacterias al periápice."
    ],

    # 054 (corr=1) -> expand distractor 0
    "odo-054": [
        "Prescribir antibióticos orales durante quince días continuos para cerrar la fístula antes de realizar la apertura cameral diagnóstica y realizar enjuagues calientes con infusión de caléndula cada cuatro horas sobre la encía inflamada para acelerar la maduración del absceso crónico.",
        "No requiere antibióticos sistémicos por ser una infección crónica drenante sin compromiso sistémico; el tratamiento es la endodoncia desinfectando con hidróxido de calcio empacado con lentulo en giro antihorario, tras lo cual la fístula cerrará espontáneamente en unos ocho días.",
        "Realizar resección quirúrgica del estoma fistuloso con bisturí bajo anestesia infiltrativa profunda sin tratar el conducto.",
        "Dejar el conducto abierto con una torunda de algodón empapada en paramonoclorofenol alcanforado durante tres semanas."
    ],

    # 055 (corr=2) -> expand distractor 0
    "odo-055": [
        "El quiste periapical tiene pulpa vital sensible al frío y el granuloma tiene pulpa necrótica no reactiva en la arcada dental con sangrado profuso a la palpación apical y aumento de volumen fluctuante en la tabla vestibular maxilar con borramiento del surco nasogeniano.",
        "El granuloma siempre mide más de cinco centímetros de diámetro y el quiste menos de un milímetro en la radiografía.",
        "Ambas presentan necrosis pulpar y radiolucidez periapical idéntica en la radiografía; el quiste verdadero presenta cavidad patológica revestida por epitelio escamoso estratificado derivado de los restos epiteliales de Malassez, confirmable solo por biopsia histopatológica.",
        "El quiste se cura únicamente con antibióticos orales y el granuloma requiere radioterapia periapical localizada."
    ],

    # 056 (corr=3) -> expand distractor 0
    "odo-056": [
        "Indica que el diente presenta necrosis pulpar aséptica y requiere de forma urgente una biopulpectomía cameral completa con instrumentación biomecánica manual o mecanizada en dos citas clínicas consecutivas con colocación de conos de gutapercha de conicidad variable.",
        "Señala la presencia de un quiste radicular inflamatorio odontogénico que exige enucleación quirúrgica con legrado.",
        "Confirma una fractura radicular vertical incompleta que demanda la exodoncia atraumática inmediata de los tres dientes.",
        "Confirma que la displasia cementoósea periapical se encuentra en etapa osteolítica en dientes vitales sanos; no requiere endodoncia ni tratamiento invasivo, únicamente seguimiento clínico y radiográfico periódico."
    ],

    # 057 (corr=0) -> expand distractor 1
    "odo-057": [
        "Indica una fractura radicular vertical; los hallazgos típicos son una bolsa periodontal estrecha y profunda localizada en un solo punto, radiolucidez en forma de «J» invertida o halo perirradicular, dolor a la masticación y necesidad de confirmación con tomografía computarizada de haz cónico (CBCT).",
        "Indica una sobreobturación apical de cemento biocerámico que generó una reacción granulomatosa estéril autolimitada en el ligamento periodontal que desaparecerá espontáneamente a los seis meses de seguimiento clínico radiográfico riguroso con radiografías periapicales digitales periódicas.",
        "Corresponde a un granuloma periapical común que se resuelve cambiando la medicación intraconducto de hidróxido de calcio.",
        "Traduce una luxación intrusiva antigua que soldó el diente al hueso alveolar sin comprometer la integridad radicular."
    ],

    # 058 (corr=1) -> expand distractor 0
    "odo-058": [
        "La reabsorción superficial es perforante de evolución galopante irreversible y la inflamatoria cura espontáneamente sin tratamiento alguno en los dientes de pacientes adolescentes o jóvenes con buena higiene oral y ausencia de placa bacteriana detectable a la inspección clínica.",
        "La reabsorción superficial es una respuesta autolimitada que cicatriza con nuevo cemento si cesa el estímulo; la reabsorción radicular externa inflamatoria es progresiva, asociada a necrosis pulpar infectada que estimula osteoclastos a través de los túbulos, requiriendo endodoncia completa e hidróxido de calcio.",
        "Ambas reabsorciones se originan exclusivamente dentro de la cámara pulpar por células clásticas de la propia pulpa.",
        "La reabsorción inflamatoria ocurre únicamente en dientes sometidos a blanqueamiento interno con perborato de sodio."
    ],

    # 059 (corr=2) -> expand distractor 1
    "odo-059": [
        "Se observa una lesión radiopaca difusa en la corona y se trata exclusivamente con enjuagues de bicarbonato sódico.",
        "Se presenta como un defecto óseo en el cuello del diente con encía hiperplásica y se cura espontáneamente sin tocar la pulpa realizando una gingivectomía con bisturí eléctrico y pulido radicular cuidadoso de la superficie de cemento radicular expuesta.",
        "Se observa un ensanchamiento radiolúcido simétrico y redondeado en forma de balón o ampolla dentro de los límites del conducto pulpar; el tratamiento es la endodoncia completa con hidróxido de calcio para detener el avance de las células clásticas.",
        "Ocurre exclusivamente en dientes con endodoncias terminadas hace veinte años y exige la amputación quirúrgica de la raíz."
    ],

    # 060 (corr=3) -> expand distractor 0
    "odo-060": [
        "Es causada por masticar hielo y se distingue porque el diente se mueve como un péndulo con sangrado constante en encía libre tras fracturarse el tercio medio de la raíz por sobrecarga biomecánica oclusal brusca no amortiguada por el ligamento periodontal.",
        "Es originada por fluorosis dental y se distingue porque el esmalte se torna transparente en las cúspides de premolares.",
        "Es producida por la ingesta de cítricos y se caracteriza por la pérdida del borde incisal con dolor leve al dulce.",
        "Ocurre típicamente tras un traumatismo severo con avulsión y desecación del ligamento periodontal; las células osteogénicas sustituyen la raíz por hueso alveolar, provocando anquilosis con sonido metálico seco a la percusión y pérdida de movilidad fisiológica."
    ],

    # 061 (corr=0) -> expand distractor 1
    "odo-061": [
        "Amoxicilina dos gramos vía oral administrados en una dosis única una hora antes del procedimiento; en pacientes alérgicos a penicilinas, clindamicina seiscientos miligramos (o azitromicina quinientos miligramos) vía oral una hora antes.",
        "Prescribir penicilina benzatínica intramuscular de un millón doscientas mil unidades cada doce horas durante quince días consecutivos tras la cita odontológica en el consultorio dental para esterilizar los tejidos blandos bucales y prevenir bacteriemias transitorias.",
        "Tomar una tableta de ampicilina de quinientos miligramos al día siguiente de la cita dental si el paciente presenta fiebre o dolor.",
        "Indicar colutorios de clorhexidina al cero punto doce por ciento sin administrar ningún tipo de antibiótico sistémico previo en el paciente."
    ],

    # 062 (corr=1) -> expand distractor 0
    "odo-062": [
        "El efecto férula es una técnica ortodóntica fija que consiste en ferulizar seis dientes anteriores con alambre trenzado de acero inoxidable y resina fluida durante seis meses continuos para evitar la pérdida de inserción periodontal tras una contusión o subluxación severa.",
        "El docente explicó que el efecto férula exige conservar al menos dos milímetros de altura de dentina coronal sana en los trescientos sesenta grados de la circunferencia dental sobre el margen gingival; esto previene fracturas radiculares catastróficas por efecto cuña del poste.",
        "Exige conservar al menos diez milímetros de esmalte en las cúspides vestibulares sin importar la dentina interproximal.",
        "Indica que el poste de fibra debe quedar flotando en la mitad del conducto sin contactar las paredes dentinarias."
    ]
}
