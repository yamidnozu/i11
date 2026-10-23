# Changelog

## Revisión Matemáticas 2018 — preguntas 35 a 41 (2026-10-22)

- Se verificaron el interés total del crédito, el margen de error de longitudes, la geometría de radios, los porcentajes de finales y el promedio de triunfos en cancha dura.
- Se añadió el bloque compartido de Grand Slam para las preguntas 38–39 y se asociaron la gráfica y las cuatro opciones gráficas de la maqueta de fútbol en la pregunta 41.
- Quedan 288 hojas revisadas y 58 borradores. TypeScript y Vitest pasan (540/540); builds normal y gated pasan.

## Revisión Matemáticas 2018 — preguntas 28 a 34 (2026-10-22)

- Se cotejaron las preguntas 28–34 con las páginas 15–18 del cuadernillo: tabla de cursos, triángulo de la escalera, baraja como tabla estructurada, octágono, simetría en el plano y modalidades de crédito.
- Se restauraron las opciones de razón trigonométrica y las cuatro tablas gráficas de la pregunta 32. Se añadió como bloque compartido el contexto y la tabla de modalidades de crédito de las preguntas 34–35.
- Se completaron siete hojas revisadas, con descartes y guiones de tres niveles. Total actualizado: 281 hojas revisadas y 65 borradores. TypeScript y Vitest pasan (540/540); builds normal y gated pasan.

## Revisión Matemáticas 2018 — preguntas 14 a 27 (2026-10-22)

- Se cotejaron las preguntas 14–27 contra las páginas 10–16 del cuadernillo y la clave oficial; se completaron explicaciones, distractores y guiones de tres niveles.
- Se asociaron gráficas/figuras en las preguntas 15, 17, 22, 23 y 26, y se reconstruyeron como tablas las preguntas 20 y 21.
- El informe y el contexto quedan en 274 hojas revisadas y 72 borradores. TypeScript y Vitest pasan (540/540); los builds normal y gated pasan.

## Revisión Matemáticas 2018 — preguntas 11 a 13 (2026-10-22)
- Se comprobó el bono sobre lotes completos en la pregunta 11, se recortaron las cuatro opciones gráficas de la pregunta 12 y se resolvió la inferencia de viajes mínimos en la pregunta 13.
- Se corrigió el formato de los pasos numerados en las preguntas 10 y 11 para que la vista los conserve legibles. Las tres hojas quedaron revisadas y sus apoyos se verificaron en la vista previa.
- El informe y el contexto quedan en 260 hojas revisadas y 86 borradores. TypeScript y Vitest pasan (540/540); los builds estándar y gated pasan.

## Revisión Matemáticas 2018 — preguntas 7 a 10 (2026-10-22)
- Se corrigió la estatura de la pregunta 8 a $3/2$ m y se limpiaron las opciones que arrastraban texto de la página siguiente.
- Se reconstruyeron los bloques compartidos: mapa y dos tablas de obesidad para las preguntas 7–8, y tabla de precios y costos para las preguntas 9–13.
- Se completaron las cuatro hojas con cálculos y descarte de alternativas. El recorte del mapa y las tablas se verificaron en `#/pregunta/`; informe y contexto quedan en 257 hojas revisadas y 89 borradores.

## Revisión Matemáticas 2018 — preguntas 4 a 6 (2026-10-22)
- Se cotejó la tabla de capacitación y se añadió como bloque compartido por las tres preguntas; se documentaron capacidades, horas y costos en overrides.
- Se corrigió y verificó la relación entre cantidad de cursos, cupos y pago total en las preguntas 4, 5 y 6. Sus hojas pedagógicas quedaron revisadas.
- El informe y el contexto quedan en 253 hojas revisadas y 93 borradores. TypeScript y Vitest pasan (540/540).

## Revisión Matemáticas 2018 — pregunta 3 (2026-10-22)
- Se cotejó la página fuente, se reconstruyó la tabla de cupos y precios en `overrides.json`, y se corrigió la opción D contaminada por la extracción del contenido siguiente.
- Se completaron explicación, distractores y hoja de tres niveles; la alternativa B se verificó con dos combinaciones viables de 140 estudiantes y costos de $5.950.000 y $5.650.000.
- El informe y el contexto quedan en 250 hojas revisadas y 96 borradores. TypeScript y Vitest pasan (540/540).

