#!/usr/bin/env python3
"""Reescritura pedagógica: pasos gráficos + guion (L1 corto, L2 con porqués, L3 otra mirada)."""
import json
H=json.load(open('content/hojas.json'));G=json.load(open('content/guiones.json'))
def B(t,a=None,k=None):
    d={'t':t}
    if a: d['a']=a
    if k: d['k']=k
    return d
def keep(old):
    out=[]
    for b in old:
        parts=[x for x in (b.get('a') or '').split('|') if not x.startswith('p:')]
        had=(b.get('a') or '')!=('|'.join(parts))
        if had and not parts: continue
        c=dict(b)
        if had: c['a']='|'.join(parts)
        out.append(c)
    return out
def rew(id,pasos,p1,p2,p3):
    H[id]['pasos']=pasos
    for n,ps in (('1',p1),('2',p2)):
        old=keep(G[id][n]);pre=[b for b in old if not (b.get('a') or '').startswith('o:')];post=[b for b in old if (b.get('a') or '').startswith('o:')]
        G[id][n]=pre+[B(*x) if isinstance(x,tuple) else x for x in ps]+post
    G[id]['3']=[B(*x) for x in p3]
TR=lambda t,f,nota=None:{'k':'traducir','titulo':t,'filas':f,**({'nota':nota} if nota else {})}
def F(d,e,r=None):
    x={'dice':d,'escribo':e}
    if r: x['rol']=r
    return x
BR=lambda t,b,ref=None,nota=None:{'k':'barras','titulo':t,'barras':b,**({'ref':ref} if ref else {}),**({'nota':nota} if nota else {})}
def bar(l,e,*segs): return {'l':l,'e':e,'segs':[{'v':v,'c':c} for v,c in segs]}
FL=lambda t,n,s,nota=None:{'k':'flujo','titulo':t,'nodos':[{'v':v,'l':l} for v,l in n],'saltos':s,**({'nota':nota} if nota else {})}
VI=lambda t,x:{'k':'vida','titulo':t,'texto':x}
CK=lambda x:{'k':'check','texto':x}

# ---------------- mat-006 ----------------
rew('mat-006',[
 VI('Imagínalo con una camiseta','Una camiseta cuesta 100.000 pesos. La tienda la sube $20\\%$ y, una semana después, la pone en oferta con $20\\%$ de descuento. ¿Queda otra vez en 100.000 pesos? Casi todos dicen que sí. Miremos qué pasa de verdad.'),
 BR('Míralo con barras',[bar('Al inicio','$100.000',(100,'azul')),bar('Sube $20\\%$: se agregan 20.000 pesos','$120.000',(100,'azul'),(20,'verde')),bar('Baja $20\\%$ de 120.000: se quitan 24.000 pesos','$96.000',(96,'azul'),(24,'rojo'))],{'v':100,'l':'precio inicial'},'Lo verde es lo que se agrega; lo rayado en rojo es lo que se quita. Se quita más de lo que se agregó, porque el $20\\%$ ahora se saca de una barra más larga.'),
 TR('¿Por qué ×1,2 y ×0,8?',[F('sube $20\\%$','100\\%+20\\%=120\\%\\Rightarrow\\times1{,}2','dato'),F('baja $20\\%$','100\\%-20\\%=80\\%\\Rightarrow\\times0{,}8','dato')],'El precio de ese momento siempre es el 100 %. Subir es quedarse con más de ese 100 %; bajar, con menos. Y 120 % es lo mismo que 1,2.'),
 FL('Hazlo paso a paso',[('$100.000','precio inicial'),('$120.000','después de subir'),('$96.000','precio final')],['\\times1{,}2\\ \\ (\\text{sube }20\\%)','\\times0{,}8\\ \\ (\\text{baja }20\\%\\ \\text{del nuevo})'],'$100.000\\cdot1{,}2=120.000$ y luego $120.000\\cdot0{,}8=96.000$.'),
 CK('Subir y bajar el mismo porcentaje no deja el precio igual: el segundo $20\\%$ se calcula sobre un precio más grande. Por eso la respuesta es $96.000$.')],
 [('Mira la barra: parte de $100.000$, sube a $120.000$ y luego baja a $96.000$. No vuelve al inicio.','p:1'),('Para calcularlo, subir $20\\%$ es multiplicar por $1{,}2$ y bajar $20\\%$ es multiplicar por $0{,}8$.','p:2'),('$100.000$ por $1{,}2$ da $120.000$; por $0{,}8$ da $96.000$.','p:3')],
 [('Pensemos en una camiseta de $100.000$. Sube y luego se rebaja el mismo porcentaje. ¿Queda igual?','p:0'),('Veamos con barras. Al subir $20\\%$ se agregan $20.000$: la barra llega a $120.000$.','p:1'),('Ahora baja $20\\%$, pero del precio nuevo: el $20\\%$ de $120.000$ es $24.000$. Se quita más de lo que se agregó.','p:1','por'),('Para no hacer la barra cada vez, uso multiplicaciones. Subir $20\\%$ es quedarse con el $120\\%$, o sea por $1{,}2$.','p:2'),('Bajar $20\\%$ es quedarse con el $80\\%$, o sea por $0{,}8$.','p:2'),('Entonces: $100.000$ por $1{,}2$ es $120.000$, y por $0{,}8$ es $96.000$.','p:3')],
 [('Es como una escalera. Subes $20$ peldaños de una escalera de $100$, y ahora estás en el $120$.',None,'ana'),('Si bajas el $20\\%$ de donde estás ahora, bajas $24$ peldaños, no $20$. Terminas más abajo de donde empezaste.',None,'ana'),('Ejemplo extremo: si sube $100\\%$ pasa de $100$ a $200$. Si baja $50\\%$ vuelve a $100$: aquí sí vuelve, pero no porque $100$ y $50$ se cancelen.',None,'ej'),('Error común: restar los porcentajes, $20-20=0$. Eso solo sirve cuando se calculan sobre el mismo precio.',None,'err')])

O=lambda id,i:H[id]['pasos'][i]
# ---------------- mat-001 taxi ----------------
o=H['mat-001']['pasos']
rew('mat-001',[
 VI('Piensa en el taxímetro','Te subes al taxi y el taxímetro ya marca 4.000 pesos, sin haber andado nada. Después, cada kilómetro suma 1.000 pesos más. Miremos eso con barras.'),
 BR('Cuánto marca según los kilómetros',[bar('0 km (apenas te subes)','$4.000',(4,'azul')),bar('1 km','$5.000',(4,'azul'),(1,'verde')),bar('2 km','$6.000',(4,'azul'),(2,'verde')),bar('7 km (tu recorrido)','$11.000',(4,'azul'),(7,'oro'))],None,'Lo azul es el arranque: se paga una sola vez y nunca crece. Lo de color crece 1.000 por cada kilómetro.'),
 o[1],o[2],o[3],CK('Sin el arranque serían 7.000 pesos. Con el arranque, 11.000.')],
 [('Mira las barras: lo azul es el arranque, que se paga una sola vez. Lo verde crece mil pesos por cada kilómetro.','p:1'),('Pasamos cada frase a matemáticas: el arranque es $4.000$, y cada kilómetro es $1.000\\cdot k$.','p:2'),('Función del costo: arranque más mil por kilómetro. Con $7$ km: $4.000+7.000=11.000$.','p:3|p:4')],
 [('Te subes al taxi: el taxímetro ya marca $4.000$ antes de moverte.','p:0'),('Con cada kilómetro suma mil más. Mira cómo crece la parte de color, pero la azul no cambia.','p:1'),('Traducimos: lo que se paga una sola vez es el arranque, $4.000$. Lo que dice «por cada» se multiplica por la cantidad de kilómetros.','p:2'),('Entonces el costo es $C=4.000+1.000\\cdot k$.','p:3'),('Con $k=7$: $1.000\\cdot7=7.000$, más el arranque $4.000$, son $11.000$.','p:4')],
 [('Es como una entrada al cine con dulces: la entrada se paga una vez, y cada dulce suma.',None,'ana'),('Ejemplo: un plan de celular con cargo fijo de $20.000$ y $500$ por cada minuto extra. El cargo fijo no depende de los minutos.',None,'ej'),('Error común: multiplicar todo por $7$, $(4.000+1.000)\\cdot7=35.000$. El arranque se paga una vez, no por kilómetro.',None,'err')])
