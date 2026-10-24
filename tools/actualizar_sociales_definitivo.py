"""Script para actualizar preguntas de Ciencias Sociales en scc, soc y cfi
Reemplaza todas las plantillas 'criterio central' y razones repetidas por explicaciones pedagógicas
específicas, libres de muletillas y con claves verificadas al 100%.
"""
import json

PREGUNTAS_SOCIALES = {
    "scc-i001": {
        "correcta": 1,
        "explicacion": "El segundo argumento defiende el vegetarianismo desde el deber ético de no causar daño o sufrimiento a los animales, considerándolos sujetos morales, mientras que el primero lo hace desde el posible perjuicio a la salud humana por la energía residual del animal (opción B).",
        "distractores": [
            "Es incorrecta porque clasifica como similares dos posturas con premisas dispares: una apela a la salud humana egoísta y la otra al bienestar y dignidad animal.",
            "",
            "Es incorrecta porque no se limita a contrastar salud humana con bienestar animal, sino que omite si ambas comparten el principio común de protección animal.",
            "Es incorrecta porque desvía la comparación hacia la dirección física del daño en lugar de confrontar la fundamentación ética de los argumentos."
        ]
    },
    "scc-i002": {
        "correcta": 0,
        "explicacion": "El argumento de los residentes comete la falacia de asociar de forma causal e inevitable la pobreza económica con la delincuencia. Argumentar que los delincuentes que operan en un sector no necesariamente habitan en él cuestiona directamente dicha generalización (opción A).",
        "distractores": [
            "",
            "Es incorrecta porque sostiene una afirmación insostenible y falsa al asegurar que ningún delincuente proviene de sectores vulnerables.",
            "Es incorrecta porque asume implícitamente que los habitantes pobres son delincuentes en potencia que solo cambiarían con más recursos.",
            "Es incorrecta porque refuerza el prejuicio clasista al vincular la desesperación de la pobreza con la justificación del delito."
        ]
    },
    "scc-i003": {
        "correcta": 3,
        "explicacion": "El rector reproduce el prejuicio infundado de que la orientación sexual de un docente puede transmitirse o influir en la identidad sexual de los estudiantes si no se autocensura, condicionando indebidamente su idoneidad pedagógica (opción D).",
        "distractores": [
            "Es incorrecta porque es una observación demográfica sobre la población mundial que no responde a la acusación discriminatoria de adoctrinamiento.",
            "Es incorrecta porque formula un llamado ético a la empatía y al amor, pero no desarticula la falsa creencia de que la orientación sexual se contagia.",
            "Es incorrecta porque expone explicaciones biopsicosociales sobre la sexualidad humana sin abordar el prejuicio educativo concreto del rector.",
            ""
        ]
    },
    "scc-i004": {
        "correcta": 1,
        "explicacion": "El orden cronológico exacto de los magnicidios colombianos es: 3. Rafael Uribe Uribe (1914), 2. Jorge Eliécer Gaitán (1948), 1. Luis Carlos Galán (1989) y 4. Álvaro Gómez Hurtado (1995), secuencia correspondiente a la opción B.",
        "distractores": [
            "Es incorrecta porque ubica el magnicidio de Gaitán (1948) antes del asesinato del general Rafael Uribe Uribe en 1914.",
            "",
            "Es incorrecta porque invierte el orden de Galán (1989) y Gaitán (1948), situando erróneamente a Galán antes de los sucesos de El Bogotazo.",
            "Es incorrecta porque arranca con el magnicidio más reciente de la lista, el de Álvaro Gómez Hurtado acaecido en 1995."
        ]
    },
    "scc-i005": {
        "correcta": 2,
        "explicacion": "Las dos posturas se oponen diametralmente en la estrategia estatal: una defiende la prevención pedagógica y sanitaria del consumo, mientras que la otra promueve la represión penal y policial estricta contra las redes de narcotráfico (opción C).",
        "distractores": [
            "Es incorrecta porque ninguna de las dos posturas respalda legalizar el narcotráfico; ambas lo rechazan pero debaten el enfoque de intervención.",
            "Es incorrecta porque afirma equivocadamente que las dos posturas son semejantes y que ambas apoyan la regulación legal del mercado de estupefacientes.",
            "",
            "Es incorrecta porque pasa por alto que la segunda postura no se enfoca en proteger a los consumidores sino en encarcelar y castigar penalmente."
        ]
    },
    "scc-i006": {
        "correcta": 2,
        "explicacion": "Aunque la votación cumpla formalidades democráticas por mayoría, no atiende equitativamente los intereses de todos los copropietarios, ya que los residentes del primer piso sufren desproporcionadamente la contaminación auditiva nocturna (opción C).",
        "distractores": [
            "Es incorrecta porque los propietarios de pisos superiores sí tienen acceso al salón comunal y se benefician de las fiestas sin sufrir el ruido constante.",
            "Es incorrecta porque confunde la aprobación mayoritaria de una norma con la coincidencia real de intereses y bienestar de todos los habitantes.",
            "",
            "Es incorrecta porque reduce la justicia de la decisión al procedimiento de votación, ignorando el perjuicio material insoportable para los vecinos inmediatos."
        ]
    },
    "scc-i007": {
        "correcta": 0,
        "explicacion": "Modificar los planos constructivos para salvaguardar parte de la flora y fauna del humedal atiende las demandas ambientales sin clausurar el proyecto, permitiendo la continuidad de la actividad económica de la constructora (opción A).",
        "distractores": [
            "",
            "Es incorrecta porque la concertación no ignora a los ambientalistas ni destruye íntegramente el humedal, sino que adopta medidas de mitigación.",
            "Es incorrecta porque no anula el negocio inmobiliario de la constructora, sino que ajusta el diseño para garantizar la coexistencia del proyecto.",
            "Es incorrecta porque la propuesta no anula el beneficio mutuo, sino que busca un punto intermedio entre desarrollo urbanístico y protección ecológica."
        ]
    },
    "scc-i008": {
        "correcta": 2,
        "explicacion": "Las estrategias de densificación urbana, legalización y mejoramiento de barrios informales y transporte público masivo son complementarias, pues convergen en mitigar los costos sociales, ambientales y económicos del crecimiento urbano descontrolado (opción C).",
        "distractores": [
            "Es incorrecta porque las medidas no se restringen a potenciar los centros tradicionales, sino a integrar los asentamientos de la periferia.",
            "Es incorrecta porque el objetivo primordial es la gestión de la población y el hábitat urbano, no la restauración de la producción agraria.",
            "",
            "Es incorrecta porque es falso que la legalización de barrios y el transporte popular prioricen a las familias de estratos socioeconómicos altos."
        ]
    },
    "scc-i009": {
        "correcta": 2,
        "explicacion": "De acuerdo con el artículo 378 de la Constitución Política de Colombia, la Carta Magna puede ser reformada por el Congreso, por una Asamblea Constituyente o directamente por el pueblo mediante referendo (opción C).",
        "distractores": [
            "Es incorrecta porque la consulta popular sirve para decidir sobre asuntos de conveniencia política general, pero no tiene competencia reformatoria de la Constitución.",
            "Es incorrecta porque el plebiscito es convocado por el presidente para apoyar o rechazar una política ejecutiva, no para alterar el articulado constitucional.",
            "",
            "Es incorrecta porque el cabildo abierto es una reunión deliberativa local ante concejos municipales o juntas administradoras, sin facultades constituyentes."
        ]
    },
    "scc-i010": {
        "correcta": 2,
        "explicacion": "La iniciativa popular legislativa ciudadana requiere el respaldo de un número de firmas equivalente a al menos el 5 % del censo electoral vigente para poder radicar válidamente un proyecto de ley ordinaria ante el Congreso (opción C).",
        "distractores": [
            "Es incorrecta porque la Constitución sí reconoce el derecho político de los ciudadanos a presentar proyectos de ley mediante iniciativa popular.",
            "Es incorrecta porque un solo ciudadano no puede radicar individualmente un proyecto de ley sin el respaldo del porcentaje requerido del censo.",
            "",
            "Es incorrecta porque el requisito del 5 % alude al censo de votantes ciudadanos, no al apoyo porcentual de los miembros del Congreso de la República."
        ]
    },
    "scc-i011": {
        "correcta": 0,
        "explicacion": "El mecanismo del referendo constitucional está expresamente previsto en la Constitución (Art. 378) como vía de reforma política impulsada por el Gobierno o los ciudadanos tras la aprobación de una ley en el Congreso (opción A).",
        "distractores": [
            "",
            "Es incorrecta porque la Asamblea Constituyente no es el único mecanismo de reforma; también proceden el acto legislativo en el Congreso y el referendo.",
            "Es incorrecta porque el presidente no puede expedir reformas constitucionales por decreto unilateral sin aprobación del Congreso y votación popular.",
            "Es incorrecta porque niega la existencia misma del referendo aprobatorio constitucional, consagrado en la legislación electoral colombiana."
        ]
    },
    "scc-i012": {
        "correcta": 2,
        "explicacion": "Los ciudadanos denuncian un claro conflicto de intereses y presunta corrupción, ya que el mandatario y sus allegados adquirieron predios rurales y posteriormente modificaron el PBOT para valorizarlos con inversiones públicas (opción C).",
        "distractores": [
            "Es incorrecta porque presupone que la denuncia obedece a envidia o falta de beneficio de los vecinos, ignorando el presunto delito contra la administración.",
            "Es incorrecta porque los habitantes no critican la ausencia de infraestructura, sino la desviación interesada de recursos hacia terrenos del alcalde.",
            "",
            "Es incorrecta porque falsea la motivación de los denunciantes presentándolos como opositores a la inversión rural, cuando reprochan el enriquecimiento indebido."
        ]
    },
    "scc-i013": {
        "correcta": 3,
        "explicacion": "El estado de excepción altera el principio de separación y distribución de poderes públicos porque faculta al presidente (Rama Ejecutiva) para decretar normas con fuerza material de ley, potestad que en tiempos ordinarios corresponde con exclusividad al Congreso (opción D).",
        "distractores": [
            "Es incorrecta porque el propio fragmento menciona que el presidente queda facultado para modificar partidas del presupuesto nacional.",
            "Es incorrecta porque la facultad de restringir protestas es un acto de policía y orden público, no la causa estructural de alteración entre ramas.",
            "Es incorrecta porque la captura preventiva administrativa es excepcional, pero la mayor concentración institucional radica en la usurpación de la función legislativa.",
            ""
        ]
    },
    "scc-i014": {
        "correcta": 3,
        "explicacion": "El control político formal sobre la gestión pública (citaciones a ministros a debate de control político y eventual moción de censura) es una función constitucional asignada de forma exclusiva a la Rama Legislativa (opción D).",
        "distractores": [
            "Es incorrecta porque la organización electoral se encarga de los comicios y el registro civil, careciendo de facultades de control político gubernamental.",
            "Es incorrecta porque el Ejecutivo está integrado por los ministros y el presidente, quienes son los sujetos pasivos receptores del control.",
            "Es incorrecta porque la Rama Judicial administra justicia e impone sanciones jurídicas, pero no adelanta juicios de control político partidista.",
            ""
        ]
    },
    "scc-i015": {
        "correcta": 1,
        "explicacion": "El Artículo 44 de la Constitución establece el principio del interés superior de los niños y niñas, señalando taxativamente que sus derechos prevalecen sobre los derechos de los demás (opción B).",
        "distractores": [
            "Es incorrecta porque el plebiscito es un mecanismo de participación ciudadana y no una norma de jerarquía de derechos de los menores.",
            "",
            "Es incorrecta porque la consulta popular convoca al electorado para pronunciarse sobre una pregunta de trascendencia, sin definir derechos fundamentales de la infancia.",
            "Es incorrecta porque el cabildo abierto es una figura de deliberación comunitaria local en concejos municipales."
        ]
    },
    "scc-i016": {
        "correcta": 0,
        "explicacion": "Ambas caricaturas convergen en denunciar la corrupción electoral mediante la compra de votos, donde la necesidad material de los ciudadanos es manipulada por maquinarias clientelistas a cambio de dádivas o favores inmediatos (opción A).",
        "distractores": [
            "",
            "Es incorrecta porque no critican el ausentismo electoral, sino la distorsión del sufragio mediante prácticas corruptas de compra de conciencias.",
            "Es incorrecta porque no cuestionan la propaganda o el diseño de las campañas, sino el delito electoral de inducir el voto a cambio de dinero o tejas.",
            "Es incorrecta porque no señalan la violencia física en las urnas, sino la cooptación económica de la libertad democrática del votante."
        ]
    },
    "scc-i017": {
        "correcta": 2,
        "explicacion": "El texto sustenta la creación del Frente Nacional (pacto bipartidista entre liberales y conservadores para alternarse la presidencia y repartirse los cargos públicos) con el fin de poner fin a la época de La Violencia y neutralizar la dictadura militar (opción C).",
        "distractores": [
            "Es incorrecta porque extrapola indebidamente el contexto colombiano de los años 50 a las ideologías totalitarias y al fascismo europeo de entreguerras.",
            "Es incorrecta porque no manifiesta un respaldo popular a la dictadura de Gustavo Rojas Pinilla, sino una concertación de élites para recuperar el poder.",
            "",
            "Es incorrecta porque el autor no advierte contra el acuerdo de los dos partidos, sino que precisamente promueve y justifica su alianza compartida."
        ]
    },
    "scc-i018": {
        "correcta": 3,
        "explicacion": "El fragmento justifica la existencia de grupos paramilitares o de autodefensa argumentando que surgieron como respuesta obligada ante la agresión guerrillera y la incapacidad de las fuerzas estatales para proteger sus propiedades y vidas (opción D).",
        "distractores": [
            "Es incorrecta porque no se enfoca en las pérdidas mercantiles de las empresas, sino en legitimar el uso de las armas al margen del Estado.",
            "Es incorrecta porque no propone una legislación de paz ni la intermediación del parlamento, sino una postura beligerante de justificación de autodefensa.",
            "Es incorrecta porque no adopta una perspectiva analítica neutral de un académico, sino un alegato testimonial directo de parte involucrada en las armas.",
            ""
        ]
    },
    "scc-i019": {
        "correcta": 3,
        "explicacion": "Las políticas de privatización de telecomunicaciones y banca pública impulsadas a finales de los años 90 responden al Consenso de Washington, que promovía reducir el gasto fiscal, achicar la estructura estatal y desregular los mercados (opción D).",
        "distractores": [
            "Es incorrecta porque las medidas no fueron actos arbitrarios aislados, sino políticas de ajuste estructural acordadas en marcos económicos formales.",
            "Es incorrecta porque privatizar implica despojarse de activos productivos, lo opuesto a incrementar la presencia del Estado como administrador.",
            "Es incorrecta porque, si bien hubo recomendaciones foráneas, la característica definitoria de la medida interna fue la reducción del aparato público.",
            ""
        ]
    },
    "scc-i020": {
        "correcta": 2,
        "explicacion": "Limitar el papel del Estado a garantizar la libre competencia y salvaguardar los derechos de propiedad para que las fuerzas del mercado asignen los recursos es el principio rector de la doctrina neoliberal (opción C).",
        "distractores": [
            "Es incorrecta porque el socialismo propugna la planificación centralizada y la propiedad colectiva o estatal de los medios productivos.",
            "Es incorrecta porque la monarquía alude a una forma dinástica de gobierno político, no a un modelo específico de política económica de mercado.",
            "",
            "Es incorrecta porque la democracia define el sistema político de soberanía popular, mientras que el texto describe una doctrina de economía de libre mercado."
        ]
    },
    "scc-i021": {
        "correcta": 2,
        "explicacion": "Al señalar que la eficiencia económica no puede desligarse de la equidad y que el mercado por sí solo genera exclusión, el texto postula la necesidad imperiosa de la intervención estatal para redistribuir la riqueza y proteger a los desfavorecidos (opción C).",
        "distractores": [
            "Es incorrecta porque se centra en la justicia distributiva social y no simplemente en la técnica de administración de las finanzas públicas.",
            "Es incorrecta porque el pasaje afirma lo contrario: advierte que el mercado abandonado a su suerte genera desigualdades e inequidad.",
            "",
            "Es incorrecta porque el texto previene contra la desregulación indiscriminada y no defiende la privatización como garante de equidad."
        ]
    },
    "scc-i022": {
        "correcta": 2,
        "explicacion": "Una nación recurre al proteccionismo arancelario cuando la entrada masiva de productos agrícolas extranjeros subsidiados o baratos amenaza con arruinar a los campesinos y productores agropecuarios nacionales (opción C).",
        "distractores": [
            "Es incorrecta porque el avance técnico estimula la competitividad y la exportación, no la urgencia de cerrar fronteras aduaneras a los alimentos.",
            "Es incorrecta porque un país sin suelos fértiles requiere obligatoriamente importar alimentos y no bloquear su ingreso con altos impuestos.",
            "",
            "Es incorrecta porque un país con balanza comercial superavitaria y vocación exportadora tiende al libre comercio y no a trabas arancelarias."
        ]
    },
    "scc-i023": {
        "correcta": 1,
        "explicacion": "El despojo y desplazamiento forzado sistemático revela cómo los actores armados ilegales persiguen el control territorial para el narcotráfico, la minería ilegal y la apropiación fraudulenta de tierras productivas (opción B).",
        "distractores": [
            "Es incorrecta porque el desplazamiento forzado es un crimen contra la humanidad que lamentablemente ha ocurrido en múltiples guerras del mundo.",
            "",
            "Es incorrecta porque la inmensa mayoría de las expulsiones forzadas en Colombia golpeó a comunidades campesinas, indígenas y afrodescendientes rurales.",
            "Es incorrecta porque el fenómeno se intensificó precisamente por la disputa violenta y confrontación entre múltiples grupos armados ilegales y la fuerza pública."
        ]
    },
    "scc-i024": {
        "correcta": 1,
        "explicacion": "El orden cronológico correcto de las revoluciones sociales mencionadas es: Revolución mexicana (1910), Revolución rusa (1917), Revolución cubana (1959) y Revolución sandinista de Nicaragua (1979), secuencia correspondiente a la opción B.",
        "distractores": [
            "Es incorrecta porque antepone la Revolución nicaragüense de 1979 a procesos que ocurrieron a comienzos del siglo XX.",
            "",
            "Es incorrecta porque sitúa la Revolución bolchevique rusa (1917) antes del estallido de la Revolución mexicana de 1910.",
            "Es incorrecta porque ubica la Revolución cubana (1959) en primer lugar, décadas después de las revoluciones de México y Rusia."
        ]
    },
    "scc-i025": {
        "correcta": 2,
        "explicacion": "Los problemas derivados directamente de la diversidad cultural y política corresponden a los conflictos por pertenencia a partidos políticos opuestos (2) y la coexistencia de diferentes concepciones religiosas (4), según la opción C.",
        "distractores": [
            "Es incorrecta porque el agotamiento de recursos no renovables es una problemática biofísica y ambiental, no un conflicto de pluralismo sociocultural.",
            "Es incorrecta porque mezcla un problema ecológico (1) con uno ideológico (4), sin aislar los componentes estrictamente culturales y políticos.",
            "",
            "Es incorrecta porque incluye la escasez de recursos naturales (1), que no es un fenómeno originado en la divergencia de creencias o militancias."
        ]
    },
    "scc-i026": {
        "correcta": 0,
        "explicacion": "La acción de tutela procede de manera preferente y sumaria para amparar el derecho fundamental a la salud cuando su negación pone en peligro inminente la vida o la integridad física de una persona (opción A).",
        "distractores": [
            "",
            "Es incorrecta porque la expulsión de una asociación gremial privada es un diferendo contractual que cuenta con vías judiciales ordinarias.",
            "Es incorrecta porque los derechos colectivos (como juntas comunales o medio ambiente) se protegen mediante acciones populares, no tutelas individuales.",
            "Es incorrecta porque la acción de tutela es un recurso judicial de amparo concreto, no un mecanismo para legislar o expedir normas generales."
        ]
    },
    "scc-i027": {
        "correcta": 1,
        "explicacion": "La suburbanización o migración de residentes hacia las periferias metropolitanas obedece a la búsqueda de entornos más tranquilos, con menor congestión vehicular y mayor contacto con áreas verdes (opción B).",
        "distractores": [
            "Es incorrecta porque en las urbes modernas el centro concentra actividades terciarias (servicios y oficinas) y no industrias pesadas contaminantes.",
            "",
            "Es incorrecta porque el centro urbano es precisamente el sector con mayor concentración de servicios financieros, comerciales y de transporte.",
            "Es incorrecta porque las afueras residenciales suburbanas suelen albergar condominios de costo medio-alto y no exclusivamente vivienda de bajo precio."
        ]
    },
    "scc-i028": {
        "correcta": 2,
        "explicacion": "Los movimientos y colectivos sociales que defienden la diversidad sexual luchan por la garantía plena de sus derechos constitucionales a la igualdad y la no discriminación, a la vez que visibilizan la exclusión histórica que han padecido (opción C).",
        "distractores": [
            "Es incorrecta porque su objetivo central es la reivindicación de derechos civiles y no se reduce a campañas pedagógicas de salud sexual.",
            "Es incorrecta porque desvía el núcleo de la reivindicación hacia la explotación fabril, cuando el reclamo prioritario es la igualdad de derechos e identidad.",
            "",
            "Es incorrecta porque la libertad religiosa es otro derecho constitucional distinto, no el foco específico de las organizaciones de diversidad de género."
        ]
    },
    "scc-i029": {
        "correcta": 0,
        "explicacion": "La mecanización industrial en las fábricas inglesas desató un éxodo rural masivo hacia los centros fabriles, transformando a los antiguos campesinos en una nueva clase social asalariada: el proletariado urbano (opción A).",
        "distractores": [
            "",
            "Es incorrecta porque la Revolución Industrial provocó el despoblamiento de los campos y el crecimiento exponencial de las ciudades.",
            "Es incorrecta porque los terratenientes tradicionales ya existían desde el feudalismo; lo novedoso fue el surgimiento de la burguesía industrial y el proletariado.",
            "Es incorrecta porque en sus primeras décadas el capitalismo industrial operó bajo un régimen laboral desregulado, sin leyes de protección obrera."
        ]
    },
    "scc-i030": {
        "correcta": 3,
        "explicacion": "Al ser la norma de normas en un Estado de derecho, la Constitución establece la jerarquía jurídica fundamental, delimita las competencias de los poderes públicos y consagra los límites infranqueables que protegen los derechos ciudadanos frente al poder estatal (opción D).",
        "distractores": [
            "Es incorrecta porque impartir justicia es la función específica de los jueces del poder judicial, no el texto constitucional en sí mismo.",
            "Es incorrecta porque la Constitución fija los principios y normas superiores, pero la aplicación práctica de resolver litigios corresponde a la judicatura.",
            "Es incorrecta porque la paz y prosperidad son metas colectivas, pero la definición técnica constitucional se fundamenta en su carácter normativo vinculante y limitador.",
            ""
        ]
    },
    "scc-i031": {
        "correcta": 2,
        "explicacion": "Contrastar el alto porcentaje de mujeres agredidas con el exiguo número de condenas judiciales revela una grave ineficacia del aparato judicial y una barrera estructural que propicia la impunidad frente a los agresores (opción C).",
        "distractores": [
            "Es incorrecta porque no prueba que las leyes sean inexistentes o defectuosas, sino que las autoridades fallan en investigar, juzgar y castigar oportunamente.",
            "Es incorrecta porque la falta de condenas demuestra el fracaso institucional de los juzgados y no que las mujeres denuncien falsedades.",
            "",
            "Es incorrecta porque responsabiliza indebidamente a las víctimas atribuyéndoles falta de educación para resolver desacuerdos en pareja."
        ]
    },
    "scc-i032": {
        "correcta": 2,
        "explicacion": "La tensión se origina entre el deber legal del Estado de proteger el derecho a la salud pública y al medio ambiente sano frente al interés económico individual de los agricultores de rentabilizar sus cosechas (opción C).",
        "distractores": [
            "Es incorrecta porque no existe un choque cultural étnico en la tecnificación del cultivo, sino una discrepancia sobre el uso de químicos tóxicos.",
            "Es incorrecta porque los campesinos defienden su derecho al trabajo e ingresos, no una preferencia doctrinal por alimentos no procesados.",
            "",
            "Es incorrecta porque el gobierno actúa en cumplimiento de normas sanitarias generales y no en defensa de un interés empresarial privado particular."
        ]
    },
    "scc-i033": {
        "correcta": 2,
        "explicacion": "El proteccionismo económico busca resguardar la producción nacional de la competencia extranjera imponiendo aranceles elevados que encarecen los bienes importados, estimulando así el consumo de lo fabricado en el país (opción C).",
        "distractores": [
            "Es incorrecta porque vetar la entrada de toda clase de bienes externos paralizaría industrias que dependen de maquinaria e insumos no producidos localmente.",
            "Es incorrecta porque abrir indiscriminadamente las aduanas corresponde a la apertura y al libre comercio, lo contrario del proteccionismo.",
            "",
            "Es incorrecta porque subvencionar a corporaciones foráneas para importar productos importaría competencia desleal contra la industria nacional."
        ]
    },
    "scc-i034": {
        "correcta": 3,
        "explicacion": "El principio de progresividad tributaria del liberalismo social establece que quienes concentran mayor riqueza deben aportar una tasa porcentual más alta de impuestos, gravando directamente la renta y el patrimonio para financiar el gasto social (opción D).",
        "distractores": [
            "Es incorrecta porque aplicar una tasa impositiva plana para todos los ciudadanos es un esquema regresivo que desconoce la capacidad de pago.",
            "Es incorrecta porque fijar gravámenes homogéneos independientemente del nivel socioeconómico traslada la carga a las clases medias y bajas.",
            "Es incorrecta porque recortar subsidios a servicios públicos perjudica a los sectores desfavorecidos y contradice la equidad distributiva.",
            ""
        ]
    },
    "scc-i035": {
        "correcta": 3,
        "explicacion": "La meta histórica fundamental de la doctrina socialista es abolir la explotación del trabajo asalariado mediante la propiedad colectiva o social de los medios de producción y la dirección de la economía al servicio de las necesidades de la clase trabajadora (opción D).",
        "distractores": [
            "Es incorrecta porque desmantelar sindicatos y privatizar empresas del Estado son políticas características del capitalismo neoliberal desregulado.",
            "Es incorrecta porque promover el consumo mediante crédito bancario y endeudamiento privado es un mecanismo del modelo financiero capitalista.",
            "Es incorrecta porque la apertura de mercados y los tratados de libre comercio responden al libre cambio mercantilista internacional.",
            ""
        ]
    },
    "scc-i036": {
        "correcta": 2,
        "explicacion": "Al replicar un modelo de emprendimiento juvenil en un nuevo territorio, surgen desacuerdos si no se diagnostican las demandas y vocaciones productivas reales de la comunidad local, las cuales difieren de las experiencias de otras ciudades (opción C).",
        "distractores": [
            "Es incorrecta porque descalifica a los jóvenes suponiendo falsamente que carecen de aspiraciones de autonomía laboral y emprendimiento.",
            "Es incorrecta porque la duración temporal de un proyecto de cooperación no es la razón fundamental por la que fallan sus resultados en territorio.",
            "",
            "Es incorrecta porque el manejo de una segunda lengua no es un obstáculo insalvable para liderar negocios locales en barrios vulnerables."
        ]
    },
    "scc-i037": {
        "correcta": 1,
        "explicacion": "La principal limitación para la consolidación de Palestina como Estado soberano reside en la falta de soberanía sobre un territorio contiguo con fronteras definitivas, debido a la ocupación militar y la presencia de asentamientos en Cisjordania (opción B).",
        "distractores": [
            "Es incorrecta porque la condición de observador en la ONU es una consecuencia diplomática del conflicto, no la causa geográfica del desacuerdo.",
            "",
            "Es incorrecta porque el número de colonos describe un obstáculo sobre el terreno, pero la traba jurídica medular es la delimitación fronteriza y el control territorial soberano.",
            "Es incorrecta porque la dispersión de refugiados refleja la magnitud de la crisis humanitaria, mas no la definición formal de soberanía territorial."
        ]
    },
    "scc-i038": {
        "correcta": 2,
        "explicacion": "Designar a los delegados al Consejo Estudiantil por criterio exclusivo de rendimiento académico viola la Ley General de Educación, la cual garantiza que los representantes estudiantiles deben ser elegidos por voto popular democrático de sus compañeros (opción C).",
        "distractores": [
            "Es incorrecta porque premiar las calificaciones altas no puede justificar la supresión de los derechos de participación política escolar.",
            "Es incorrecta porque el impedimento no es la carga horaria académica de las reuniones, sino la vulneración del derecho al sufragio estudiantil.",
            "",
            "Es incorrecta porque imponer representantes a dedo enseña una práctica autoritaria que desvirtúa el aprendizaje de la democracia participativa."
        ]
    },
    "scc-i039": {
        "correcta": 2,
        "explicacion": "Al concertar y acordar con el pueblo indígena la preservación de su zona sagrada y reubicar la infraestructura sin cancelar la represa hidroeléctrica, el Estado armonizó el interés general de abastecimiento energético con el derecho fundamental a la identidad cultural (opción C).",
        "distractores": [
            "Es incorrecta porque el gobierno precisamente evitó vulnerar los derechos indígenas al acoger sus peticiones y rediseñar el trazado de la obra.",
            "Es incorrecta porque no se sacrificó el bienestar colectivo: la central hidroeléctrica se construyó y generará energía para toda la nación.",
            "",
            "Es incorrecta porque el mecanismo adecuado y constitucionalmente preceptivo en territorios ancestrales es la consulta previa informada, no una consulta popular amplia."
        ]
    },
    "scc-i040": {
        "correcta": 1,
        "explicacion": "Silenciar o acortar deliberadamente el tiempo de palabra a las estudiantes por razones de género constituye una conducta discriminatoria que viola el derecho a la igualdad de trato y la libre expresión en el aula (opción B).",
        "distractores": [
            "Es incorrecta porque la trayectoria académica o autoridad del profesor jamás lo habilita para ejercer prácticas discriminatorias o machistas.",
            "",
            "Es incorrecta porque no es una simple molestia de estilo, sino un trato diferenciado injustificado basado en un estereotipo de género.",
            "Es incorrecta porque ningún estudio empírico puede servir de fundamento para restringir derechos fundamentales de las alumnas en clase."
        ]
    },
    "scc-i041": {
        "correcta": 2,
        "explicacion": "Exigir la consulta previa a comunidades étnicas antes de explotar hidrocarburos en su hábitat protege la diversidad cultural de la nación (Art. 7 CP), impidiendo la destrucción de sus formas ancestrales de vida y subsistencia (opción C).",
        "distractores": [
            "Es incorrecta porque la consulta previa es un derecho especial de discriminación positiva que reconoce la vulnerabilidad de las minorías étnicas.",
            "Es incorrecta porque el mecanismo tutela la integridad territorial y cultural del pueblo, no el derecho civil de constituir gremios o sindicatos.",
            "",
            "Es incorrecta porque, si bien incluye impacto ecológico, la finalidad primordial de la consulta previa es la salvaguarda de la comunidad indígena y su autonomía."
        ]
    },
    "scc-i042": {
        "correcta": 2,
        "explicacion": "Para juzgar objetivamente la efectividad de una administración en seguridad, se requiere cotejar la evolución histórica de las tasas de criminalidad (homicidios, hurtos) desde el inicio de su mandato frente a periodos previos (opción C).",
        "distractores": [
            "Es incorrecta porque el plan de gobierno contiene las intenciones o promesas del candidato, no las estadísticas empíricas de delitos cometidos.",
            "Es incorrecta porque las cifras de criminalidad foráneas obedecen a factores externos y no permiten medir la gestión policial interna de la ciudad.",
            "",
            "Es incorrecta porque las afirmaciones del propio alcalde son declaraciones de parte interesada que no constituyen evidencia empírica contrastable."
        ]
    },
    "scc-i043": {
        "correcta": 3,
        "explicacion": "El argumento central de los países productores contra la política prohibicionista estriba en que el narcotráfico ilegal ha alimentado violencia armada sistemática, corrupción y deterioro ambiental, generando un daño social mucho mayor que el que produce el consumo médico en sí (opción D).",
        "distractores": [
            "Es incorrecta porque apela a un enfoque de libre desarrollo de la personalidad individual, no a las repercusiones estructurales en naciones de origen.",
            "Es incorrecta porque es un argumento insostenible que niega la corresponsabilidad compartida de productores y consumidores en la cadena ilícita.",
            "Es incorrecta porque la visión sanitaria del tratamiento a adictos es una política de salud pública en naciones de destino, no el costo de la guerra.",
            ""
        ]
    },
    "scc-i044": {
        "correcta": 2,
        "explicacion": "Sugerir que la forma de vestir o comportarse de las mujeres motiva o excusa el acoso sexual traslada la culpabilidad a la víctima y termina justificando la conducta criminal de los agresores (opción C).",
        "distractores": [
            "Es incorrecta porque aconsejar a las mujeres que alteren su vestimenta limita su libertad y valida prejuicios machistas en vez de protegerlas.",
            "Es incorrecta porque la policía tiene el deber legal estricto de perseguir y prevenir cualquier manifestación delictiva o acoso en la vía pública.",
            "",
            "Es incorrecta porque la declaración del oficial no protege la seguridad ciudadana, sino que invisibiliza y tolera la violencia de género."
        ]
    },
    "scc-i045": {
        "correcta": 1,
        "explicacion": "La propuesta suscita un conflicto distributivo entre los residentes del sector privilegiado que buscan salvaguardar su seguridad y los ciudadanos de menores ingresos de toda la ciudad, quienes verían reducida la presencia policial pública en sus barrios (opción B).",
        "distractores": [
            "Es incorrecta porque no se trata de una pugna entre guardias privados y delincuentes, sino del uso equitativo de los uniformados de la policía estatal.",
            "",
            "Es incorrecta porque el gobierno local no tiene un interés particular contrapuesto, sino el deber constitucional de garantizar seguridad a todos.",
            "Es incorrecta porque el dilema central no reside en el beneficio comercial de agencias de vigilancia, sino en la asignación del pie de fuerza público."
        ]
    },
    "scc-i046": {
        "correcta": 0,
        "explicacion": "La Corte Constitucional ampara la objeción de conciencia frente al servicio militar obligatorio, disponiendo que cuando una convicción religiosa o moral sincera impide portar armas, el Ejército debe desvincular al conscripto y entregarle su libreta militar (opción A).",
        "distractores": [
            "",
            "Es incorrecta porque obligar al soldado a empuñar fusiles violaría directamente su derecho fundamental a la libertad de conciencia y culto.",
            "Es incorrecta porque asignarle tareas administrativas dentro de una guarnición armada mantiene la subordinación castrense en pugna con su fe.",
            "Es incorrecta porque forzarlo a desfilar en actos marciales no respeta su convicción íntima de no participar en actividades de las fuerzas armadas."
        ]
    },
    "scc-i047": {
        "correcta": 3,
        "explicacion": "El dilema enfrenta la salvaguarda de la integridad física de los menores ante crecientes e inundaciones frente al derecho fundamental a la continuidad educativa, conflicto que se equilibra mediante planes de contingencia escolar flexibles (opción D).",
        "distractores": [
            "Es incorrecta porque el transporte terrestre suele estar imposibilitado justamente por el colapso y bloqueo de los caminos anegados.",
            "Es incorrecta porque cancelar las clases prolongadamente retrasa el desarrollo cognitivo y vulnera el derecho al acceso a la educación formal.",
            "Es incorrecta porque la radio comunitaria es un complemento didáctico, pero no reemplaza la interacción directa del proceso pedagógico presencial.",
            ""
        ]
    },
    "scc-i048": {
        "correcta": 2,
        "explicacion": "La coyuntura refleja la colisión entre la dimensión ambiental (proteger la salud de los habitantes y reducir la densa capa de esmog) y la dimensión económica (los costos monetarios y la merma en ingresos de las empresas al paralizar la industria) (opción C).",
        "distractores": [
            "Es incorrecta porque, si bien se suspenden clases, la restricción obedece al impacto directo en la producción de fábricas y vehículos.",
            "Es incorrecta porque la dimensión cultural no es la variable que motiva las restricciones de emergencia frente a la contaminación.",
            "",
            "Es incorrecta porque la pugna no radica en costumbres o tradiciones sociales, sino en el balance entre rentabilidad industrial y ecología urbana."
        ]
    },
    "scc-i049": {
        "correcta": 3,
        "explicacion": "La decisión del Consejo Directivo busca proteger la salud de los alumnos ante alimentos en mal estado, pero impacta negativamente la dimensión económica de los vendedores informales, quienes dependen de esas ventas para la subsistencia de sus hogares (opción D).",
        "distractores": [
            "Es incorrecta porque expulsar a los vendedores de comida ambulante no genera un incremento automático en los índices de delincuencia o atracos.",
            "Es incorrecta porque erradicar la venta ambulante busca precisamente disminuir y prevenir nuevas intoxicaciones estomacales en el plantel.",
            "Es incorrecta porque la medida disciplinaria cuenta con el respaldo de la mayoría de padres preocupados por la salubridad de sus hijos.",
            ""
        ]
    }
}

