# Informe de procesamiento: Matemáticas Saber 11 2026

## Checklist de trabajo

- [x] Leer `docs/CONTEXTO.md`, `docs/CHANGELOG.md`, `content/README.md`, `src/content/schema.ts`, scripts de importación/hojas y ejemplos `mat-101`, `mat-104`, `ing-101`.
- [x] Inspeccionar solo el cuadernillo de Matemáticas configurado; no se procesaron los demás PDFs.
- [x] Implementar runner con siete etapas persistidas, manifiesto, CLI, caché, configuración y plugin de cuadernillo.
- [x] Invalidar la caché cuando cambian runner/plugin/configuración.
- [x] Reanudar generación de 50 hojas borrador, preservando hojas revisadas y overrides.
- [x] Añadir validación de overrides e incorporar `propio` y `licenciado` al esquema de procedencias.
- [x] Ejecutar reconstrucción limpia de Matemáticas y comprobar salida determinista.
- [x] Revisar cinco páginas rasterizadas y sus rutas renderizadas: `mat-i001`, `mat-i010`, `mat-i020`, `mat-i035`, `mat-i050`.
- [x] `npx tsc --noEmit`, `VITE_ICFES=1 npx vitest run` y `npm run build`.
- [ ] Conseguir texto fiel con `pdftotext -layout`; no está instalado en este entorno y el respaldo actual pierde símbolos/dígitos.
- [ ] Corregir la extracción estructural y asociar figuras/opciones con preguntas, verificando cada recorte contra el PDF.
- [ ] Elaborar soluciones, explicaciones y descartes reales para las 50 hojas. No inventar razonamientos: siguen en borrador hasta resolver y revisar cada pregunta.
- [ ] Implementar extractores semánticos funcionales para marcos, guías, lecturas con imágenes y simulacros; hoy son adaptadores provisionales.
- [ ] Generar afirmaciones/competencias desde un marco válido y asignar nivel sustentado.
- [ ] Hacer commits separados por etapa y por el documento procesado.
- [ ] Procesar otros documentos solo después del visto bueno previsto en el encargo original.

## Resultado actual

- Documento: `docus/01_Matematicas_Saber11_2026_ICFES.pdf`, 35 páginas, hash registrado en `docus/manifest.json`.
- Preguntas estructuradas: 50 (`mat-i001`–`mat-i050`); 50 claves detectadas.
- Marcadas para revisión: 28; errores detectados visualmente en fórmulas, dígitos y clasificación de algunas opciones. Las candidatas vectoriales todavía no están asociadas con seguridad a cada pregunta.
- Hojas: 50 borradores, 0 revisadas. Explicaciones y descartes docentes siguen pendientes.
- Contenido ICFES en `content/icfes/mat/preguntas.json`; el plugin `icfes-gate` conserva el gate de build. Páginas completas y trazos están bajo `work/`.

## Validación y reconstrucción

`npx tsc --noEmit`: pasó. `VITE_ICFES=1 npx vitest run`: 15 archivos, 244 pruebas aprobadas, sin fallos. `npm run build`: pasó; Vite avisa que el chunk JS principal (904.39 kB sin comprimir) supera 300 kB.

Se borraron `work/<doc>` y archivos generados en `content/icfes/mat`, conservando overrides y hojas revisadas; la regeneración completa dio SHA-256 `f21f70b9f0baea6161a0404b91fdea0c2f653224121f05fb9ba4e94af9b5415b`. Una ejecución inmediata en caché mantuvo el mismo SHA-256.

El cotejo visual encontró que el resultado no está listo para publicarse ni para usarse como banco de estudio: en `mat-i010`, `mat-i035` y `mat-i050` se perdieron o alteraron datos del enunciado; en `mat-i035`/`mat-i050` las opciones están marcadas como gráficas sin reconstrucción fiel. Por eso siguen pendientes corrección contra fuente y autoría pedagógica, aunque el validador de forma y la suite pasen.

## Pendientes y límites

`pdftotext` no está en el PATH. El extractor usa PyMuPDF, no la extracción literal solicitada. Los plugins de marco/guía/lectura/simulacro no son parsers completos. Las hojas generadas son esqueletos, no soluciones. No procesé otros PDFs. No se ha hecho todavía ningún commit de esta entrega.
