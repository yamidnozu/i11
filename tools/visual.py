"""Pasos visuales (traducir / tanteo / puntos). Se ejecuta al final de build_content.py sobre hojas.json y guiones.json."""
import json,re
H=json.load(open('content/hojas.json'));G=json.load(open('content/guiones.json'))
def shift(id,k):
    for n in G[id]:
        for b in G[id][n]:
            a=b.get('a')
            if a: b['a']=re.sub(r'p:(\d+)',lambda m:'p:%d'%(int(m.group(1))+(1 if int(m.group(1))>=k else 0)),a)
def insertar(id,k,paso,beats):
    """beats: {nivel: (indice_en_guion, beat)}"""
    shift(id,k); H[id]['pasos'].insert(k,paso)
    for n,(i,b) in beats.items(): G[id][n].insert(i,b)
def beat(t,a=None): d={'t':t}; a and d.__setitem__('a',a); return d
def cambia(id,n,i,t,a=None):
    G[id][n][i]['t']=t
    if a is not None: G[id][n][i]['a']=a

# mat-001 taxi: de la frase al símbolo
insertar('mat-001',0,{'k':'traducir','titulo':'Pasa cada frase a matemáticas','filas':[
 {'dice':'$4.000 de arranque','escribo':'4.000','rol':'dato'},
 {'dice':'$1.000 por cada kilómetro','escribo':'1.000\\cdot k','rol':'dato'},
 {'dice':'recorrido de 7 km','escribo':'k=7','rol':'dato'},
 {'dice':'¿Cuánto cuesta?','escribo':'C=\\ ?','rol':'pide'}],
 'nota':'Lo fijo se suma una sola vez. Lo que dice «por cada» se multiplica por la cantidad.'},
 {'1':(2,beat('Paso cada frase a matemáticas: el arranque es $4.000$, cada kilómetro es $1.000\\cdot k$, y $k$ vale $7$.','p:0')),
  '2':(5,beat('Paso cada frase a matemáticas: arranque $4.000$; «por cada kilómetro» es $1.000\\cdot k$; y $k=7$.','p:0'))})
insertar('mat-001',0,{'k':'tabla','titulo':'Prueba con pocos kilómetros','cols':['Kilómetros','Cuánto marca el taxi'],'filas':[['0','4.000'],['1','4.000 + 1.000 = 5.000'],['2','4.000 + 2·1.000 = 6.000'],['3','4.000 + 3·1.000 = 7.000'],['7','4.000 + 7·1.000 = 11.000']]},
 {'1':(2,beat('Pruebo con pocos kilómetros. Con cero ya marca $4.000$. Cada kilómetro que se agrega suma $1.000$. Con $7$ kilómetros son $11.000$.','p:0')),
  '2':(5,beat('Pruebo con pocos kilómetros. Con $0$ marca $4.000$; con $1$, $5.000$; con $2$, $6.000$. Cada kilómetro suma $1.000$.','p:0'))})
