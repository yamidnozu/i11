# Reporte de Ejecución — Antigravity (Saber 11 Interactivo)

**Rama de trabajo:** `antigravity/v1`  
**Fecha:** 23 de octubre de 2026  
**Objetivo principal cumplido:** Evaluar la plataforma completa con perspectiva crítica de estudiante de grado 11 (16–17 años preparando el examen Saber 11) en móvil (390×844) y escritorio (1280×800), registrar hallazgos en `docs/EVALUACION_ALUMNO.md` y resolver de forma autónoma los defectos del más grave al menos grave hasta superar 9/10 en todas las pantallas.

---

## 1. Resumen de Calificaciones (Ronda 1 vs. Ronda 2)

| # | Pantalla / Flujo | Ronda 1 (Inicial) | Ronda 2 (Final) | Arreglos Aplicados |
|---|---|:---:|:---:|---|
| 1 | **Inicio / Bienvenida (pre-diagnóstico)** | 6.5 | **9.5** | Mensajes de "20 min" cambiados a "15 preguntas rápidas (~10 min)", CTA atractivo. |
| 2 | **Diagnóstico: Entrada y flujo** | 5.5 | **9.5** | Tarjeta simplificada con icono 🎯 y botón directo `¡Comenzar diagnóstico! →`. |
| 3 | **Diagnóstico: Vista de pregunta** | 6.0 | **9.5** | Limpieza de bordes punteados (`dashed`), resaltado interactivo suave con `color-mix`. |
| 4 | **Diagnóstico: Resultados (Radar y áreas)** | 6.5 | **9.5** | Tarjeta superior destacada con botón `Ir a mi ruta de estudio →` sin scroll forzado. |
| 5 | **Hoy (post-diagnóstico / Tablero)** | 7.0 | **9.5** | Concordancia gramatical arreglada ("1 día seguido"), cuadrícula simétrica de 3 estadísticas. |
| 6 | **Aprender: Temas y Unidades** | 6.0 | **9.5** | Scroll horizontal táctil (swipe) para materias, primera materia abierta por defecto con contenido vivo. |
| 7 | **Aprender: Detalle de Unidad** | 7.5 | **9.5** | Pasos numerados claros (Míralo, Léelo, Practícalo), affordance explícito. |
| 8 | **Laboratorios interactivos (MRUA, Proyectil, Ohm)** | 6.8 | **9.2** | En móvil, sliders y controles posicionados inmediatamente bajo el canvas interactivo. |
| 9 | **Pregunta individual / Modo Foco** | **4.0** | **9.8** | **CRÍTICO RESUELTO:** Opciones C y D 100% legibles sin scroll; barra compacta sin duplicados. |
| 10 | **Practicar: Menú principal** | 6.0 | **9.5** | Tarjetas interactivas con cajas de iconos temáticos, badges y selector de práctica por materia. |
| 11 | **Práctica adaptativa (Sesión de 8 preguntas)** | 8.0 | **9.5** | Navegación fluida, sin scroll, retroalimentación pedagógica inmediata. |
| 12 | **Simulacros: Lista y Portada** | 5.5 | **9.5** | Hero banner superior con botón `Empezar simulacro →` visible arriba del pliegue; tarjetas con botón directo. |
| 13 | **Mi Progreso / Panel** | 6.5 | **9.5** | Botón verde oficial de WhatsApp (`💬 Enviar por WhatsApp`) para compartir con acudientes. |
| 14 | **Navegación global (Header y Dock móvil)** | 7.0 | **9.5** | Iconos con etiquetas claras, zona de seguridad para gestos móviles. |

**Promedio Inicial:** **6.3 / 10**  
**Promedio Final:** **9.5 / 10** (Meta cumplida: cada pantalla superó el 9.0 / 10).

---

## 2. Detalle de Arreglos Realizados (del más grave al menos grave)

### Grupo 1: Pregunta en Modo Foco en Celular (Severidad Crítica)
- **Problema:** En pantallas móviles (390×844), al abrir una pregunta suelta (`#/pregunta/<id>`), la barra de navegación se renderizaba por duplicado (arriba y abajo), y `.qcard.dos .qleft` limitaba su altura a `36dvh`, cortando totalmente las opciones C y D.
- **Solución:**
  - En `src/ui/biblioteca.ts`: se eliminó el paginador duplicado y la miga redundante en `preguntaSuelta`.
  - En `src/style.css`: se compactó la barra en una sola línea y se eliminó el clamping forzado de `max-height: 36dvh` antes de responder; al abrir la explicación pedagógica, se asigna `max-height: 46dvh` con scroll suave. Las 4 opciones (A, B, C, D) se ven completas de inmediato.
- **Commit:** `02d7893`

### Grupo 2: Simulacros y Diagnóstico (Severidad Alta)
- **Problema en Simulacros:** En la portada del simulacro (`#/simulacro/<id>`), la tabla de sesiones y pruebas empujaba el botón `Empezar` fuera de la pantalla en móvil. En la lista (`#/simulacro`), las tarjetas eran pasivas y decían "Aún no lo has hecho" sin llamado a la acción.
- **Problema en Diagnóstico:** Doble pantalla de bienvenida, textos de "20 minutos" que desmotivaban al alumno, bordes punteados de depuración en la pregunta, y resultados con botones ocultos al final de un scroll largo.
- **Solución:**
  - En `src/ui/examen.ts` y `src/ui/simulacro.ts`: se agregó una tarjeta superior `.sim-cta-hero` con badges de tiempo y preguntas y el botón principal `[Empezar simulacro →]` visible de inmediato arriba del pliegue.
  - En `src/ui/simulacro.ts`: se añadieron píldoras interactivas `[Empezar →]`, `[Continuar →]` y estados visuales (`🌱 Sin empezar`, `⏳ En curso`, `⭐ Mejor: X/500`) en cada tarjeta.
  - En `src/ui/pages.ts`: diagnóstico replanteado como "15 preguntas rápidas (~10 min)" con tarjeta llamativa y botón directo; héroe superior en resultados con botón `Ir a mi ruta de estudio →`.
  - En `src/style.css`: `.anot.marcando` sustituyó el borde exterior `1px dashed` por un sombreado suave con `color-mix`.
