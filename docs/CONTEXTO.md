# Saber 11 — Contexto del proyecto (para continuar en otro lado)

## Qué es
Plataforma web premium de preparación para Saber 11 (pre-ICFES, Colombia). SPA en Vite + TypeScript. Laboratorios interactivos, práctica adaptativa, diagnóstico, simulacros en modo examen, explicaciones del "profe" en 3 niveles, PWA. Backend: Cloudflare Pages Functions + D1. Pagos con Wompi (fuera de alcance de las mejoras).

## Modelo de negocio (decisión del dueño)
- Dos versiones: **gratuita con TODO el contenido** y **premium que solo cambia el color (paletas) de la plataforma**. El contenido no se vende.
- Código: `hasAccess = () => true`; `hasPremium = () => FREE_MODE || paid`. Paletas con `html[data-paleta=…]`, guardada en `localStorage saber11.paleta`.

## Objetivos de calidad
- Pedagogía ≥ 9/10: español colombiano natural, narración del profe en 3 niveles, explicaciones gráficas.
- Sin scroll de página en la vista de pregunta (modo foco).
- Diseño plano y premium.
- Todo el contenido controlable por JSON (preguntas, bloques, figuras, hojas, simulacros, laboratorios).
- Simuladores con la experiencia del examen real, más mejoras propias.

## Comandos
- Instalar: `npm install`
- Pruebas: `npx vitest run` (442 pruebas) · tipos: `npx tsc --noEmit`
- Build gratis: `VITE_FREE_MODE=1 npx vite build` · con contenido ICFES: añadir `VITE_ICFES=1`
- Vista previa: `npx vite preview --port 4173`
- Regenerar contenido base: `python3 tools/build_content.py` (+ `tools/tono.py`); hojas del pack de formato: `python3 tools/icfes_hojas.py` (idempotente)

## Estructura del contenido (`content/`)
- `questions/*.json`, `lessons/`, `packs/**/*.json` (preguntas, bloques, unidades, simulacros, labs), `simulacros/*.json`, `bloques/*.json`.
- `hojas.json`, `guiones.json`, `enfoques.json` se mezclan por id (`conExtras`); una pregunta de pack puede llevar `hoja` embebida.
- `niveles.json`: niveles generales de desempeño del contenido propio; `content/icfes/niveles_desempeno.json`: descriptores oficiales extraídos y gated.
- `icfes/`: contenido oficial del ICFES, **apagado por defecto** (ver licencia).
- Ver `content/README.md` para el formato completo.

### Pregunta
`id` (`mat-101`, ICFES: `mat-i001`), `area`, `evidencia`, `nivel` 1–4, `enunciado`, `opciones` (2–8, A–H), `correcta`, `explicacion`, `distractores` (uno por opción, `''` en la correcta), `origen` (`original` | `icfes`; icfes exige `fuente`), opcionales: `bloque`, `figuras[]`, `opcionesFig[]`, `afirmacion`, `competencia`, `parte`, `hoja`, `revisar[]`.

### Figuras (`Figura`)
`img` (src archivo o https), `svg` (sanitizado), `escena` (dibujo declarativo, mismo motor de los labs), `tabla`, `pendiente` (hueco con número de página). Varias por pregunta; también por opción (`opcionesFig`) y por bloque.

### Bloques
Contexto compartido «Responde las preguntas X a Y de acuerdo con la siguiente información», con texto y figuras mostradas una vez por grupo.

### Hoja (explicación por pregunta)
`{modo, marcas[], pasos[], enfoque, guion{1,2,3}}`. Pasos: idea, calc, tabla, ejemplo, linea, check, traducir, tanteo, puntos, grafica, barras, flujo, vida, glosa, escucha, escena. Reglas probadas por test: sin dígitos sueltos en la narración (números dentro de `$…$`), el nivel 2 descarta todas las opciones erróneas, marcas = subcadenas no solapadas del enunciado, inglés entre `{{…}}`, la hoja necesita un paso `check`.

### Simulacros
`SimulacroDef.modo:'examen'` con `sesiones[{titulo,minutos,pruebas[]}]`; `armarExamen` mantiene juntos los grupos de un bloque; `comoExamen` convierte simulacros antiguos. Estado en `saber11.sim.<id>`, historial `saber11.simhist`.

## Navegación (v49)
Pestañas: Hoy, Aprender, Practicar, Progreso. Extra: `#/mapa` (10 casos "Quiero…" + ruta completa), migas de pan, `#/contenido` (biblioteca), `#/pregunta/<id>`, `#/sesion?area=<área>` (práctica por materia), `#/sesion?modo=repaso`.