# ---------------- mat-003 probabilidad ----------------
o=H['mat-003']['pasos']
rew('mat-003',[
 VI('Imagina que metes la mano sin mirar','Una bolsa con 3 fichas rojas y 5 azules. Metes la mano a ciegas y sacas una. ¿Qué tan fácil es que sea roja? Hay pocas rojas entre varias fichas, así que no es tan fácil. La probabilidad lo mide con una fracción.'),
 o[1],
 {'k':'calc','titulo':'La regla de la probabilidad','lineas':['P=\\frac{\\text{las que quiero}}{\\text{todas las que hay}}','P(\\text{roja})=\\frac{3}{8}'],'nota':'Arriba van las fichas que quiero (rojas). Abajo van todas las fichas, rojas y azules juntas.'},
 CK('$3/5$ compara rojas con azules: eso no es probabilidad, porque abajo faltan las rojas.')],
 [('Dibuja la bolsa: $3$ rojas y $5$ azules. En total hay $8$ fichas.','p:1'),('Probabilidad es las que quiero sobre todas las que hay: $3$ sobre $8$.','p:2')],
 [('Es una bolsa con fichas, y sacas una sin mirar.','p:0'),('Cuento las rojas, que son las que quiero: tres. Y las azules: cinco. Total de fichas: ocho.','p:1'),('La regla: las que quiero, sobre todas las que hay. Es decir, $3$ sobre $8$.','p:2'),('Ojo: abajo van las ocho, no solo las cinco azules. Por eso $3/5$ está mal.','p:3','err')],
 [('Es como una rifa con $8$ boletas: si tienes $3$, tienes $3$ de $8$ posibilidades de ganar.',None,'ana'),('Ejemplo: en un salón de $30$ hay $10$ que usan gafas. Si eliges a uno al azar, la probabilidad de que use gafas es $10/30$.',None,'ej'),('Error común: comparar contra las otras, $3$ rojas contra $5$ azules. Siempre se compara contra el total.',None,'err')])
# ---------------- mat-004 estadística ----------------
o=H['mat-004']['pasos']
rew('mat-004',[
 VI('Media y mediana, con un ejemplo','La media es como repartir parejo: juntas todo y lo repartes igual entre todos. La mediana es el que queda parado justo en el medio de la fila. Un dato enorme, como el 8, jala la media hacia arriba, pero a la mediana casi no le importa.'),
 BR('Los datos con barras',[bar('Dato 1','2',(2,'azul')),bar('Dato 2','3',(3,'azul')),bar('Dato 3','3',(3,'azul')),bar('Dato 4','4',(4,'azul')),bar('Dato 5 (el que se elimina)','8',(8,'rojo'))],{'v':4,'l':'media con el 8 = 4'},'La barra roja es la que estira la media. Sin ella, la media baja.'),
 o[0],
 CK('La media bajó de 4 a 3, porque el 8 la jalaba hacia arriba. La mediana sigue en 3, porque el del medio es el mismo.')],
 [('Estos son los datos. El $8$ es el más largo: jala la media.','p:1'),('Comparo antes y después de quitarlo: la media baja de $4$ a $3$ y la mediana sigue en $3$.','p:2')],
 [('Primero, qué es cada cosa. La media reparte parejo; la mediana es el dato del medio.','p:0'),('Miro los datos en barras. El $8$ es el que se sale de lo normal.','p:1'),('Con el $8$: suma $20$, entre $5$ datos, media $4$. Sin el $8$: suma $12$, entre $4$ datos, media $3$.','p:2'),('La mediana: ordeno los datos y tomo el del centro. Con cuatro datos hay dos del centro, $3$ y $3$, y su promedio es $3$. No cambió.','p:2')],
 [('Piensa en el salario de una tienda: todos ganan casi igual, pero el dueño gana muchísimo. La media sube por el dueño, la mediana no se mueve.',None,'ana'),('Ejemplo: en $1, 2, 3$ la media y la mediana son $2$. Si cambias el $3$ por $30$, la media sube a $11$ y la mediana sigue en $2$.',None,'ej'),('Error común: pensar que si un dato desaparece, todo cambia. La mediana puede quedarse quieta.',None,'err')])
# ---------------- mat-005 dados ----------------
o=H['mat-005']['pasos']
rew('mat-005',[
 VI('Un dado tiene 6 caras, dos dados tienen 36 casos','Con el primer dado puede salir cualquiera de 6 números. Y por cada uno de esos, el segundo dado también puede dar 6. Entonces hay 6 por 6, o sea 36 casos posibles. Los pones todos en una tabla y miras cuántos suman 7.'),
 o[0],o[1],o[2],CK('El $7$ es la suma que más veces se repite con dos dados: por eso es la más probable.')],
 [('La tabla muestra los $36$ casos. Los marcados suman $7$: son $6$.','p:1'),('Probabilidad es los casos que quiero sobre todos: $6$ sobre $36$, que es $1/6$.','p:3')],
 [('Con dos dados hay $6\\cdot6=36$ casos distintos.','p:0'),('Los pongo en una tabla: un dado en las filas, el otro en las columnas, y dentro la suma.','p:1'),('Marco los que dan $7$. Son $6$ parejas: $(1,6)$, $(2,5)$, $(3,4)$, $(4,3)$, $(5,2)$ y $(6,1)$.','p:2'),('$(1,6)$ y $(6,1)$ cuentan por separado, porque son dados distintos.','p:2','por'),('Probabilidad: casos que quiero sobre casos totales, $6/36$, que simplificado es $1/6$.','p:3')],
 [('Es como tener $36$ boletas en una bolsa y que $6$ sean premiadas.',None,'ana'),('Ejemplo: para sumar $12$ solo sirve $(6,6)$. Es $1$ de $36$, mucho más difícil que el $7$.',None,'ej'),('Error común: decir que hay $11$ sumas posibles, de $2$ a $12$, y que todas valen igual. No: unas se repiten más que otras.',None,'err')])
# ---------------- cie-001 proyectil ----------------
o=H['cie-001']['pasos']
rew('cie-001',[
 VI('Piensa en patear un balón','Cuando pateas un balón, sube, llega a lo más alto y baja. Lo lejos que cae es el alcance. Depende de dos cosas: con qué fuerza lo pateas y qué tan inclinado. Con 45° llega lo más lejos posible.'),
 o[0],
 BR('Cuánto avanza según la inclinación',[bar('15°','20 m',(20,'azul')),bar('30° (tu caso)','34,6 m',(34.6,'oro')),bar('45°','40 m',(40,'verde')),bar('60°','34,6 m',(34.6,'azul')),bar('75°','20 m',(20,'azul'))],None,'Con 45° llega más lejos. Con 30° y con 60° llega lo mismo, 34,6 m. Así que 30° tiene que dar menos de 40.'),
 o[1],
 {'k':'calc','titulo':'Fórmula del alcance','lineas':['R=\\frac{v_0^2\\,\\sin(2\\theta)}{g}'],'nota':'Esta fórmula ya junta todo: sube y baja con la gravedad, y avanza a rapidez constante. Solo hay que reemplazar.'},
 o[4],o[5]],
 [('Mira cuánto avanza según el ángulo. Con $30°$ llega menos que con $45°$, que es el máximo de $40$ m.','p:2'),('Uso la fórmula del alcance: velocidad al cuadrado por seno del doble del ángulo, dividido entre $g$.','p:4'),('Reemplazo: $400\\cdot0{,}866$ entre $10$ da $34{,}6$ m. Opción B.','p:5')],
 [('Pateas un balón: sube y baja. Nos piden qué tan lejos cae.','p:0'),('Esa es la distancia entre donde sale y donde cae, sobre el suelo.','p:1'),('Si cambio el ángulo, cambia el alcance. El máximo es con $45°$, $40$ m. Con $30°$ tiene que ser menos.','p:2'),('Paso los datos a símbolos: $v_0=20$, el ángulo es $30°$ y $g=10$.','p:3'),('La fórmula del alcance es $v_0^2\\sin(2\\theta)/g$.','p:4'),('Primero el doble del ángulo: $60°$. Su seno es $0{,}866$. Luego $20^2=400$. $400\\cdot0{,}866=346{,}4$ y entre $10$ da $34{,}6$ m.','p:5')],
 [('Es como lanzar agua con una manguera: apuntando muy arriba cae cerca, apuntando muy plano también cae cerca. A medio camino llega más lejos.',None,'ana'),('Ejemplo: $15°$ y $75°$ dan el mismo alcance, porque suman $90°$.',None,'ej'),('Error común: elegir $40$ m, el máximo, sin fijarse en que el ángulo no es $45°$.',None,'err')])