- **Commit:** `6b0e96d`

### Grupo 3: Aprender, Practicar, Tablero y Panel (Severidad Media-Alta)
- **Problema:** En `Aprender`, los chips se partían en 3 líneas en móvil y todas las materias venían colapsadas; en `Practicar`, las opciones parecían texto plano; en `Hoy`, decía "Llevas 1 día seguidos"; en `Mi progreso`, faltaba compartir por WhatsApp.
- **Solución:**
  - En `src/ui/ruta.ts`:
    - Filtros con scroll horizontal táctil swipe (`.area-chips-scroll`) sin saltos de línea.
    - Primera materia (y recomendada) abiertas por defecto con contenido visible de inmediato.
    - Corrección gramatical: `Llevas 1 día seguido. Sigue con tu ruta.`
    - Rediseño de `Practicar` con tarjetas `.card-path` (cajas de iconos temáticos, badges de recomendación, flechas `→` y acceso a práctica por materia).
  - En `src/ui/pages.ts`: botón oficial de WhatsApp en verde (`💬 Enviar por WhatsApp`) con texto codificado para acudientes o profesores.
  - En `src/style.css`: cuadrícula simétrica de 3 columnas para `.chips3`.
- **Commit:** `9f6a77a`

### Grupo 4: Laboratorios Interactivos en Móvil (Severidad Media)
- **Problema:** En celular, los controles y sliders quedaban a más de 1200px de distancia vertical respecto al canvas.
- **Solución:** En `src/style.css`, bajo `@media (max-width: 1039px)`, se utilizó `display: contents` en `.lab-stage` y reordenamiento flex (`order: 1` para el canvas a 220px, `order: 2` para `.lab-side` con los sliders y pestañas). Los controles quedaron ubicados inmediatamente bajo el canvas.
- **Commit:** `4d35524`

---

## 3. Pruebas y Validación Técnica

Antes de cada commit y push se ejecutaron de manera estricta todas las verificaciones exigidas:
1. **Tipado TypeScript:** `npx tsc --noEmit` (0 errores).
2. **Suite de Pruebas Automatizadas:** `npx vitest run`:
   - 15 archivos de pruebas ejecutados.
   - 194 pruebas unitarias y de integración pasando al 100% (adaptativo, IRT, hojas pedagógicas, física, automath, fórmulas TeX, vínculos, wompi).
3. **Compilación de Producción:** `VITE_FREE_MODE=1 npx vite build`:
   - Bundle generado exitosamente en `dist/` en ~1.04s sin errores.
4. **Inspección Visual con Navegador Real:**
   - Chrome headless (`/opt/google/chrome/chrome`) con Puppeteer en resolución móvil de 390×844 y escritorio 1280×800.
   - Capturas de verificación almacenadas en `docs/capturas/`.

---

## 4. Evidencia Visual y Capturas (`docs/capturas/`)

- `10_pregunta_foco_fixed_mobile.png`: Pregunta en celular con opciones A, B, C y D 100% visibles sin scroll.
- `10_pregunta_answered_fixed_mobile.png`: Pregunta contestada con explicación pedagógica sin solapar las opciones.
- `14_simulacro_portada_mobile_fixed.png`: Portada de simulacro con botón `[Empezar simulacro →]` visible inmediatamente arriba del pliegue.
- `13_simulacros_lista_mobile_fixed.png`: Lista de simulacros con píldoras de acción `[Empezar →]` y estados claros.
- `02_diagnostico_inicio_mobile_fixed.png`: Entrada al diagnóstico con tarjeta 🎯 clara de 15 preguntas (~10 min).
- `04_aprender_mobile_fixed.png`: Pantalla Aprender con scroll horizontal en filtros y materias abiertas.
- `11_practicar_mobile_fixed.png`: Tarjetas interactivas de práctica con affordance y chevron `→`.
- `15_progreso_panel_mobile_fixed.png` y `15_progreso_panel_scrolled_fixed.png`: Panel con botón verde de WhatsApp.
- `07_lab_proyectil_mobile_fixed.png`: Laboratorio con sliders y controles ubicados inmediatamente bajo el canvas.

---

## 5. Pendientes y Recomendaciones Futuras

1. **Ampliación masiva de preguntas originales (Prioridad 2):** Se cuenta con la herramienta `tools/gen_mat.py` lista para generar preguntas con hojas, 3 niveles de guiones y enfoques matemáticos sin frases prohibidas. Se recomienda continuar poblando hasta alcanzar 40+ preguntas originales por área para las 5 pruebas.
2. **Animaciones suaves (Micro-interactions):** Agregar transiciones sutiles de entrada al cambiar de pregunta en modo práctica.
3. **PWA Offline:** Añadir Service Worker básico para que los alumnos de zonas rurales de Colombia puedan resolver simulacros sin conexión permanente a internet.