# mat-002: desde cero — qué es cortar el eje, de dónde sale la regla de los dos números, y cómo se llega a x=1 y x=3
G2=G['mat-002']
H['mat-002']['pasos']=[
 {'k':'grafica','titulo':'Mira qué te piden','coef':[1,-4,3],'x':[-0.5,4.5],'puntos':[{'x':1,'y':0,'l':'x = ?'},{'x':3,'y':0,'l':'x = ?'}],'nota':'«Corta el eje x» es tocar la línea horizontal. En esos dos puntos la altura (y) vale 0. Buscamos los valores de x.'},
 {'k':'calc','titulo':'Altura cero: igualo a cero','lineas':['f(x)=0','x^2-4x+3=0'],'nota':'Como en esos puntos la altura es 0, igualo la función a 0.'},
 {'k':'calc','titulo':'¿De dónde sale? De multiplicar dos paréntesis','lineas':['(x+m)(x+n)','=x^2+mx+nx+m\\cdot n','=x^2+(m+n)x+m\\cdot n'],'nota':'m y n son dos números secretos. Multiplicar los paréntesis da esa forma; nosotros vamos al revés.'},
 {'k':'traducir','titulo':'Compara con tu ecuación','filas':[{'dice':'el número que acompaña a $x$: $-4$','escribo':'m+n=-4','rol':'dato'},{'dice':'el número solo: $3$','escribo':'m\\cdot n=3','rol':'dato'}],'nota':'Por eso se buscan dos números que sumen −4 y multipliquen 3.'},
 {'k':'tanteo','titulo':'Busca los dos números','busco':'Busco dos números que multipliquen 3 y sumen −4.','cols':['Pareja','Multiplican','Suman'],'filas':[
   {'a':'$1$ y $3$','b':'$1\\cdot3=3$','c':'$1+3=4$','ok':False},
   {'a':'$-1$ y $-3$','b':'$(-1)(-3)=3$','c':'$-1-3=-4$','ok':True}],
  'nota':'Primero listo las parejas que multiplican 3 (solo hay dos). De ésas, la que suma −4 es la que sirve.'},
 {'k':'calc','titulo':'Arma los paréntesis con esos números','lineas':['(x+m)(x+n)=0','(x+(-1))(x+(-3))=0','(x-1)(x-3)=0'],'nota':'x + (−1) se escribe x − 1, y x + (−3) se escribe x − 3.'},
 {'k':'calc','titulo':'Un producto da 0 si uno de los dos es 0','lineas':['x-1=0\\ \\Rightarrow\\ x=1','x-3=0\\ \\Rightarrow\\ x=3'],'nota':'¿Qué número menos 1 da 0? El 1. ¿Y menos 3? El 3.'},
 {'k':'grafica','titulo':'Comprueba en la gráfica','coef':[1,-4,3],'x':[-0.5,4.5],'puntos':[{'x':1,'y':0,'l':'x = 1'},{'x':3,'y':0,'l':'x = 3'}],'nota':'La curva toca el eje justo en 1 y en 3.'},
 {'k':'calc','titulo':'Verifica reemplazando','lineas':['f(1)=1-4+3=0','f(3)=9-12+3=0'],'nota':'Si al reemplazar da 0, es un punto donde corta.'},
 {'k':'check','texto':'Los cortes con el eje x son x = 1 y x = 3.'}]
P=beat
G2['1']=[G2['1'][0],G2['1'][1],
 P('Cortar el eje $x$ es tocar la línea horizontal. Todavía no sabemos cuánto vale $x$ en esos dos puntos.','p:0'),
 P('En esos puntos la altura es cero. Entonces igualo la función a cero: $x^2-4x+3=0$.','p:1'),
 P('Esta ecuación sale de multiplicar dos paréntesis. Si multiplico $(x+m)(x+n)$, queda $x^2+(m+n)x+m\\cdot n$.','p:2'),
 P('Comparo con la mía: lo que acompaña a la $x$ es $-4$, así que $m+n=-4$. El número solo es $3$, así que $m\\cdot n=3$.','p:3'),
 P('Busco dos números que multipliquen $3$ y sumen $-4$. Pruebo $1$ y $3$: suman $4$, no sirve. Pruebo $-1$ y $-3$: multiplican $3$ y suman $-4$. Sirven.','p:4'),
 P('Con $-1$ y $-3$ armo los paréntesis: $(x-1)(x-3)=0$.','p:5'),
 P('Un producto da cero solo si uno de los dos es cero. Entonces $x=1$ o $x=3$.','p:6'),
 P('Se confirma en la gráfica: la curva toca el eje en $1$ y en $3$. Opción B.','p:7|o:B:ok')]
G2['2']=G2['2'][:3]+G2['1'][2:9]+[P('Lo confirmo en la gráfica: la curva toca el eje en $1$ y en $3$.','p:7'),P('Verifico: $f(1)=1-4+3=0$ y $f(3)=9-12+3=0$.','p:8')]+G2['2'][7:]
for b in G2['3']:
    if b.get('a')=='p:4': b['a']='p:9'
# mat-003: dibujar y contar
H['mat-003']['pasos'][1]={'k':'puntos','titulo':'Dibuja la bolsa y cuenta','grupos':[{'n':3,'l':'rojas (las que quiero)','c':'rojo'},{'n':5,'l':'azules','c':'azul'}],
 'lineas':['\\text{totales}=3+5=8','P(\\text{roja})=\\frac{3}{8}'],'nota':'Abajo va el total de fichas (8), no solo las azules.'}
