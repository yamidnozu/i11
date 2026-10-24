# PRIORIDAD YA — Sección Odontología (Endodoncia)

Yamid pidió (24 oct 2026, ~3:10 PM Bogotá): **parar lo anterior** y agregar una sección nueva de estudio de odontología a partir del PDF/transcripción de clase. Cuando esté incluida: **commit + push** a `antigravity/v1` (eso publica solo en https://icfes.edevcore.com). Avisar al terminar. Sin pedir aprobación.

## Fuente (obligatoria)
- PDF: `docs/fuentes/endodoncia-clase1-3corte.pdf`
- Texto extraído: `docs/fuentes/endodoncia-clase1-3corte.txt` (transcripción Clase 1 – endodoncia 3er corte)

Extrae temas, criterios clínicos y enseñanzas del profesor. **No copies texto largo al pie de la letra** si suena a conversación cruda: reescríbelo en lenguaje claro de estudio. Inventa **casos clínicos originales** coherentes con la clase (no copies pacientes reales de la grabación).

## Qué construir
1. **Nueva área / sección visible** en la app, al mismo nivel que Matemáticas / Lectura / etc., con nombre claro: **Odontología** (o **Endodoncia** si queda mejor en el menú). Id sugerido: `odontologia`.
2. Banco de **preguntas de opción múltiple** + **casos clínicos** (mínimo **25–40** ítems para empezar), cubriendo al menos:
   - Motivo de consulta y problema actual (inicio, localización, intensidad 0–10, duración, frecuencia, desencadenantes, alivio, espontaneidad, dolor nocturno)
   - Análisis del dolor (agudo/sordo/pulsátil; pulpar vs periapical)
   - Examen extraoral e intraoral (simetría, edema, fístulas extra/intraorales, caries, restauraciones, fracturas, color, tejidos blandos/periodontales)
   - Pruebas pulpares: frío, calor, eléctrica (qué indican; pulpa normal vs pulpitis irreversible vs necrosis; aislamiento relativo)
   - Percusión y palpación; movilidad; evaluación periodontal
   - Radiografía como **ayuda**, no como diagnóstico solo
   - Diagnóstico pulpar (normal, pulpitis reversible, irreversible sintomática/asintomática, necrosis)
   - Diagnóstico apical (incl. periodontitis apical, osteítis condensante si aparece en la fuente)
   - Dolor referido
   - Protocolo / formato clínico básico (tablas, hallazgos coherentes; sin inventar hallazgos contradictorios)
3. **Cada pregunta** debe tener el **mismo flujo pedagógico** que el resto de la plataforma en práctica:
   - opciones + clave correcta verificada
   - explicación
   - razones específicas por distractor (nada de plantillas tipo "Es incorrecta porque…")
   - hoja / pistas / pasos / guion / niveles del profesor (el mismo esquema que usan las otras áreas: `hoja`, `guion`, `pasos`, `enfoque`, etc.)
   - casos clínicos con enunciado rico (paciente, síntoma, hallazgos) y pregunta de decisión diagnóstica o de procedimiento de examen
4. UI: la sección debe aparecer en **Práctica** (y mapa/ruta si aplica), usable en **móvil**, con coachmarks si ya existen para otras áreas.
5. Textos en **español sencillo**, tono de estudio clínico para estudiante de odontología colombiano.

## Cómo trabajar (en bloque)
- Extiende `AreaId` / `AREAS` / carga de `content/questions/` / hojas asociadas.
- Genera JSON por scripts cuando puedas; verifica con tests existentes; un commit claro; `git pull --rebase` y `git push` a `antigravity/v1`.
- **NO** toques `main`, **NO** deploys manuales, **NO** secretos, **NO** actives `VITE_ICFES` en el build público, **NO** pagos.
- Si el ENCARGO_COMPLETAR / ronda de corrección ICFES estaba a medias: **deja eso pausado**; esta sección odontología es primero. Después se retoma.

## Criterio de listo
- Sección visible en la app local y, tras el push, en https://icfes.edevcore.com
- ≥25 preguntas/casos con flujo completo
- `ANTIGRAVITY_REPORT.md` menciona odontología con números honestos (cuántas preguntas, qué temas)
