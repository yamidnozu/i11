# Changelog

## Pipeline documental inicial (2026-10)
- Añadido `tools/pipeline/` con siete etapas persistidas, manifiesto y caché que se invalida al cambiar el código/configuración; reconstrucción de Matemáticas determinista.
- Primera estructuración de 50 preguntas del cuadernillo Matemáticas 2026 bajo `content/icfes/mat/`; 28 requieren cotejo y las 50 hojas siguen en borrador.
- Procedencias `propio` y `licenciado` en el esquema; validación de IDs/campos y comprobación posterior de overrides.
- Vitest con ICFES: 244/244; `tsc --noEmit` y build pasan. Build avisa que el chunk principal supera 300 kB.
- `pdftotext` no está disponible; se usó PyMuPDF. El cotejo en cinco páginas renderizadas encontró errores de extracción pendientes. Ver `informe_icfes.md`.

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
