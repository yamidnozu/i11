# ENCARGO — Mejorar la sección Odontología (Endodoncia)

Pedido de Yamid (24 oct 2026): "Están bien, pero hace falta conectar **todos los temas del PDF** y que estén **mejor explicados**. Revisa bien."

Fuente obligatoria: `docs/fuentes/endodoncia-clase1-3corte.txt` (2580 líneas). **Ojo: son DOS clases.**
- **Clase 1** (líneas 1–927): historia clínica, examen, pruebas, radiografía, diagnóstico pulpar y apical, formato clínico, pruebas especiales.
- **Clase 2 "patologías"** (líneas 932–2580): anatomía y funciones de la pulpa, causas, cada patología con **clínica + radiografía + tratamiento**, controles, apexogénesis y apexificación, pólipo pulpar, reabsorciones, anacoresis y profilaxis antibiótica.
  El banco actual casi no usa la Clase 2, y el profesor dijo que **el parcial es de patologías, con casos clínicos y "diagnóstico y plan de tratamiento"** (líneas 1561–1565, 2508–2519).

Reglas: solo la rama `antigravity/v1`; `git pull --rebase` antes de cada push; no tocar `main`; no hacer deploys manuales; no leer secretos; no activar `VITE_ICFES`; no tocar pagos. Trabaja **por lotes con scripts** y verifica con los tests.

---

## 1. Resumen para Yamid
- Las 30 preguntas cubren bien lo básico de la Clase 1: pulpitis, necrosis, abscesos, fístula, percusión, radiografía como ayuda.
- **Falta casi toda la Clase 2**: tratamientos, controles, reabsorciones, apexogénesis y apexificación, antibióticos, profilaxis, anatomía y causas.
- **Hay 1 respuesta mala** (odo-016, anestesia selectiva: dice lo contrario de lo que enseñó el profesor) y **2 explicaciones que contradicen al profesor** (odo-018 y odo-005).
- La "ayuda paso a paso" es igual de genérica en las 30 preguntas y en el primer paso ya dice la respuesta.
- Las respuestas siguen el orden A, B, C, D, A, B… y se pueden adivinar.

---

## 2. Mapa de las 30 preguntas (tema y calidad de 1 a 5)
Calidad: 5 = fiel a la clase y bien explicada; 3 = correcta pero le falta lo que enseñó el profesor; 1 = errónea.

