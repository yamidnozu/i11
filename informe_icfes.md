# Informe del pipeline documental

## Lista de tareas

- [x] Leer la documentación, el esquema, los importadores/hojas y los ejemplos de referencia indicados.
- [x] Implementar etapas separadas en disco, manifiesto, configuración y caché que incluye la herramienta de texto y el código de plugin.
- [x] Implementar plugins de extracción para cuadernillos, marcos, guías, infografías/lectura con imágenes y simulacros; procesar los **38 PDFs** encontrados en `docus/`.
- [x] Extraer texto con `pdftotext -layout`, rasterizar páginas completas, guardar candidatos vectoriales y registrar las etapas en el manifiesto.
- [x] Separar preguntas sin clave detectada en `pendientes_clave.json`, sin asignarles una opción correcta inventada.
- [x] Generar unidades y simulacros para cuadernillos con preguntas y clave detectadas.
- [x] Mantener `docus/` y `work/` fuera de Git y dejar el contenido derivado en `content/icfes/`, bajo el gate de build.
- [x] Probar reconstrucción limpia de Matemáticas y caché: salida idéntica.
- [x] Ejecutar `npx tsc --noEmit`, `VITE_ICFES=1 npx vitest run` y `npm run build`.
- [x] Todas las hojas de los cinco cuadernillos tienen guion y descarte; mat-i038 conserva una salvedad porque la tabla no explicita que las categorías cubran a los 110 clientes.
- [x] Revisar ocho hojas de Ciencias (preguntas 2, 11, 12 y 17 en ambos cuadernillos) con solución y descarte individual de todas las alternativas incorrectas; el contenido coincide exactamente entre años.
- [x] Revisar otras ocho hojas (preguntas 16, 19, 20 y 22 en ambos cuadernillos), cotejando la igualdad de enunciado, opciones y clave entre años.
- [x] Revisar tres hojas más con opciones textuales y razonamiento claro (transcripción de proteínas, velocidad del sonido y presión atmosférica) en ambos cuadernillos.
- [x] Revisar las hojas de solubilidad y análisis de fases y completar el lote de tablas/control experimental; conservar las que ya estaban aprobadas.
- [x] Revisar cinco hojas de Ciencias (contaminantes, herencia, ondas, residuos y acidez) en ambas ediciones.
- [x] Cotejar con las páginas fuente cuatro gráficas y diagramas: línea de tendencia, curva de calentamiento, electroforesis y trayectorias de ratones. Completar las hojas con la evidencia observada.
- [x] Revisar la red trófica, diagramas de fuerza, gráficas de resistencia y velocidad de reacción, y pruebas de oxidación; completar cinco hojas por edición.
- [x] Revisar gráficamente los ocho casos que aún tenían hojas genéricas: modelos de partículas, enfriamiento, evidencia de insecticidas, vectores relativos, gráficas de crecimiento, energía potencial, ecosistema abierto y velocidad del sonido. 50/50 hojas de Ciencias quedan revisadas en cada año; las figuras de opciones aún requieren segmentación individual.
- [x] Cotejar visualmente las 50 preguntas de Matemáticas y su clave oficial; corregir alternativas vacías, datos/tablas y contextos compartidos. Se revisaron las 50 hojas; mat-i038 está revisada con cálculo condicional y conserva una salvedad porque la tabla no determina las intersecciones necesarias.
- [x] Restaurar las opciones textuales de las 14 preguntas de Sociales que habían quedado como placeholders; cotejar recortes de 29 preguntas por cada cuadernillo de Ciencias y asociar la infografía original de Lectura como bloque para 42–49.
- [x] Comparar cinco renders con sus páginas fuente en `#/pregunta/<id>`: cie-i001, cie-i029, cie-i047, cie-i048 y lec-i046. Las figuras se ven en el recorte ampliado; las opciones que aún no están segmentadas individualmente siguen señaladas.
- [x] Extraer y enlazar individualmente las opciones gráficas de 9 preguntas por cuadernillo de Ciencias: 36 recortes por PDF, 72 PNG en total. Cada `opcionesFig` contiene su receta `recorteFuente` para reconstruir la opción directamente del PDF.
- [x] Revisar las 49 hojas pedagógicas de Lectura Crítica con argumentos, descarte de opciones, marcas y guion de tres niveles. Cotejadas visualmente las caricaturas de las preguntas 13, 14, 21 y 25, y la infografía compartida de las preguntas 42–49.
- [x] Revisar las 49 hojas pedagógicas de Sociales, con análisis de argumentos, participación ciudadana, política pública y conflicto de intereses.
- [x] Revisar mat-i038 con cálculo condicional de inclusión y exclusión; mantener un aviso porque el enunciado no explicita que todos los clientes eligieron pizza o alguna bebida registrada.
- [x] Estructurar semánticamente los marcos disponibles de Matemáticas, Ciencias, Lectura Crítica, Sociales e Inglés en `content/icfes/marco.json`; asociar IDs de competencia/afirmación/evidencia a las 248 preguntas: Matemáticas (50/50), Lectura (49/49), Sociales (49/49) y Ciencias (50/50 por edición).
- [x] Extraer y ordenar los niveles de desempeño de los cinco PDFs en `content/icfes/niveles_desempeno.json`; el ICFES no publica una matriz que asigne directamente un nivel a cada pregunta.
- [ ] Completar la estructuración y cotejo de documentos antiguos e Inglés; 2018 Sociales y Matemáticas ya tienen estructura preliminar y hojas borrador, mientras otros documentos siguen como transcripciones por página.
- [x] Auditar claves y formato de numeración de los cuadernillos antiguos restantes. Se hallaron claves explícitas en Sociales 2018, Matemáticas 2018 y el cuadernillo general de 2014; usan numeración `1.` en vez de encabezados `Pregunta n`, y el de 2014 mezcla áreas. Se añadió un modo numerado con revisión obligatoria para los dos cuadernillos de 2018.
- [x] Añadir extracción numerada con revisión explícita y procesar Sociales y Matemáticas 2018: 49 preguntas por documento, 49 claves oficiales por documento y 49 hojas borrador por prueba. Las 98 preguntas quedan marcadas para cotejo de transcripción/figuras; una pregunta de Matemáticas tiene enunciado no delimitado y conserva un marcador de revisión en vez de contenido supuesto.
- [x] Cotejar visualmente Matemáticas 2018, pregunta 1, asociar el recorte vectorial de la figura y completar su hoja de tres niveles con clave y descartes verificados; después de este cotejo quedaban 97 borradores en las pruebas de 2018.
- [x] Cotejar visualmente Matemáticas 2018, pregunta 3; reconstruir su tabla como figura desde la página fuente, corregir el texto de la opción D contaminado por la página siguiente y documentar la comparación de costos en override y hoja revisada. Quedan 96 borradores de 2018.
- [x] Cotejar las páginas fuente de Matemáticas 2018, preguntas 4 a 6; reconstruir la tabla de capacitación como contexto compartido, comprobar costos/capacidades y completar las tres hojas de solución. Quedan 93 borradores en las pruebas de 2018.
- [x] Cotejar Matemáticas 2018, preguntas 7 a 10; asociar el recorte completo del mapa de obesidad, reconstruir sus dos tablas y la tabla compartida de precios, reparar la estatura fraccionaria de la pregunta 8 y limpiar opciones contaminadas por saltos de página. Completar las cuatro hojas y verificar sus claves en el render.
- [x] Cotejar Matemáticas 2018, preguntas 11 a 13; verificar el bono sobre lotes completos, recortar las cuatro opciones gráficas de la pregunta 12 y completar los razonamientos de la 13. Ajustar la puntuación de los pasos numerados de las preguntas 10 y 11 para que se lean correctamente en la vista.
- [x] Cotejar Matemáticas 2018, preguntas 14 a 20; resolver el cambio de área, la proporcionalidad gráfica, promedio, áreas y relaciones algebraicas; asociar la gráfica y reconstruir la tabla de publicidad.
- [x] Cotejar Matemáticas 2018, preguntas 21 a 27; verificar conteo de podios, corte triangular, cartabón, promedio y dispersión, permutaciones, gráfico circular y comparación de récords; asociar las tres figuras y reconstruir la tabla.
- [x] Cotejar Matemáticas 2018, preguntas 28 a 34; reconstruir las tablas de cursos y baraja, corregir las razones de la escalera, asociar el octágono y las cuatro tablas gráficas, resolver la reflexión y compartir el contexto de crédito.
- [x] Cotejar portada, metadatos y créditos editoriales de los dos documentos externos y completar las citas disponibles.
- [x] Recuperar las claves oficiales de 13 preguntas de Ciencias por cuadernillo mediante overrides citados; verificar las 13 hojas de 2026 contra el cuadernillo de 2025 antes de reutilizarlas.
- [ ] Confirmar derechos/licencias de SED Cartagena y del libro de preparación de 2017; los PDF no incluyen permiso de reutilización y ambos continúan bajo gate.
- [x] Crear commits locales individuales por cada uno de los 38 documentos. La implementación del pipeline/configuración y la actualización documental quedaron agrupadas en dos commits, no en commits separados por cada etapa interna.

