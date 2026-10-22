# Saber 11 interactivo (Pre-ICFES)

Plataforma independiente, **no oficial del ICFES**. Los puntajes son **estimaciones**. Contenido original.

## Ejecutar
```
npm install
npm test                         # 47 tests (matemática, física, química, adaptativo, Wompi, contenido)
VITE_FREE_MODE=1 npm run dev     # modo libre (sin pago) para desarrollo
npm run build
```
## Despliegue (Cloudflare Pages + D1)
1. `wrangler d1 create saber11` → `database_id` en `wrangler.toml`; `npm run db:init`.
2. Secretos (nunca en el repo): `wrangler pages secret put WOMPI_PUBLIC_KEY | WOMPI_PRIVATE_KEY | WOMPI_INTEGRITY_SECRET | WOMPI_EVENTS_SECRET`.
3. Ajusta `SITE_URL` y `WOMPI_API`. En Wompi, URL de eventos: `https://TU-DOMINIO/api/pay/webhook`.
4. `npm run build && wrangler pages deploy dist`.

## Incluye
- Motor de simuladores declarativo (`src/core`): params, lógica pura, Canvas, gráficas, tabla, retos verificables, registro validado. Añadir uno = crear un `SimConfig` y registrarlo en `src/sims/index.ts`.
- 11 simuladores: proyectil (RK4+bisección), MRUA, Ohm, lentes, gases, funciones (parser seguro), balanceo (fracciones exactas), Punnett, Lotka-Volterra, probabilidad, estadística.
- Adaptativo: IRT 3PL + EAP, información de Fisher, Elo con incertidumbre, repaso espaciado tipo FSRS, racha, puntajes por área/global con error.
- Diagnóstico gratis; práctica, lecciones y simulacro (con checkpoint) con acceso de pago; panel con resumen para acudiente.
- Wompi: firma de integridad en servidor, webhook con checksum, actualización idempotente, consulta con llave privada, consentimiento de acudiente.
- PWA (manifest + service worker), teclado/aria-live, botones ±, paleta Okabe-Ito.

## Pendiente / límites (honesto)
- Banco semilla: 27 preguntas y 2 lecciones originales. Falta el volumen real: generar con Claude (con verificación + revisión docente). `tools/generate` NO está implementado aún.
- No implementados: geometría arrastrable, energía, ondas, átomo, célula, redes tróficas, mapa de Colombia (requiere GeoJSON del IGAC), IndexedDB completo (hoy localStorage), icono PNG.
- Lectura, inglés (voz del navegador), tutela y línea de tiempo son versiones simples.
- Verificar antes de lanzar: ponderaciones del puntaje global y calibración (`src/adaptive/areas.ts`) — aproximaciones de la investigación, no datos oficiales; revisión legal (Habeas Data, retracto); pruebas reales en sandbox de Wompi.
- Etiquetas de ejes en canvas pequeñas en pantallas muy angostas.