## Pipeline documental — asociación de marcos y niveles (2026-10-22)
- Se enlazaron competencia, afirmación y evidencia para las 248 preguntas de Matemáticas, Lectura Crítica, Sociales y Ciencias; los paquetes se regeneraron desde sus overrides.
- Se completó el marco semántico de esas áreas y se incorporó el modelo de lectura/uso del lenguaje de Inglés en `content/icfes/marco.json`.
- Se estructuraron los descriptores por nivel de los cinco documentos oficiales en `content/icfes/niveles_desempeno.json`, bajo el gate ICFES; `src/content/index.ts` exporta estos datos y el marco cuando `VITE_ICFES=1`.
- La guía de orientación 2026 aporta el marco semántico de Matemáticas. Se completaron los enlaces de Ciencias: 50/50 preguntas por edición.
- Se asignaron niveles pedagógicos estimados del 1 al 4 a las 248 preguntas mediante overrides persistentes; la estimación combina demanda de razonamiento y descriptores oficiales, y queda separada del nivel de desempeño oficial del estudiante.
- El informe y el contexto reflejan el avance comprobado y los pendientes documentales/licencias.

## Pipeline documental inicial (2026-10)
- Añadido `tools/pipeline/` con siete etapas persistidas, caché por hash/código/configuración y plugins para cuadernillos, marcos, guías, infografías y simulacros.
- Procesados los 38 PDFs disponibles: 1.209 páginas, 4.201 candidatos vectoriales, 222 preguntas con clave y 26 en pendientes de clave. Las transcripciones no semánticas se guardan por página en `documento.json`.
- Matemáticas: 50 preguntas; una pregunta marcada por una ambigüedad de datos; alternativas recuperadas; 49 hojas revisadas y una en borrador (mat-i038 sigue en revisión por ambigüedad de la tabla).
- Esquema ampliado con procedencias `propio` y `licenciado`; validación de overrides y exclusión de transcripciones completas del glob de preguntas de la app.
- Poppler usa `pdftotext -layout`. Vitest con ICFES: 416/416; `tsc --noEmit` y build pasan. Vite advierte que el chunk principal supera 300 kB. Ver `informe_icfes.md`.

## Pipeline documental — revisión de Sociales, Lectura y Ciencias (2026-10-22)
- Recuperadas por override las claves oficiales de 13 preguntas en cada cuadernillo de Ciencias 2025 y 2026; quedan 50 preguntas por cuadernillo, sin claves pendientes.
- Las 13 hojas revisadas de Ciencias 2026 se reutilizaron para 2025 solo después de comprobar igualdad exacta de enunciado, opciones y clave. Cada copia conserva su estado y contenido revisado.
- Cotejados visualmente los recortes de pregunta en ambas pruebas de Ciencias; se limpiaron avisos de figura ya asociada. Se mantienen pendientes las opciones gráficas que aún necesitan recorte individual y enlaces específicos al marco.
- Recuperadas literalmente las opciones de 14 preguntas de Sociales que se habían confundido con imágenes; se eliminaron sus falsos placeholders gráficos.
- Asociada la infografía de tránsito de la página 36 de Lectura Crítica a un único bloque compartido por las preguntas 42–49; corregidos números de página capturados como parte de opciones.
- El detector de símbolos ya no marca usos ordinarios de “tan”. `enriquecer` crea como máximo diez hojas por lote y reanuda sin reemplazar hojas existentes.
- El parser de cuadernillos elimina los números de página pegados al final de la última opción, preservando opciones que sí son números (verificado, por ejemplo, en `cie-i016`).
- Los recortes compartidos pueden declararse con página y rectángulo en `recorteFuente`; la etapa `figuras` reconstruye PNG desde el PDF y registra la salida, de modo que borrar `work/` y el PNG no elimina la receta.
- Validación: `npx tsc --noEmit` y `VITE_ICFES=1 npx vitest run` (442/442) pasan. El informe separa lo terminado de las revisiones pedagógicas, gráficas y de licencias aún abiertas.