# ---------------- cie-002 MRUA ----------------
o=H['cie-002']['pasos']
rew('cie-002',[
 VI('Piensa en un carro que arranca','Un carro parte quieto y va acelerando: cada segundo va más rápido que el anterior. Por eso cada segundo recorre más metros que el anterior, y la distancia no es simplemente velocidad por tiempo.'),
 o[0],
 BR('Distancia acumulada, segundo a segundo',[bar('Segundo 1 (va a 3 m/s)','1,5 m',(1.5,'azul')),bar('Segundo 2 (va a 6 m/s)','6 m',(6,'azul')),bar('Segundo 3 (va a 9 m/s)','13,5 m',(13.5,'azul')),bar('Segundo 4 (va a 12 m/s)','24 m',(24,'oro'))],None,'La velocidad sube 3 m/s cada segundo, y la distancia crece cada vez más rápido.'),
 o[2],o[3],
 FL('Compruébalo con la velocidad media',[('$12\\ \\text{m/s}$','velocidad al final: 3 · 4'),('$6\\ \\text{m/s}$','velocidad media: (0 + 12) ÷ 2'),('$24\\ \\text{m}$','distancia: 6 · 4')],['\\text{promedio de la inicial y la final}','\\times4\\ \\text{s}'],'Si hubiera ido siempre a 6 m/s, habría recorrido lo mismo: 24 m.'),
 o[4]],
 [('Los datos: parte del reposo, aceleración $3$, tiempo $4$ segundos.','p:1'),('Mira las barras: cada segundo recorre más. Al cuarto lleva $24$ metros.','p:2'),('La fórmula con $v_0=0$ es un medio de $a$ por $t$ al cuadrado: $\\frac{1}{2}\\cdot3\\cdot16=24$ m.','p:3|p:4')],
 [('Un carro arranca desde el reposo y acelera.','p:0'),('Paso los datos a símbolos: $v_0=0$, $a=3$, $t=4$. Busco la distancia $x$.','p:1'),('Veamos segundo a segundo: la velocidad sube $3$ cada vez, y la distancia acumulada va $1{,}5$, $6$, $13{,}5$ y $24$ metros.','p:2'),('Esa regla se resume en una fórmula. Como parte del reposo, $v_0=0$ y queda $x=\\frac{1}{2}at^2$.','p:3'),('Reemplazo: $4^2=16$, por $3$ da $48$, mitad de $48$ es $24$ m.','p:4'),('Compruebo: la velocidad final es $12$ y la media es $6$. Seis por cuatro segundos son $24$ m.','p:5')],
 [('Es como llenar un tanque con una llave que se abre cada vez más: al principio cae poquito, al final cae mucho.',None,'ana'),('Ejemplo: en $2$ segundos recorre $\\frac{1}{2}\\cdot3\\cdot4=6$ m, y en $4$ segundos $24$ m: el doble de tiempo, cuatro veces la distancia.',None,'ej'),('Error común: calcular $a\\cdot t=12$ m. Eso es la velocidad final, no la distancia.',None,'err')])
# ---------------- cie-003 Ohm ----------------
o=H['cie-003']['pasos']
rew('cie-003',[
 VI('Piensa en agua en una manguera','El voltaje es la presión del agua, la resistencia es qué tan angosta está la manguera y la corriente es cuánta agua sale. Más presión: sale más. Manguera más angosta: sale menos.'),
 o[0],
 BR('Con 12 V, ¿qué pasa si cambia la resistencia?',[bar('R = 3 Ω (manguera ancha)','4 A',(4,'verde')),bar('R = 6 Ω (tu caso)','2 A',(2,'oro')),bar('R = 12 Ω (manguera angosta)','1 A',(1,'azul'))],None,'A más resistencia, menos corriente. Por eso, para hallar la corriente, se divide entre la resistencia.'),
 o[1],
 FL('Reemplaza',[('$12\\ \\text{V}$','voltaje'),('$2\\ \\text{A}$','corriente')],['\\div6\\ \\Omega\\ \\ (\\text{la resistencia})'],'$I=\\frac{12\\ \\text{V}}{6\\ \\Omega}=2\\ \\text{A}$'),
 o[3]],
 [('Los datos: $R=6$, $V=12$, y busco la corriente $I$.','p:1'),('Mira las barras: a más resistencia, menos corriente. Así que se divide.','p:2'),('La ley de Ohm despejada es $I=V/R$: $12$ entre $6$ da $2$ amperios.','p:3|p:4')],
 [('Piensa en una manguera: presión, angostura y agua que sale.','p:0'),('Paso los datos a símbolos: $R=6$, $V=12$, y la corriente $I$ es la incógnita.','p:1'),('Con la misma fuente, si la resistencia crece, la corriente baja. Esto ya me dice que voy a dividir.','p:2'),('La ley de Ohm dice $V=I\\cdot R$. Para dejar $I$ sola divido los dos lados entre $R$.','p:3'),('Reemplazo: $12$ voltios entre $6$ ohmios da $2$ amperios.','p:4')],
 [('Es como una fila en la puerta del colegio: más voltaje es más empuje, más resistencia es una puerta más angosta, y la corriente son los estudiantes que pasan.',None,'ana'),('Ejemplo: con $12$ V y $12\\ \\Omega$ pasa $1$ A, la mitad.',None,'ej'),('Error común: multiplicar $12\\cdot6=72$. La corriente baja cuando la resistencia sube, no crece.',None,'err')])