## Resumen

- Documentos procesados: **38/38**, con sus siete etapas registradas en `docus/manifest.json`.
- Páginas: **1.209**. Candidatos vectoriales: **4.201**; son candidatos de trabajo, no todas figuras asociadas.
- Siete cuadernillos estructurados: **346 preguntas con clave, cero pendientes** (50 Matemáticas 2026, 49 Lectura 2026, 50 Ciencias por edición 2025/2026, 49 Sociales 2021, 49 Sociales 2018 y 49 Matemáticas 2018). Las 26 claves inicialmente pendientes de Ciencias se resolvieron con overrides y cita al cuadernillo oficial.
- **248/248 preguntas tienen referencias a competencia, afirmación y evidencia validadas contra los marcos.** Los niveles 1–4 son estimaciones pedagógicas asignadas por demanda de razonamiento; no son niveles oficiales ICFES por ítem. mat-i038 conserva una salvedad, aunque su hoja está revisada. Las 72 opciones gráficas ya están recortadas individualmente.
- **281 hojas revisadas y 65 borradores**. Las 248 preguntas de las cinco pruebas iniciales conservan sus hojas revisadas. En Sociales 2018 hay 49 borradores; en Matemáticas 2018 hay 16 borradores y 33 hojas revisadas (pregunta 1 y preguntas 3–34). Las demás requieren cotejar enunciados, opciones y apoyos gráficos contra el PDF. Matemáticas 2018 pregunta 48 conserva un aviso por enunciado no delimitado.
- Siete simulacros generados, todos marcados “En revisión”.
- La auditoría confirmó claves adicionales en 2014, 2018, Inglés 2021 y 2024. Inglés y el cuadernillo mixto de 2014 todavía requieren extractores específicos. Inglés repite posiciones por examen y comparte bancos de opciones; el OCR también duplica/desplaza algunos números, así que falta cotejo por página antes de mapear claves. La búsqueda en fuentes oficiales de Cartagena y del editor/autor del libro 2017 no localizó una licencia escrita; la ausencia de un resultado público no sustituye autorización del titular.
- Figuras verificadas y asociadas: 29 recortes de pregunta en cada cuadernillo de Ciencias, más la infografía compartida de Lectura Crítica para las preguntas 42–49. Las imágenes oficiales solo entran al build con `VITE_ICFES=1`.
- La app importa preguntas, marcos y niveles oficiales solo detrás de `VITE_ICFES=1`; las transcripciones completas `documento.json` no se incorporan al bundle.