# mat-006: por qué 1,2 y 0,8
insertar('mat-006',0,{'k':'traducir','titulo':'Pasa cada cambio a una multiplicación','filas':[
 {'dice':'sube $20\\%$','escribo':'100\\%+20\\%=120\\%=1{,}2\\ \\Rightarrow\\ \\times1{,}2','rol':'dato'},
 {'dice':'baja $20\\%$','escribo':'100\\%-20\\%=80\\%=0{,}8\\ \\Rightarrow\\ \\times0{,}8','rol':'dato'}],
 'nota':'El precio actual siempre es el 100 %. Subir o bajar es quedarse con más o menos de ese 100 %.'},
 {'1':(2,beat('Pasa cada cambio a una multiplicación: subir $20\\%$ es quedarse con el $120\\%$, o sea por $1{,}2$. Bajar $20\\%$ es quedarse con el $80\\%$, por $0{,}8$.','p:0')),
  '2':(5,beat('Primero traduzco: subir $20\\%$ es $100+20=120\\%$, o sea por $1{,}2$. Bajar $20\\%$ es $100-20=80\\%$, por $0{,}8$.','p:0'))})

# ---------- segunda tanda: ciencias, estadística, dados, inglés ----------
def auto(id,k,paso,t1=None,t2=None):
    shift(id,k); H[id]['pasos'].insert(k,paso)
    for n,t in (('1',t1),('2',t2)):
        if not t: continue
        bs=G[id][n]; j=next((x for x,b in enumerate(bs) if re.search(r'p:%d(?!\d)'%(k+1),b.get('a') or '')),None)
        if j is None: j=next((x for x,b in enumerate(bs) if 'o:' in (b.get('a') or '')),len(bs))
        bs.insert(j,beat(t,'p:%d'%k))
def retext(id,n,sub,t):
    for b in G[id][n]:
        if sub in (b.get('a') or '') and b['t']: b['t']=t; return
    raise SystemExit('retext '+id+n+sub)
TR=lambda t,f,nota=None:{'k':'traducir','titulo':t,'filas':f,'nota':nota} if nota else {'k':'traducir','titulo':t,'filas':f}
def F(d,e,r=None):
    x={'dice':d,'escribo':e}
    if r: x['rol']=r
    return x
# cie-001 proyectil
H['cie-001']['pasos'][2]['lineas']=['2\\theta=2\\cdot30^\\circ=60^\\circ','\\sin 60^\\circ\\approx0{,}866','R=\\frac{20^2\\cdot0{,}866}{10}','R=\\frac{400\\cdot0{,}866}{10}=\\frac{346{,}4}{10}=34{,}6\\ \\text{m}']
H['cie-001']['pasos'][2]['nota']='Primero el ángulo doble (60°), luego el seno (con calculadora), luego 20² = 400 y al final se divide entre g.'
auto('cie-001',0,TR('Pasa los datos a símbolos',[F('rapidez inicial de $20\\ \\text{m/s}$','v_0=20\\ \\text{m/s}','dato'),F('ángulo de $30°$','\\theta=30^\\circ','dato'),F('$g=10\\ \\text{m/s}^2$','g=10\\ \\text{m/s}^2','dato'),F('su alcance horizontal','R=\\ ?','pide')],'v₀ se lee «v cero»: la rapidez con que sale la pelota. θ es la letra griega theta, el ángulo.'),
 'Paso los datos a símbolos: la rapidez inicial es $v_0=20$, el ángulo $\\theta=30°$, $g=10$, y piden el alcance $R$.','Paso los datos a símbolos: $v_0=20$, $\\theta=30°$, $g=10$. Lo que no sé es el alcance, $R$.')
auto('cie-001',0,{'k':'grafica','titulo':'Mira qué te piden','coef':[-0.0166667,0.57735,0],'x':[-2,38],'puntos':[{'x':0,'y':0,'l':'sale'},{'x':34.64,'y':0,'l':'R = ?'}],'nota':'El alcance es qué tan lejos cae la pelota, medido sobre el suelo desde donde se patea.'},
 'Miremos qué piden. La pelota sale, sube, baja, y el alcance es qué tan lejos cae sobre el suelo.','Miremos qué piden. La pelota sale, sube y baja. El alcance es la distancia horizontal desde donde se patea hasta donde cae.')
