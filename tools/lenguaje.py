import re,glob,sys
R=[
("Con porqués","Con explicación"),("Otra mirada","Con ejemplos"),("'Corto'","'Resumido'"),
("Lo esencial, rápido","Solo lo esencial"),
("Por qué cada paso y por qué no las otras","Explico cada paso y por qué las otras no"),
("Con analogías y ejemplos","Con ejemplos de la vida diaria"),
("Lo que sé","Mis datos"),
("Lo que piden","Lo que preguntan"),("Qué piden","Qué preguntan"),
("'Resolver tú'","'Hazlo tú'"),("Tú lo haces, con guía","Yo te guío, paso a paso"),
("'Entender', 'De qué trata la pregunta'","'Empezar', 'De qué trata la pregunta'"),
("Ver resuelto","Ver la solución"),("El profe lo explica","El profe la explica"),
("Te digo de qué tema es, en qué te fijas para reconocerlo y los pasos para resolverla.","Te cuento de qué tema es, en qué te fijas para reconocerlo y cómo se resuelve."),
("Si no entiendes, pasa a la explicación siguiente: cada una es más sencilla.","Si algo no te quedó claro, pasa a la siguiente explicación: cada una es más sencilla."),
("Me trabé: necesito ayuda","Necesito ayuda"),("Me rindo: ver explicación","No sé: ver la explicación"),
("Rayar a mano en la hoja","Escribir a mano en la hoja"),("Hoja de rayar","Hoja de borrador"),
("Si te trabas","Si no logras avanzar"),("Vas cerca:","Casi lo logras:"),
("Todavía no, mira otra vez.","Todavía no. Míralo de nuevo."),
("Ese orden no es: vuelve a intentarlo.","Ese orden no es correcto. Inténtalo de nuevo."),
("Eso no es lo más importante aquí. Prueba con otra parte.","Esa parte no es lo principal. Prueba con otra."),
("¿Quedó claro? ","¿Te quedó claro? "),("Sí, ya lo entendí","Sí, todo claro"),
("Primero leo el enunciado con calma.","Vamos a leer el enunciado con calma."),
("Primero leo todo el enunciado, con calma.","Vamos a leer todo el enunciado, con calma."),
("Esto es importante.","Fíjate en esto."),("Hago la cuenta","Hagamos la cuenta"),("'Sigo con esto'","'Sigamos'"),
("Ahora sí, mi plan paso a paso.","Ahora sí, vamos paso a paso."),
("Así sé por dónde empezar.","Así sabemos por dónde empezar."),
("'Error típico'","'Error común'"),("Error típico:","Error común:"),("'Contraejemplo'","'Caso contrario'"),
("Ahora sí","Ahora sí"),
]
RX=[
(r"b\('Leam?os\.'",  "b('Vamos a leer el enunciado con calma.'"),
(r"b\('Leemos\.'",   "b('Vamos a leer el enunciado con calma.'"),
(r"b\('Leemos con calma\.'","b('Vamos a leer el enunciado con calma.'"),
(r"b\('Leamos el problema\.'","b('Vamos a leer el problema con calma.'"),
(r"(?<=b\(')Piden ","Nos piden "),(r"(?<=[.!?] )Piden ","Nos piden "),
(r"(?<=b\(')Leem?os la ","Vamos a leer la "),(r"(?<=b\(')Leamos la ","Vamos a leer la "),
(r"(?<=b\(')Leem?os el ","Vamos a leer el "),(r"(?<=b\(')Leamos el ","Vamos a leer el "),
]
files=glob.glob('src/ui/*.ts')+['tools/%s.py'%x for x in ('g1','g2','g3','g4','g5','visual','visual3','enfoques','campos','make_hojas','make_ing')]
tot=0
for f in files:
    try:s=open(f,encoding='utf8').read()
    except: continue
    o=s
    for a,b in R: s=s.replace(a,b)
    for a,b in RX: s=re.sub(a,b,s)
    if s!=o: open(f,'w',encoding='utf8').write(s); tot+=1; print('ok',f)
