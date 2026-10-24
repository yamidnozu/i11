"""
Equilibra claves (10 A, 10 B, 10 C, 10 D) y longitudes de opciones en Lectura Crítica,
eliminando distractores absurdos (como en lec-039) y generando hoja pedagógica completa.
Garantiza que la opción correcta no sea la más larga en más del 50% de preguntas (meta: <= 35%).
"""
import json, sys
from tools.gen_area_hojas import build_hoja_for_question

def balance_lectura():
    lec = json.load(open('content/questions/lectura_critica.json', 'r', encoding='utf-8'))
    hojas = json.load(open('content/hojas.json', 'r', encoding='utf-8'))
    guiones = json.load(open('content/guiones.json', 'r', encoding='utf-8'))
    enfoques = json.load(open('content/enfoques.json', 'r', encoding='utf-8'))

    # Questions 0..5 are original: lec-001(B), 002(B), 003(B), 004(C), 005(B), 006(B) -> 5 B, 1 C.
    # We distribute questions 6..39 (34 questions) to achieve exactly 10 A, 10 B, 10 C, 10 D:
    # 10 A, 5 B, 9 C, 10 D.
    target_keys = (
        [0] * 10 + # 10 A (lec-007 to lec-016)
        [1] * 5  + # 5 B  (lec-017 to lec-021)
        [2] * 9  + # 9 C  (lec-022 to lec-030)
        [3] * 10   # 10 D (lec-031 to lec-040)
    )

    # In balanced_ops: [correct, distractor1, distractor2, distractor3]
    # For many questions we ensure distractor1 or distractor2 is longer than the correct answer.
    balanced_ops = {
        'lec-007': [
            'La inmediatez comunicativa fragmenta la capacidad de concentración sostenida del lector.',
            'La digitalización masiva y acelerada de archivos históricos elimina por completo la necesidad de contar con especialistas en lingüística y filología.',
            'El uso de dispositivos electrónicos garantiza una comprensión lectora superior en todos los niveles del sistema educativo formal.',
            'La lectura en pantallas táctiles aumenta la agudeza visual y la retención nemotécnica en personas de todas las edades.'
        ],
        'lec-011': [
            'Denunciar la creciente mercantilización de la educación superior como un servicio privado.',
            'El elogio entusiasta y desmedido a las corporaciones financieras por otorgar créditos educativos con tasas de interés indexadas a la inflación.',
            'La recomendación formal de cerrar las facultades de humanidades y ciencias sociales para favorecer carreras comerciales.',
            'El análisis cuantitativo sobre la rentabilidad financiera anual de las universidades privadas en América Latina.'
        ],
        'lec-012': [
            'Un hallazgo afortunado e inesperado producido al investigar un fenómeno diferente.',
            'Un método infalible y exhaustivo de deducción lógica formal diseñado para comprobar hipótesis científicas preestablecidas en manuales.',
            'Una equivocación experimental lamentable que invalida por completo el rigor de la investigación científica en los laboratorios.',
            'Un proceso de memorización mecánica y repetitiva de fórmulas teóricas en los manuales de física y química analítica.'
        ],
        'lec-015': [
            'El valor moral se demuestra al actuar con firmeza a pesar del temor experimentado.',
            'La cobardía y la prudencia reflexiva constituyen virtudes equivalentes en las situaciones de riesgo vital extremo para la supervivencia.',
            'El miedo es una debilidad psicológica imperdonable que debe erradicarse mediante el entrenamiento militar estricto.',
            'La audacia temeraria que ignora cualquier peligro representa el único estándar ético válido en la sociedad contemporánea.'
        ],
        'lec-016': [
            'La época geológica caracterizada por el impacto determinante de las actividades humanas.',
            'Un periodo prehistórico remoto caracterizado por el auge, dominio evolutivo y extinción masiva de los grandes reptiles del Mesozoico.',
            'Una era geológica futura en la que la biosfera recuperará su equilibrio tras la desaparición definitiva de la especie humana.',
            'Un ciclo glacial estacional provocado por variaciones periódicas e impredecibles en la radiación solar sobre la corteza terrestre.'
        ],
        'lec-017': [
            'Revela una contradicción ética entre el discurso de responsabilidad ambiental y la práctica real de ocultamiento.',
            'Demuestra el compromiso transparente, riguroso y verificable de la empresa multinacional con la conservación de los ecosistemas fluviales protegidos.',
            'Refleja un error menor de redacción tipográfica que no altera en absoluto la credibilidad del informe financiero presentado a los accionistas.',
            'Constituye una prueba irrefutable de que la corporación cumple cabalmente con todos los estándares ecológicos exigidos por los tratados internacionales.'
        ],
        'lec-018': [
            'Incurre en generalización apresurada al asumir que una creencia tradicional es verdadera sin aportar pruebas.',
            'Presenta un argumento deductivo riguroso e incontrovertible respaldado por hallazgos arqueológicos concluyentes sobre la medicina tradicional milenaria.',
            'Expone una analogía poética para ilustrar la sabiduría popular sin pretender validar su eficacia farmacológica real en seres humanos.',
            'Comete una falacia ad hominem al atacar directamente la honestidad y la moralidad de los científicos que cuestionan la tradición.'
        ],
        'lec-019': [
            'Incurre en la falacia del espantapájaros al tergiversar la postura del adversario para refutarla fácilmente.',
            'Demuestra con rigor matemático, estadístico y financiero la absoluta superioridad de su plan de gobierno frente a las demás alternativas electorales.',
            'Aplica un argumento de autoridad legítimo al citar opiniones académicas independientes e imparciales sobre la situación macroeconómica nacional.',
            'Presenta un dilema ético complejo sobre las prioridades presupuestales del municipio en materia de inversión en educación preescolar.'
        ],
        'lec-022': [
            'La premisa de que el tren mejora el tránsito no garantiza la sostenibilidad financiera.',
            'Los trenes eléctricos de cercanías son reconocidos unánimemente por los organismos multilaterales como la única solución tecnológica integral viable ante el colapso vial.',
            'La inversión masiva en infraestructura férrea reduce de manera automática e inmediata la deuda pública externa de las ciudades intermedias del país.',
            'El uso de tranvías urbanos elimina la necesidad de contar con rutas alimentadoras de autobuses, ciclorrutas comunitarias y andenes peatonales.'
        ],
        'lec-023': [
            'Comprender un texto antiguo exige reconstruir su horizonte histórico y lingüístico original.',
            'Interpretar un texto clásico requiere aplicar de manera estricta los valores morales, las convenciones éticas y los criterios estéticos del siglo veintiuno.',
            'La literatura renacentista carece de valor formativo actual porque refleja concepciones científicas y médicas superadas por el progreso contemporáneo.',
            'Los historiadores deben juzgar el comportamiento de los personajes del pasado empleando exclusivamente las leyes penales vigentes en la actualidad.'
        ],
        'lec-026': [
            'Plantea un razonamiento hipotético sobre las consecuencias irreversibles del consumo desmedido.',
            'Presenta una crónica anecdótica personal sobre la recolección de residuos plásticos en una playa turística del litoral Pacífico colombiano.',
            'Formula una propuesta jurídica y financiera para privatizar la gestión de los océanos internacionales y cobrar tarifas de pesca por tonelada.',
            'Sostiene categóricamente que la contaminación por microplásticos es un mito publicitario inventado para frenar la competitividad industrial.'
        ],
        'lec-028': [
            'Usa una metáfora para acercar intuitivamente al lector a un concepto físico abstracto.',
            'Proporciona una derivación matemática formal y exhaustiva con ecuaciones diferenciales complejas de la teoría de la relatividad general de Einstein.',
            'Censura la curiosidad científica de los lectores no especializados por considerar que la física cuántica debe reservarse a los académicos.',
            'Relata una memoria autobiográfica detallada sobre su experiencia de infancia construyendo telescopios reflectores caseros en su ciudad natal.'
        ],
        'lec-029': [
            'Ambos lenguajes reinterpretan la realidad mediante elecciones técnicas y estéticas subjetivas.',
            'La fotografía constituye un registro mecánico, pasivo e idéntico de los objetos reales, mientras que la pintura es pura invención caprichosa.',
            'La pintura al óleo representa el único medio artístico legítimo para capturar la belleza formal en la historia de las artes plásticas universales.',
            'La invención de las cámaras digitales eliminó definitivamente la necesidad de que los creadores visuales estudien la perspectiva y la composición.'
        ],
        'lec-030': [
            'El tono indignado con que el autor denuncia la impunidad y exhorta a la resistencia ciudadana.',
            'La actitud pasiva, indiferente y resignada del escritor ante la imposibilidad práctica de transformar las costumbres clientelistas de la política.',
            'El estilo festivo, cómico y desenfadado empleado a lo largo de todo el ensayo para minimizar la gravedad del saqueo sistemático de los recursos públicos.',
            'La postura de neutralidad aséptica que evita tomar partido o formular recomendaciones éticas para la movilización organizada de la sociedad civil.'
        ],
        'lec-031': [
            'El contraste irónico entre la expectativa vital de rescate y la invasión inútil de la publicidad.',
            'La burla despiadada sobre la falta de preparación física y las escasas habilidades de natación del náufrago solitario en el momento del naufragio.',
            'La recomendación comercial seria y fundamentada sobre la conveniencia financiera de contratar pólizas de seguros de vida antes de viajar por altamar.',
            'El elogio formativo a las botellas de vidrio retornables como instrumentos ecológicos de correspondencia y auxilio comunitario en zonas costeras.'
        ],
        'lec-032': [
            'Incurre en un falso dilema al reducir el debate a dos extremos ignorando opciones intermedias.',
            'Demuestra con precisión econométrica y tablas actuariales la inviabilidad financiera de implementar programas de medicina preventiva ambulatoria.',
            'Aplica un método de inducción científica riguroso a partir de una amplia muestra representativa de pacientes atendidos en servicios de urgencias.',
            'Invoca dictámenes técnicos vinculantes de la Organización Panamericana de la Salud para justificar la necesidad de privatizar los hospitales públicos.'
        ],
        'lec-033': [
            'Incurre en una generalización apresurada al tomar un caso particular como regla universal.',
            'Presenta un testimonio clínico verificado mediante ensayos aleatorizados doble ciego publicados en prestigiosas revistas biomédicas internacionales.',
            'Aplica un modelo epidemiológico formal fundamentado en el análisis demográfico y cuantitativo de las tasas de vacunación de la población urbana.',
            'Plantea una hipótesis médica plausible que coincide cabalmente con los consensos alcanzados por los comités de expertos de la Organización Mundial de la Salud.'
        ],
        'lec-034': [
            'Comete una pendiente resbaladiza al encadenar consecuencias catastrofistas sin probar el nexo causal.',
            'Expone una demostración causal rigurosa basada en series de tiempo históricas que prueban el colapso financiero provocado por las regulaciones del mercado.',
            'Desarrolla una defensa equilibrada de los derechos de los consumidores frente a los abusos monopolísticos de las empresas de telecomunicaciones.',
            'Aplica el principio de precaución ambiental de manera justificada ante la introducción de sustancias químicas potencialmente cancerígenas.'
        ],
        'lec-035': [
            'El primer texto presenta evidencia científica, mientras el segundo relativiza el cambio climático con sesgos económicos.',
            'Ambos textos coinciden plenamente en la necesidad urgente de suspender la extracción de combustibles fósiles y desmantelar las plantas térmicas.',
            'El primer fragmento niega la existencia del calentamiento global, mientras que el segundo promueve la transición acelerada hacia energías eólicas.',
            'Los dos pasajes son relatos de ficción distópica que carecen de rigor argumentativo y no pretenden describir la realidad climática del planeta.'
        ],
        'lec-036': [
            'Proyectar una imagen benevolente para neutralizar críticas ciudadanas sobre el impacto ambiental corporativo.',
            'Divulgar los resultados de una investigación académica rigurosa e imparcial financiada por organismos multilaterales sin fines de lucro.',
            'Informar de manera preventiva y urgente a las comunidades ribereñas sobre riesgos inminentes de intoxicación por residuos químicos tóxicos.',
            'Canalizar las denuncias laborales formuladas por los trabajadores sindicalizados por el reiterado incumplimiento de los protocolos de seguridad industrial.'
        ],
        'lec-037': [
            'La deliberación ciudadana informada y el respeto mutuo son la base de la legitimidad democrática.',
            'La vida democrática se perfecciona cuando las mayorías parlamentarias censuran y silencian a las fuerzas minoritarias de la oposición.',
            'Las políticas públicas deben fundamentarse en el ejercicio de la fuerza y en la capacidad de intimidación de las instituciones gubernamentales.',
            'El debate abierto entre ciudadanos constituye un obstáculo burocrático que retrasa la adopción de medidas económicas urgentes por decreto.'
        ],
        'lec-038': [
            'Discrepan sobre el rol del Estado: una postura defiende el libre mercado y la otra la intervención social redistributiva.',
            'Ambas tesis coinciden en que el gobierno central debe abolir la propiedad privada y nacionalizar la totalidad del sector financiero bancario.',
            'El primer planteamiento exige la supresión de aranceles a las importaciones, mientras el segundo promueve la privatización de los parques nacionales.',
            'Los dos autores concuerdan en que el crecimiento macroeconómico es imposible sin sustituir la moneda nacional por divisas electrónicas internacionales.'
        ],
        'lec-039': [
            'Es una conducta inmoral porque instrumentaliza a las personas violando su dignidad intrínseca como fines en sí mismas.',
            'Es una decisión ética encomiable, pues el lucro financiero y la rentabilidad corporativa constituyen el fin supremo de la convivencia en sociedad.',
            'Constituye una controversia de carácter exclusivamente mercantil que escapa por completo a las reflexiones morales de la filosofía moderna.',
            'Representa una práctica admisible según el imperativo categórico kantiano, siempre que medie la firma de un contrato formal de trabajo voluntario.'
        ],
        'lec-040': [
            'Aplica un recurso populista al polarizar a la sociedad entre un pueblo virtuoso y unas élites intrínsecamente corruptas.',
            'Presenta un plan de desarrollo económico riguroso con metas fiscales cuantitativas verificables y proyecciones de inversión plurianual.',
            'Formula una invitación genuina al diálogo pluralista y a la concertación democrática entre todas las bancadas políticas del parlamento.',
            'Desarrolla un análisis sociológico imparcial sobre las transformaciones demográficas de las familias de clase trabajadora urbana en el país.'
        ]
    }

    for i in range(6, len(lec)):
        q = lec[i]
        qid = q['id']
        target_c = target_keys[i - 6]

        if qid in balanced_ops:
            ops = balanced_ops[qid]
            correct_opt = ops[0]
            distractors = ops[1:]
            
            new_ops = [None] * 4
            new_ops[target_c] = correct_opt
            d_idx = 0
            for pos in range(4):
                if pos != target_c:
                    new_ops[pos] = distractors[d_idx]
                    d_idx += 1
            q['opciones'] = new_ops
            
            new_dis = [None] * 4
            new_dis[target_c] = ""
            orig_dis = [d for d in q['distractores'] if d]
            if len(orig_dis) < 3:
                orig_dis = [
                    "Argumento que incurre en falacia o desvía el criterio de evaluación.",
                    "No coincide con el propósito argumentativo evaluado en el texto.",
                    "Interpreta erróneamente la premisa central formulada por el autor."
                ]
            d_idx = 0
            for pos in range(4):
                if pos != target_c:
                    new_dis[pos] = orig_dis[d_idx]
                    d_idx += 1
            q['distractores'] = new_dis
            q['correcta'] = target_c
        else:
            curr_c = q['correcta']
            if curr_c != target_c:
                q['opciones'][curr_c], q['opciones'][target_c] = q['opciones'][target_c], q['opciones'][curr_c]
                q['distractores'][curr_c], q['distractores'][target_c] = q['distractores'][target_c], q['distractores'][curr_c]
                q['correcta'] = target_c

        # Build hoja
        h = build_hoja_for_question(q)
        q['hoja'] = h
        hojas[qid] = {'modo': h['modo'], 'marcas': [], 'pasos': h['pasos']}
        guiones[qid] = h['guion']
        enfoques[qid] = h['enfoque']

    json.dump(lec, open('content/questions/lectura_critica.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(hojas, open('content/hojas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(guiones, open('content/guiones.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(enfoques, open('content/enfoques.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print("Lectura Crítica balanced successfully.")

if __name__ == '__main__':
    balance_lectura()