# ---------------- cie-004 balanceo ----------------
o=H['cie-004']['pasos']
rew('cie-004',[
 VI('Balancear es como una receta','Una reacción reordena los átomos: los que entran son los mismos que salen, solo cambian de pareja. Balancear es ajustar cuántas moléculas hay de cada una para que no sobre ni falte ningún átomo.'),
 o[0],o[1],o[2],
 {'k':'calc','titulo':'Oxígeno','lineas':['3\\ \\text{CO}_2\\to3\\cdot2=6\\ \\text{O}','4\\ \\text{H}_2\\text{O}\\to4\\cdot1=4\\ \\text{O}','6+4=10\\ \\text{átomos de O}','\\text{cada O}_2\\ \\text{trae 2: }10\\div2=5'],'nota':'El número de adelante multiplica cada átomo de la molécula. Cuento todos los O que hay en los productos, y reparto de a 2 en cada O₂.'},
 o[4],o[5]],
 [('Primero el carbono: $3$ en el propano, así que $3$ $\\text{CO}_2$. Luego el hidrógeno: $8$, así que $4$ $\\text{H}_2\\text{O}$.','p:2|p:3'),('Al final el oxígeno: $6+4=10$ átomos, y en cada $\\text{O}_2$ hay dos, así que $5$.','p:4'),('Compruebo en la tabla: todo coincide a ambos lados.','p:5')],
 [('Es una receta: los átomos que entran deben salir.','p:0'),('Voy en orden: carbono, hidrógeno y al final el oxígeno, porque aparece en dos productos.','p:1'),('Carbono: el propano tiene $3$ átomos de C, así que necesito $3$ $\\text{CO}_2$.','p:2'),('Hidrógeno: tiene $8$, y cada agua usa $2$, así que $4$ $\\text{H}_2\\text{O}$.','p:3'),('Oxígeno: $3\\cdot2=6$ más $4\\cdot1=4$, son $10$ átomos. Cada $\\text{O}_2$ trae $2$, entonces $5$.','p:4'),('Verifico contando: C $3$ y $3$, H $8$ y $8$, O $10$ y $10$.','p:5')],
 [('Es como armar sándwiches: si cada sándwich lleva $2$ panes y quieres $5$, necesitas $10$ panes.',None,'ana'),('Ejemplo: $\\text{H}_2+\\text{O}_2\\to\\text{H}_2\\text{O}$ queda $2\\text{H}_2+\\text{O}_2\\to2\\text{H}_2\\text{O}$.',None,'ej'),('Error común: cambiar los números pequeños de abajo, como el $2$ de $\\text{O}_2$. Solo se cambian los coeficientes de adelante.',None,'err')])
# ---------------- cie-005 genética ----------------
o=H['cie-005']['pasos']
o[2]['filas']=[['A','AA','Aa'],['a','Aa','*aa']]
rew('cie-005',[
 VI('Piensa en dos monedas','Cada planta Aa tiene dos letras, y al formar una semilla entrega solo una, al azar, como lanzar una moneda. Dos plantas son dos monedas: hay cuatro combinaciones posibles, todas igual de probables.'),
 o[0],o[1],o[2],o[3],o[4]],
 [('Cada padre entrega $A$ o $a$, mitad y mitad.','p:1'),('Cruzo las dos monedas en un cuadro: salen $4$ casillas.','p:3'),('Solo una es $aa$: probabilidad $1/4$.','p:4')],
 [('Cada planta tiene dos letras: $A$ y $a$.','p:0'),('Al hacer una semilla da una de las dos, con probabilidad $1/2$ cada una.','p:1'),('Armo el cuadro: padre en las columnas, madre en las filas.','p:2'),('Salen $AA$, $Aa$, $Aa$ y $aa$: cuatro casillas igual de probables.','p:3'),('Solo una casilla es $aa$, el recesivo: $1$ de $4$.','p:4'),('$Aa$ se ve igual que $AA$ porque $A$ domina, por eso no cuenta como recesivo.','p:4','por')],
 [('Es como lanzar dos monedas: la probabilidad de dos caras es $1/4$.',None,'ana'),('Ejemplo: de $100$ semillas, se esperan unas $25$ recesivas y $75$ con la característica dominante.',None,'ej'),('Error común: elegir $1/2$ porque hay dos letras. Eso sería una letra, no dos.',None,'err')])
# ---------------- cie-006 lentes ----------------
o=H['cie-006']['pasos']
rew('cie-006',[
 VI('Piensa en una lupa','Una lente convergente junta los rayos de luz, como una lupa. El foco es el punto donde se juntan los rayos que vienen paralelos. Según qué tan lejos pongas el objeto del foco, la imagen se forma en un lugar distinto.'),
 o[0],o[1],
 BR('Dónde queda cada cosa (en cm)',[bar('Foco f','10',(10,'gris')),bar('Objeto dₒ','15',(15,'azul')),bar('Doble del foco, 2f','20',(20,'gris')),bar('Imagen dᵢ (la que vamos a calcular)','30',(30,'oro'))],None,'El objeto está entre f y 2f, así que la imagen queda del otro lado, más lejos que 2f.'),
 o[2],o[3],o[4],o[5]],
 [('Los datos: foco $10$ y objeto a $15$ cm. El objeto queda entre $f$ y $2f$.','p:1'),('Predigo: imagen real, invertida y lejos. Mira las barras.','p:3'),('Ecuación de lentes y resto fracciones: $1/10-1/15=1/30$, o sea $d_i=30$ cm.','p:5|p:6')],
 [('Una lente convergente es como una lupa.','p:0'),('Paso los datos a símbolos: $f=10$ cm y $d_o=15$ cm.','p:1'),('Antes de calcular, predigo. El objeto está entre $f$ y $2f$, así que la imagen será real, invertida y más lejos que $2f$.','p:2'),('Mira las barras: la imagen debería estar más allá de $20$.','p:3'),('La ecuación de lentes: uno sobre $f$ es uno sobre $d_o$ más uno sobre $d_i$.','p:4'),('Despejo: $1/10-1/15$. Para restar busco denominador común, $30$: $3/30-2/30=1/30$. Entonces $d_i=30$.','p:5'),('El aumento es $-30/15=-2$: negativo, invertida; dos veces más grande.','p:6')],
 [('Es como proyectar con una lupa una ventana sobre la pared: la imagen sale al revés.',None,'ana'),('Ejemplo: si el objeto está justo en $2f$, la imagen queda también en $2f$ y del mismo tamaño.',None,'ej'),('Error común: elegir «virtual y derecha», que pasa cuando el objeto está más cerca que el foco, no más lejos.',None,'err')])
# ---------------- cie-008 gases ----------------
o=H['cie-008']['pasos']
rew('cie-008',[
 VI('Piensa en un globo','Un gas llena todo el espacio que le des. Cuánto espacio ocupa depende de cuántas partículas hay, qué tan caliente está y cuánto lo aprietan. Hay una fórmula que junta las tres cosas.'),
 o[0],
 {'k':'calc','titulo':'Gas ideal: despeja V','lineas':['P\\cdot V=n\\cdot R\\cdot T','\\frac{P\\cdot V}{P}=\\frac{n\\cdot R\\cdot T}{P}','V=\\frac{n\\cdot R\\cdot T}{P}'],'nota':'Para dejar V sola divido los dos lados entre P.'},
 o[2],
 BR('Si 1 mol ocupa 22,4 L en estas condiciones',[bar('1 mol','22,4 L',(22.4,'azul')),bar('2 mol (tu caso)','44,8 L',(22.4,'azul'),(22.4,'oro'))],None,'El doble de gas ocupa el doble de espacio.'),
 o[3]],
 [('Los datos: $n=2$, $T=273{,}15$, $P=1$, $R=0{,}082$.','p:1'),('Despejo $V$ en $PV=nRT$: $V=nRT/P$.','p:2'),('$2\\cdot0{,}082\\cdot273{,}15$ da $44{,}8$ litros.','p:3|p:4')],
 [('Un gas llena el espacio que le des.','p:0'),('Paso los datos a símbolos: $n=2$ moles, $T=273{,}15$ kelvin, $P=1$ atmósfera.','p:1'),('La ley del gas ideal es $PV=nRT$. Para dejar $V$ sola, divido los dos lados entre $P$.','p:2'),('Multiplico paso a paso: $2\\cdot0{,}082=0{,}164$, y $0{,}164\\cdot273{,}15$ da $44{,}8$ litros.','p:3'),('Compruebo: con $273{,}15$ K y $1$ atm, un mol ocupa $22{,}4$ L, así que dos moles ocupan $44{,}8$ L.','p:4')],
 [('Es como llenar una piscina: el doble de agua necesita el doble de espacio.',None,'ana'),('Ejemplo: con $3$ mol en las mismas condiciones ocuparían $3\\cdot22{,}4=67{,}2$ L.',None,'ej'),('Error común: usar grados Celsius en vez de kelvin. Siempre se usa kelvin.',None,'err')])