| id | tema | calidad | nota |
|---|---|---|---|
| odo-001 | Pulpitis irreversible sintomática (frío >30 s, dolor nocturno) | 4 | Falta "calor aumenta, frío alivia" y la conducta (endodoncia, se puede en 1 cita). |
| odo-002 | Fibras A-delta / C | 3 | Va más allá de la clase (la clase solo dice: agudo = A-delta, sordo = C). Errata: "estoma pulpar" → "estroma". |
| odo-003 | Pulpitis reversible | 4 | Falta la regla del profe ("dolor con dulce = reversible"), la base intermedia (ionómero/Theracal) y que tras restaurar el frío **sigue positivo normal**. |
| odo-004 | Fistulografía | 4 | Quitar "exactitud matemática". Falta: cono 30–35; si el cono queda **a la mitad de la raíz** es de origen periodontal, si llega al **ápice** es periapical. |
| odo-005 | Necrosis + periodontitis apical asintomática | 3 | **Contradicción**: la explicación dice "(granuloma o quiste)". El profe: no es clasificación; solo la histología lo distingue. Falta el tratamiento: hidróxido de calcio 8–10 días, **no en una cita**. |
| odo-006 | Cicatriz de fístula (palpación dura) | 5 | Muy fiel a la clase. |
| odo-007 | Periodontitis apical por trauma oclusal | 5 | Fiel (piedra en el zapato). |
| odo-008 | Corona: frío no sirve → fricción | 4 | Agregar: dolor al calor = proceso de necrosis (según el profe). |
| odo-009 | Pulpitis irreversible asintomática por exposición | 4 | Falta: según el sangrado puede ir a terapia pulpar vital y no siempre a endodoncia. |
| odo-010 | Técnica de percusión | 3 | El punto clave del profe es "golpecito leve porque el ligamento inflamado duele mucho". La razón del distractor D no explica nada. |
| odo-011 | Absceso apical agudo (diagnóstico) | 3 | Falta TODO el manejo, que es pregunta de examen: antibiótico (amoxicilina; clindamicina si es alérgico), trismus, drenaje, no dejar abierto, algodón estéril + temporal, no teflón. |
| odo-012 | Radiografía = ayuda, no medio | 3 | Genérica. Faltan los ejemplos del profe: 2D de algo 3D, amalgama palatina que "entra" a la cámara, ápice aparente, cono "pasado" por el trabeculado, raíz extra que aparece al angular. |
| odo-013 | Necrosis + absceso apical crónico | 3 | Falta: **no se medica**; primero terapia con hidróxido de calcio y luego endodoncia; la fístula cierra en ~8 días. |
| odo-014 | Regla de Clark (SLOB) | 2 | **No está en la clase.** Reemplazar por "angular la radiografía para ver otra raíz" (líneas 906–912) o marcarla como complemento. |
| odo-015 | Prueba de cavidad | 3 | El caso del profe es un **paciente mayor**: diente oscuro por más dentina, cámara retraída, frío negativo y sin lesión. Sin anestesia; si siente, pulpa vital → base y sellar. La explicación no da esa idea. |
| odo-016 | Anestesia selectiva | **1** | **RESPUESTA EQUIVOCADA.** El profe (líneas 614–629): primero se bloquea el **dentario inferior** (una sola punción duerme toda la mandíbula). Si el dolor se quita, era abajo; si sigue, era arriba. Además se verifica labio y media lengua dormidos. La clave correcta es la **opción A**; hay que reescribir el distractor, la explicación y la hoja. |
| odo-017 | Diente fisurado / prueba de cuña | 4 | El profe usa la **cuña de madera de operatoria**, cúspide por cúspide. "Tooth Slooth" y el dolor al soltar no vienen de la clase. |
| odo-018 | Osteítis condensante | **2** | **Contradicción**: el enunciado dice "difusa y bien delimitada" y la explicación dice "circunscrita". El profe: es **radiopaca DIFUSA**; si es muy circunscrita, hay que pensar en otra patología (hipercementosis, cementoma). Falta: no desaparece con el tratamiento; si crece, sospechar otra cosa. |
| odo-019 | Dolor nocturno (decúbito) | 4 | Bien. |
| odo-020 | Técnica de la prueba de frío | 4 | Bien. Agregar la "tríada" (se quita rápido = sana; sigue = irreversible; no siente = necrosis) y la conducta: nada / endodoncia / endodoncia. Corregir la frase confusa "del diente de control antes del diente sospechoso". |
| odo-021 | Pólipo pulpar | 2 | **Error clínico**: el primer molar a los 14 años ya tiene el ápice cerrado (usar 8–9 años o el 2.º molar). Falta: diferenciar de la hiperplasia gingival (¿tiene conexión con la encía?) y el tratamiento: pulpotomía, o endodoncia + núcleo + corona si se perdió >60 %. |
| odo-022 | Absceso periapical vs periodontal | 4 | Agregar el criterio del cono de la fistulografía (mitad de la raíz vs ápice). |
| odo-023 | Alarma: diseminación (Ludwig) | 3 | Útil, pero conectarlo con lo de la clase: submandibular, sublingual, cuello, dificultad para respirar, trismus. |
| odo-024 | Redacción radiográfica ("imagen radiolúcida compatible con") | 4 | Falta: anotar **las superficies** de la caries (la grapa puede fracturar una corona con >60 % de caries, y eso tiene consecuencias legales). |
| odo-025 | Necrosis postraumática | 4 | Falta: el calendario de controles postrauma y que las secuelas pueden aparecer hasta 6 años después. |
| odo-026 | Alivio con agua fría (PIS avanzada) | 4 | Bien. |
| odo-027 | Escala de Miller | 2 | **No está en la clase.** Lo que dijo el profe: la movilidad indica trauma (diente subluxado) y se interpreta junto con el sondaje. Reemplazar o marcar como complemento. |
| odo-028 | Recubrimiento directo con biocerámico | 3 | Falta: la decisión depende del sangrado, la Biodentine y los controles (15 días y 3, 6 y 12 meses con prueba de sensibilidad; si duele → conductos). |
| odo-029 | Previamente iniciado | 4 | Bien. |
| odo-030 | Previamente tratado + PA sintomática | 3 | Falta la conducta del profe: la lesión cicatriza a partir del **3.er mes** y se controla cada 3 meses; a los 6 meses con dolor o si la lesión crece → retratamiento; si hay sobreobturación → cirugía. |

Promedio aproximado: **3,4 / 5**.

---

## 3. Temas del PDF SIN cobertura (0 preguntas) o débiles