## Importador ICFES
`python3 tools/importar_icfes.py texto.txt --area matematicas --pref mat --prueba "Prueba Matemáticas" [--figuras figuras.json]` → `content/icfes/<pref>/preguntas.json`. Figuras sin archivo → `pendiente`. Lo dudoso → `revisar`. Solo entra al build con `VITE_ICFES=1` (plugin `icfes-gate` en `vite.config.ts`).

## Pipeline documental (2026-10)
`python tools/pipeline/run.py` procesa los 38 PDFs de `docus/` en siete etapas reanudables; configuración, plugins y guía están en `tools/pipeline/`. Hay siete cuadernillos estructurados: 346 preguntas con clave y siete simulacros en revisión. Hay 257 hojas revisadas y 89 borradores: las 248 iniciales y las preguntas 1 y 3–10 de Matemáticas 2018 están revisadas; las demás preguntas nuevas de 2018 esperan cotejo. La figura de la pregunta 1 está recortada y asociada; las preguntas 3 a 10 incluyen tablas, figura o contextos cotejados en overrides. Matemáticas 2018 pregunta 48 conserva un enunciado sin delimitar. mat-i038 mantiene una salvedad porque la tabla no prueba que las categorías cubran a los 110 clientes. Las 248 preguntas de Matemáticas 2026, Lectura, Sociales 2021 y Ciencias (50/50 por edición) tienen referencias a competencia, afirmación y evidencia específicas; los reactivos de 2018 aún no se enlazaron a marcos. Los cinco PDFs de niveles se recopilaron en `content/icfes/niveles_desempeno.json`; los marcos de las cinco áreas están en `content/icfes/marco.json`. Los niveles por pregunta son estimaciones pedagógicas 1–4 guardadas en overrides. Inglés y otros documentos antiguos aún esperan extractor; las licencias de dos documentos externos tampoco están acreditadas. Poppler usa `pdftotext -layout`; el pipeline crea hasta diez hojas faltantes por lote y preserva las existentes. Ver `informe_icfes.md`; el contenido oficial permanece bajo el gate de ICFES. `docus/` y `work/` no se versionan.

## Licencia ICFES (importante)
Los términos oficiales del ICFES para sus publicaciones permiten uso académico/investigativo y **prohíben transformar o usar con fines de lucro** ([cuadernillo oficial 2026, términos de uso](https://www.icfes.gov.co/wp-content/uploads/2026/03/16-feb-cuadernillo-de-preguntas-lectura-critica-saber-11-2026.pdf)). La plataforma cobra paletas (ingreso), así que publicar preguntas/imágenes literales del ICFES requiere **permiso escrito del ICFES**. Mientras no exista, `content/icfes/` queda fuera del build publicado. Alternativa segura: preguntas originales con el mismo formato.

## Documentos fuente disponibles
`docus/` contiene 38 PDFs (cuadernillos, guías, marcos, niveles, infografías y materiales complementarios). El pipeline ya generó transcripción por página, raster completo e índice de candidatos vectoriales en `work/`; siete cuadernillos tienen preguntas estructuradas. De las 98 nuevas de 2018, nueve preguntas de Matemáticas ya se cotejaron y 89 esperan revisión y asociación semántica. También quedan figuras candidatas por revisar.

## Pendientes del pipeline documental
1. Construir extractores para los cuadernillos antiguos restantes y los de Inglés; los dos documentos 2018 ya tienen preguntas preliminares, aún sin cotejo/relación con marcos.
2. Revisar siete simulacros generados, marcados “En revisión”.
3. Conservar la salvedad de mat-i038: su resultado depende de asumir que las categorías de la tabla cubren a los 110 clientes.
4. Acreditar las licencias de SED Cartagena y del libro de preparación 2017 antes de cualquier distribución.
5. Hacer cotejo visual adicional de las figuras candidatas que aún no están enlazadas a preguntas.

Otros pendientes del producto (voz en celular, banco propio y laboratorios) son independientes de este pipeline. Pagos, legal y PWA quedan fuera de alcance de esta tarea.
## Preferencias de trabajo del dueño
Español informal ("tú"); mensajes finales concisos (enlace/archivo + un siguiente paso); ahorrar tokens; decir que la voz no se probó en dispositivo real; no guardar memoria sin preguntar.
