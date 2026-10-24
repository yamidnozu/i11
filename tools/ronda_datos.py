import json, sys
sys.path.insert(0, 'tools')
import ronda_fix as r

def q(i):
    p = i.split('-')[0]
    return [x for x in r.rd(f'content/icfes/{p}/preguntas.json')['preguntas'] if x['id'] == i][0]

C = {}
# --- Inglés: comparativo/superlativo e in/along/on
for p in ('ena', 'eng', 'ing'):
    C[f'{p}-i038'] = {'distractores': [
        '{{larger}} es comparativo: sirve para contrastar dos grupos («larger than…»). Aquí nadie se compara con otro y, tras «The», la frase pide señalar el grupo mayor de todos.',
        '',
        '{{large}} es grado positivo (grande, sin comparar). Después de «The» y con el sentido de «el de mayor tamaño» hace falta el superlativo con -est.']}
    C[f'{p}-i039'] = {'distractores': [
        '',
        '{{along}} significa «a lo largo de» (un río, un camino) y describe una línea; el parque es un área y la frase dice que los lobos están dentro de ella.',
        '{{on}} es «sobre» una superficie (on the table); para estar dentro de un parque o territorio se usa {{in}}.']}

# --- mat-i002 / mth-i002
q_m = q('mat-i002'); q_t = q('mth-i002')
ops = list(q_m['opciones']); ops[0] = 'Sí, porque, sin importar cómo varíe la tasa de cambio, el porcentaje de aumento en dólares es el mismo en pesos.'
C['mat-i002'] = {'opciones': ops, 'distractores': [
    'Solo se cumple porque esta vez la tasa es fija: si cambiara durante el mes, el porcentaje en pesos sería distinto. La opción generaliza a cualquier variación y eso es falso.',
    'No hace falta el monto: el porcentaje se conserva sin importar cuánto dinero se invierta, porque capital y ganancia se multiplican por la misma tasa de cambio.',
    '',
    'El factor de 4.000 vuelve más grandes las cantidades en pesos, pero el aumento es la razón ganancia/inversión y ese factor se cancela: el porcentaje sigue siendo 3 %.']}
C['mth-i002'] = {'distractores': [
    'Solo se cumple porque esta vez la tasa es fija: si cambiara durante el mes, el porcentaje en pesos sería distinto. La opción generaliza a cualquier variación y eso es falso.',
    'No hace falta el monto: el porcentaje se conserva sin importar cuánto dinero se invierta, porque capital y ganancia se multiplican por la misma tasa de cambio.',
    '',
    'El factor de 2.000 vuelve más grandes las cantidades en pesos, pero el aumento es la razón ganancia/inversión y ese factor se cancela: el porcentaje sigue siendo 3 %.']}

C['cfi-i015'] = {'distractores': [
    'Confunde «enteros menores que 11» con los valores de j. Sirve cualquier entero j > 11 (12, 13, 100…) para obtener un racional menor que k + 1/11, y esos j son infinitos.',
    '',
    'j = 11 da exactamente k + 1/11, que es el límite y no un número menor que él; los racionales buscados usan j mayor que 11.',
    'j = 10 da k + 0,1, que es mayor que k + 1/11, no menor. Además no existe un «más cercano»: para cualquier j siempre hay otro mayor que queda más cerca de k.']}

MEZ = ['', 
    'Sustancia pura exige composición fija. El acero tiene cantidades distintas de hierro y carbono entre muestras, así que no es compuesto aunque se vea uniforme.',
    'Heterogénea significa que se distinguen fases a simple vista; el acero es uniforme, por tanto homogénea. Tener varios elementos no basta para ser heterogénea.',
    'Concluye «sustancia pura» a partir de un dato que dice lo contrario: que las muestras tengan composición diferente indica mezcla de composición variable.']
for i in ('cfi-i077', 'cna-i028', 'cie-i028'): C[i] = {'distractores': MEZ}

C['cfi-i085'] = {'distractores': [
    'A pone el vagón alto en t1 y bajo en t2: invierte la secuencia; la gráfica muestra energía baja en t1 y la mayor altura en t2.',
    'B mantiene el vagón abajo hasta t3 y solo sube en t4; la gráfica ya alcanza su valor máximo en t2, no al final.',
    'C asciende hasta la cima en t2, pero luego sigue descendiendo en t3 y t4: no repite un nivel bajo en t3 ni termina en una plataforma intermedia en t4.',
    '']}

for i in ('cna-i027', 'cie-i027'):
    C[i] = {'distractores': [
        '',
        'Reconoce que la presión baja, pero saca la conclusión inversa: con menos presión atmosférica el vapor la iguala antes, así que hierve a menor temperatura, no mayor.',
        'Menos aire cambia la temperatura de ebullición, no impide hervir: el agua sigue hirviendo cuando su presión de vapor iguala la atmosférica, que en 25 km es muy baja.',
        'La baja presión no congela el agua: la congelación depende de la temperatura; el enunciado relaciona la ebullición con la presión de vapor.']}

for i in ('cie-i032', 'cna-i032'):
    C[i] = {'distractores': [
        'La refracción hace que la imagen aparente suba, no baje: al salir del agua los rayos se alejan de la normal y el ojo los prolonga hacia arriba.',
        'Si el farol se viera a la misma altura la luz no se desviaría, pero la figura 2 muestra que el rayo sí cambia de dirección al cruzar de medio.',
        '',
        'La refracción cambia la posición aparente del farol, no lo da vuelta: no hay cruce de rayos que invierta la imagen.']}

C['cfi-i105'] = {'distractores': [
    'Una bicicleta va por carretera, pero la definición apunta a un vehículo motorizado para conductor y un acompañante; la bike es de pedales y normalmente de un solo ocupante.',
    'A boat navega sobre el agua, no por carretera (by road).',
    'A bus transporta a decenas de pasajeros, no solo a una o dos personas.',
    'A helicopter vuela por el aire, no se desplaza por carretera.',
    '',
    'Un avión es un medio de transporte aéreo para cientos de viajeros, no terrestre.',
    'A truck sí va por carretera, pero es un vehículo pesado pensado para carga y no para uno o dos pasajeros de forma típica.',
    'A train circula por vías férreas y lleva muchos pasajeros, no va por carretera.']}

qq = q('cfi-i040'); o = list(qq['opciones'])
o[0] = 'Que en esa comunidad nunca llega a existir amor entre los esposos, ni antes ni después de casarse.'
o[2] = 'Que las mujeres de esa comunidad sienten temor a enamorarse de sus esposos y por eso lo ocultan.'
C['cfi-i040'] = {'opciones': o, 'distractores': [
    'Afirma que nunca hay amor entre esposos, pero el texto muestra actitudes distintas: algunas aceptan el amor después de casarse.',
    '',
    'El pasaje no menciona temor a enamorarse; habla de negar el apego, y negarlo no es lo mismo que tenerle miedo.',
    'El pasaje no dice que el amor de las mujeres quede sin correspondencia; habla de si el amor es condición del matrimonio.']}

if __name__ == '__main__':
    r.aplicar(C)
    print('muletillas limpiadas en', r.limpiar_muletillas(), 'preguntas')