### Clase 1
| Tema (líneas) | Cobertura |
|---|---|
| Motivo de consulta: lista de causas (dolor, sensibilidad, inflamación, cambio de color, fractura, trauma, fístula, hallazgo radiográfico, tratamiento previo) (7–11) | **0** |
| Problema actual: 8 datos (inicio, localización, intensidad 0–10, duración, frecuencia, desencadenantes, alivio, espontaneidad) + nocturno (13–42) | **0** directa (solo el nocturno, en 019) |
| "Dolor con dulce = pulpitis reversible" (312–314) | **0** |
| Por qué se buscan fístulas extra **e** intraorales (el absceso drena afuera o adentro) (64–92) | **0** |
| Tríada de la prueba de frío + conducta + comparar con un diente sano (126–143, 104) | débil |
| Prueba de calor: ya casi no se hace; vaselina; barra de gutapercha; +5 °C necrosa; dolor al calor = necrosis en curso (164–178, 2415–2422) | **0** |
| Prueba eléctrica: solo mide la respuesta sensorial, no el estado del tejido; vitalómetro, electrodo, gancho labial (180–187) | **0** |
| Movilidad y evaluación periodontal: sondaje, sangrado, bolsas, ubicación de la fístula; pulpar vs periodontal vs combinado (224–237, 851–855) | débil (027 es de Miller, fuera de la clase) |
| Qué mirar en la radiografía: raíces, conductos, LPD, lámina dura, reabsorción; periapical ≠ periodontal (239–247, 517–519) | **0** |
| Radiografía inicial obligatoria: dilaceración, curvatura, conducto ya tratado, **lima fracturada** (responsabilidad legal) (498–508) | **0** |
| Lesión periapical con medidas (tanto por tanto); radiopacidades (osteítis, cementosis por estadios) (508–516) | **0** |
| "Pulpa sana" aunque tenga una restauración que no afecta (1195–1213) | **0** |
| Formato clínico / protocolo: tablas (datos, motivo, hallazgos clínicos y radiográficos, pruebas pulpares —frío, calor, eléctrica, estimulación directa— y periapicales —percusión, palpación, presión—, remoción de caries, cavidad, especiales, diagnóstico, pronóstico, plan, aprobación, tabla de conductometría/lima/punto de referencia, desobturación, técnica, irrigante, cemento, restauración) (411–704) | débil (solo 024) |
| Error del ejemplo: "sin fractura visible" + "exposición pulpar" = contradicción (459–465) | **0** (ideal para una pregunta de "encuentra el error") |
| Consentimiento informado (riesgos: dolor, inflamación, infección, perforación, instrumento fracturado) (690–697) | **0** |
| Anestesia intrapulpar ("directa") y técnica del bloqueo del dentario inferior (bisel hacia hueso, aspirar, depositar lento) (646–672) | **0** |
| Fístula activa vs inactiva (745–764) | débil |
| Prueba de oclusión (865–871) | ok (007) |