## Pipeline documental — lote pedagógico de Ciencias (2026-10-22)
- Se revisaron ocho hojas (preguntas 2, 11, 12 y 17 de los cuadernillos 2025 y 2026), con razonamiento, descarte individual de distractores y comprobación del contexto.
- Para el salto bungee se cotejó la longitud natural de la banda con la distancia de caída; como aún no se estira, la transformación corresponde a energía gravitacional a cinética.
- El total sube a 83 hojas revisadas y baja a 165 borradores; las alternativas gráficas, las evidencias del marco y otras hojas aún requieren trabajo.
- Validación tras el lote: `npx tsc --noEmit` y `VITE_ICFES=1 npx vitest run` (442/442).


## Pipeline documental — segundo lote pedagógico de Ciencias (2026-10-22)
- Se revisaron preguntas de traducción del ARN, transferencia de electrones, sensibilidad a antibióticos y calor específico, con solución y descarte individual de distractores en ambos cuadernillos.
- Se comprobó que enunciado, opciones y clave coinciden entre las ediciones 2025 y 2026 antes de reutilizar las hojas.
- El acumulado queda en 91 hojas revisadas y 157 borradores; continúan pendientes las opciones gráficas, los enlaces a evidencias del marco y las hojas restantes.


## Pipeline documental — tercer lote pedagógico de Ciencias (2026-10-22)
- Se añadieron soluciones completas para la transcripción de proteínas, la velocidad del sonido en agua y aire y la presión atmosférica en altura.
- Se verificaron las hojas existentes de configuración electrónica, fuerzas, presión atmosférica y mezclas; esas cuatro ya estaban revisadas y no se reemplazaron.
- Acumulado actual: 99 hojas revisadas y 149 borradores.


## Pipeline documental — cuarto lote pedagógico de Ciencias (2026-10-22)
- Se añadieron hojas razonadas para solubilidad, clasificación de fases y controles experimentales, sin reemplazar las hojas que ya estaban revisadas.
- Se cotejaron las diferencias menores de OCR entre los cuadernillos de ambos años; la pregunta de clasificación conserva la misma observación, alternativas y clave.
- Acumulado actualizado: 105 hojas revisadas y 143 borradores.


## Pipeline documental — quinto lote pedagógico de Ciencias (2026-10-22)
- Se completaron hojas de análisis de contaminantes, herencia, ondas, manejo de residuos y acidez, con descarte individual de distractores.
- Se mantuvo como borrador la pregunta sobre memoria espacial en ratones porque su justificación depende de cotejar la figura original.
- Acumulado actualizado: 115 hojas revisadas y 133 borradores.


## Pipeline documental — sexto lote pedagógico de Ciencias (2026-10-22)
- Se cotejaron con el PDF original las gráficas de tendencia, calentamiento y electroforesis, y el esquema de trayectorias de los ratones.
- Se completaron cuatro soluciones con lectura explícita de esos apoyos, sin depender de la transcripción plana.
- Acumulado: 123 hojas revisadas y 125 borradores.


## Pipeline documental — séptimo lote pedagógico de Ciencias (2026-10-22)
- Se cotejaron figuras de red trófica, fuerzas, resistencia eléctrica, velocidad de reacción y pruebas de oxidación con el PDF fuente.
- Se completaron cinco hojas por edición con explicaciones ligadas a esas evidencias.
- Acumulado: 133 hojas revisadas y 115 borradores.


## Pipeline documental — octavo lote pedagógico de Ciencias (2026-10-22)
- Se revisaron visualmente las opciones gráficas pendientes de las ocho preguntas que aún conservaban hojas genéricas, y se escribieron soluciones y descartes a partir de los cuadernillos.
- Los dos cuadernillos de Ciencias quedan con 50/50 hojas pedagógicas revisadas cada uno. Las imágenes de opciones siguen señaladas para segmentación individual en el contenido.
- Total: 149 hojas revisadas y 99 borradores en los cinco paquetes.


## Pipeline documental — opciones gráficas de Ciencias (2026-10-22)
- Añadidas 72 recetas deterministas `recorteFuente`: cuatro alternativas por cada una de nueve preguntas en ambos cuadernillos.
- Los PNG se reconstruyen desde las páginas fuente y se referencian en `opcionesFig`; las imágenes solo pasan al build con `VITE_ICFES=1`.
- Verificación visual de los recortes terminada. Pendientes actuales: estructurar documentos antiguos, revisar simulacros, la salvedad de mat-i038, cotejo visual adicional y acreditación de dos licencias externas.

