"""Varía los distractores, enfoque y guiones de ena/eng/ing i038 e i039
para que cada cuadernillo tenga su redacción propia, no plantilla compartida.
"""
import json

DATA = {
    'ena-i038': {
        'A': '{{larger}} es una forma comparativa que requiere contrastar dos entidades concretas (como en «larger than another»). En esta oración no hay un segundo grupo de comparación y el artículo «The» exige la forma superlativa.',
        'C': '{{large}} es el adjetivo en grado positivo simple (grande). Al estar precedido por el artículo definido «The» y referirse al grupo de mayor magnitud entre todos, la regla gramatical impone el superlativo {{largest}}.',
        'tema': 'Gramática en inglés: adjetivos superlativos',
        'que': 'Identificar la forma superlativa {{largest}} requerida tras el artículo definido «The».',
        'clave': 'El artículo «The» antepuesto al adjetivo exige el superlativo {{largest}} para señalar al grupo de mayor tamaño de todos.'
    },
    'eng-i038': {
        'A': '{{larger}} funciona en estructuras de comparación relativa entre dos elementos; aquí se define la población más numerosa de lobos de todo el parque, lo cual demanda la terminación de superlativo -est.',
        'C': '{{large}} describe tamaño de manera absoluta sin graduación de superioridad. La presencia de {{The ______ group}} señala al conjunto de mayor tamaño existente, descartando el grado positivo neutro.',
        'tema': 'Uso de la lengua en inglés: grados del adjetivo',
        'que': 'Reconocer que la descripción de la población principal de lobos exige el grado superlativo {{largest}}.',
        'clave': 'En este contexto biológico, se designa a la mayor manada existente en el parque nacional mediante el superlativo {{largest}}.'
    },
    'ing-i038': {
        'A': '{{larger}} solo sería apropiado si se comparara este grupo con otro mediante «than»; al no haber término de contraste y tener «The» adelante, corresponde el grado superlativo absoluto.',
        'C': '{{large}} no aporta el sentido superlativo que exige el contexto ecológico del texto, donde se resalta que esta manada es la de mayor tamaño entre todas las registradas.',
        'tema': 'Comprensión textual en inglés: formas superlativas',
        'que': 'Determinar el adjetivo adecuado para indicar el grupo de mayor tamaño registrado en la reserva.',
        'clave': 'La construcción {{The ______ group}} denota superioridad absoluta y se completa correctamente con {{largest}}.'
    },
    'ena-i039': {
        'B': '{{along}} denota desplazamiento o ubicación en sentido longitudinal (a lo largo de una línea o río); un parque nacional constituye una superficie o área geográfica cerrada, no una franja lineal.',
        'C': '{{on}} se reserva para el contacto sobre superficies externas planas o elevaciones; para indicar permanencia o hábitat dentro de los límites de un parque natural se emplea la preposición {{in}}.',
        'tema': 'Preposiciones de lugar en inglés',
        'que': 'Elegir la preposición de lugar {{in}} para expresar que los animales habitan dentro de los límites de un parque.',
        'clave': 'Estar o habitar en el interior de un área geográfica o parque delimitado se expresa en inglés con la preposición {{in}}.'
    },
    'eng-i039': {
        'B': '{{along}} se utiliza para describir movimiento o alineación paralela a un camino o costa, lo cual no aplica a una manada que habita en el interior de una reserva natural montañosa.',
        'C': '{{on}} indicaría posición física encima de un objeto («on the surface»); los animales viven dentro del territorio delimitado del parque, requiriendo {{in}}.',
        'tema': 'Uso preposicional en inglés',
        'que': 'Identificar que la relación espacial de residencia en una reserva natural exige la preposición {{in}}.',
        'clave': 'Los lobos etíopes existen dentro del territorio del parque nacional; por ende, la preposición precisa es {{in}}.'
    },
    'ing-i039': {
        'B': '{{along}} implica una trayectoria longitudinal continua; el parque nacional es un espacio territorial bidimensional o tridimensional dentro del cual reside la especie amenazada.',
        'C': '{{on}} no expresa inclusión dentro de un espacio geográfico o perímetro de conservación, sentido que en inglés corresponde exclusivamente a {{in}}.',
        'tema': 'Gramática y preposiciones espaciales en inglés',
        'que': 'Seleccionar la preposición de inclusión espacial {{in}} requerida para la ubicación en un parque nacional.',
        'clave': 'Para indicar presencia o residencia dentro del área de un parque nacional, la preposición correcta es {{in}}.'
    }
}