## Resultados por documento

| Documento | Plugin | Páginas PDF | Preguntas válidas | Sin clave | Candidatos figura | Salida |
|---|---:|---:|---:|---:|---:|---|
| `01_Matematicas_Saber11_2026_ICFES` | cuadernillo | 35 | 50 | 0 | 80 | 1 simulacro |
| `02_Lectura_Critica_Saber11_2026_ICFES` | cuadernillo | 44 | 49 | 0 | 53 | 1 simulacro; infografía compartida en preguntas 42–49 |
| `03_Ciencias_Naturales_Saber11_2026_ICFES` | cuadernillo | 42 | 50 | 0 | 148 | 1 simulacro; 13 claves por override citado |
| `04_Ciencias_Naturales_Saber11_2025_ICFES` | cuadernillo | 42 | 50 | 0 | 148 | 1 simulacro; 13 claves por override citado |
| `05_Ingles_Saber11_2024_ICFES` | cuadernillo | 25 | 0 | 0 | 61 | 1 pág. guardadas |
| `07_Sociales_y_Ciudadanas_Saber11_2021` | cuadernillo | 30 | 49 | 0 | 143 | 1 simulacro; 14 opciones restauradas desde PDF |
| `08_Ingles_Saber11_2021` | cuadernillo | 24 | 0 | 0 | 136 | 1 pág. guardadas |
| `09_Lectura_Critica_Saber11_2018` | cuadernillo | 33 | 0 | 0 | 132 | 1 pág. guardadas |
| `10_Sociales_y_Ciudadanas_Saber11_2018` | cuadernillo | 21 | 49 | 0 | 94 | 1 simulacro; hojas borrador, revisar transcripción |
| `11_Matematicas_Saber11_2018` | cuadernillo | 28 | 49 | 0 | 108 | 1 simulacro; 33 hojas revisadas, 16 borradores |
| `14_Ingles_Saber11_2018` | cuadernillo | 21 | 0 | 0 | 74 | 1 pág. guardadas |
| `15_Cuadernillo_Saber11_2014` | cuadernillo | 40 | 0 | 0 | 44 | 1 pág. guardadas |
| `16_Guia_Orientacion_Saber11_2026_2_CalA` | guia | 73 | 0 | 0 | 450 | 1 pág. guardadas |
| `17_Guia_Orientacion_Saber11_2026_1_CalB` | guia | 73 | 0 | 0 | 447 | 1 pág. guardadas |
| `18_Guia_Orientacion_Saber11_2025_2` | guia | 61 | 0 | 0 | 417 | 1 pág. guardadas |
| `19_Guia_Orientacion_Saber11_2025_1_Nov2024` | guia | 61 | 0 | 0 | 417 | 1 pág. guardadas |
| `21_Guia_Orientacion_Saber11_2022_1` | guia | 62 | 0 | 0 | 454 | 1 pág. guardadas |
| `22_Guia_Orientacion_Saber11_2017_2` | guia | 115 | 0 | 0 | 244 | 1 pág. guardadas |
| `28_Marco_Referencia_Lectura_Critica_ICFES` | marco | 58 | 0 | 0 | 35 | 1 pág. guardadas |
| `30_Marco_Referencia_Sociales_ICFES` | marco | 49 | 0 | 0 | 28 | 1 pág. guardadas |
| `31_Marco_Referencia_Ciencias_Naturales_ICFES` | marco | 49 | 0 | 0 | 44 | 1 pág. guardadas |
| `32_Marco_Referencia_Ingles_ICFES` | marco | 18 | 0 | 0 | 27 | 1 pág. guardadas |
| `33_Niveles_Desempeno_Lectura_Critica_2025` | marco | 5 | 0 | 0 | 14 | 1 pág. guardadas |
| `34_Niveles_Desempeno_Matematicas_2025` | marco | 6 | 0 | 0 | 18 | 1 pág. guardadas |
| `35_Niveles_Desempeno_Sociales_2025` | marco | 5 | 0 | 0 | 14 | 1 pág. guardadas |
| `36_Niveles_Desempeno_Ciencias_Naturales` | marco | 5 | 0 | 0 | 19 | 1 pág. guardadas |
| `37_Niveles_Desempeno_Ingles_2025` | marco | 5 | 0 | 0 | 14 | 1 pág. guardadas |
| `38_Infografia_Generalidades_Saber11_2025` | lectura_imagenes | 1 | 0 | 0 | 9 | 1 pág. guardadas |
| `39_Infografia_Matematicas_2025` | lectura_imagenes | 1 | 0 | 0 | 7 | 1 pág. guardadas |
| `40_Infografia_Lectura_Critica_Sept2025` | lectura_imagenes | 1 | 0 | 0 | 6 | 1 pág. guardadas |
| `41_Infografia_Lectura_Critica_Mar2025` | lectura_imagenes | 1 | 0 | 0 | 6 | 1 pág. guardadas |
| `42_Infografia_Sociales_Sept2025` | lectura_imagenes | 1 | 0 | 0 | 9 | 1 pág. guardadas |
| `43_Infografia_Sociales_Ago2025` | lectura_imagenes | 1 | 0 | 0 | 9 | 1 pág. guardadas |
| `44_Infografia_Ciencias_Naturales_2025` | lectura_imagenes | 1 | 0 | 0 | 6 | 1 pág. guardadas |
| `45_Infografia_Ingles_2025` | lectura_imagenes | 1 | 0 | 0 | 9 | 1 pág. guardadas |
| `46_Manual_PLEXI_Online_PreSaber11A` | guia | 26 | 0 | 0 | 26 | 1 pág. guardadas |
| `47_Guia_Preparacion_SED_Cartagena` | guia | 3 | 0 | 0 | 3 | 1 pág. guardadas |
| `48_Libro_Pre_ICFES_Completo_6_Cuestionarios` | cuadernillo | 142 | 0 | 0 | 248 | 1 pág. guardadas |

