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
- [ ] Revisar las 271 hojas nuevas de Inglés y 2014, completar la transcripción visual y pedagógica, enlazar marcos donde existan y cotejar figuras candidatas. Las 346 hojas originales siguen revisadas; mat-i038 conserva una salvedad sobre la cobertura de la tabla.
- [x] Auditar claves y formato de numeración de los cuadernillos antiguos restantes. Se hallaron claves explícitas en Sociales 2018, Matemáticas 2018 y el cuadernillo general de 2014; usan numeración `1.` en vez de encabezados `Pregunta n`, y el de 2014 mezcla áreas. Se añadió un modo numerado con revisión obligatoria para los dos cuadernillos de 2018.
- [x] Añadir extracción numerada con revisión explícita y procesar Sociales y Matemáticas 2018: 49 preguntas por documento, 49 claves oficiales por documento y 49 hojas borrador por prueba. La revisión posterior completó ambas pruebas: cada hoja conserva sus cambios pedagógicos separados del contenido base en archivos de hoja y overrides.
- [x] Cotejar visualmente Matemáticas 2018, pregunta 1, asociar el recorte vectorial de la figura y completar su hoja de tres niveles con clave y descartes verificados.
- [x] Cotejar visualmente Matemáticas 2018, pregunta 3; reconstruir su tabla como figura desde la página fuente, corregir el texto de la opción D contaminado por la página siguiente y documentar la comparación de costos en override y hoja revisada. Quedan 96 borradores de 2018.
- [x] Cotejar las páginas fuente de Matemáticas 2018, preguntas 4 a 6; reconstruir la tabla de capacitación como contexto compartido, comprobar costos/capacidades y completar las tres hojas de solución.
- [x] Cotejar Matemáticas 2018, preguntas 7 a 10; asociar el recorte completo del mapa de obesidad, reconstruir sus dos tablas y la tabla compartida de precios, reparar la estatura fraccionaria de la pregunta 8 y limpiar opciones contaminadas por saltos de página. Completar las cuatro hojas y verificar sus claves en el render.
- [x] Cotejar Matemáticas 2018, preguntas 11 a 13; verificar el bono sobre lotes completos, recortar las cuatro opciones gráficas de la pregunta 12 y completar los razonamientos de la 13. Ajustar la puntuación de los pasos numerados de las preguntas 10 y 11 para que se lean correctamente en la vista.
- [x] Cotejar Matemáticas 2018, preguntas 14 a 20; resolver el cambio de área, la proporcionalidad gráfica, promedio, áreas y relaciones algebraicas; asociar la gráfica y reconstruir la tabla de publicidad.
- [x] Cotejar Matemáticas 2018, preguntas 21 a 27; verificar conteo de podios, corte triangular, cartabón, promedio y dispersión, permutaciones, gráfico circular y comparación de récords; asociar las tres figuras y reconstruir la tabla.
- [x] Cotejar Matemáticas 2018, preguntas 28 a 34; reconstruir las tablas de cursos y baraja, corregir las razones de la escalera, asociar el octágono y las cuatro tablas gráficas, resolver la reflexión y compartir el contexto de crédito.
- [x] Cotejar Matemáticas 2018, preguntas 35 a 41; verificar interés total, margen de error, geometría de circunferencia, porcentajes de finales, promedio de cancha dura, racionales y escala; asociar la gráfica de tenis, la cancha y sus opciones.
- [x] Cotejar portada, metadatos y créditos editoriales de los dos documentos externos y completar las citas disponibles.
- [x] Recuperar las claves oficiales de 13 preguntas de Ciencias por cuadernillo mediante overrides citados; verificar las 13 hojas de 2026 contra el cuadernillo de 2025 antes de reutilizarlas.
- [ ] Confirmar derechos/licencias de SED Cartagena y del libro de preparación de 2017; los PDF no incluyen permiso de reutilización y ambos continúan bajo gate.
- [x] Crear commits locales individuales por cada uno de los 38 documentos. La implementación del pipeline/configuración y la actualización documental quedaron agrupadas en dos commits, no en commits separados por cada etapa interna.

## Resumen

