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
- `niveles.json`: niveles de desempeño oficiales (4 por prueba).
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
`python tools/pipeline/run.py` procesa los 38 PDFs de `docus/` en siete etapas reanudables; config, plugins y guía están en `tools/pipeline/`. Hay cinco cuadernillos estructurados: 248 preguntas con clave, cero claves pendientes y cinco simulacros marcados En revisión. Matemáticas: 50 preguntas cotejadas visualmente y con clave; 49 hojas revisadas y mat-i038 en borrador por ambigüedad. Ciencias: dos cuadernillos de 50 preguntas, claves cotejadas; 50 hojas revisadas por prueba. Lectura Crítica: 49 borradores y una infografía compartida asociada a las preguntas 42–49. Sociales: 49 borradores; se restauraron las opciones textuales de 14 preguntas que el extractor clasificó erróneamente como gráficas. En conjunto hay 149 hojas revisadas, 99 borradores y 45 preguntas con avisos de revisión (evidencia de marco, opciones gráficas sin recorte individual o la ambigüedad de mat-i038). Aún falta la revisión pedagógica de esas hojas, asociar evidencias de marco y estructurar pregunta por pregunta documentos antiguos que hoy están como transcripción paginada. Poppler usa `pdftotext -layout`; el pipeline crea hasta diez hojas faltantes por lote y preserva las existentes. Ver `informe_icfes.md`; el contenido oficial sigue bajo el gate de ICFES. `docus/` y `work/` no se versionan.

## Licencia ICFES (importante)
Los términos oficiales del ICFES para sus publicaciones permiten uso académico/investigativo y **prohíben transformar o usar con fines de lucro** ([cuadernillo oficial 2026, términos de uso](https://www.icfes.gov.co/wp-content/uploads/2026/03/16-feb-cuadernillo-de-preguntas-lectura-critica-saber-11-2026.pdf)). La plataforma cobra paletas (ingreso), así que publicar preguntas/imágenes literales del ICFES requiere **permiso escrito del ICFES**. Mientras no exista, `content/icfes/` queda fuera del build publicado. Alternativa segura: preguntas originales con el mismo formato.

## Documentos fuente disponibles
`docus/` contiene 38 PDFs (cuadernillos, guías, marcos, niveles, infografías y materiales complementarios). El pipeline ya generó transcripción por página, raster completo e índice de candidatos vectoriales en `work/`; las asociaciones gráficas y lecturas semánticas siguen pendientes de revisión.

## Pendientes
1. Verificar las transcripciones y asociar figuras candidatas a sus preguntas/contextos.
2. Revisar y completar las hojas pedagógicas de las otras 99 hojas borrador de las cinco pruebas estructuradas; Matemáticas tiene 49 revisadas y mat-i038 en borrador.
3. `content/marco.json` desde los marcos de referencia (competencias, afirmaciones, evidencias).
4. Banco propio: hoy ~43 preguntas; hacen falta ~254 para simulacros completos (preguntas originales, publicables).
5. Probar la voz en un celular real (nunca probada en dispositivo).
6. Migrar los 10 laboratorios que siguen en TS a JSON.
7. Fecha del examen al empezar; panel para profesores.
8. Fuera de alcance: Pagos, legal, PWA (no tocar).

## Preferencias de trabajo del dueño
Español informal ("tú"); mensajes finales concisos (enlace/archivo + un siguiente paso); ahorrar tokens; decir que la voz no se probó en dispositivo real; no guardar memoria sin preguntar.