# ---------------- cie-009 ecología ----------------
o=H['cie-009']['pasos']
rew('cie-009',[
 VI('Piensa en zorros y conejos','Los zorros viven de los conejos. Si los zorros mueren más rápido, para que su población no se acabe hace falta que haya más conejos disponibles. Esa es la idea que dice la fórmula.'),
 o[0],
 BR('Presas en equilibrio según la mortalidad γ',[bar('γ = 0,5','25 presas',(25,'azul')),bar('γ = 1 (se duplica)','50 presas',(25,'azul'),(25,'oro'))],None,'Con δ = 0,02: si la mortalidad sube al doble, el equilibrio de presas sube al doble.'),
 o[2],CK('La respuesta es: aumenta. γ está arriba en la fracción: si sube, el resultado sube.')],
 [('El equilibrio de presas es $\\gamma/\\delta$.','p:1'),('Con números: $\\gamma=0{,}5$ da $25$; $\\gamma=1$ da $50$. Sube.','p:2')],
 [('Piensa en zorros y conejos.','p:0'),('El equilibrio de las presas es $x^*=\\gamma/\\delta$.','p:1'),('Con $\\delta=0{,}02$: si $\\gamma=0{,}5$ da $25$, y si $\\gamma=1$ da $50$. Aumentó.','p:2'),('Tiene sentido: si los depredadores mueren más, hacen falta más presas para sostenerlos.','p:3')],
 [('Es como una panadería con clientes que se van rápido: para mantener la tienda llena necesitas que lleguen más.',None,'ana'),('Ejemplo: si $\\gamma$ se triplica, $x^*$ se triplica.',None,'ej'),('Error común: pensar que menos depredadores significa menos presas. Es al revés en este equilibrio.',None,'err')])

TB=lambda t,c,f:{'k':'tabla','titulo':t,'cols':c,'filas':f}
EJ=lambda t,si,no:{'k':'ejemplo','titulo':t,'si':si,'no':no}
# ---------------- lec-001 ----------------
o=H['lec-001']['pasos']
rew('lec-001',[
 VI('Piensa en medir una escuela','Alguien dice: «esa escuela es mala porque casi nadie saca libros de su biblioteca». Pero la gente también va a estudiar, a usar internet y a reunirse. Medir con un solo número deja por fuera cosas valiosas. Esa es la idea del texto.'),
 TB('Cómo está armado el texto',['Parte','Qué hace'],[['Las bibliotecas no solo prestan libros…','Da razones'],['Por eso…','Avisa que viene la conclusión'],['…medir solo por préstamos es engañoso','Lo que el autor cuestiona']]),
 TR('Las pistas del texto',[F('no solo prestan libros','\\text{hacen más cosas que prestar}','dato'),F('Por eso','\\text{aquí viene la conclusión}','clave'),F('engañoso','\\text{el autor critica esa forma de medir}','clave')],'«Engañoso» es una palabra de crítica: avisa qué está cuestionando el autor.'),
 CK('Cuestiona la medida (solo por préstamos). No dice que haya pocos libros, ni pocas bibliotecas, ni que los trámites digitales sean malos.')],
 [('El texto da razones: las bibliotecas hacen más que prestar libros.','p:1'),('Luego «por eso» anuncia la conclusión: medir solo por préstamos es engañoso.','p:2')],
 [('Primero, una idea sencilla: no se puede medir algo valioso con un solo número.','p:0'),('El texto empieza con razones: refugio, trámites y encuentro.','p:1'),('«Por eso» avisa que viene la conclusión.','p:1','por'),('Y la conclusión critica medir el valor solo por préstamos. «Engañoso» es la pista de que lo cuestiona.','p:2')],
 [('Es como medir a una persona solo por su nota de matemáticas: se pierde todo lo demás.',None,'ana'),('Ejemplo: un parque no se mide solo por cuántos entran, sino por lo que hacen ahí.',None,'ej'),('Error común: elegir la opción que repite palabras del texto, como «trámites digitales», sin preguntar qué se cuestiona.',None,'err')])
# ---------------- lec-002 ----------------
o=H['lec-002']['pasos']
rew('lec-002',[
 VI('¿Llovió y se jugó?','Lo normal es que con lluvia el partido se cancele. Pero aquí se jugó: pasó lo contrario de lo esperado. Cuando dos ideas chocan así, se une con un conector de oposición.'),
 o[0],o[1],o[2]],
 [('Las ideas chocan: llovió, pero se jugó.','p:1'),('Para ideas que chocan sirve «sin embargo».','p:2')],
 [('Pensemos qué esperábamos: si llueve, no se juega.','p:0'),('Pero se jugó. Es lo contrario de lo esperado: una oposición.','p:1'),('Conectores de oposición: «sin embargo», «pero», «aunque». Los otros sirven para consecuencia, suma o causa.','p:2')],
 [('Es como decir «hacía frío, sin embargo salimos»: la segunda parte contradice lo esperado.',None,'ana'),('Ejemplo: «Estudió mucho; sin embargo, no aprobó».',None,'ej'),('Error común: elegir «por lo tanto», que une una causa con su resultado esperado.',None,'err')])
# ---------------- lec-003 ----------------
o=H['lec-003']['pasos']
rew('lec-003',[
 VI('Piensa en una regla del colegio','«Todos los que entregaron el proyecto aprobaron». Camila no aprobó. Si hubiera entregado, habría aprobado. Entonces no pudo haber entregado.'),
 o[0],
 TB('Prueba las dos posibilidades',['Si Camila…','Entonces…','¿Cuadra?'],[['entregó','aprobó','No: ella no aprobó'],['*no entregó','no pasa nada','*Sí, es la única que cuadra']]),
 o[2],CK('Camila no entregó el proyecto.')],
 [('Lo escribo como flecha: entregar lleva a aprobar. Camila no aprobó.','p:1'),('Pruebo: si hubiera entregado, habría aprobado. No cuadra. Entonces no entregó.','p:2')],
 [('La regla dice: entregar lleva a aprobar.','p:1'),('Camila no aprobó. Pruebo las dos posibilidades.','p:2'),('Si entregó, entonces aprobó, pero no aprobó: imposible.','p:2'),('Si no entregó, no hay contradicción. Es la única que cuadra.','p:2'),('Es el mismo patrón que «si llueve la calle se moja; la calle está seca, entonces no llovió».','p:3')],
 [('Es como un detective: si el culpable tuviera llaves, habría entrado. No entró, así que no tenía llaves.',None,'ana'),('Ejemplo: «Todos los peces nadan. Eso no nada, entonces no es un pez».',None,'ej'),('Error común: al revés, «aprobó, entonces entregó»; la regla no dice eso.',None,'err')])
# ---------------- ing-001 ----------------
o=H['ing-001']['pasos']
rew('ing-001',[
 VI('Un sticker para el verbo','En inglés, cuando hablas de la rutina de una sola persona (he, she, it), al verbo se le pega una -s o -es, como un sticker. Con I, you, we y they no se pega nada.'),
 o[0],o[1],o[2]],
 [('She es una sola persona y every day es rutina: presente simple con -es.','p:1'),('Con she el verbo lleva sticker: go se vuelve goes.','p:2')],
 [('Un sticker: he, she e it piden -s o -es en el verbo.','p:0'),('Miro las pistas: she es una persona, every day es rutina.','p:1'),('Mira la tabla: con I, you, we, they va go; con he, she, it va goes.','p:2')],
 [('Es como una puerta con timbre: she la abre con -es.',None,'ana'),('Ejemplo: {{He plays}}, {{she watches}}, {{it rains}}.',None,'ej'),('Error común: elegir {{go}} porque es la forma que ya conoces.',None,'err')])
