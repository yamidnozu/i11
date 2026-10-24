"""
Equilibra claves (10 A, 10 B, 10 C, 10 D) y longitudes de opciones en Inglés (content/questions/ingles.json),
eliminando distractores absurdos y reduciendo el sesgo de longitud a menos del 25%.
Genera la hoja pedagógica completa interactiva (enfoque, pasos, guion de 3 niveles).
"""
import json
from tools.gen_area_hojas import build_hoja_for_question

# Opciones ajustadas para eliminar sesgo de longitud y distractores absurdos
AJUSTES_ING = {
    'ing-006': {
        'opciones': [
            'In a restaurant kitchen and food preparation area',
            'At a school or university examination hallway',
            'Inside a quiet cinema or commercial movie theater',
            'At a professional sports arena or football stadium'
        ],
        'distractores': [
            'En la cocina de un restaurante los avisos son de higiene o seguridad alimentaria («wash hands»), no de exámenes.',
            '',
            'En un cine se pide apagar los celulares durante la película, pero no se realizan exámenes académicos.',
            'En un estadio deportivo reina el ruido y los vítores de la multitud, incompatible con la solicitud de silencio para un examen.'
        ]
    },
    'ing-008': {
        'opciones': [
            'At a railway station departure platform',
            'At a highway petrol service station',
            'Inside a local neighbourhood pharmacy',
            'In an interactive modern art museum'
        ],
        'distractores': [
            '',
            'En una gasolinera los avisos prohíben fumar o apagar el motor al cargar combustible, no hay trenes ni plataformas.',
            'En una farmacia se venden medicamentos con receta y productos de cuidado personal.',
            'En un museo de arte los avisos prohíben tocar las pinturas o usar flash fotográfico.'
        ]
    },
    'ing-009': {
        'opciones': [
            'At a designer clothing boutique in a shopping mall',
            'In a power station or electrical equipment room',
            'At an outdoor municipal playground for children',
            'Inside a commercial pet shop selling birds and fish'
        ],
        'distractores': [
            'En una boutique de ropa los letreros anuncian probadores («fitting rooms») o descuentos de temporada.',
            '',
            'En un parque infantil público los avisos velan por la seguridad de los niños y juegos recreativos.',
            'En una tienda de mascotas los avisos señalan alimentos para perros o gatos y acuarios.'
        ]
    },
    'ing-010': {
        'opciones': [
            'At an ATM or electronic cash dispensing machine',
            'At a commercial bowling alley recreational lane',
            'In a botanical garden educational greenhouse',
            'At a dental healthcare clinic appointment room'
        ],
        'distractores': [
            '',
            'En una bolera los avisos indican la pista de juego asignada y el alquiler de zapatos deportivos especiales.',
            'En un jardín botánico los carteles informan sobre especies vegetales, flores y senderos naturales.',
            'En una clínica odontológica los letreros refieren a consultas odontológicas y salas de espera.'
        ]
    },
    'ing-012': {
        'opciones': [
            'A city commuter bicycle',
            'An emergency ambulance',
            'A deep-sea naval submarine',
            'An agricultural farm tractor'
        ],
        'distractores': [
            'Una bicicleta es un vehículo a pedal para una sola persona, no para transportar heridos.',
            '',
            'Un submarino navega bajo el agua para investigación marina o fines militares.',
            'Un tractor se usa en labores agrícolas de campo para arar o remolcar carga pesada.'
        ]
    },
    'ing-017': {
        'opciones': [
            'Yes, I enjoy swimming in warm water.',
            'Twice a week, on Tuesdays and Thursdays.',
            'Last summer during holidays with friends.',
            'It is approximately three meters deep.'
        ],
        'distractores': [
            'Responde afirmativamente con gustos personales («yes»), pero la pregunta indaga por frecuencia («how often»).',
            '',
            'Indica un momento en el pasado («last summer»), pero la pregunta indaga por una rutina regular.',
            'Describe la profundidad de la piscina («three meters deep»), no la frecuencia de uso.'
        ]
    },
    'ing-018': {
        'opciones': [
            'Sure, here you go! Take good care of it.',
            'No, I am taking an afternoon rest now.',
            'I arrived home very early this morning.',
            'The grammar examination starts tomorrow.'
        ],
        'distractores': [
            '',
            'Responde sobre estar descansando, ignorando la petición de préstamo del diccionario.',
            'Menciona la hora de llegada a casa, sin relación con el favor solicitado.',
            'Afirma cuándo es el examen sin responder si presta o no el diccionario.'
        ]
    },
    'ing-019': {
        'opciones': [
            'Congratulations on completing your practical driving test today!',
            'I\'m sorry to hear that. Don\'t worry, you\'ll pass next time!',
            'My family purchased two brand-new vehicles earlier this year.',
            'Learning to operate motor vehicles requires extensive practice.'
        ],
        'distractores': [
            'Felicita a la persona («congratulations»), pasando por alto que acaba de reprobar el examen («failed»).',
            '',
            'Comenta sobre compras de carros de su familia, sin empatía ni coherencia con la noticia del amigo.',
            'Expresa una generalidad sobre conducir en lugar de brindar una respuesta interpersonal de apoyo.'
        ]
    },
    'ing-020': {
        'opciones': [
            'I would love to! Thank you so much for inviting me.',
            'Happy birthday to everyone celebrating graduation today!',
            'I reached fifteen years of age during the last holiday.',
            'The chocolate celebration cake was exceptionally tasty!'
        ],
        'distractores': [
            '',
            'Felicita por cumpleaños a los graduandos, confundiendo las ocasiones festivas.',
            'Menciona su propia edad, sin responder a la invitación formulada.',
            'Habla sobre una torta en tiempo pasado («was delicious»), en vez de aceptar o rechazar la invitación futura.'
        ]
    },
    'ing-021': {
        'opciones': [
            'It is size medium and fits comfortably well.',
            'It is made of imported organic cotton fabric.',
            'It is eighty-five thousand Colombian pesos.',
            'It is hanging inside the fourth fitting room.'
        ],
        'distractores': [
            'Indica la talla («size medium»), pero la pregunta «how much is…» pide el precio de la prenda.',
            'Señala el material de confección («cotton»), pero la pregunta indaga por el costo monetario.',
            '',
            'Informa la ubicación del probador («fitting room»), no el precio del artículo.'
        ]
    },
    'ing-022': {
        'opciones': [
            'Yes, I went there with my school two years ago.',
            'No, I never eat sweet desserts after lunch.',
            'Yes, I will travel there tomorrow at midday.',
            'The arid landscape gets very cold at midnight.'
        ],
        'distractores': [
            '',
            'Confunde el desierto («desert», con una s) con el postre («dessert», con doble s).',
            'Usa el tiempo futuro («will visit») para responder a una pregunta sobre experiencias previas («have you ever»).',
            'Describe el clima del desierto en lugar de responder si ha visitado o no el lugar.'
        ]
    },
    'ing-026': {
        'opciones': [
            'would open',
            'will open',
            'had opened',
            'have opened'
        ],
        'distractores': [
            '',
            '«Will» corresponde al primer condicional (situación real o probable), no al segundo condicional hipotético.',
            '«Had opened» forma la estructura del tercer condicional en el pasado, no del segundo condicional con presente.',
            '«Have opened» en presente perfecto no sigue la regla gramatical del condicional hipotético.'
        ]
    },
    'ing-030': {
        'opciones': [
            'travel',
            'traveling',
            'traveled',
            'to travel'
        ],
        'distractores': [
            'Usa la forma base del verbo («travel»), omitiendo la regla de que tras preposición se requiere gerundio.',
            '',
            'Usa el pasado simple («traveled»), que no encaja tras la preposición «in».',
            'Usa el infinitivo con «to», pero tras la preposición «in» la regla gramatical exige la terminación -ing.'
        ]
    },
    'ing-031': {
        'opciones': [
            'Because they mistakenly find floating plastic bags much more nutritious than fish.',
            'Because they confuse plastic bags with jellyfish, which are their natural food.',
            'Because coastal fishermen deliberately discard plastic bags to feed marine animals.',
            'Because female sea turtles utilize discarded plastic bags to construct ocean nests.'
        ],
        'distractores': [
            'El texto no afirma que las tortugas consideren el plástico más nutritivo, sino que lo confunden visualmente.',
            '',
            'El texto menciona la contaminación marina de actividades humanas, no que los pescadores alimenten tortugas a propósito.',
            'El texto explica que las tortugas ingieren el plástico al alimentarse, no que lo usen para anidar.'
        ]
    },
    'ing-032': {
        'opciones': [
            'It provided diesel generators to every household to guarantee electricity during tropical storms.',
            'It brought clean, continuous energy that improved education, healthcare, and local economic activities.',
            'It forced local communities to abandon agricultural projects and relocate permanently to urban cities.',
            'It closed all rural educational centers and public health clinics across the entire remote territory.'
        ],
        'distractores': [
            'El proyecto reemplazó precisamente los generadores de diésel por paneles solares ecológicos.',
            '',
            'El proyecto buscaba arraigar y fortalecer las comunidades en su territorio, no forzar su desplazamiento.',
            'El texto señala que las escuelas y centros de salud se beneficiaron y mejoraron su atención, no que cerraron.'
        ]
    },
    'ing-034': {
        'opciones': [
            'To promote commercial wildlife photography expeditions aimed at locating spectacled bears in remote cloud forests.',
            'To describe culinary recipes utilizing wild berries and fruits gathered by indigenous people in mountain ecosystems.',
            'To raise urgent awareness about the ecological importance of the spectacled bear and advocate for its conservation.',
            'To explain technical engineering guidelines for building paved highways across protected Andean national reserves.'
        ],
        'distractores': [
            'El texto no es un folleto turístico ni promueve safaris fotográficos en la cordillera.',
            'Menciona los frutos que come el oso como dispersor de semillas, no recetas gastronómicas humanas.',
            '',
            'El artículo advierte sobre la fragmentación del hábitat causada por carreteras, no enseña a construirlas.'
        ]
    },
    'ing-035': {
        'opciones': [
            'To consume caffeinated energy drinks before studying late at night during exam weeks.',
            'To avoid using electronic screens in the bedroom before sleeping to ensure quality rest.',
            'To sleep only four hours nightly in order to have additional time for academic tasks.',
            'To perform vigorous cardiovascular exercise immediately before lying down in bed.'
        ],
        'distractores': [
            'El texto desaconseja consumir cafeína o bebidas energizantes en la noche porque alteran el ciclo de sueño.',
            '',
            'El texto recomienda dormir entre 8 y 9 horas diarias para un adecuado desarrollo cognitivo adolescente.',
            'El artículo sugiere realizar actividad física en la tarde y relajarse antes de acostarse, no hacer ejercicio intenso nocturno.'
        ]
    },
    'ing-036': {
        'opciones': [
            'Because it allows the coffee bean to develop complex sugars, acidity, and rich aromas.',
            'Because it causes coffee shrubs to generate double the quantity of beans in one week.',
            'Because it transforms the harvested coffee cherries completely dark, brittle, and dry.',
            'Because it enables agricultural workers to collect ripe coffee cherries in snowstorms.'
        ],
        'distractores': [
            '',
            'La altitud ralentiza el crecimiento en lugar de acelerarlo, lo que favorece la calidad sobre la cantidad rápida.',
            'El proceso de maduración en altura no reseca el fruto, sino que concentra nutrientes y azúcares naturales.',
            'En las regiones cafeteras de Colombia no hay tormentas de nieve; la altitud cafetera se ubica entre 1.400 y 2.000 msnm.'
        ]
    },
    'ing-037': {
        'opciones': [
            'Entirely skeptical and hostile, demanding an absolute worldwide prohibition on algorithmic systems across clinical medicine.',
            'Cautiously optimistic and balanced, acknowledging its diagnostic power while emphasizing that human doctors remain indispensable.',
            'Largely indifferent and unconcerned, asserting that digital algorithms will produce negligible consequences in daily healthcare.',
            'Extremely fearful and alarmist, arguing that automated medical robots will displace all human practitioners within two months.'
        ],
        'distractores': [
            'El autor no prohíbe ni rechaza la inteligencia artificial; reconoce expresamente sus valiosos aportes en detección temprana.',
            '',
            'El texto demuestra un interés profundo y un análisis exhaustivo del impacto tecnológico en la medicina moderna.',
            'El autor descarta la visión alarmista de reemplazo total y destaca que la empatía humana es irreemplazable.'
        ]
    },
    'ing-038': {
        'opciones': [
            'Paying an admission fee of seventy-five dollars at the entrance counter.',
            'Completing the mandatory online registration form before November 5.',
            'Bringing your own professional broadcasting microphone and video cameras.',
            'Attending the sessions only if you are over fifty years of age or retired.'
        ],
        'distractores': [
            'El aviso indica expresamente que el evento es de entrada libre («free admission»), sin costo en taquilla.',
            '',
            'Los equipos audiovisuales son provistos por los organizadores del congreso juvenil.',
            'El evento está dirigido a estudiantes de secundaria y universitarios, no exclusivamente a mayores de 50 años.'
        ]
    },
    'ing-039': {
        'opciones': [
            'The book presents a meticulous historical investigation of classical military strategies during the decline of the Western Roman Empire.',
            'The novel receives an unfavorable review due to its predictable storyline, shallow dialogue, and unconvincing ethical conclusions.',
            'The literary critic explicitly declines to assess the narrative quality because the documented sources were insufficiently authenticated.',
            'The book is highly recommended for its compelling characters and thought-provoking themes, despite a minor pacing flaw in the middle.'
        ],
        'distractores': [
            'La reseña trata sobre una novela contemporánea de ficción, no una biografía de generales romanos.',
            'El autor elogia ampliamente la obra («compelling characters», «thought-provoking») y la califica de lectura imprescindible.',
            'El crítico sí leyó y evaluó la obra con criterio riguroso, destacando sus fortalezas narrativas.',
            ''
        ]
    },
    'ing-040': {
        'opciones': [
            'A specialized alpine rescue team reached their bivouac shelter with hot food, dry blankets, and satellite radios.',
            'The expedition members decided to terminate the ascent immediately and commence a dangerous descent toward base camp.',
            'A catastrophic mechanical breakdown in their oxygen regulators forced the mountaineers to descend without delay.',
            'The storm clouds suddenly cleared and the sunrise revealed that the summit was only fifty meters away.'
        ],
        'distractores': [
            'El relato no menciona helicópteros ni equipos de rescate externos; los escaladores continuaron por sus propios medios.',
            'Los montañistas perseveraron en el ascenso en vez de rendirse y regresar al campamento base.',
            'No hubo fallas en los tanques de oxígeno; el obstáculo principal era la intensa ventisca de nieve.',
            ''
        ]
    }
}