### Clase 2 (patologías) — la más importante para el parcial
| Tema (líneas) | Cobertura |
|---|---|
| Anatomía pulpar: cameral vs radicular; capas (odontoblastos, zona pobre, zona rica, núcleo) (953–981) | **0** |
| Funciones de la pulpa: formativa, nutritiva, sensitiva, defensiva, inductora (983–1001) | **0** |
| Tejidos periapicales (foramen, ligamento, cemento, hueso) y sus funciones (1003–1040) | **0** |
| Causas: bacteriana, traumática, iatrogénica (refrigeración, fresa sin corte, ortodoncia con fuerza excesiva; químicos y físicos según el profe) y **anacoresis** (1041–1155, 2424–2442) | **0** |
| Controles postrauma: el día del golpe, 15 días, 1 mes, 3, 6 y 12 meses y cada año hasta 6 años; clínico + radiográfico (1134–1150) | **0** |
| Clasificación AAE 2019 (el profe menciona una nueva de 2026) (1157–1172) | débil |
| Pulpa normal: frío 1–2 s, pruebas periapicales negativas, sin tratamiento (1174–1220) | débil |
| PIS: >30 s, calor ↑ frío ↓, decúbito, dolor difuso que luego se localiza, LPD ensanchado en fase avanzada; tratamiento: endodoncia, pulpotomía de urgencia, extracción como última opción (1292–1377, 2102–2112) | diagnóstico sí; **tratamiento 0** |
| **Edad / ápice abierto: apexogénesis (pulpotomía, pulpa vital) vs apexificación (pulpa muerta, medicamento: hidróxido de calcio/MTA/Biodentine)**; hemostasia con suero frío 5 min; hidróxido duro; puente dentinario; no usar eugenolato (2114–2160) | **0** |
| Pólipo pulpar: diferencial con la hiperplasia gingival; tratamiento según el tejido remanente (2162–2217) | débil (021, con un error) |
| Necrosis: gris/café-amarillento, pérdida de brillo, todas las pruebas negativas; tratamiento (1418–1459) | ok (025) |
| Previamente tratado / iniciado: retratamiento; **sobreobturación = cirugía**; controles; cicatriza desde el 3.er mes; cono a ~0,5 mm (1461–1621) | **conducta 0** |
| PA sintomática: causas (necrosis, conducto infectado, sobreobturación, oclusión) (1479–1539) | débil |
| PA asintomática: cuándo pedir tomografía; **imagen en "J" invertida = posible fractura radicular** (1623–1675) | **0** |
| Lesión periapical: **no obturar en una cita**; hidróxido de calcio 8–10 días (la PI sí se puede en 1 cita); cirugía apical si la lesión crece; exodoncia como última opción (1679–1710) | **0** |
| AAA: manejo completo (antibiótico solo cuando se necesita; amoxicilina / clindamicina si es alérgico; trismus; drenaje por conducto o incisión; **nunca dejar abierto**; algodón estéril + temporal, no teflón; volver a citar) (1712–1818) | **0** (011 solo diagnostica) |
| AAC: no medicar; hidróxido de calcio y luego endodoncia; la fístula cierra sola en ~8 días; vehículos (anestesia, suero, agua destilada); léntulo o lima en sentido **antihorario**; punta de papel (1820–1901) | **0** |
| Granuloma/quiste **no es clasificación**; solo la histología lo define (1903–1918) | **0** (y 005 lo contradice) |
| Osteítis condensante: radiopaca difusa; no se va; si crece, otra patología; diferencial con hipercementosis, cementoma (3 estadios) y odontoma; si el frío es positivo en un cementoma → no se hace endodoncia (1920–2040) | débil (018 contradice) |
| Relación entre diagnóstico pulpar y periapical: es una secuencia, pero no siempre van juntos (2042–2067) | **0** |
| Salvar el diente: alargamiento coronal vs implante (2068–2088) | **0** |
| **Reabsorción radicular**: fisiológica vs patológica; **interna** (forma de balón, origen pulpar, hidróxido de calcio pH 12,4, si es perforante → endo + cirugía); **externa** superficial (ortodoncia → retirar la causa), inflamatoria (→ endodoncia), por reemplazo (avulsión); mancha rosada; tomografía (2219–2336) | **0** |
| **Profilaxis antibiótica** (endocarditis, fiebre reumática, lupus, diabetes no controlada, problemas de aorta; 1 hora antes) (2443–2460) | **0** |

---

## 4. Problemas de forma (en las 30)
1. **Clave predecible**: las respuestas van 0,1,2,3,0,1,2,3… → **barajar las opciones al azar** en las 30 (y en las nuevas), actualizando `correcta`, `distractores` y las `o:X` del guion.
2. **Hoja genérica**: `enfoque.plan` tiene **los mismos 3 pasos** en las 30 preguntas ("Identificar los síntomas…", "Evaluar la respuesta pulpar…", "Correlacionar…"). El guion abre y cierra con las mismas frases en las 30, y el paso 3 dice "pruebas de sensibilidad y examen periapical" aun en preguntas que no son de eso.
3. **Guion nivel 1 delata la respuesta** en el 3.er mensaje en las 30. En Matemáticas el nivel 1 tiene unos 6 pasos guiados antes de dar la respuesta. Hacer lo mismo: dato → regla del profe → descartar → concluir.
4. `pasos`: solo 2 "idea" + 1 "check". Subir a 3–5 pasos con la **regla del profesor** citada en palabras sencillas.
5. `marcas.nota` repite `campo`: poner una nota útil ("esto apunta a pulpa", "esto apunta a periápice").
6. Explicaciones correctas pero técnicas y **sin tratamiento**. Cada caso debe cerrar con: diagnóstico pulpar + diagnóstico periapical + **plan de tratamiento** + "error típico" + "frase del profe".

---