## v49 — Mapa y orientación
- `#/mapa`: lista "Quiero…" con 10 casos a un toque y ruta completa (Empieza, Aprende, Practica, Mide, Biblioteca) con conteos reales y "Estás aquí".
- Migas de pan en pantallas internas; ocultas en las pestañas principales y en modo foco.
- Práctica por materia (`#/sesion?area=…`) con accesos desde Practicar y el mapa.
- Hoy: bloque "Ir directo a…"; bienvenida enlaza al mapa. Botón de colores con icono de paleta.

## v48 — Demo de pregunta con imagen
- `content/packs/demo-imagen.json` (mat-901) + `public/img/demo-barras.png`.

## v47 — Preparación para contenido ICFES
- `origen:'icfes'` (exige `fuente`), figura `pendiente`, cita de fuente visible.
- `tools/importar_icfes.py` (preguntas, bloques, clave, unidad, `--figuras`, `b:<bloque>`).
- Plugin `icfes-gate`: `content/icfes/` solo entra con `VITE_ICFES=1`.

## v46 — Niveles de desempeño
- `content/niveles.json`, panel "Tu nivel en cada prueba"; niveles por rango oficial.

## v41–v45 — Formato cuadernillo
- Figuras (img/svg/escena/tabla), bloques compartidos, opciones A–H, `opcionesFig`.
- Modo examen: sesiones con reloj único, paleta de preguntas, hoja de respuestas, hoja de operaciones, revisión completa, historial.
- Biblioteca de contenido (`#/contenido`), `#/pregunta/<id>`.
- Paletas de color (premium = solo color).
- Pack `formato-icfes`: 12 preguntas originales con hoja/enfoque/guion completos, simulacros cuadernillo-ejemplo y cuadernillo-oficial.

## Antes
- Naturalización del español, auditoría general, contenido y explicaciones controlables por JSON, 3 niveles del profe, modo foco sin scroll, diseño plano premium.

## Correcciones destacadas
- Opciones fuera de vista en examen (modo foco → `data-libre`).
- Aviso falso de "se acabó el tiempo" (intervalos duplicados).
- Corte de niveles fuera por uno (ahora por rango).
- Paleta insertada en lugar equivocado en `main.ts`.


## Pipeline documental — Lectura completa y primer lote de Sociales (2026-10-22)
- Se completaron y cotejaron las 49 hojas de Lectura Crítica, incluidos los argumentos sobre textos, caricaturas e infografía.
- Se verificaron visualmente las páginas fuente de las caricaturas de las preguntas 13, 14, 21 y 25, y la infografía asociada a las preguntas 42–49.
- Se revisaron las primeras diez hojas de Sociales; el acumulado sube a 208 revisadas y baja a 40 borradores.
- El paquete se reconstruyó con `python tools/pipeline/run.py --doc 02_Lectura_Critica_Saber11_2026_ICFES --desde empaquetar` y el de Sociales con su documento correspondiente. Vitest con `VITE_ICFES=1`: 442/442.


## Pipeline documental — hojas pedagógicas completas (2026-10-22)
- Se completaron las 49 hojas de Sociales y la hoja de mat-i038 con razonamiento y descarte de todas las opciones.
- mat-i038 se resuelve por inclusión y exclusión bajo la suposición de que todos los clientes están cubiertos por las categorías de la tabla; se mantiene el aviso porque el enunciado no lo explicita.
- Los cinco cuadernillos estructurados quedan con 248/248 hojas y cero borradores.
- Validación de contenido: `VITE_ICFES=1 npx vitest run`, 442/442 pruebas.