# ---------------- ing-002 ----------------
o=H['ing-002']['pasos']
rew('ing-002',[
 VI('Un plan con condición','Si llueve mañana, ¿qué haces? Es un plan posible, no algo que ya pasó. En inglés se arma en dos partes: if más presente, y el resultado con will.'),
 o[0],o[1],
 EJ('Cómo suena bien y mal',['If it rains, we will stay.','If you study, you will pass.'],['If it will rain, we stay. (después de if no va will)','If it rains, we stayed. (pasado: no es plan)']),
 o[2]],
 [('La frase tiene una condición y un resultado en futuro.','p:1'),('If más presente, will más verbo: {{will stay}}.','p:2')],
 [('Es un plan posible: lo que pasaría si llueve mañana.','p:0'),('La condición va con presente: {{it rains}}. Y {{tomorrow}} avisa que es futuro.','p:1'),('El resultado se arma con {{will}} más el verbo.','p:2'),('Las otras opciones usan pasado o formas mal armadas.','p:3')],
 [('Es como decir en español «si llueve, nos quedamos»: primero la condición, luego el resultado.',None,'ana'),('Ejemplo: {{If I see her, I will say hi}}.',None,'ej'),('Error común: poner {{will}} también después de {{if}}.',None,'err')])
# ---------------- ing-003 ----------------
rew('ing-003',[
 VI('Un cartel es como un horario','Cuando lees un cartel, lo que no está escrito no cuenta como abierto. Solo vale lo que dice. Revisa día por día.'),
 TB('La semana según el cartel',['Día','¿Abre?'],[['Monday','Sí, 8 a.m.–6 p.m.'],['Tuesday','Sí, 8 a.m.–6 p.m.'],['Wednesday','Sí, 8 a.m.–6 p.m.'],['Thursday','Sí, 8 a.m.–6 p.m.'],['Friday','Sí, 8 a.m.–6 p.m.'],['Saturday','No aparece'],['*Sunday','*No aparece: no abre'],['Holidays','Cerrado']]),
 CK('Sunday no está en el horario, así que no abre.')],
 [('El cartel dice Monday–Friday: de lunes a viernes. Sunday es domingo y no aparece.','p:1')],
 [('Leo el cartel como un horario.','p:0'),('{{Monday–Friday}} es de lunes a viernes, de $8$ a $6$. Sábado y domingo no aparecen, entonces no abre.','p:1'),('{{Closed on holidays}}: tampoco abre los festivos.','p:1')],
 [('Es como el menú de un restaurante: si no está escrito, no lo tienen.',None,'ana'),('Ejemplo: «Open Mon–Sat» significa que el domingo está cerrado.',None,'ej'),('Error común: pensar que si no dice «closed» entonces está abierto.',None,'err')])
# ---------------- ing-004 ----------------
o=H['ing-004']['pasos']
rew('ing-004',[
 VI('¿Te prestan o prestas?','Los libros son de la biblioteca. Ella te los presta por dos semanas y luego los devuelves. Tú los recibes prestados: eso es borrow. Lend es cuando tú le prestas algo a otro.'),
 FL('Quién da y quién recibe',[('Biblioteca','dueña del libro'),('Tú','recibes el libro')],['\\text{ella lo presta (lend)  ·  tú lo pides prestado (borrow)}']),
 o[0],o[1]],
 [('La biblioteca presta, tú recibes: {{borrow}}.','p:1')],
 [('Los libros son de la biblioteca.','p:0'),('Ella los presta, o sea {{lend}}. Tú los recibes prestados: {{borrow}}.','p:1'),('Mira la tabla: borrow lo hace quien recibe.','p:2')],
 [('Es como pedir una pelota prestada: tú pides, borrow; el dueño presta, lend.',None,'ana'),('Ejemplo: {{Can I borrow your pen?}}',None,'ej'),('Error común: {{buy}} y {{sell}} tienen que ver con plata, y aquí no se paga.',None,'err')])
# ---------------- soc-001 ----------------
o=H['soc-001']['pasos']
rew('soc-001',[
 VI('Un derecho que no puede esperar','Imagina que te niegan una atención médica urgente. Esperar meses un juicio normal no sirve: necesitas ayuda ya. Para eso la Constitución de 1991 creó la tutela.'),
 o[0],o[1],o[2]],
 [('Antes de 1991 no había un camino directo. La Constitución de 1991 creó la tutela.','p:1'),('Sirve para pedir protección inmediata de derechos fundamentales.','p:2')],
 [('Un derecho urgente no puede esperar.','p:0'),('En 1886 no existía un mecanismo directo. En 1991 se crea la tutela.','p:1'),('Cualquier persona puede pedir al juez protección, y él decide en máximo $10$ días.','p:1'),('Sirve para derechos vulnerados, no para cambiar leyes ni elegir presidente.','p:2')],
 [('Es como llamar a urgencias: no esperas una cita, pides ayuda ya.',None,'ana'),('Ejemplo: si un colegio te niega el cupo sin razón, puedes presentar una tutela.',None,'ej'),('Error común: confundirla con cambiar leyes, que le toca al Congreso.',None,'err')])
# ---------------- soc-002 ----------------
o=H['soc-002']['pasos']
o[0]['filas'][0]=['*Legislativa','*Congreso (Senado y Cámara)','*Hace las leyes']
rew('soc-002',[
 VI('Piensa en un colegio','Alguien escribe las reglas, otro las hace cumplir y otro decide cuando hay conflictos. En Colombia el poder está dividido igual, en tres ramas, para que nadie tenga todo.'),
 o[0],o[1],o[2]],
 [('Son tres ramas. La que hace las leyes es la legislativa: el Congreso.','p:1')],
 [('Tres ramas: una escribe las reglas, otra las ejecuta, otra juzga.','p:1'),('Legislativa viene de legislar, que es hacer leyes.','p:2'),('La electoral no es una de las tres ramas: es un organismo que organiza elecciones.','p:2')],
 [('Es como un partido: uno escribe el reglamento, otro dirige el juego y otro es el árbitro.',None,'ana'),('Ejemplo: el Congreso aprueba una ley, el presidente la aplica y un juez resuelve si alguien la incumple.',None,'ej'),('Error común: elegir «Ejecutiva» porque suena a quien manda.',None,'err')])
# ---------------- soc-003 ----------------
o=H['soc-003']['pasos']
rew('soc-003',[
 VI('Piensa en un testigo','Quien estuvo ahí cuenta lo que vio: es una fuente primaria. Quien lo cuenta después, leyendo otras fuentes, es una fuente secundaria.'),
 o[0],o[1],o[2]],
 [('Una carta de 1810 de un testigo es de la época: fuente primaria.','p:1')],
 [('Un testigo cuenta lo que vio.','p:0'),('Los de la izquierda son de la época. Los de la derecha se escribieron después.','p:1'),('La carta de 1810 está en el momento de los hechos. El historiador de hoy la usa como evidencia.','p:2')],
 [('Es como el video de una cámara en el partido, frente a un comentarista que lo cuenta al día siguiente.',None,'ana'),('Ejemplo: un diario de 1810 es primaria; un libro de texto de hoy es secundaria.',None,'ej'),('Error común: pensar que una opinión no sirve. Sirve como fuente aunque sea parcial.',None,'err')])
# ---------------- soc-004 ----------------
o=H['soc-004']['pasos']
rew('soc-004',[
 VI('Ordena como la historia de tu familia','Primero el abuelo, luego tu papá, luego tú. Aquí igual: se ordena por el año. Solo mira los números.'),
 o[0],o[1],o[2]],
 [('Ordeno por año: $1810$, $1886$, Frente Nacional, $1991$.','p:1')],
 [('Solo importa el orden de los años.','p:0'),('En la línea: $1810$, $1886$, $1958$ a $1974$ y $1991$.','p:1'),('Truco: primero los de $1800$ y luego los de $1900$.','p:2')],
 [('Es como los capítulos de una serie: cada uno ocurre después del anterior.',None,'ana'),('Ejemplo: $1810$ va antes que $1991$, aunque suene al revés.',None,'ej'),('Error común: dejarse llevar por la opción que empieza con la Constitución de $1991$.',None,'err')])