## 5. Lista de arreglos EN ORDEN
1. **Corregir odo-016** (clave → opción A: bloquear primero el dentario inferior). Reescribir el distractor de A, la explicación, las pistas, la clave del enfoque y el guion. Agregar la comprobación de labio y media lengua dormidos.
2. **Corregir odo-018** (osteítis = radiopaca **difusa**; quitar "circunscrita/bien delimitada"; agregar el diferencial y que no desaparece).
3. **Corregir odo-005** (quitar "granuloma o quiste"; agregar el hidróxido de calcio 8–10 días, no en una cita).
4. **Corregir odo-021** (edad o diente coherente con ápice abierto; diferencial con la hiperplasia gingival; tratamiento).
5. Errata en odo-002 ("estroma"); quitar "exactitud matemática" en odo-004; arreglar la frase de odo-020; mejorar el distractor D de odo-010.
6. odo-014 (Clark) y odo-027 (Miller): **reemplazarlos** por temas de la clase (radiografía angulada que muestra otra raíz; movilidad y sondaje para pulpar vs periodontal), o marcarlos `"origen":"complemento"`.
7. Enriquecer las explicaciones de 001, 003, 008, 009, 011, 012, 013, 015, 017, 022, 023, 024, 025, 028 y 030 con lo que les falta según la tabla de la sección 2 (sobre todo la **conducta/tratamiento**).
8. **Rehacer la `hoja` de las 30** (plan propio por pregunta, guion de nivel 1 con 5–7 pasos sin dar la respuesta al inicio, pasos con la regla del profe).
9. **Barajar las claves** (respuestas A/B/C/D al azar, más o menos balanceadas).
10. **Agregar unas 32 preguntas nuevas** (odo-031 a odo-062), casos clínicos con pregunta de diagnóstico **y/o plan de tratamiento**:
    - Historia clínica: motivo de consulta (1), los 8 datos del problema actual (1), dolor con dulce (1), fístula extra vs intraoral (1).
    - Pruebas: tríada del frío + conducta (1), prueba de calor y riesgo de +5 °C (1), qué mide la eléctrica (1), movilidad/sondaje pulpar vs periodontal (1), fístula activa/inactiva (1).
    - Radiografía y formato: qué evaluar y periapical vs periodontal (1), radiografía inicial y lima fracturada (1), superficies de la caries y la grapa (1), "encuentra el error" del formato (1), consentimiento informado (1), anestesia intrapulpar / técnica del dentario inferior (1).
    - Clase 2 bases: capas de la pulpa (1), funciones de la pulpa (1), tejidos periapicales (1), causas + anacoresis (1), iatrogenia por calor/fresa/ortodoncia (1), controles postrauma (1).
    - Tratamientos: PIS en ápice abierto → apexogénesis (1), necrosis en ápice abierto → apexificación (1), PA → no obturar en una cita, hidróxido 8–10 días (1), AAA manejo completo con antibiótico/drenaje/algodón (2), AAC sin medicar + hidróxido de calcio con léntulo antihorario (1), previamente tratado: control a 1, 3 y 6 meses vs retratamiento vs cirugía por sobreobturación (2), "J" invertida → tomografía/fractura (1).
    - Diferenciales: granuloma vs quiste no es diagnóstico clínico (1), osteítis vs hipercementosis/cementoma (1), reabsorción interna vs externa (1), tipos de externa (superficial/inflamatoria/reemplazo) (1), relación pulpar–periapical (1), profilaxis antibiótica (1), salvar el diente vs implante (1).
    Repartir en las unidades de `content/unidades.json` y crear **2 unidades nuevas**: `u-odo-bases` (anatomía, funciones, causas) y `u-odo-tratamientos` (tratamientos y controles, reabsorciones, profilaxis). Mover odo-016, odo-017 y odo-023 fuera de "Historia clínica" si encajan mejor en Pruebas o en Periapical.
11. Verificar: tests existentes + script que confirme que (a) ninguna hoja tiene `plan` idéntico a otra, (b) la clave está balanceada, (c) no hay distractor vacío salvo en la correcta y (d) cada tema de la sección 3 tiene ≥1 pregunta.
12. Actualizar `ANTIGRAVITY_REPORT.md` con números honestos (cuántas preguntas, qué temas, qué se corrigió). `git pull --rebase` → commit → push a `antigravity/v1` (publica solo en icfes.edevcore.com). Avisar.

---
Nota: esta auditoría se hizo el 24 oct 2026 hacia las 4:05 PM (hora de Bogotá), sobre el commit `3d94847` más los cambios sin commit que había en ese momento (`tools/balance_odontologia.py`, que balancea la longitud de las opciones y agrega competencia/afirmación). Ese script **no arregla** nada de lo de arriba: odo-016 sigue con la clave 3 (opción D), que está mal. Integra estos arreglos encima de ese trabajo, sin perderlo.
