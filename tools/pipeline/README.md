# Pipeline de documentos

`python tools/pipeline/run.py [--doc ID|archivo.pdf] [--desde etapa] [--forzar] [--solo etapa]`

Etapas independientes: `detectar → texto → figuras → estructurar → enriquecer → validar → empaquetar`. Cada una persiste su salida en `work/<id>/<etapa>/`; el manifiesto `docus/manifest.json` registra SHA-256, fecha y firma de caché. `--desde` invalida/recalcula desde la etapa indicada; `--solo` requiere archivos de etapas anteriores. Los PDFs y el trabajo local se ignoran en Git.

## Configurar documentos

Edita `config.json`: rutas, prefijos, área, procedencia, año, prueba, DPI y tolerancia de agrupación vectorial. Añade un registro en `documents`. Para un tipo nuevo crea `tipos/<tipo>.py` con `detectar(ctx)`, `extraer(ctx)` y `estructurar(ctx)`; el contexto entrega `source`, `spec`, `config`, `dirs` y `root`. Las salidas de cada función se serializan como JSON en la etapa correspondiente. Las firmas de caché incluyen PDF, configuración y código del runner/plugin; la etapa de empaquetado también incluye los hashes de `overrides.json` y de cada hoja. Las hojas existentes se preservan, incluso si siguen en borrador, para no descartar cambios humanos; edítalas para mejorar la pedagogía y marca `revisada` solo tras cotejarla.

Estado actual: hay 38 PDFs configurados en `config.json`. `cuadernillo.py` extrae preguntas cuando reconoce marcadores y claves; las que no tienen clave pasan a `pendientes_clave.json`, nunca reciben una respuesta inventada. `marco.py`, `guia.py`, `lectura_imagenes.py` y el fallback de `simulacro_armado.py` conservan transcripción literal por página y candidatos gráficos en `content/icfes/<prefijo>/documento.json`. Son plugins funcionales de extracción, pero la interpretación de competencias, afirmaciones, ejemplos y niveles sigue pendiente de validación semántica. Los documentos sin marcadores de pregunta se guardan como transcripción, no como un banco vacío de preguntas.

## Reanudar y reconstruir

Una ejecución normal omite etapas con firma vigente. Usa `--desde enriquecer` para regenerar hojas y etapas posteriores, o `--forzar` para recalcular. El pipeline nunca pisa hojas existentes; las que faltan se crean como borradores. `overrides.json` mapea id a campos: `{"mat-i001":{"explicacion":"..."}}`. No edites `preguntas.json` generado: conserva correcciones de preguntas allí y el trabajo pedagógico en `hojas/<id>.json`.

La extracción de figuras guarda páginas completas y candidatos vectoriales; su asociación semántica se debe cotejar visualmente. No hay todavía asociación automática fiable de figura a pregunta, SVG sanitizado ni tablas/opciones gráficas semánticamente reconstruidas. Se prefiere `pdftotext -layout`; si no está en `PATH`, se usa el respaldo PyMuPDF y se declara en el artefacto de texto. En este equipo se instaló Poppler con Winget; abre una terminal nueva para que herede el `PATH`. La herramienta seleccionada forma parte de la firma de caché. Las salidas `documento.json` son transcripciones fuente, no packs de preguntas, y `src/content/index.ts` importa de ICFES solo `preguntas.json` para evitar meter documentos enteros al bundle.

Overrides: usa `overrides.json` como objeto `{ "<id-estable>": { "<campo>": valor } }`. El empaquetador rechaza IDs inexistentes y no permite cambiar `id`; `__paquete__` puede reemplazar campos de nivel superior permitidos como bloques compartidos; vuelve a validar fuente, opciones y clave después de aplicar cambios. Las hojas se guardan una por pregunta; el generador no reemplaza ninguna hoja existente. Para regenerar una hoja borrador, guarda primero una copia fuera del directorio y elimina solo ese archivo antes de ejecutar `--desde enriquecer`.

El contenido oficial permanece en `content/icfes/`, excluido del build salvo `VITE_ICFES=1`. No publiques material ICFES con fines de lucro sin autorización escrita.
