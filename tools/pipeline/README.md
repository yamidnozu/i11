# Pipeline documental reutilizable

Ejecuta desde la raíz del repositorio:

```sh
python tools/pipeline/run.py
python tools/pipeline/run.py --doc 01_Matematicas_Saber11_2026_ICFES
python tools/pipeline/run.py --doc archivo.pdf --desde figuras
python tools/pipeline/run.py --doc archivo.pdf --solo validar
python tools/pipeline/run.py --doc archivo.pdf --forzar
```

El pipeline recorre `detectar → texto → figuras → estructurar → enriquecer → validar → empaquetar`. Cada fase lee y escribe artefactos JSON/PNG en `work/<documento>/<etapa>/`; una fase no depende de objetos en memoria de la anterior. `docus/manifest.json` guarda el SHA-256 del PDF, tipo, prefijo, área, estado, firma, hash de salida y fecha de cada etapa. Si no cambian PDF, configuración, código del plugin ni correcciones manuales, las fases se omiten. `--desde` recalcula esa fase y las siguientes; `--solo` ejecuta una fase y exige que sus entradas estén en disco. `--forzar` recalcula desde la primera etapa seleccionada.

## Configuración y plugins

`config.json` controla las rutas `docus` y `work`, `batch_size`, DPI, tolerancia de agrupación, prefijo, área, origen, año, cita, prueba y tipo de cada documento. Los nombres de fase son estables. Para añadir un documento, copia el PDF a la ruta configurada y agrega una entrada bajo `documents`.

Un tipo nuevo es un archivo `tipos/<tipo>.py` con tres funciones `detectar(ctx)`, `extraer(ctx)` y `estructurar(ctx)`. El contexto contiene `source` (PDF), `spec` (configuración del documento), `config`, `dirs` (directorios de etapas), `work`, `doc` y `root`. Las funciones retornan objetos serializables; el runner los guarda en disco. El plugin debe depender de los artefactos de etapas anteriores, no de salidas temporales en memoria. Los tipos existentes son `cuadernillo`, `marco`, `guia`, `lectura_imagenes`, `simulacro_armado` y el fallback `documento`. `cuadernillo` acepta encabezados `Pregunta n` / `Question n` y, si hay clave, números antiguos `n.`; estos últimos se generan con `revisar` para cotejo porque OCR puede confundirlos con listas, preguntas gráficas o tablas. Para un libro o material escolar, define `origen: "propio"` o `"licenciado"`, su cita y un plugin que extraiga solo contenido autorizado; no uses `icfes` salvo para fuentes oficiales ICFES.

## Correcciones y hojas

No edites `content/icfes/<prefijo>/preguntas.json`: se vuelve a generar. Guarda cada corrección de pregunta en `content/icfes/<prefijo>/overrides.json`, por ID y campo, por ejemplo:

```json
{
  "mat-i001": {
    "opciones": ["…", "…", "…", "…"],
    "correcta": 2,
    "explicacion": "…"
  }
}
```

Las correcciones de paquete van en `__paquete__`; `bloques_agregar` añade bloques compartidos de forma idempotente. El campo `nivel` (1–4) se estima por demanda de razonamiento, no se copia como supuesto desde el nivel oficial del evaluado; guarda la decisión por pregunta en el mismo override para que sobreviva a reconstrucciones. Mantén diferenciadas las competencias de desempeño y la dificultad pedagógica del ítem. El empaquetador rechaza IDs desconocidos, cambios de ID, clave fuera de rango, opciones ausentes y citas faltantes. Una clave documentada en el override puede resolver una pregunta pendiente; incluye en `fuente` la cita completa.

Las hojas editables viven en `hojas/<id>.json`. Cada ejecución crea hasta `batch_size` (por defecto diez) hojas que faltan, en orden estable. Las hojas existentes, y en particular las `revisada`, nunca se reemplazan. Para continuar un lote ejecuta de nuevo con `--desde enriquecer`; para reconstruir una hoja borrador, respáldala y elimina solo ese archivo antes de reanudar. El estado `revisada` significa que una persona cotejó y aprobó el contenido pedagógico, no que el pipeline haya rellenado una plantilla.

## Figuras y revisión humana

`texto` usa `pdftotext -layout` y conserva la transcripción literal; declara PyMuPDF si Poppler no está instalado. `figuras` rasteriza páginas completas para cotejo y registra trazos vectoriales candidatos. Puede producir recortes de pregunta y de cada opción gráfica cuando `overrides.json` vincula figuras `img` mediante `figuras` u `opcionesFig`; cada opción admite su propio `recorteFuente`. Un recorte manual reproducible puede guardar `recorteFuente: { "pagina": 36, "rect": [x0, y0, x1, y1] }` en la figura del override; la etapa lo regenera desde el PDF con el DPI de config y guarda su registro en `work/<documento>/figuras/`. La figura compartida por un conjunto de preguntas se guarda como `bloque` mediante `__paquete__.bloques_agregar`. `tipo: "tabla"` y `opcionesFig` se usan únicamente cuando su contenido se reconstruyó y verificó; si la extracción no es fiable, conserva `revisar` con el motivo. No se debe inferir texto ni respuesta desde un recorte ambiguo. La extracción semántica automática de tablas, SVG sanitizados y diagramas aún requiere validación específica por documento.

## Validar, publicar y reconstruir

Tras procesar un documento:

```sh
npx tsc --noEmit
VITE_ICFES=1 npx vitest run
```

El material ICFES se guarda exclusivamente bajo `content/icfes/`. El build normal lo excluye; solo la variable `VITE_ICFES=1` permite que el plugin copie JSON e imágenes al resultado. No publiques material ICFES con fines de lucro sin permiso escrito. `docus/` y `work/` permanecen en `.gitignore`; los PDF fuente no se versionan.

Para reconstrucción limpia, conserva `overrides.json` y hojas revisadas, respáldalas si hace falta y elimina solo los artefactos de trabajo y el contenido generado del prefijo. Ejecuta otra vez el documento con `--forzar`. Compara las salidas normalizadas y sus SHA-256; deja el original intacto hasta confirmar que la reconstrucción es equivalente.