def update_q(q, code, qnum):
    qid = f'{code}-{qnum}'
    info = DATA[qid]
    correcta = q['correcta']
    # Build distractores list
    if qnum == 'i038':
        opt_A, opt_C = info['A'], info['C']
        q['distractores'] = [opt_A, '', opt_C]
        no_items = [
            {'t': 'Opción A', 'p': 'Pero ' + opt_A[0].lower() + opt_A[1:]},
            {'t': 'Opción C', 'p': 'Pero ' + opt_C[0].lower() + opt_C[1:]}
        ]
        g2 = [
            {'a': 'leer', 't': 'Relacionemos la pista con la información del pasaje.'},
            {'a': 'p:1', 't': info['clave']},
            {'a': 'o:A:no', 'k': 'err', 't': f'La opción A no corresponde: {opt_A}'},
            {'a': 'o:C:no', 'k': 'err', 't': f'La opción C no corresponde: {opt_C}'},
            {'a': 'o:B:ok', 't': 'La opción {{largest}} sí responde a la pista.'}
        ]
    else: # i039
        opt_B, opt_C = info['B'], info['C']
        q['distractores'] = ['', opt_B, opt_C]
        no_items = [
            {'t': 'Opción B', 'p': 'Pero ' + opt_B[0].lower() + opt_B[1:]},
            {'t': 'Opción C', 'p': 'Pero ' + opt_C[0].lower() + opt_C[1:]}
        ]
        g2 = [
            {'a': 'leer', 't': 'Relacionemos la pista con la información del pasaje.'},
            {'a': 'p:1', 't': info['clave']},
            {'a': 'o:B:no', 'k': 'err', 't': f'La opción B no corresponde: {opt_B}'},
            {'a': 'o:C:no', 'k': 'err', 't': f'La opción C no corresponde: {opt_C}'},
            {'a': 'o:A:ok', 't': 'La opción {{in}} sí responde a la pista.'}
        ]
    
    h = q.get('hoja', {})
    if 'enfoque' in h:
        h['enfoque']['tema'] = info['tema']
        h['enfoque']['que'] = info['que']
        h['enfoque']['clave'] = info['clave']
        h['enfoque']['no'] = no_items
    if 'guion' in h:
        h['guion']['2'] = g2
        if '1' in h['guion'] and len(h['guion']['1']) >= 3:
            h['guion']['1'][2]['t'] = info['clave']

def main():
    for code in ['ena', 'eng', 'ing']:
        preg_path = f'content/icfes/{code}/preguntas.json'
        with open(preg_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for q in data['preguntas']:
            if q['id'] in (f'{code}-i038', f'{code}-i039'):
                qnum = q['id'].split('-')[1]
                qid = q['id']
                update_q(q, code, qnum)
                # also update hoja file
                hoja_path = f'content/icfes/{code}/hojas/{qid}.json'
                try:
                    with open(hoja_path, 'r', encoding='utf-8') as hf:
                        hdata = json.load(hf)
                    hobj = hdata.get('hoja', hdata)
                    dummy_q = {'correcta': q['correcta'], 'hoja': hobj}
                    update_q(dummy_q, code, qnum)
                    with open(hoja_path, 'w', encoding='utf-8') as hf:
                        json.dump(hdata, hf, ensure_ascii=False, indent=2)
                        hf.write('\n')
                except FileNotFoundError:
                    pass
        
        with open(preg_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'Actualizado {preg_path}')

if __name__ == '__main__':
    main()