## Validaciones

- TypeScript: `npx tsc --noEmit` pasó.
- Vitest con `VITE_ICFES=1`: **540/540 pruebas**; `npx tsc --noEmit` pasó.
- Build estándar: pasó; bundle JavaScript **599.50 kB** (gzip 203.43 kB). Build con `VITE_ICFES=1`: pasó; bundle JavaScript **2,439.62 kB** (gzip 457.38 kB), incluyendo marcos, niveles oficiales y las preguntas agregadas. El build normal excluye el material ICFES; el build gated contiene sus JSON e imágenes. Ambos avisan que el chunk supera 300 kB.
- Reconstrucción de Matemáticas tras borrar `work/01_Matematicas...` y el paquete generado: SHA-256 `90601de71edec55d67752ba6170c316b6e5823dce17ac68eb906e6717552a33f`; paquete y 50 archivos de hojas idénticos. Se preservaron overrides y 50 hojas revisadas, incluida la hoja de mat-i038 con su salvedad documentada; la reconstrucción tras completar los enlaces volvió a dar el mismo hash.
- Idempotencia: el recálculo reciente de Matemáticas ejecutó 7/7 etapas; la segunda ejecución omitió las **7/7** por caché, sin errores. Tras regenerar los cinco cuadernillos se verificó que ninguna opción terminara en folio; la respuesta numérica `cie-i016` D conservó el valor `10`.

## Límites que siguen abiertos

El pipeline procesa los documentos, pero las hojas borrador y simulacros todavía requieren revisión editorial/pedagógica. Las 248 preguntas de las cinco pruebas iniciales tienen marcos y hojas revisadas; de las 98 de Sociales y Matemáticas 2018, 33 hojas están revisadas y 65 siguen en borrador. Matemáticas 2018 preguntas 3 a 34 ya tienen tablas, figuras o contexto cotejados y asociados; la pregunta 48 conserva un enunciado no delimitado. Quedan la salvedad de mat-i038, extractores para Inglés y el cuadernillo mixto de 2014, siete simulacros en revisión y dos licencias externas sin autorización comprobada. Dos guías largas provocan avisos de estructura del PDF en PyMuPDF, aunque sus siete etapas terminan; no se reportaron fallos de etapa. El contenido ICFES permanece bajo `content/icfes/` y detrás del gate. No se hizo push; `saber11-repo.tar.gz` sigue sin agregar.
