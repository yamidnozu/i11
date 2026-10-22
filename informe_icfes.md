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
- [ ] Completar soluciones y distractores razonados para las otras 172 preguntas; sus hojas siguen como borradores, no como material pedagógico aprobado.
- [x] Cotejar visualmente las 50 preguntas de Matemáticas y su clave oficial; corregir alternativas vacías, datos/tablas y contextos compartidos. Se revisaron 49 hojas; mat-i038 sigue borrador porque la tabla no determina las intersecciones necesarias.
- [ ] Cotejar las 71 preguntas restantes marcadas en Ciencias, Lectura y Sociales, asociar 30 opciones gráficas y comprobar sus transcripciones.
- [ ] Convertir marcos y niveles a `content/marco.json` semántico y enlazar competencia/afirmación/evidencia a cada pregunta. Hoy se conserva el texto por página, sin interpretación automática.
- [ ] Estructurar preguntas de los documentos antiguos y el cuadernillo de Inglés que no contienen marcadores reconocidos; hoy se preservan sus páginas como transcripción.
- [x] Cotejar portada, metadatos y créditos editoriales de los dos documentos externos y completar las citas disponibles.
- [ ] Confirmar derechos/licencias de SED Cartagena y del libro de preparación de 2017; los PDF no incluyen permiso de reutilización y ambos continúan bajo gate.
- [x] Crear commits locales individuales por cada uno de los 38 documentos. La implementación del pipeline/configuración y la actualización documental quedaron agrupadas en dos commits, no en commits separados por cada etapa interna.

## Resumen

- Documentos procesados: **38/38**, con sus siete etapas completas en `docus/manifest.json`.
- Páginas: **1209**. Candidatos vectoriales: **4201**. Son recortes de trabajo; no equivalen a figuras asociadas y verificadas en cada pregunta.
- Preguntas con clave detectada y empaquetadas: **222**. Preguntas apartadas por clave no detectada: **26**.
- Preguntas con marcas de revisión: **72** (71 de otros cuadernillos y la pregunta mat-i038). Opciones gráficas aún pendientes de reconstrucción: **30**.
- Hojas: **222**. En Matemáticas, 49 están `revisada` y una `borrador`; las otras 172 siguen en `borrador`.
- Simulacros generados: uno por cada uno de los cinco cuadernillos que se estructuraron como preguntas. Contienen solo IDs con clave detectada y se etiquetan “En revisión”.
- La app importa de `content/icfes/` solo `preguntas.json`; las transcripciones completas `documento.json` no se incorporan al bundle.

## Resultados por documento

| Documento | Plugin | Páginas PDF | Preguntas válidas | Sin clave | Candidatos figura | Salida |
|---|---:|---:|---:|---:|---:|---|
| `01_Matematicas_Saber11_2026_ICFES` | cuadernillo | 35 | 50 | 0 | 80 | 1 simulacro |
| `02_Lectura_Critica_Saber11_2026_ICFES` | cuadernillo | 44 | 49 | 0 | 53 | 1 simulacro |
| `03_Ciencias_Naturales_Saber11_2026_ICFES` | cuadernillo | 42 | 37 | 13 | 148 | 1 simulacro |
| `04_Ciencias_Naturales_Saber11_2025_ICFES` | cuadernillo | 42 | 37 | 13 | 148 | 1 simulacro |
| `05_Ingles_Saber11_2024_ICFES` | cuadernillo | 25 | 0 | 0 | 61 | 1 pág. guardadas |
| `07_Sociales_y_Ciudadanas_Saber11_2021` | cuadernillo | 30 | 49 | 0 | 143 | 1 simulacro |
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
- Vitest con `VITE_ICFES=1`: **416/416 pruebas** pasaron, sin avisos de contenido.
- Build estándar: pasó; bundle JavaScript **599.22 kB** (gzip 203.34 kB). Build con `VITE_ICFES=1`: pasó; bundle JavaScript **1,556.41 kB** (gzip 297.04 kB). Ambos avisan que el chunk supera 300 kB.
- Reconstrucción de Matemáticas: SHA-256 `5a1b51d971fb5341f1518e9fe06030b7c0692fccff49d23a56a22a46b10d1d90`; las hojas manuales quedaron idénticas antes y después de regenerar.
- Caché global: **266/266 etapas** en caché; los hashes de salida no cambiaron. Reconstrucción repetida con caché tras el test limpio: salida idéntica.

## Límites que siguen abiertos

El pipeline procesa los documentos y conserva el material por pregunta o por página, pero no termina la revisión editorial/pedagógica. Para Matemáticas: 50 preguntas, claves cotejadas con la tabla oficial del PDF; se corrigieron alternativas vacías, se añadieron bloques compartidos para 4–6 y 9–13. Queda mat-i038 en revisión por ambigüedad de datos. El contenido oficial permanece bajo `content/icfes/` y detrás del gate. Commits locales: `aca0408` (pipeline), `18f8e8a` (documentación) y 38 commits `content: process …`, uno por documento. No se hizo push; el archivo no relacionado `saber11-repo.tar.gz` quedó sin agregar.
