# Changelog

## Pipeline documental inicial (2026-10)
- Añadido `tools/pipeline/` con siete etapas persistidas, caché por hash/código/configuración y plugins para cuadernillos, marcos, guías, infografías y simulacros.
- Procesados los 38 PDFs disponibles: 1.209 páginas, 4.201 candidatos vectoriales, 222 preguntas con clave y 26 en pendientes de clave. Las transcripciones no semánticas se guardan por página en `documento.json`.
- Matemáticas: 50 preguntas; 29 marcadas, 11 con opciones gráficas sin asociar; 50 hojas borrador.
- Esquema ampliado con procedencias `propio` y `licenciado`; validación de overrides y exclusión de transcripciones completas del glob de preguntas de la app.
- Poppler usa `pdftotext -layout`. Vitest con ICFES: 416/416; `tsc --noEmit` y build pasan. Vite advierte que el chunk principal supera 300 kB. Ver `informe_icfes.md`.

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