def balance_ingles():
    ing = json.load(open('content/questions/ingles.json', 'r', encoding='utf-8'))
    hojas = json.load(open('content/hojas.json', 'r', encoding='utf-8'))
    guiones = json.load(open('content/guiones.json', 'r', encoding='utf-8'))
    enfoques = json.load(open('content/enfoques.json', 'r', encoding='utf-8'))

    # ing-001..004 are original: 1 A, 2 B, 1 C, 0 D
    # Target for ing-005 to ing-040 (36 questions):
    # A: 9 (ing-005 to ing-013)
    # B: 8 (ing-014 to ing-021)
    # C: 9 (ing-022 to ing-030)
    # D: 10 (ing-031 to ing-040)
    # Total: 10 A, 10 B, 10 C, 10 D (40 questions)
    target_keys = (
        [0] * 9 +   # 9 A  (ing-005 to ing-013)
        [1] * 8 +   # 8 B  (ing-014 to ing-021)
        [2] * 9 +   # 9 C  (ing-022 to ing-030)
        [3] * 10    # 10 D (ing-031 to ing-040)
    )

    t_idx = 0
    for q in ing:
        qid = q['id']
        idx = int(qid.split('-')[1])
        if idx <= 4:
            continue

        # Aplicar mejoras de opciones y distractores si existen
        if qid in AJUSTES_ING:
            q['opciones'] = list(AJUSTES_ING[qid]['opciones'])
            q['distractores'] = list(AJUSTES_ING[qid]['distractores'])
            # Encuentra la clave correcta actual (la que tiene distractor vacio)
            curr_c = q['distractores'].index('')
            q['correcta'] = curr_c
        else:
            curr_c = q['correcta']

        target_c = target_keys[t_idx]
        t_idx += 1

        if curr_c != target_c:
            q['opciones'][curr_c], q['opciones'][target_c] = q['opciones'][target_c], q['opciones'][curr_c]
            q['distractores'][curr_c], q['distractores'][target_c] = q['distractores'][target_c], q['distractores'][curr_c]
            q['correcta'] = target_c

        h = build_hoja_for_question(q)
        q['hoja'] = h
        hojas[qid] = {'modo': h['modo'], 'marcas': [], 'pasos': h['pasos']}
        guiones[qid] = h['guion']
        enfoques[qid] = h['enfoque']

    json.dump(ing, open('content/questions/ingles.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(hojas, open('content/hojas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(guiones, open('content/guiones.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(enfoques, open('content/enfoques.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print("Ingles balanced and hojas generated successfully.")

if __name__ == '__main__':
    balance_ingles()
