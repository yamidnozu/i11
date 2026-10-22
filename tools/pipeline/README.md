# Pipeline de documentos

`python tools/pipeline/run.py [--doc ID|archivo.pdf] [--desde etapa] [--forzar] [--solo etapa]`

Etapas independientes: `detectar → texto → figuras → estructurar → enriquecer → validar → empaquetar`. Cada una persiste su salida en `work/<id>/<etapa>/`; el manifiesto `docus/manifest.json` registra SHA-256, fecha y firma de caché. `--desde` invalida/recalcula desde la etapa indicada; `--solo` requiere archivos de etapas anteriores. Los PDFs y el trabajo local se ignoran en Git.

## Configurar documentos

Edita `config.json`: rutas, prefijos, área, procedencia, año, prueba, DPI y tolerancia de agrupación vectorial. Añade un registro en `documents`. Para un tipo nuevo crea `tipos/<tipo>.py` con `detectar(ctx)`, `extraer(ctx)` y `estructurar(ctx)`; el contexto entrega `source`, `spec`, `config`, `dirs` y `root`. Las salidas de cada función se serializan como JSON en la etapa correspondiente. Las firmas de caché incluyen PDF, configuración y código del runner/plugin.

Estado actual: `cuadernillo.py` estructura el cuadernillo de Matemáticas. `marco.py`, `guia.py`, `lectura_imagenes.py` y `simulacro_armado.py` son adaptadores provisionales, no extractores semánticos completos. No registres ni proceses esos tipos hasta implementar su parser y validación específicos. Para otros tipos, define su interfaz en un módulo independiente, extrae solo afirmaciones presentes en la fuente y marca lo incierto con `revisar`.

## Reanudar y reconstruir

Una ejecución normal omite etapas con firma vigente. Usa `--desde enriquecer` para regenerar hojas y etapas posteriores, o `--forzar` para recalcular. El pipeline conserva `overrides.json` y hojas con `estado: revisada`; las hojas nuevas quedan como borradores. `overrides.json` mapea id a campos: `{"mat-i001":{"explicacion":"..."}}`. No edites archivos generados: conserva toda corrección allí o en `hojas/<id>.json`.

La extracción de figuras guarda páginas completas y candidatos vectoriales; su asociación semántica se debe cotejar visualmente. No hay todavía asociación automática fiable de figura a pregunta, SVG sanitizado ni tablas/opciones gráficas semánticamente reconstruidas. Se prefiere `pdftotext -layout`; si no está en `PATH`, se usa el respaldo PyMuPDF y se declara en el artefacto de texto. En este equipo se instaló Poppler con Winget; abre una terminal nueva para que herede el `PATH`. La herramienta seleccionada forma parte de la firma de caché. El cotejo de Matemáticas detectó transcripciones incorrectas; las preguntas y hojas quedan marcadas como borrador y no deben considerarse listas para estudio.

Overrides: usa `overrides.json` como objeto `{ "<id-estable>": { "<campo>": valor } }`. El empaquetador rechaza IDs inexistentes y no permite cambiar `id`; vuelve a validar fuente, opciones y clave después de aplicar cambios. Las hojas se guardan una por pregunta; el generador conserva las que tengan `estado: revisada` y rellena/reemplaza borradores al reanudar.

El contenido oficial permanece en `content/icfes/`, excluido del build salvo `VITE_ICFES=1`. No publiques material ICFES con fines de lucro sin autorización escrita.
