"""Refina mth-i002 y cfi-i105 con alineación exacta de distractores,
números hablados en palabras y pasos individuales en guion 2.
"""
import json

def fix_mth002():
    distractores = [
        'Solo se cumple porque esta vez la tasa es fija: si cambiara durante el mes, el porcentaje en pesos sería distinto. La opción generaliza a cualquier variación y eso es falso.',
        'No hace falta el monto: el porcentaje se conserva sin importar cuánto dinero se invierta, porque capital y ganancia se multiplican por la misma tasa de cambio.',
        '',
        'El factor de dos mil vuelve más grandes las cantidades en pesos, pero el aumento es la razón ganancia/inversión y ese factor se cancela: el porcentaje sigue siendo tres por ciento.'
    ]
    no_items = [
        {'t': 'Opción A', 'p': 'Pero solo se cumple porque esta vez la tasa es fija: si cambiara durante el mes, el porcentaje en pesos sería distinto. La opción generaliza a cualquier variación y eso es falso.'},
        {'t': 'Opción B', 'p': 'Pero no hace falta el monto: el porcentaje se conserva sin importar cuánto dinero se invierta, porque capital y ganancia se multiplican por la misma tasa de cambio.'},
        {'t': 'Opción D', 'p': 'Pero el factor de dos mil vuelve más grandes las cantidades en pesos, pero el aumento es la razón ganancia/inversión y ese factor se cancela: el porcentaje sigue siendo tres por ciento.'}
    ]
    pistas = [
        'Analiza qué ocurre con el rendimiento en pesos cuando la tasa de cambio entre dólar y peso se mantiene fija.',
        'Comprueba que la ganancia porcentual en pesos es idéntica al tres por ciento en dólares si no hay variación cambiaria.'
    ]
    g2 = [
        {'t': 'Llama $P$ al capital inicial en dólares y multiplícalo por uno coma cero tres para incluir la ganancia.'},
        {'t': 'Al convertir ambos valores a pesos, se multiplican por dos mil y su proporción de aumento sigue igual.'},
        {'a': 'o:A:no', 'k': 'err', 't': 'La opción A no corresponde: solo se cumple porque esta vez la tasa es fija; si cambiara durante el mes, el porcentaje en pesos variaría.'},
        {'a': 'o:B:no', 'k': 'err', 't': 'La opción B no corresponde: el porcentaje se conserva sin importar el capital exacto invertido.'},
        {'a': 'o:D:no', 'k': 'err', 't': 'La opción D no corresponde: el factor de dos mil afecta por igual al capital y a la ganancia, por lo que el aumento porcentual sigue siendo tres por ciento.'},
        {'a': 'o:C:ok', 't': 'A ignora la condición de tasa fija; B pide un monto innecesario; D confunde valor absoluto con porcentaje. La respuesta es C.'}
    ]

    # in preguntas.json
    p_path = 'content/icfes/mth/preguntas.json'
    with open(p_path) as f:
        data = json.load(f)
    for q in data['preguntas']:
        if q['id'] == 'mth-i002':
            q['distractores'] = distractores
            h = q.get('hoja', {})
            if 'enfoque' in h:
                h['enfoque']['no'] = no_items
                h['enfoque']['pistas'] = pistas
            if 'guion' in h:
                h['guion']['2'] = g2
    with open(p_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    # in hoja file
    h_path = 'content/icfes/mth/hojas/mth-i002.json'
    with open(h_path) as f:
        hdata = json.load(f)
    hoja = hdata.get('hoja', hdata)
    hoja['enfoque']['no'] = no_items
    hoja['enfoque']['pistas'] = pistas
    hoja['guion']['2'] = g2
    with open(h_path, 'w', encoding='utf-8') as f:
        json.dump(hdata, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('mth-i002 actualizado')

def fix_cfi105():
    distractores = [
        'A {{bike}} va por carretera pero se mueve a pedal; la definición pide un vehículo con motor para una o dos personas como la {{motorbike}}.',
        'A {{boat}} navega sobre el agua, no por carretera (by road).',
        'A {{bus}} transporta a decenas de pasajeros, no solo a una o dos personas.',
        'A {{helicopter}} vuela por el aire, no se desplaza por carretera.',
        '',
        'A {{plane}} es un medio de transporte aéreo para muchos viajeros; no va por carretera ni es para una o dos personas.',
        'A {{truck}} sí va por carretera, pero es un vehículo pesado pensado para carga y no para uno o dos pasajeros de forma típica.',
        'A {{train}} circula por vías férreas y lleva muchos pasajeros, no va por carretera.'
    ]
    no_items = [
        {'t': 'Opción A', 'p': 'Pero a {{bike}} va por carretera pero se mueve a pedal; la definición pide un vehículo con motor para una o dos personas como la {{motorbike}}.'},
        {'t': 'Opción B', 'p': 'Pero a {{boat}} navega sobre el agua, no por carretera (by road).'},
        {'t': 'Opción C', 'p': 'Pero a {{bus}} transporta a decenas de pasajeros, no solo a una o dos personas.'},
        {'t': 'Opción D', 'p': 'Pero a {{helicopter}} vuela por el aire, no se desplaza por carretera.'},
        {'t': 'Opción F', 'p': 'Pero a {{plane}} es un medio de transporte aéreo para muchos viajeros; no va por carretera ni es para una o dos personas.'},
        {'t': 'Opción G', 'p': 'Pero a {{truck}} sí va por carretera, pero es un vehículo pesado pensado para carga y no para uno o dos pasajeros de forma típica.'},
        {'t': 'Opción H', 'p': 'Pero a {{train}} circula por vías férreas y lleva muchos pasajeros, no va por carretera.'}
    ]
    g2 = [
        {'a': 'leer', 't': 'Leamos la definición y analicemos cada vehículo descartado.'},
        {'a': 'o:A:no', 'k': 'err', 't': 'La opción A no corresponde: {{bike}} se mueve a pedal y no con motor.'},
        {'a': 'o:B:no', 'k': 'err', 't': 'La opción B no corresponde: {{boat}} navega sobre el agua y no por carretera.'},
        {'a': 'o:C:no', 'k': 'err', 't': 'La opción C no corresponde: {{bus}} es de transporte masivo y no para una o dos personas.'},
        {'a': 'o:D:no', 'k': 'err', 't': 'La opción D no corresponde: {{helicopter}} es transporte aéreo y no terrestre.'},
        {'a': 'o:F:no', 'k': 'err', 't': 'La opción F no corresponde: {{plane}} vuela por el aire para cientos de pasajeros.'},
        {'a': 'o:G:no', 'k': 'err', 't': 'La opción G no corresponde: {{truck}} es un vehículo pesado de carga comercial.'},
        {'a': 'o:H:no', 'k': 'err', 't': 'La opción H no corresponde: {{train}} circula por vías férreas y no por carretera.'},
        {'a': 'o:E:ok', 't': 'Por descarte confirmamos que la opción E {{motorbike}} es la respuesta correcta.'}
    ]

    p_path = 'content/icfes/cfi/preguntas.json'
    with open(p_path) as f:
        data = json.load(f)
    for q in data['preguntas']:
        if q['id'] == 'cfi-i105':
            q['distractores'] = distractores
            h = q.get('hoja', {})
            if 'enfoque' in h:
                h['enfoque']['no'] = no_items
            if 'guion' in h:
                h['guion']['2'] = g2
    with open(p_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    h_path = 'content/icfes/cfi/hojas/cfi-i105.json'
    with open(h_path) as f:
        hdata = json.load(f)
    hoja = hdata.get('hoja', hdata)
    hoja['enfoque']['no'] = no_items
    hoja['guion']['2'] = g2
    with open(h_path, 'w', encoding='utf-8') as f:
        json.dump(hdata, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('cfi-i105 actualizado')

if __name__ == '__main__':
    fix_mth002()
    fix_cfi105()
