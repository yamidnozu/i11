# Encargo para Antigravity (Gemini 3.8) — Saber 11 interactivo

Trabajas de forma autónoma: toma tú las decisiones, no esperes aprobación. El dueño (Yamid) revisará el resultado al final.

## Objetivo
Llevar la plataforma Saber 11 (Pre-ICFES) a un estado listo para lanzar al público gratis y de forma legal, con la mejor calidad posible. Lee primero `docs/CONTEXTO.md`, `docs/FUNCIONALIDADES_Y_PRUEBA.md`, `README.md` e `informe_icfes.md`.

## Prioridades (en orden)
1. **Banco propio y original** (lo más importante): como el contenido literal del ICFES no se puede publicar con fines de lucro (ver "Licencia ICFES" en CONTEXTO.md), crea preguntas ORIGINALES con el mismo formato y estilo Saber 11 para las 5 áreas (Matemáticas, Lectura Crítica, Sociales y Ciudadanas, Ciencias Naturales, Inglés). Meta: al menos 40 por área, con clave correcta verificada, explicación, distractores y hoja pedagógica que cumpla las reglas probadas por los tests. Español colombiano natural. No copies enunciados del ICFES.
2. **Simulacros completos** armados solo con el banco original, con experiencia de examen real.
3. **Calidad del producto**: revisa en el navegador (vista celular 390x844 y escritorio) los flujos de diagnóstico, práctica, simulacro, aprender y progreso; corrige errores, textos confusos y diseño. Sin scroll en la vista de pregunta (modo foco).
4. Pendientes del README que aporten valor (laboratorios faltantes, etc.) si queda tiempo.

## Reglas obligatorias
- Trabaja SOLO en la rama `antigravity/v1`. Nunca toques `main`, nunca hagas force-push.
- Haz commits pequeños y descriptivos en español y `git push -u origin antigravity/v1` al final de cada bloque grande.
- NO despliegues nada (nada de `wrangler pages deploy`, `wrangler d1`, `wrangler secret`, ni publicar).
- NO leas ni imprimas secretos (`.dev.vars`, `.env*`, tokens). NO cambies la lógica de pagos Wompi ni de acceso/seguridad.
- `content/icfes/` debe seguir fuera del build normal (gate `VITE_ICFES=1`).
- Antes de cada commit: `npx tsc --noEmit` y `npx vitest run` deben pasar; `VITE_FREE_MODE=1 npx vite build` debe compilar.
- No inventes datos oficiales ni digas que algo es oficial del ICFES.

## Al terminar
Escribe `ANTIGRAVITY_REPORT.md` en español sencillo: qué hiciste, cuántas preguntas nuevas por área, qué probaste, qué falta y capturas en `docs/capturas/`. Haz commit y push.