- Documentos procesados: **38/38**, con sus siete etapas registradas en `docus/manifest.json`.
- Páginas: **1.209**. Candidatos vectoriales: **4.201**; son candidatos de trabajo, no todas figuras asociadas.
- Once cuadernillos estructurados: **617 preguntas con clave**, incluidos 346 de los siete paquetes iniciales, 150 de Inglés (tres documentos) y 121 del cuadernillo mixto de 2014. Cuatro posiciones 2014 con clave `N/A` no son preguntas de selección múltiple y quedaron fuera del total.
- **346 preguntas tienen referencias a competencia, afirmación y evidencia**: las 248 iniciales y los 98 reactivos de Matemáticas/Sociales 2018. Los 271 reactivos nuevos de Inglés y 2014 aún no están enlazados a marcos. Los niveles 1–4 son estimaciones pedagógicas, no niveles oficiales por pregunta. mat-i038 conserva una salvedad. Las 72 opciones gráficas de Ciencias ya están recortadas individualmente.
- **346 hojas revisadas** para los siete paquetes originales. Hay además **271 hojas borrador** de Inglés y 2014, generadas en lotes reanudables; no equivalen a explicaciones pedagógicas aprobadas. Las 150 preguntas de Inglés y las 121 de 2014 están marcadas `revisar`; las 49 preguntas de Sociales 2018 tienen transcripción corregida y la figura de la 16 asociada.
- **7 simulacros iniciales auditados** con cobertura completa y sin IDs duplicados. Hay cuatro paquetes nuevos en revisión: tres de Inglés con dos secciones de 25 preguntas y uno de 2014 dividido por área. Sus unidades/simulacros requieren una auditoría visual adicional. Los minutos son referencias de práctica, no duraciones oficiales.
- Se añadieron los plugins `ingles` y `mixto2014`: separan exámenes con numeración reiniciada, usan claves independientes y configuran las áreas del cuadernillo mixto. Los reactivos sin transcripción inequívoca conservan placeholders explícitos y `revisar`; hace falta cotejo por página antes de uso. La búsqueda de licencias para Cartagena y el libro 2017 no encontró permiso escrito.
- Figuras verificadas y asociadas: 29 recortes de pregunta en cada cuadernillo de Ciencias, más la infografía compartida de Lectura Crítica para las preguntas 42–49. Las imágenes oficiales solo entran al build con `VITE_ICFES=1`.
- La app importa preguntas, marcos y niveles oficiales solo detrás de `VITE_ICFES=1`; las transcripciones completas `documento.json` no se incorporan al bundle.

## Resultados por documento

| Documento | Plugin | Páginas PDF | Preguntas válidas | Sin clave | Candidatos figura | Salida |
|---|---:|---:|---:|---:|---:|---|
| `01_Matematicas_Saber11_2026_ICFES` | cuadernillo | 35 | 50 | 0 | 80 | 1 simulacro |
| `02_Lectura_Critica_Saber11_2026_ICFES` | cuadernillo | 44 | 49 | 0 | 53 | 1 simulacro; infografía compartida en preguntas 42–49 |
| `03_Ciencias_Naturales_Saber11_2026_ICFES` | cuadernillo | 42 | 50 | 0 | 148 | 1 simulacro; 13 claves por override citado |
| `04_Ciencias_Naturales_Saber11_2025_ICFES` | cuadernillo | 42 | 50 | 0 | 148 | 1 simulacro; 13 claves por override citado |
| `05_Ingles_Saber11_2024_ICFES` | ingles | 25 | 50 | 0 | 61 | 1 simulacro; 2 exámenes de 25; 50 marcadas `revisar` |
| `07_Sociales_y_Ciudadanas_Saber11_2021` | cuadernillo | 30 | 49 | 0 | 143 | 1 simulacro; 14 opciones restauradas desde PDF |
| `08_Ingles_Saber11_2021` | ingles | 24 | 50 | 0 | 136 | 1 simulacro; 2 exámenes de 25; 50 marcadas `revisar` |
| `09_Lectura_Critica_Saber11_2018` | cuadernillo | 33 | 0 | 0 | 132 | 1 pág. guardadas |
| `10_Sociales_y_Ciudadanas_Saber11_2018` | cuadernillo | 21 | 49 | 0 | 94 | 1 simulacro; 49 hojas revisadas; preguntas 4, 16 y 25 corregidas/asociadas |
| `11_Matematicas_Saber11_2018` | cuadernillo | 28 | 49 | 0 | 108 | 1 simulacro; 49 hojas revisadas |
| `14_Ingles_Saber11_2018` | ingles | 21 | 50 | 0 | 74 | 1 simulacro; 2 exámenes de 25; 50 marcadas `revisar` |
| `15_Cuadernillo_Saber11_2014` | mixto2014 | 40 | 121 | 0 | 44 | 1 simulacro dividido en 5 áreas; 4 posiciones `N/A` excluidas; 121 marcadas `revisar` |
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
- Vitest con `VITE_ICFES=1`: **811/811 pruebas**; `npx tsc --noEmit` pasó.
- Build estándar: pasó; bundle JavaScript **599.70 kB** (gzip 203.46 kB). Build con `VITE_ICFES=1`: pasó; bundle JavaScript **3,625.98 kB** (gzip 536.71 kB), con el nuevo contenido bajo gate. Ambos avisan que el chunk supera 300 kB.
- Reconstrucción forzada de Matemáticas 2018: SHA-256 de `content/icfes/mth/preguntas.json` antes y después idéntico: `76f949eeff538a2b73122645954483e2a88d5f212b50e3cf1107c109f05fe229` (reconstrucción forzada 2026-10-22).
- Reconstrucción de Matemáticas tras borrar `work/01_Matematicas...` y el paquete generado: SHA-256 `90601de71edec55d67752ba6170c316b6e5823dce17ac68eb906e6717552a33f`; paquete y 50 archivos de hojas idénticos. Se preservaron overrides y 50 hojas revisadas, incluida la hoja de mat-i038 con su salvedad documentada; la reconstrucción tras completar los enlaces volvió a dar el mismo hash.
- Idempotencia: el recálculo reciente de Matemáticas ejecutó 7/7 etapas; la segunda ejecución omitió las **7/7** por caché, sin errores. Tras regenerar los cinco cuadernillos se verificó que ninguna opción terminara en folio; la respuesta numérica `cie-i016` D conservó el valor `10`.

