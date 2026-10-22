# campo = lo que se escribe en la ficha "Mis datos"; w = etiqueta de la fila (opcional)
ADD={
 'mat-006':[m('El precio final','pide','lo que hay que hallar')],
 'soc-001':[m('sirve para','pide','la función de la tutela')],
 'soc-002':[m('la rama del poder público','clave','son tres ramas')],
 'soc-003':[m('es una fuente','pide','el tipo de fuente')],
}
for k,v in ADD.items():
    have={x['frag'] for x in H[k]['marcas']}
    H[k]['marcas']+= [x for x in v if x['frag'] not in have]
C={
'cie-001':{'20 m/s':'$v_0=20\\ \\text{m/s}$','30°':'$\\theta=30^\\circ$','g = 10 m/s²':'$g=10\\ \\text{m/s}^2$','sin aire':('Sin rozamiento: $v_x$ constante','Condición'),'alcance horizontal':'$R=\\ ?$'},
'cie-002':{'parte del reposo':'$v_0=0$','aceleración constante de 3 m/s²':'$a=3\\ \\text{m/s}^2$','4 s':'$t=4\\ \\text{s}$','¿Qué distancia recorre':'$x=\\ ?$'},
'cie-003':{'6 Ω':'$R=6\\ \\Omega$','12 V':'$V=12\\ \\text{V}$','La corriente':'$I=\\ ?$'},
'cie-004':{'C₃H₈ + O₂ → CO₂ + H₂O':('Reacción sin balancear','Reacción'),'coeficiente del O₂':'Coeficiente de $\\text{O}_2=\\ ?$'},
'cie-005':{'Aa':'Padres $Aa$','Dos plantas heterocigotas':'Cruce $Aa\\times Aa$','recesivo (aa)':'$P(aa)=\\ ?$'},
'cie-006':{'lente convergente':'Convergente: $f>0$','f = 10 cm':'$f=+10\\ \\text{cm}$','15 cm':'$d_o=15\\ \\text{cm}$','La imagen es':'$d_i=\\ ?$ y tipo de imagen'},
'cie-008':{'2 mol':'$n=2\\ \\text{mol}$','273,15 K':'$T=273{,}15\\ \\text{K}$','1 atm':'$P=1\\ \\text{atm}$','R = 0,082 atm·L/mol·K':'$R=0{,}082\\ \\text{atm·L/mol·K}$','ocupan':'$V=\\ ?$'},
'cie-009':{'mortalidad de los depredadores (γ)':'$\\gamma$ sube','γ/δ':'$x^*=\\frac{\\gamma}{\\delta}$'},
'mat-001':{'$4.000 de arranque':'Parte fija: 4.000 pesos','$1.000 por cada kilómetro':'Variable: 1.000 pesos por km','7 km':'$k=7\\ \\text{km}$','¿Cuánto cuesta':'$C(7)=\\ ?$'},
'mat-002':{'$f(x)=x^2-4x+3$':'$f(x)=x^2-4x+3$','corta el eje $x$':('$f(x)=0$','Condición')},
'mat-003':{'3 fichas rojas':'Favorables: $3$','5 azules':'Otras: $5$','sea roja':'$P(\\text{roja})=\\ ?$'},
'mat-004':{'2, 3, 3, 4, 8':'$2,\\ 3,\\ 3,\\ 4,\\ 8$','media 4 y mediana 3':'$\\bar{x}=4,\\ \\text{Me}=3$','se elimina el dato 8':'Quitar el $8$','qué ocurre':'¿Qué pasa con $\\bar{x}$ y Me?'},
'mat-005':{'dos dados':'Casos totales: $6\\cdot6=36$','suma sea 7':'$P(\\text{suma}=7)=\\ ?$'},
'mat-006':{'$100.000':'$P_0=100.000$','sube 20 %':'Sube: $\\times1{,}2$','baja 20 %':'Baja: $\\times0{,}8$ del nuevo','El precio final':'$P_f=\\ ?$'},
'lec-001':{'no solo prestan libros':('Refugio, trámites y encuentro','Razones'),'Por eso':('Viene la conclusión','Conector'),'medir su valor solo por el número de préstamos resulta engañoso':('Medir por préstamos es engañoso','Tesis'),'¿Qué cuestiona el autor?':('Buscar lo que el autor critica','Pregunta')},
'lec-002':{'Llovió toda la noche':('Lo esperable: no se juega','Idea 1'),'el partido se jugó':('Lo contrario a lo esperado','Idea 2'),'___':('Falta un conector de oposición','Falta')},
'lec-003':{'Todos los estudiantes que entregaron el proyecto aprobaron':('$\\text{entregar}\\rightarrow\\text{aprobar}$','Premisa 1'),'Camila no aprobó':('Camila: no aprobó','Premisa 2'),'Se puede concluir':('Lo que obliga el texto','Pregunta')},
'ing-003':{'Monday–Friday':('Lunes a viernes','When'),'8 a.m.–6 p.m.':('Horario: 8–18 h','Hours'),'Closed on holidays':('Festivos: cerrado','Also'),'Sunday':('¿Domingo está en la lista?','Question')},
'soc-001':{'tutela':'Mecanismo de protección rápida','Constitución de 1991':'Año 1991, art. 86','sirve para':'Función de la tutela'},
'soc-002':{'hace las leyes':'Quien hace las leyes','la rama del poder público':'Son tres ramas'},
'soc-003':{'1810':'Año 1810','un testigo de los hechos':'Vivió el hecho','para un historiador de hoy':'Quien la lee hoy no cambia el tipo','es una fuente':'¿Primaria o secundaria?'},
'soc-004':{'orden cronológico':'Del más antiguo al más reciente'},
}
for k,d in C.items():
    for mk in H[k].get('marcas',[]):
        v=d.get(mk['frag'])
        if v is None: continue
        if isinstance(v,tuple): mk['campo'],mk['w']=v
        else: mk['campo']=v
