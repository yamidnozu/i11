# Changelog

## Pipeline documental inicial (2026-10)
- Añadido `tools/pipeline/` con siete etapas persistidas, caché por hash/código/configuración y plugins para cuadernillos, marcos, guías, infografías y simulacros.
- Procesados los 38 PDFs disponibles: 1.209 páginas, 4.201 candidatos vectoriales, 222 preguntas con clave y 26 en pendientes de clave. Las transcripciones no semánticas se guardan por página en `documento.json`.
- Matemáticas: 50 preguntas; una pregunta marcada por una ambigüedad de datos; alternativas recuperadas; 49 hojas revisadas y una en borrador (mat-i038 sigue en revisión por ambigüedad de la tabla).
- Esquema ampliado con procedencias `propio` y `licenciado`; validación de overrides y exclusión de transcripciones completas del glob de preguntas de la app.
- Poppler usa `pdftotext -layout`. Vitest con ICFES: 416/416; `tsc --noEmit` y build pasan. Vite advierte que el chunk principal supera 300 kB. Ver `informe_icfes.md`.

## Pipeline documental — revisión de Sociales, Lectura y Ciencias (2026-10-22)
- Recuperadas por override las claves oficiales de 13 preguntas en cada cuadernillo de Ciencias 2025 y 2026; quedan 50 preguntas por cuadernillo, sin claves pendientes.
- Las 13 hojas revisadas de Ciencias 2026 se reutilizaron para 2025 solo después de comprobar igualdad exacta de enunciado, opciones y clave. Cada copia conserva su estado y contenido revisado.
- Cotejados visualmente los recortes de pregunta en ambas pruebas de Ciencias; se limpiaron avisos de figura ya asociada. Se mantienen pendientes las opciones gráficas que aún necesitan recorte individual y enlaces específicos al marco.
- Recuperadas literalmente las opciones de 14 preguntas de Sociales que se habían confundido con imágenes; se eliminaron sus falsos placeholders gráficos.
- Asociada la infografía de tránsito de la página 36 de Lectura Crítica a un único bloque compartido por las preguntas 42–49; corregidos números de página capturados como parte de opciones.
- El detector de símbolos ya no marca usos ordinarios de “tan”. `enriquecer` crea como máximo diez hojas por lote y reanuda sin reemplazar hojas existentes.
- El parser de cuadernillos elimina los números de página pegados al final de la última opción, preservando opciones que sí son números (verificado, por ejemplo, en `cie-i016`).
- Los recortes compartidos pueden declararse con página y rectángulo en `recorteFuente`; la etapa `figuras` reconstruye PNG desde el PDF y registra la salida, de modo que borrar `work/` y el PNG no elimina la receta.
- Validación: `npx tsc --noEmit` y `VITE_ICFES=1 npx vitest run` (442/442) pasan. El informe separa lo terminado de las revisiones pedagógicas, gráficas y de licencias aún abiertas.


## Pipeline documental — lote pedagógico de Ciencias (2026-10-22)
- Se revisaron ocho hojas (preguntas 2, 11, 12 y 17 de los cuadernillos 2025 y 2026), con razonamiento, descarte individual de distractores y comprobación del contexto.
- Para el salto bungee se cotejó la longitud natural de la banda con la distancia de caída; como aún no se estira, la transformación corresponde a energía gravitacional a cinética.
- El total sube a 83 hojas revisadas y baja a 165 borradores; las alternativas gráficas, las evidencias del marco y otras hojas aún requieren trabajo.
- Validación tras el lote: `npx tsc --noEmit` y `VITE_ICFES=1 npx vitest run` (442/442).


## Pipeline documental — segundo lote pedagógico de Ciencias (2026-10-22)
- Se revisaron preguntas de traducción del ARN, transferencia de electrones, sensibilidad a antibióticos y calor específico, con solución y descarte individual de distractores en ambos cuadernillos.
- Se comprobó que enunciado, opciones y clave coinciden entre las ediciones 2025 y 2026 antes de reutilizar las hojas.
- El acumulado queda en 91 hojas revisadas y 157 borradores; continúan pendientes las opciones gráficas, los enlaces a evidencias del marco y las hojas restantes.


## Pipeline documental — tercer lote pedagógico de Ciencias (2026-10-22)
- Se añadieron soluciones completas para la transcripción de proteínas, la velocidad del sonido en agua y aire y la presión atmosférica en altura.
- Se verificaron las hojas existentes de configuración electrónica, fuerzas, presión atmosférica y mezclas; esas cuatro ya estaban revisadas y no se reemplazaron.
- Acumulado actual: 99 hojas revisadas y 149 borradores.


## Pipeline documental — cuarto lote pedagógico de Ciencias (2026-10-22)
- Se añadieron hojas razonadas para solubilidad, clasificación de fases y controles experimentales, sin reemplazar las hojas que ya estaban revisadas.
- Se cotejaron las diferencias menores de OCR entre los cuadernillos de ambos años; la pregunta de clasificación conserva la misma observación, alternativas y clave.
- Acumulado actualizado: 105 hojas revisadas y 143 borradores.


## Pipeline documental — quinto lote pedagógico de Ciencias (2026-10-22)
- Se completaron hojas de análisis de contaminantes, herencia, ondas, manejo de residuos y acidez, con descarte individual de distractores.
- Se mantuvo como borrador la pregunta sobre memoria espacial en ratones porque su justificación depende de cotejar la figura original.
- Acumulado actualizado: 115 hojas revisadas y 133 borradores.


## Pipeline documental — sexto lote pedagógico de Ciencias (2026-10-22)
- Se cotejaron con el PDF original las gráficas de tendencia, calentamiento y electroforesis, y el esquema de trayectorias de los ratones.
- Se completaron cuatro soluciones con lectura explícita de esos apoyos, sin depender de la transcripción plana.
- Acumulado: 123 hojas revisadas y 125 borradores.

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
