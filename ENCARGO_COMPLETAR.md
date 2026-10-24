# Encargo de Yamid (24 oct 2026): completar TODO lo que falta en explicaciones

Trabaja sin pedir aprobación, ronda tras ronda, hasta terminar. Reglas de siempre: solo rama antigravity/v1, `git pull --rebase` antes de cada push, tsc + vitest + build deben pasar, commits pequeños por bloque. Cada push se publica solo en https://icfes.edevcore.com (en modo público SIN VITE_ICFES; el contenido ICFES sigue oculto, NO lo actives en la publicación). No toques pagos, secretos ni main.

## Diagnóstico actual (medido con script)
- 617 preguntas ICFES en content/icfes: solo 303 completas de verdad.
- 176 tienen la explicación general como "Pendiente de solución verificada" (en 175 de ellas la sección "Empezar" ya trae la idea correcta: aprovéchala).
- ~212 tienen "Pendiente" en el por qué de cada opción incorrecta y ~308 repiten la misma frase genérica en todas ("No coincide con la resolución…"); las trampas también son genéricas ("Parece posible al mirar un dato aislado").
- Peores cuadernillos: Lectura Crítica 2026 (0/49), Sociales 2021 (0/49), Matemáticas 2026 (1/50), Ciencias 2026 y 2025 (12/50). Mejores (úsalos como modelo de calidad): Sociales 2018, Matemáticas 2018 (p.ej. pregunta 10 del banano), cuadernillo 2014, Inglés.
- 216 preguntas están repetidas entre cuadernillos (~401 distintas): cuando una copia está buena y otra mala, reutiliza la buena.
- 7 preguntas con texto basura del PDF dentro de una opción (p.ej. Lectura 2026 pregunta 5). 4 marcadas "por revisar" por clave dudosa: verifícalas resolviéndolas tú.
- 43 figuras pendientes. Competencia falta en 121 y afirmación en 271.
- Ninguna ICFES tiene ejercicio guiado ("Hazlo tú" con borrador) ni gráficas/tablas en los pasos ni enlace a laboratorio. Las propias sí: úsalas como estándar.
- Banco propio: 39 de 41 completas; completa las 2 que faltan. Además el banco propio es muy pequeño (Sociales 6, Inglés 6, Lectura 8): escribe preguntas ORIGINALES nuevas (no copias del ICFES) hasta al menos 40 por área, con el flujo completo, para que la versión pública tenga simulacros que varíen. Ajusta textos engañosos: "Saber 11 completo (2 sesiones)" no debe prometer 9 horas si no hay preguntas suficientes; "Matemáticas intensivo" debe usar todas las de matemáticas.

## Qué hacer
1. Para CADA pregunta ICFES incompleta: resuélvela de verdad y escribe explicación general real, por qué es incorrecta CADA opción mala (concreto, qué error comete el alumno), trampas específicas, paso a paso (con tabla/gráfica cuando ayude), los 3 niveles del profe, competencia/afirmación. Prohibido texto de relleno o "Pendiente". Si no puedes verificar la clave, márcala y explícalo en el informe en vez de inventar.
2. Limpia el texto basura, verifica las 4 dudosas, resuelve las figuras pendientes (recórtalas del PDF o recréalas en SVG).
3. Añade ejercicio guiado y, donde aplique, enlace a laboratorio en las ICFES (empieza por las de Matemáticas y Ciencias).
4. UX celular (afecta a TODAS las preguntas): tras responder en 390x844 hoy solo aparece "¡Bien!" / "Todavía no" y la explicación queda escondida hasta "Ver la solución". Muestra de inmediato el "por qué tienta" de la opción elegida y la explicación corta, como en escritorio, sin que tape las opciones.
5. Agrega un test/script de calidad que falle si hay "Pendiente", frases repetidas en distractores o campos vacíos, y úsalo para medir el avance.
6. Anota avance y cifras en docs/EVALUACION_ALUMNO.md y al final en ANTIGRAVITY_REPORT.md (cuántas completas antes/después por cuadernillo).

---
# RONDA DE CORRECCIÓN (24 oct, 9:55 AM) — auditoría externa encontró problemas. Hazlo antes de declarar terminado.
Tu `tools/auditoria_calidad.py` solo busca frases exactas; el relleno reformulado pasa. Una revisión manual encontró:
1. **Sociales 2021 (46/49) y Sociales 2014/cfi (27):** las 3 razones de opciones malas tienen la misma estructura ("La opción X plantea «…». Pero no responde al criterio central: …"). Escríbelas de verdad, específicas por opción. Arregla palabras partidas al limpiar ("ne- gocio", "cen- tros", "compro- misos").
2. **Explicación contradice la clave:** soc-i007 (defiende A, dice "la respuesta es B") y soc-i013 (habla de D, clave C). Corrige.
3. **Dañaste preguntas que estaban bien (Ciencias):** 10 explicaciones reales cambiadas por frase de catálogo ("Explica comprender que a partir de la investigación científica…"), 11 razones genéricas ("No corresponde al fenómeno físico o químico evaluado para la opción B"), 11 razones movidas a la opción equivocada (p.ej. cna-i036, cie-i049, cfi-i001; en cfi-i001 sumas falsas "18+9+23=50%"). Recupera lo bueno con `git show f84265f:<archivo>` y mejora sin degradar.
4. Quita la muletilla "Parece razonable si se omite una pista del modelo. Pero La…" (66 razones). Pistas genéricas repetidas subieron de 116 a 215: hazlas específicas.
5. **mat-i038:** le quitaste la marca "por revisar" sin resolverla. Resuélvela de verdad o vuelve a marcarla. Revisa también las otras 3 dudosas con solución real.
6. **Fórmulas rotas** (14, p.ej. "$rac32x$" en mat-i019, "\theta" mal escapado en cie-015): arregla el escape de LaTeX.
7. **Preguntas nuevas (170):** clave y contenido bien, pero las opciones malas son absurdas (ej. "precios en cero", "Kant la aplaudiría") y la respuesta se adivina: la correcta es la más larga en 109/170 (Sociales 32/36, Lectura 31/34), D es correcta solo 1 vez, Lectura usa B en 28/34. Reescribe distractores que tienten de verdad (errores típicos de alumno), opciones de largo parecido, clave repartida A/B/C/D ~25% cada una. Arregla razones intercambiadas (mat-019, mat-040, cie-010). Agrega a las 170 el flujo completo como las propias buenas: "Empezar" con pistas y trampas, paso a paso, los 3 niveles del profe, y ejercicio guiado donde aplique.
8. **Endurece el revisor** para que falle con: razones con la misma estructura (similitud alta tras quitar citas/letras), razones que repiten la explicación, preguntas sin pistas/pasos/profe, LaTeX roto, explicación que nombra una opción distinta a la clave, sesgo de posición o de largo de la clave. Hay scripts de referencia en /workspace/aud/a1.py–a7.py (solo léelos).
Commits pequeños por bloque, git pull --rebase antes de cada push. Actualiza ANTIGRAVITY_REPORT.md con cifras honestas.