# =============== INGLÉS: estrategia completa ===============
GL=lambda t,fr,dice,nota=None:{'k':'glosa','titulo':t,'frase':[{'en':a,'es':b,'pron':c} for a,b,c in fr],'dice':dice,**({'nota':nota} if nota else {})}
ESC=lambda t,fr,nota=None:{'k':'escucha','titulo':t,'frases':[{'en':a,'es':b,'pron':c} for a,b,c in fr],**({'nota':nota} if nota else {})}
# --- ing-001
rew('ing-001',[
 VI('Un sticker para el verbo','En inglés, cuando hablas de la rutina de una sola persona (he, she, it), al verbo se le pega una -s o -es, como un sticker. Con I, you, we y they no se pega nada.'),
 GL('Palabra por palabra',[('She','ella','shi'),('goes','va','gous'),('to','a','tu'),('school','escuela','scúl'),('every day','todos los días','évri dei')],'Ella va a la escuela todos los días.','Toca cada palabra para oírla.'),
 TR('Las pistas de la frase',[F('She','\\text{una sola persona: he / she / it}','dato'),F('every day','\\text{rutina: presente simple}','dato'),F('go','\\text{con she: goes}','clave')],'En presente simple, a he, she e it se les agrega -s o -es al verbo.'),
 TB('Presente simple: quién lleva sticker',['Sujeto','Verbo'],[['{{I}}, {{you}}, {{we}}, {{they}}','{{go}}'],['*{{he}}, {{she}}, {{it}}','*{{goes}}  (-es)']]),
 ESC('Escúchalas y repítelas en voz alta',[('She goes to school every day.','Ella va a la escuela todos los días.','shi gous tu scúl évri dei'),('He plays soccer.','Él juega fútbol.','ji pleis sóquer'),('It rains a lot.','Llueve mucho.','it reins a lat')],'Fíjate en cómo suena la -s del final: «gous», «pleis», «reins».'),
 CK('{{She}} va con {{goes}}: es una sola persona y una rutina.')],
 [('Primero entendamos la frase: {{She goes to school every day}}. Ella va a la escuela todos los días.','p:1'),('Con {{she}}, el verbo lleva sticker: {{go}} se vuelve {{goes}}.','p:2|p:3'),('Escúchala: {{!She goes to school every day.}}','p:4'),('Repítela tú en voz alta. Opción B.','p:4')],
 [('Un sticker: he, she e it piden -s o -es en el verbo. I, you, we y they no.','p:0'),('Entendamos la frase palabra por palabra: {{she}}, ella; {{goes}}, va; {{to school}}, a la escuela; {{every day}}, todos los días.','p:1'),('Miro las pistas: {{she}} es una sola persona. {{Every day}} es una rutina.','p:2'),('Mira la tabla: con {{I}}, {{you}}, {{we}} y {{they}} va {{go}}. Con {{he}}, {{she}} e {{it}} va {{goes}}.','p:3'),('Escucha cómo suena y repítela: {{!She goes to school every day.}}','p:4')],
 [('Es como un sticker en la camiseta: solo {{he}}, {{she}} e {{it}} lo llevan.',None,'ana'),('Ejemplo: {{He plays}}, {{she watches}}, {{it rains}}.',None,'ej'),('Error común: decir {{She go}}. Suena natural en español porque acá el verbo no cambia, pero en inglés sí.',None,'err')])
# --- ing-002
rew('ing-002',[
 VI('Un plan con condición','Si llueve mañana, ¿qué haces? Es un plan posible, no algo que ya pasó. En inglés se arma en dos partes: if más presente, y el resultado con will.'),
 GL('Palabra por palabra',[('If','si','if'),('it rains','llueve','it reins'),('tomorrow','mañana','tumórrou'),('we','nosotros','uí'),('will stay','nos quedaremos','uíl stei'),('at home','en casa','at jóum')],'Si llueve mañana, nos quedaremos en casa.','Toca cada parte para oírla.'),
 TR('Las partes de la frase',[F('If it rains','\\text{condición: if + presente}','dato'),F('tomorrow','\\text{es futuro}','dato'),F('we ___ at home','\\text{resultado: will + verbo}','clave')],'Es el primer condicional: algo posible en el futuro.'),
 TB('Primer condicional',['Parte','Forma'],[['{{If}} …','presente simple: {{it rains}}'],['*Resultado','*{{will}} + verbo: {{will stay}}']]),
 EJ('Cómo suena bien y mal',['{{If it rains, we will stay.}}','{{If you study, you will pass.}}'],['{{If it will rain, we stay.}} (después de if no va will)','{{If it rains, we stayed.}} (pasado: no es plan)']),
 ESC('Escúchalas y repítelas en voz alta',[('If it rains tomorrow, we will stay at home.','Si llueve mañana, nos quedamos en casa.','if it reins tumórrou, uí uíl stei at jóum'),('If you study, you will pass.','Si estudias, vas a aprobar.','if yu státi, yu uíl pas'),('If she calls, I will answer.','Si ella llama, yo contesto.','if shi cols, ai uíl ánser')],'La palabra {{will}} suena «uíl».'),
 CK('Condición posible en futuro: {{if}} + presente, y {{will}} + verbo. Respuesta: {{will stay}}.')],
 [('Entendamos la frase: {{If it rains tomorrow, we will stay at home}}. Si llueve mañana, nos quedamos en casa.','p:1'),('La condición va con presente: {{it rains}}. Y el resultado, con {{will}} más el verbo.','p:2|p:3'),('Escúchala: {{!If it rains tomorrow, we will stay at home.}}','p:5'),('Opción B: {{will stay}}.','p:5')],
 [('Es un plan posible: lo que pasaría si llueve mañana.','p:0'),('Palabra por palabra: {{if}}, si; {{it rains}}, llueve; {{tomorrow}}, mañana; {{will stay}}, nos quedaremos.','p:1'),('Miro las partes: la condición va en presente, {{it rains}}. {{Tomorrow}} dice que es futuro.','p:2'),('El resultado se arma con {{will}} más el verbo base.','p:3'),('Así suena bien, y así suena mal: después de {{if}} no va {{will}}.','p:4'),('Escucha y repite: {{!If it rains tomorrow, we will stay at home.}}','p:5')],
 [('Es como decir en español «si llueve, nos quedamos»: primero la condición, luego el resultado.',None,'ana'),('Ejemplo: {{If I see her, I will say hi.}}',None,'ej'),('Error común: poner {{will}} también después de {{if}}.',None,'err')])
