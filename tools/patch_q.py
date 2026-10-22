
import json,glob
E={
'cie-001':r"$R=\frac{v_0^2\,\sin(2\theta)}{g}=\frac{400\cdot\sin 60^\circ}{10}\approx34{,}64\ \text{m}$.",
'cie-002':r"$x=\frac{1}{2}at^2=\frac{1}{2}\cdot3\cdot16=24\ \text{m}$.",
'cie-003':r"$I=\frac{V}{R}=\frac{12}{6}=2\ \text{A}$ (ley de Ohm).",
'cie-006':r"$\frac{1}{d_i}=\frac{1}{10}-\frac{1}{15}=\frac{1}{30}$, entonces $d_i=30\ \text{cm}$. Positiva: real e invertida ($M=-2$).",
'cie-008':r"$V=\frac{nRT}{P}=\frac{2\cdot0{,}082\cdot273{,}15}{1}\approx44{,}8\ \text{L}$.",
'cie-009':r"Presas en equilibrio $x^*=\frac{\gamma}{\delta}$: si $\gamma$ crece, $x^*$ crece. Hacen falta más presas para sostener a los depredadores.",
'mat-001':r"El costo es $C=4.000+1.000\cdot7=11.000$. Es una función lineal: parte fija + parte variable.",
'mat-002':r"$x^2-4x+3=(x-1)(x-3)=0$, así que $x=1$ y $x=3$.",
'mat-003':r"Las que sirven (las rojas) son 3 y en total hay $3+5=8$ fichas, entonces $\frac{3}{8}$.",
'mat-004':r"Con 2, 3, 3, 4: media $\bar{x}=\frac{12}{4}=3$ y mediana $\text{Me}=\frac{3+3}{2}=3$. La media es sensible al valor extremo; la mediana no.",
'mat-005':r"Hay 6 parejas que suman 7 de 36 posibles: $\frac{6}{36}=\frac{1}{6}$.",
'mat-006':r"$100.000\cdot1{,}2=120.000$; $120.000\cdot0{,}8=96.000$. Los porcentajes se aplican sobre bases distintas.",
}
OPT={'mat-002':[r"$x=-1$ y $x=-3$",r"$x=1$ y $x=3$",r"$x=0$ y $x=3$",r"$x=2$ y $x=4$"]}
for f in glob.glob('content/questions/*.json'):
    d=json.load(open(f)); ch=False
    for q in d:
        if q['id'] in E and q['explicacion']!=E[q['id']]: q['explicacion']=E[q['id']]; ch=True
        if q['id'] in OPT: q['opciones']=OPT[q['id']]; ch=True
        if q['id']=='mat-002': q['enunciado']=r"La función $f(x)=x^2-4x+3$ corta el eje $x$ en los puntos:"; ch=True
    if ch: json.dump(d,open(f,'w'),ensure_ascii=False,indent=2)