## Límites que siguen abiertos

Los siete paquetes originales conservan sus 346 hojas revisadas. Inglés y el cuadernillo mixto de 2014 añaden 271 reactivos con clave y hojas borrador; todos están marcados `revisar` y requieren cotejo visual, reconstrucción de pasajes/opciones y explicación pedagógica antes de uso. Cuatro simulacros nuevos están separados por examen/área pero aún requieren auditoría visual. Quedan enlaces de marco para estos 271 reactivos, la salvedad de `mat-i038`, candidatos gráficos no asociados y permisos escritos para dos documentos externos. El contenido ICFES permanece bajo el gate y `saber11-repo.tar.gz` sigue sin agregar.


## Revisión adicional — Matemáticas 2018 (preguntas 2 y 42–49)
- Se completaron las hojas revisadas de las preguntas 2 y 42 a 49; se incorporaron los apoyos gráficos de 42 y 44 y la tabla compartida de subsidios para 43–45.
- Se limpió la última marca obsoleta de cotejo en la pregunta 1 tras confirmar la figura ya asociada. Matemáticas 2018 queda en 49/49 hojas revisadas y cero preguntas con `revisar`.
- Recortes de 42 y 44 cotejados visualmente contra el PDF. Reconstrucción forzada determinista; TypeScript, Vitest gated 540/540 y builds estándar/gated pasan.

## Revisión adicional — Sociales 2018 (preguntas 1–49)
- Se cotejaron las páginas fuente que contienen las 49 preguntas y su tabla oficial de respuestas.
- Se corrigieron las preguntas 4 y 25, que la extracción había separado/mapeado de forma incorrecta; la 16 ahora incluye las dos caricaturas recortadas desde la página original.
- Las 49 hojas incluyen tres niveles, enfoque y descarte de las tres alternativas incorrectas. Se registró la fuente completa por pregunta y `revisar` queda vacío tras cotejo.
- Reconstrucción forzada idempotente: SHA-256 antes y después `a813698cbce1e152fa011fdc4362cd93edd26a99a63f6cd6caa9b0d0039fe92`. TypeScript pasó y Vitest gated: 540/540.

## Auditoría de simulacros y unidades (2026-10-22)
- Se revisaron los siete paquetes, comprobando área, IDs únicos y cobertura completa e igual entre el simulacro y la unidad del cuadernillo.
- Se corrigieron los paquetes de Ciencias 2025 y 2026: las 13 claves resueltas por override ya entran en simulacro y unidad; ambos pasan de 37 a 50 preguntas.
- La duración se deja como estimación de práctica de un minuto por reactivo, no como tiempo oficial del examen.
- Reconstrucción forzada de la etapa mpaquetar en los siete documentos: los siete SHA-256 de preguntas.json permanecieron idénticos; los hashes están reflejados en los artefactos y los overrides por paquete.


## Nuevos extractores para Inglés y el cuadernillo mixto (2026-10-22)
- Se implementaron los plugins `ingles` y `mixto2014` y se configuraron los tres cuadernillos de Inglés (2024/2021/2018) más el mixto de 2014.
- Inglés: 150 posiciones (25 por examen en cada PDF), claves separadas por examen, IDs correlativos únicos y cuatro simulacros/unidades estructurados.
- 2014: 121 preguntas de selección múltiple con clave, cinco áreas y cuatro posiciones de respuesta `N/A` excluidas; cada área tiene su unidad/sección.
- Se generaron 271 hojas en borrador en lotes de diez, sin sobrescribirlas al reanudar. Todas las preguntas de esos cuatro paquetes conservan `revisar` porque faltan cotejos visuales/textuales y trabajo pedagógico.
- Se enlazaron Matemáticas 2018 y Sociales 2018 a los IDs de competencia, afirmación y evidencia del marco mediante overrides persistentes (98 reactivos).
- Se corrigió la validación para conservar simulacros/unidades con múltiples secciones y se preservaron las transcripciones `documento.json` como artefactos separados. Verificación: TypeScript, Vitest 811/811, build normal y build `VITE_ICFES=1` pasan. La reconstrucción forzada de empaquetado conservó los hashes: `ing` `bb963908b1627cb68278eb09d8761d3ca1c0ea7751c004b6f90b4044571dfc01`, `ena` `5f19c0981d26b4fe9c2e8442e35b2868d32a98541099a48f2018d659d1b574bf`, `eng` `dd8e093a2b59c9d43ba961a224a7e2286aa0a95b0dc7a38fea02dc906838c1c7`, `cfi` `c22565856901ccc535a21f6a7ccd5e8c51c2267b5e9aae9b93eff65e0b73333a`. También fueron idénticas las reconstrucciones de `mth` y `scc` después de asociar los marcos.
