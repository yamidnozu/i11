# Informe de procesamiento: Matemáticas Saber 11 2026

## Checklist de trabajo

- [x] Leer `docs/CONTEXTO.md`, `docs/CHANGELOG.md`, `content/README.md`, `src/content/schema.ts`, scripts de importación/hojas y ejemplos `mat-101`, `mat-104`, `ing-101`.
- [x] Configurar y procesar exclusivamente el cuadernillo de Matemáticas (35 páginas; 50 preguntas).
- [x] Implementar runner con siete etapas persistidas, manifiesto, CLI, caché, configuración y plugin de cuadernillo.
- [x] Invalidar caché cuando cambian runner/plugin/configuración o herramienta de extracción.
- [x] Añadir validación de overrides e incorporar `propio` y `licenciado` al esquema de procedencias.
- [x] Instalar Poppler y extraer texto con `pdftotext -layout`.
- [x] Ejecutar reconstrucción limpia preservando overrides/hojas revisadas; comparar el JSON con corrida de caché.
- [x] Cotejar cinco rutas renderizadas (#/pregunta/mat-i001, i010, i020, i035, i050) y páginas rasterizadas.
- [x] Ejecutar `npx tsc --noEmit`, `VITE_ICFES=1 npx vitest run` y `npm run build`.
- [ ] Corregir números y fórmulas perdidos por el PDF/extracción y asociar figuras/opciones de forma fiel.
- [ ] Escribir explicaciones, distractores y hojas pedagógicas reales para las 50 preguntas; no son publicables como enseñanza mientras sean plantillas.
- [ ] Implementar parsers semánticos completos para marco, guía, lectura con imágenes y simulacro; actualmente son adaptadores temporales.
- [ ] Obtener afirmaciones/competencias desde un marco válido y asignar nivel con fundamento.
- [ ] Crear commits separados por etapa y por documento; hasta ahora hay commits agrupados del pipeline, Matemáticas y documentación.
- [ ] Procesar los demás documentos solo después del visto bueno establecido en el encargo original.

## Resultado actual

- 50 preguntas estructuradas, IDs `mat-i001`–`mat-i050`; clave detectada para las 50. El parser conserva dígitos aislados que pueden pertenecer a pasos y recorta pie/encabezado de página sin tragarse las opciones.
- 80 candidatos vectoriales en 35 páginas rasterizadas. La detección geométrica aún no equivale a figuras asociadas a preguntas.
- 28 preguntas marcadas con `revisar`; 22 no dispararon heurísticas, pero aún no se consideran validadas por persona. Quedan 7 preguntas con opciones gráficas representadas como huecos pendientes.
- Hojas: 50 borradores, 0 revisadas. Explicaciones y descartes docentes no están completos.
- Contenido en `content/icfes/mat/preguntas.json`, aún detrás de `icfes-gate`; archivos de trabajo bajo `work/`.

## Validación y reconstrucción

- `npx tsc --noEmit`: pasó.
- `VITE_ICFES=1 npx vitest run`: 15 archivos, 244/244 pruebas, sin fallos.
- `npm run build`: pasó; advertencia Vite por chunk principal de 902.56 kB sin comprimir (>300 kB).
- Se eliminó `work/<doc>` y la salida generada de `content/icfes/mat`, preservando overrides/hojas revisadas; se regeneraron las siete etapas con Poppler. SHA-256: `24a777642d65c7e6f14c44d3cd3fcbd9cd88833b13b5f4f97cadddece4f605f6`. La corrida inmediata en caché conservó el mismo hash.

El cotejo de la UI confirma mejoras con Poppler, pero no exactitud total: `mat-i010` conserva los números de paso tras corregir el limpiado y `mat-i035`/`mat-i050` ya muestran opciones textuales correctas. `mat-i050` todavía mezcla trazos de figura en el enunciado; siete reactivos mantienen opciones gráficas sin figura asociada. Las opciones gráficas todavía no se reconstruyen. Por tanto, el material sigue como borrador y las pruebas verdes validan estructura/formato, no fidelidad ni corrección pedagógica.

## Pendientes y límites

Los plugins `marco`, `guia`, `lectura_imagenes` y `simulacro_armado` aún reutilizan el parser de cuadernillo y no cumplen semánticamente el objetivo. Las hojas son esqueletos. No se procesaron otros PDFs. El código y los datos generados quedaron en cuatro commits locales; `saber11-repo.tar.gz` sigue sin rastrear y no se incluyó. No se hizo push.
