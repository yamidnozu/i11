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
- [x] Estructurar semánticamente los marcos disponibles de Matemáticas, Ciencias, Lectura Crítica, Sociales e Inglés en `content/icfes/marco.json`; asociar IDs de competencia/afirmación/evidencia a Matemáticas (50/50), Lectura (49/49), Sociales (49/49) y Ciencias (13/50 por edición).
- [x] Extraer y ordenar los niveles de desempeño de los cinco PDFs en `content/icfes/niveles_desempeno.json`; el ICFES no publica una matriz que asigne directamente un nivel a cada pregunta.
- [ ] Estructurar preguntas de los documentos antiguos y el cuadernillo de Inglés que no contienen marcadores reconocidos; hoy se preservan sus páginas como transcripción.
- [x] Cotejar portada, metadatos y créditos editoriales de los dos documentos externos y completar las citas disponibles.
- [x] Recuperar las claves oficiales de 13 preguntas de Ciencias por cuadernillo mediante overrides citados; verificar las 13 hojas de 2026 contra el cuadernillo de 2025 antes de reutilizarlas.
- [ ] Confirmar derechos/licencias de SED Cartagena y del libro de preparación de 2017; los PDF no incluyen permiso de reutilización y ambos continúan bajo gate.
- [x] Crear commits locales individuales por cada uno de los 38 documentos. La implementación del pipeline/configuración y la actualización documental quedaron agrupadas en dos commits, no en commits separados por cada etapa interna.

## Resumen

- Documentos procesados: **38/38**, con sus siete etapas registradas en `docus/manifest.json`.
- Páginas: **1.209**. Candidatos vectoriales: **4.201**; son candidatos de trabajo, no todas figuras asociadas.
- Cinco cuadernillos estructurados: **248 preguntas con clave, cero pendientes** (50 Matemáticas, 49 Lectura Crítica, 50 Ciencias 2026, 50 Ciencias 2025 y 49 Sociales). Las 26 claves inicialmente pendientes de Ciencias se resolvieron con overrides y cita al cuadernillo oficial.
- **74 preguntas conservan evidencia pendiente de asociación específica**: 37 por cada edición de Ciencias. Matemáticas, Lectura y Sociales tienen sus 148 asociaciones enlazadas a los marcos. mat-i038 tiene una salvedad de interpretación, aunque su hoja está revisada. Las 72 opciones gráficas ya están recortadas individualmente. No son avisos ocultos ni se marcan como aprobadas.
- **248 hojas revisadas, 0 borradores**. Matemáticas 50/50 (mat-i038 explicada bajo supuesto explícito); Ciencias 50/50 por año; Lectura 49/49; Sociales 49/49. Las preguntas repetidas se cotejan entre versiones; i008 presenta diferencias menores de transcripción OCR (incluido «sustencia»), revisadas contra el mismo procedimiento, opciones y clave.
- Cinco simulacros generados, todos marcados “En revisión”.
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
| `10_Sociales_y_Ciudadanas_Saber11_2018` | cuadernillo | 21 | 0 | 0 | 94 | 1 pág. guardadas |
| `11_Matematicas_Saber11_2018` | cuadernillo | 28 | 0 | 0 | 108 | 1 pág. guardadas |
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
- Vitest con `VITE_ICFES=1`: la última ejecución pasó **442/442 pruebas**, sin avisos de contenido.
- Build estándar: pasó; bundle JavaScript **599.40 kB** (gzip 203.40 kB). Build con `VITE_ICFES=1`: pasó; bundle JavaScript **1,975.08 kB** (gzip 388.04 kB), incluyendo marcos y niveles oficiales. El build normal deja los JSON oficiales vacíos mediante el gate y no crea `dist/icfes/`; el build gated contiene las imágenes oficiales. Ambos avisan que el chunk supera 300 kB.
- Reconstrucción de Matemáticas tras borrar `work/01_Matematicas...` y el paquete generado: SHA-256 `0b558683429201827e426eba779fd9c39e49e3111bc85cdbf20d510da65fc596`; paquete y 50 archivos de hojas idénticos. Se preservaron overrides y hojas, incluida la hoja revisada mat-i038 con su salvedad documentada.
- Idempotencia: el recálculo terminó 266/266 etapas; la segunda ejecución omitió las **266/266** por caché, sin errores. Tras regenerar los cinco cuadernillos se verificó que ninguna opción terminara en folio; la respuesta numérica `cie-i016` D conservó el valor `10`.

## Límites que siguen abiertos

El pipeline procesa los documentos y conserva el material por pregunta o por página, pero no termina la revisión editorial/pedagógica. Para Matemáticas: 50 preguntas, claves cotejadas; se corrigieron alternativas vacías, se añadieron bloques compartidos para 4–6 y 9–13. mat-i038 está revisada, con una salvedad por ambigüedad de datos. Persisten 74 asociaciones de evidencia sin cotejar contra el marco (Ciencias), la salvedad de mat-i038 y 2 licencias de materiales externos sin autorización comprobada. Los documentos antiguos y el cuadernillo de Inglés permanecen como transcripción, sin banco de preguntas estructurado. Dos guías largas provocan avisos de estructura del PDF en PyMuPDF, aunque sus siete etapas terminan; no se reportaron fallos de etapa. El contenido ICFES permanece bajo `content/icfes/` y detrás del gate. No se hizo push; `saber11-repo.tar.gz` sigue sin agregar.