## Pipeline documental — cuadernillos antiguos de 2018 (2026-10-22)
- El plugin de cuadernillos reconoce claves con los encabezados antiguos y extrae reactivos numerados `n.` con marcas explícitas de revisión.
- Se estructuraron 49 preguntas para Sociales 2018 y 49 para Matemáticas 2018; las 98 están bajo `content/icfes/`, citan la fuente y tienen clave. Se generaron 49 hojas borrador por documento, reanudando lotes de diez.
- Las 98 preguntas requieren cotejo de transcripción, opciones, figuras y vínculo al marco antes de aprobarse; Matemáticas 2018 pregunta 48 conserva el aviso de enunciado no delimitado.
- Se actualizaron el informe, el contexto y la guía del pipeline. `npx tsc --noEmit` pasó; `VITE_ICFES=1 npx vitest run`: 501/501; builds normal y con gate pasaron (se conserva el aviso de tamaño de chunk).
- La pregunta `mth-i001` se cotejó visualmente contra la página fuente y el render; se asoció el recorte vectorial de las rutas y se sustituyó su hoja genérica por una solución revisada de tres niveles. Quedan 97 hojas borrador entre ambas pruebas de 2018.
- Validación final de este lote: TypeScript pasó, Vitest gated **540/540**, y los builds estándar y gated compilaron; persiste la advertencia de chunk superior a 300 kB.


## Pipeline documental — cierre de Matemáticas 2018 (2026-10-22)
- Se completaron las hojas de las preguntas 2 y 42–49, con tabla compartida de subsidios (43–45) y figuras verificadas para 42 y 44.
- Matemáticas 2018 queda con 49/49 hojas revisadas y sin marcas `revisar`; el saldo real pasa a 49 hojas borrador, todas de Sociales 2018.
- Verificación: `npx tsc --noEmit`, `VITE_ICFES=1 npx vitest run` (540/540), build normal y gated, y reconstrucción forzada con hash idéntico `76f949eeff538a2b73122645954483e2a88d5f212b50e3cf1107c109f05fe229`.


## Pipeline documental — cierre de Sociales 2018 (2026-10-22)
- Se cotejaron y revisaron las 49 preguntas y sus hojas pedagógicas de tres niveles; cada una tiene explicación, enfoque, descarte de todas las opciones incorrectas y cita completa.
- Se reparó el mapeo de la pregunta 4 y se reconstruyó la lista de la 25; se recortaron y asociaron las caricaturas originales de la 16.
- Los siete cuadernillos estructurados quedan con 346 hojas revisadas y cero borradores. Validación: TypeScript, Vitest gated 540/540, builds estándar y gated; reconstrucción forzada idéntica (`a813698cbce1e152fa011fdc4362cd93edd26a99a63f6cd6caa9b0d0039fe92`).


## Pipeline documental — auditoría de simulacros (2026-10-22)
- Los siete simulacros y unidades quedaron vinculados a todas las preguntas de cada cuadernillo, con IDs únicos y área coincidente.
- Se restauraron las 13 preguntas con clave por override que faltaban en cada simulacro de Ciencias; ambos ahora cubren 50 preguntas.
- La duración visible es una estimación de práctica de un minuto por pregunta, no tiempo oficial.
- Se comprobó que cada unidad conserva sus preguntas completas sin marcar el simulacro como `unidad.sim` (ese campo reserva el enlace para laboratorios).
- Se forzó la reconstrucción de mpaquetar para los siete cuadernillos; cada salida conservó su SHA-256.


## Pipeline documental — Inglés y cuadernillo mixto (2026-10-22)
- Añadidos los plugins `ingles` y `mixto2014`, configurados para los tres cuadernillos de Inglés y el cuadernillo de 2014.
- Inglés: 150 posiciones con clave, numeración correlativa única y dos secciones de 25 por documento. Cuadernillo 2014: 121 preguntas con clave en cinco áreas; cuatro posiciones `N/A` quedan excluidas de la selección múltiple.
- Se generaron 271 hojas borrador mediante lotes reanudables de diez. Todas esas preguntas conservan `revisar`; no se presentan como aprobadas.
- Asociadas las 98 preguntas de Matemáticas y Sociales 2018 con competencia, afirmación y evidencia del marco mediante overrides persistentes.
- La validación preserva paquetes multisección y las transcripciones `documento.json` existentes. Vitest gated: 811/811; TypeScript y builds normal/gated pasan.
- Reconstrucción completa desde los PDFs, tras apartar artefactos `work/<doc>` y paquetes generados; las seis salidas de Inglés, 2014, Matemáticas 2018 y Sociales 2018 conservaron sus SHA-256.