# cie-002 MRUA
H['cie-002']['pasos'][0]['nota']='Como parte del reposo, v₀ = 0 y el término v₀·t desaparece.'
auto('cie-002',0,{'k':'tabla','titulo':'Por qué recorre más cada segundo','cols':['Segundo','Velocidad (3·t)','Distancia acumulada'],'filas':[['1','3 m/s','1,5 m'],['2','6 m/s','6 m'],['3','9 m/s','13,5 m'],['4','12 m/s','24 m']]},
 'Veamos qué pasa segundo a segundo. Cada segundo va más rápido, así que recorre más que el anterior. Al cuarto segundo lleva $24$ metros.','Veamos qué pasa segundo a segundo: la velocidad sube $3$ cada segundo, y la distancia acumulada va $1{,}5$, $6$, $13{,}5$ y $24$ metros. No es velocidad por tiempo, porque la velocidad cambia.')
auto('cie-002',0,TR('Pasa los datos a símbolos',[F('parte del reposo','v_0=0','dato'),F('aceleración constante de $3\\ \\text{m/s}^2$','a=3\\ \\text{m/s}^2','dato'),F('$4\\ \\text{s}$','t=4\\ \\text{s}','dato'),F('¿qué distancia recorre?','x=\\ ?','pide')],'«Parte del reposo» quiere decir que al inicio está quieto: velocidad inicial 0.'),
 'Paso los datos a símbolos: velocidad inicial cero, aceleración $3$, tiempo $4$, y piden la distancia $x$.','Paso los datos a símbolos: parte del reposo es $v_0=0$; $a=3$; $t=4$; y no sé $x$.')
# cie-003 Ohm
H['cie-003']['pasos'][0]={'k':'calc','titulo':'Despeja la corriente','lineas':['V=I\\cdot R','\\frac{V}{R}=\\frac{I\\cdot R}{R}','I=\\frac{V}{R}'],'nota':'La ley de Ohm: voltaje = corriente × resistencia. Para dejar I sola divido los dos lados entre R; a la derecha la R se cancela.'}
auto('cie-003',0,TR('Pasa los datos a símbolos',[F('resistencia de $6\\ \\Omega$','R=6\\ \\Omega','dato'),F('fuente de $12\\ \\text{V}$','V=12\\ \\text{V}','dato'),F('la corriente','I=\\ ?','pide')],'R es lo que frena, V es lo que empuja, I es lo que realmente pasa.'),
 'Paso los datos a símbolos: la resistencia $R=6$, el voltaje $V=12$, y la corriente $I$ es lo que no sé.','Paso los datos a símbolos: $R=6\\ \\Omega$, $V=12\\ \\text{V}$, y piden la corriente $I$.')
retext('cie-003','1','p:1','La ley de Ohm dice $V=I\\cdot R$. Para dejar la corriente sola divido los dos lados entre $R$ y queda $I=V/R$.')
retext('cie-003','2','p:1','La ley de Ohm: $V=I\\cdot R$. Como piden $I$, la dejo sola dividiendo entre $R$ los dos lados: $I=V/R$.')
# cie-005 genética
auto('cie-005',0,{'k':'puntos','titulo':'Qué da cada padre','grupos':[{'n':1,'l':'A (dominante)','c':'azul'},{'n':1,'l':'a (recesivo)','c':'rojo'}],'lineas':['P(A)=\\frac{1}{2}','P(a)=\\frac{1}{2}'],'nota':'Una planta Aa tiene dos letras. Al formar una semilla da una de las dos, al azar.'},
 'Una planta $Aa$ tiene dos letras. Cuando forma una semilla, da una de las dos, al azar: $A$ o $a$, mitad y mitad.','Una planta $Aa$ tiene dos letras. Al formar una semilla entrega solo una de ellas, al azar: la mitad de las veces $A$ y la mitad $a$.')
# cie-006 lentes
H['cie-006']['pasos'][2]['lineas']=['\\frac{1}{d_i}=\\frac{1}{f}-\\frac{1}{d_o}','\\frac{1}{d_i}=\\frac{1}{10}-\\frac{1}{15}','\\frac{1}{d_i}=\\frac{3}{30}-\\frac{2}{30}=\\frac{1}{30}','d_i=30\\ \\text{cm}']
H['cie-006']['pasos'][2]['nota']='Para restar fracciones busco un denominador común: 30 (10 y 15 caben en 30). Al final doy vuelta: si 1/dᵢ = 1/30, entonces dᵢ = 30.'
auto('cie-006',0,TR('Pasa los datos a símbolos',[F('lente convergente de $f=10\\ \\text{cm}$','f=10\\ \\text{cm}','dato'),F('objeto a $15\\ \\text{cm}$','d_o=15\\ \\text{cm}','dato'),F('¿cómo es la imagen?','d_i=\\ ?','pide')],'f es el foco, dₒ la distancia al objeto y dᵢ la distancia a la imagen.'),
 'Paso los datos a símbolos: el foco $f=10$, el objeto está a $d_o=15$, y la distancia de la imagen $d_i$ es lo que no sé.','Paso los datos a símbolos: $f=10$ centímetros, $d_o=15$ centímetros. Busco $d_i$, la distancia de la imagen.')