# --- ing-003
rew('ing-003',[
 VI('Un cartel es como un horario','Cuando lees un cartel, lo que no está escrito no cuenta como abierto. Solo vale lo que dice. No traduzcas todo: busca el día que te preguntan.'),
 GL('El cartel, parte por parte',[('Library','biblioteca','láibrari'),('Open','abierto','óupen'),('Monday–Friday','de lunes a viernes','mándei fráidei'),('8 a.m.–6 p.m.','de 8 de la mañana a 6 de la tarde','éit ei-em tu sics pi-em')],'Biblioteca. Abierto de lunes a viernes, de 8 de la mañana a 6 de la tarde.'),
 GL('El final del cartel',[('Closed','cerrado','clóusd'),('on','en','on'),('holidays','festivos','jólideis')],'Cerrado en festivos.'),
 TB('La semana según el cartel',['Día','¿Abre?'],[['{{Monday}}','Sí, 8 a.m.–6 p.m.'],['{{Tuesday}}','Sí, 8 a.m.–6 p.m.'],['{{Wednesday}}','Sí, 8 a.m.–6 p.m.'],['{{Thursday}}','Sí, 8 a.m.–6 p.m.'],['{{Friday}}','Sí, 8 a.m.–6 p.m.'],['{{Saturday}}','No aparece'],['*{{Sunday}}','*No aparece: no abre'],['{{Holidays}}','Cerrado']]),
 ESC('Escúchalas y repítelas en voz alta',[('Can you go on Sunday?','¿Puedes ir el domingo?','can yu gou on sándei'),('No, it is not open on Sunday.','No, no abre el domingo.','nou, it is not óupen on sándei')],'Sunday suena «sándei», no «sunday» como se lee.'),
 CK('{{Sunday}} no está en el horario, así que no abre.')],
 [('El cartel dice: {{Open Monday–Friday}}. Abierto de lunes a viernes.','p:1'),('Y {{Closed on holidays}}: cerrado en festivos.','p:2'),('{{Sunday}} es domingo y no aparece en la lista. Entonces no abre.','p:3'),('Escucha: {{!No, it is not open on Sunday.}} Opción C.','p:4')],
 [('Leo el cartel como un horario.','p:0'),('Parte por parte: {{open}}, abierto; {{Monday–Friday}}, de lunes a viernes; {{8 a.m.–6 p.m.}}, de ocho de la mañana a seis de la tarde.','p:1'),('Y al final: {{closed on holidays}}, cerrado en festivos.','p:2'),('Miro la semana. Sábado y domingo no aparecen, entonces no abre.','p:3'),('Escucha la pregunta y la respuesta: {{!Can you go on Sunday?}} {{!No, it is not open on Sunday.}}','p:4')],
 [('Es como el menú de un restaurante: si no está escrito, no lo tienen.',None,'ana'),('Ejemplo: {{Open Mon–Sat}} significa que el domingo está cerrado.',None,'ej'),('Error común: pensar que si no dice {{closed}}, entonces está abierto.',None,'err')])
# --- ing-004
rew('ing-004',[
 VI('¿Te prestan o prestas?','Los libros son de la biblioteca. Ella te los presta por dos semanas y luego los devuelves. Tú los recibes prestados: eso es borrow. Lend es cuando tú le prestas algo a otro.'),
 GL('Palabra por palabra',[('You','tú','yu'),('can','puedes','can'),('borrow','pedir prestado','bórrou'),('books','libros','buks'),('from the library','de la biblioteca','from de láibrari'),('for two weeks','por dos semanas','for tu uíks')],'Puedes pedir prestados libros de la biblioteca por dos semanas.'),
 FL('Quién da y quién recibe',[('Biblioteca','dueña del libro'),('Tú','recibes el libro')],['\\text{ella lo presta (lend)  ·  tú lo pides prestado (borrow)}']),
 TB('Los dos verbos',['Verbo','Quién lo hace'],[['*{{borrow}}','*tú: recibes prestado'],['{{lend}}','el otro: te presta, da']]),
 ESC('Escúchalas y repítelas en voz alta',[('You can borrow books for two weeks.','Puedes pedir prestados libros por dos semanas.','yu can bórrou buks for tu uíks'),('Can I borrow your pen?','¿Me prestas tu lapicero?','can ai bórrou yor pen'),('The library lends books.','La biblioteca presta libros.','de láibrari lends buks')],'{{Borrow}} suena «bórrou».'),
 CK('Tú recibes los libros de la biblioteca: {{borrow}}.')],
 [('La frase dice que puedes pedir prestados libros por dos semanas.','p:1'),('La biblioteca presta, tú recibes: {{borrow}}.','p:2|p:3'),('Escucha: {{!You can borrow books for two weeks.}} Opción A.','p:4')],
 [('Los libros son de la biblioteca.','p:0'),('Palabra por palabra: {{you can borrow}}, tú puedes pedir prestado; {{books}}, libros; {{for two weeks}}, por dos semanas.','p:1'),('Ella presta, {{lend}}. Tú recibes prestado, {{borrow}}.','p:2'),('Mira la tabla: {{borrow}} lo hace quien recibe.','p:3'),('Escucha y repite: {{!You can borrow books for two weeks.}}','p:4')],
 [('Es como pedir una pelota prestada: tú pides, {{borrow}}; el dueño presta, {{lend}}.',None,'ana'),('Ejemplo: {{Can I borrow your pen?}}',None,'ej'),('Error común: {{buy}} y {{sell}} tienen que ver con plata, y aquí no se paga.',None,'err')])
# guía ("Resolver tú") y enfoques: inglés envuelto para que se pueda escuchar
import re as _re
def _wrap(x): return _re.sub(r'"([^"À-ÿ¿¡]+)"',lambda m:'{{'+m.group(1)+'}}',x)
for k in ('ing-001','ing-002','ing-003','ing-004'):
    H[k]['guia']=json.loads(_wrap(json.dumps(H[k]['guia'],ensure_ascii=False)).replace('\\"','"')) if False else H[k]['guia']
H['ing-001']['guia'][0]['items'][0]['p']='¿Qué tipo de acción es {{every day}}?';H['ing-001']['guia'][0]['items'][1]['p']='¿Qué persona es {{She}}?'
H['ing-002']['guia'][0]['items'][1]['why']='{{If it rains}}.';H['ing-002']['guia'][0]['items'][2]['why']='{{Will stay}}.'
H['ing-003']['guia']=[{'k':'asignar','titulo':'Lee el cartel','items':[{'p':'¿Qué es?','op':['Horario de una biblioteca','Un anuncio de venta','Un menú'],'ok':0,'why':'{{Library}} es biblioteca y {{Open}} indica el horario.'},{'p':'¿Cuándo abre?','op':['De lunes a viernes, de 8 a 6','Todos los días','Solo en festivos'],'ok':0,'why':'{{Monday–Friday}}: solo entre semana.'},{'p':'¿El domingo está en la lista?','op':['No','Sí'],'ok':0,'why':'Si el día no está en el horario, está cerrado.'}]}]
H['ing-004']['guia'][0]['items'][0]['why']='{{You can ___ books from the library.}}'
E_=json.load(open('content/enfoques.json'))
def _w(o):
    if isinstance(o,str): return _re.sub(r'"([^"À-ÿ¿¡]+)"',lambda m:'{{'+m.group(1)+'}}',o)
    if isinstance(o,list): return [_w(x) for x in o]
    if isinstance(o,dict): return {a:_w(b) for a,b in o.items()}
    return o
for k in ('ing-001','ing-002','ing-003','ing-004'): E_[k]=_w(E_[k])
PAL={'ing-001':['every day','Every day','She','she','He','he','it','I','you','we','they','goes','go','is'],
 'ing-002':['will stay','would stay','If','if','it','rains','tomorrow','we','will','would','stayed','staying','stay'],
 'ing-003':['8 a.m.–6 p.m.','Closed on holidays','Monday–Friday','Sunday','Open','Library','holidays'],
 'ing-004':['lend to','buy to','borrow','lend','buy','sell']}
def _en(o,ws):
    if isinstance(o,str):
        rx=_re.compile(r'(?<![\w{])('+'|'.join(_re.escape(w) for w in sorted(ws,key=len,reverse=True))+r')(?![\w}])')
        return ''.join(x if i%2 else rx.sub(lambda m:'{{'+m.group(1)+'}}',x) for i,x in enumerate(_re.split(r'(\{\{.+?\}\})',o)))
    if isinstance(o,list): return [_en(x,ws) for x in o]
    if isinstance(o,dict): return {a:(b if a in ('tema',) else _en(b,ws)) for a,b in o.items()}
    return o
for k,ws in PAL.items(): E_[k]=_en(E_[k],ws)
json.dump(E_,open('content/enfoques.json','w'),ensure_ascii=False,indent=1)
json.dump(H,open('content/hojas.json','w'),ensure_ascii=False,indent=1);json.dump(G,open('content/guiones.json','w'),ensure_ascii=False,indent=1)
print('visual3 ok')