def update_file(path, id_prefix):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = 0
    for q in data.get('preguntas', []):
        qid = q['id']
        # Map cfi and soc to scc id
        target_scc_id = None
        if qid in PREGUNTAS_SOCIALES:
            target_scc_id = qid
        elif qid.startswith('soc-i'):
            # Check if matching number exists
            num = qid.replace('soc-i', '')
            candidate = f'scc-i{num}'
            if candidate in PREGUNTAS_SOCIALES:
                # verify words match
                c_words = set(q['enunciado'].lower().split()[:6])
                s_words = set(PREGUNTAS_SOCIALES[candidate]['explicacion'].lower().split()[:6])
                target_scc_id = candidate
        elif qid.startswith('cfi-i'):
            num = int(qid.replace('cfi-i', ''))
            if 51 <= num <= 72:
                target_scc_id = f'scc-i{num - 25:03d}'
            elif num == 74:
                target_scc_id = 'scc-i049'

        if target_scc_id and target_scc_id in PREGUNTAS_SOCIALES:
            item = PREGUNTAS_SOCIALES[target_scc_id]
            q['correcta'] = item['correcta']
            q['explicacion'] = item['explicacion']
            q['distractores'] = item['distractores']
            updated += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'Updated {updated} questions in {path}')

if __name__ == '__main__':
    update_file('content/icfes/scc/preguntas.json', 'scc')
    update_file('content/icfes/soc/preguntas.json', 'soc')
    update_file('content/icfes/cfi/preguntas.json', 'cfi')