# cie-008 gases
H['cie-008']['pasos'][1]['lineas']=['V=\\frac{2\\cdot0{,}082\\cdot273{,}15}{1}','2\\cdot0{,}082=0{,}164','0{,}164\\cdot273{,}15\\approx44{,}8\\ \\text{L}']
auto('cie-008',0,TR('Pasa los datos a símbolos',[F('$2\\ \\text{mol}$','n=2\\ \\text{mol}','dato'),F('$273{,}15\\ \\text{K}$','T=273{,}15\\ \\text{K}','dato'),F('$1\\ \\text{atm}$','P=1\\ \\text{atm}','dato'),F('$R=0{,}082$','R=0{,}082','dato'),F('¿cuánto ocupan?','V=\\ ?','pide')],'n es la cantidad de gas (en moles), T la temperatura en kelvin, P la presión y V el volumen.'),
 'Paso los datos a símbolos: $n=2$, $T=273{,}15$, $P=1$, $R=0{,}082$, y piden el volumen $V$.','Paso los datos a símbolos: $n=2$ moles, $T=273{,}15$ kelvin, $P=1$ atmósfera, $R=0{,}082$. Busco $V$.')
# mat-004 estadística: comparar antes y después
H['mat-004']['pasos'][0]={'k':'tabla','titulo':'Compara antes y después','cols':['','Con el 8','Sin el 8'],'filas':[['Datos','2, 3, 3, 4, 8','2, 3, 3, 4'],['Suma','2+3+3+4+8 = 20','2+3+3+4 = 12'],['Media (suma ÷ cuántos)','20 ÷ 5 = 4','12 ÷ 4 = 3'],['Mediana (dato del centro)','3','(3+3) ÷ 2 = 3']]}
# mat-005 dados: todas las combinaciones
rows=[[str(i)]+[('*' if i+j==7 else '')+str(i+j) for j in range(1,7)] for i in range(1,7)]
auto('mat-005',0,{'k':'tabla','titulo':'Todas las combinaciones','cols':['+','1','2','3','4','5','6'],'filas':rows},
 'Hagamos la tabla con todas las sumas posibles: seis por seis, treinta y seis casillas. Las marcadas son las que dan $7$: son $6$.','Hagamos la tabla con todas las sumas: un dado en las filas y el otro en las columnas. Son $6\\times6=36$ casillas. Las marcadas dan $7$, y son $6$.')
# inglés
auto('ing-001',0,TR('Mira cada pista de la frase',[F('She','\\text{tercera persona: he / she / it}','dato'),F('every day','\\text{rutina: presente simple}','dato'),F('go','\\text{con he / she / it: goes}','clave')],'En presente simple, a he, she e it se les agrega -s o -es al verbo.'),
 'Miro cada pista: {{She}} es tercera persona, {{every day}} es una rutina, así que presente simple, y con she el verbo lleva -es.','Miro cada pista: {{She}} es tercera persona; {{every day}} es una rutina, o sea presente simple; y con {{she}} el verbo lleva -es.')
auto('ing-002',0,TR('Mira cada parte de la frase',[F('If it rains','\\text{condición: if + presente (rains)}','dato'),F('tomorrow','\\text{es futuro}','dato'),F('we ___ at home','\\text{resultado: will + verbo}','clave')],'Es el primer condicional: algo posible en el futuro.'),
 'Miro cada parte: {{if it rains}} es la condición, {{tomorrow}} es futuro, así que el resultado lleva {{will}} más el verbo.','Miro cada parte: {{if it rains}} es la condición en presente; {{tomorrow}} indica futuro; y el resultado se arma con {{will}} más el verbo.')
json.dump(H,open('content/hojas.json','w'),ensure_ascii=False,indent=1)
json.dump(G,open('content/guiones.json','w'),ensure_ascii=False,indent=1)
print('visual ok')
