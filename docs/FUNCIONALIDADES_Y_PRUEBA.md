# Funcionalidades y prueba guiada

Esta guía describe lo que ofrece hoy la plataforma y cómo hacer un recorrido manual básico pero completo. Está dirigida a quien quiera conocer el producto o comprobar sus flujos principales en un navegador.

## 1. Qué es la plataforma

Saber 11 es una plataforma web de preparación para el examen Saber 11. Incluye estudio por temas, preguntas, simulacros, laboratorios interactivos y seguimiento del progreso. Los puntajes son estimaciones pedagógicas, no resultados oficiales del ICFES.

La aplicación está construida con Vite y TypeScript. La interfaz navega mediante rutas hash (`#/...`). Las respuestas y el avance se guardan principalmente en `localStorage` del navegador.

## 2. Funcionalidades disponibles

### Inicio y ruta de estudio

- **Hoy** presenta el diagnóstico inicial o, después de completarlo, un tablero con la actividad sugerida, la racha, un puntaje estimado y el nivel por área.
- El **diagnóstico** contiene 15 preguntas adaptativas, tres por área. Al terminar muestra un resumen por área y permite ir a la ruta o al panel de progreso.
- **Mapa de la plataforma** ofrece accesos directos a las actividades y recorridos disponibles.

### Aprender

- **Temas y unidades** organizan el estudio por área y tema. Según el contenido disponible, una ruta puede incluir laboratorio, lección y práctica guiada.
- **Laboratorios** permiten explorar modelos y simulaciones interactivas. La lista y el alcance dependen de los simuladores registrados en el proyecto.
- **Lecciones** presentan contenido explicativo.
- **Preguntas** muestran enunciado, opciones, figuras o tablas, respuesta y explicación cuando esos datos están disponibles. Algunas incluyen una hoja pedagógica con enfoque, marcas, pasos y guion del profe en tres niveles.
- Las preguntas individuales tienen navegación anterior/siguiente cuando pertenecen a una secuencia y permiten volver a su banco.
- El banco oficial del ICFES solo aparece cuando se habilita explícitamente con `VITE_ICFES=1`. Consulta la sección de contenido oficial antes de compilar o distribuirlo.

### Practicar

- **Sesión de práctica** propone ocho preguntas adaptadas al nivel estimado. Informa el resultado al responder y termina con un resumen y preguntas por repasar.
- Se puede filtrar la práctica por área y hacer una sesión de repaso espaciado cuando hay preguntas pendientes.
- **Simulacros** presentan cuadernillos con secciones, reloj, guardado del avance, navegación por preguntas, revisión y resultado estimado. El formato y la cantidad de preguntas dependen del simulacro elegido.
- El **diagnóstico** se puede repetir para actualizar la estimación del nivel por área.
- **Actividades** reúne ejercicios complementarios de lectura, inglés, ciudadanía y línea de tiempo, según el contenido habilitado.

### Progreso y preferencias

- **Mi progreso** resume respuestas, racha, repasos pendientes y estimaciones por área cuando ya hay actividad registrada.
- La interfaz incluye tema claro/oscuro, controles accesibles por teclado y paletas de color. Algunas paletas pueden estar restringidas según la configuración de acceso.
- En dispositivos compatibles, el proyecto incluye manifest y service worker para capacidades PWA.

## 3. Preparar una ejecución local

Requisitos: Node.js/npm compatibles con el proyecto y, para procesar documentos, Python y las dependencias descritas en `tools/pipeline/README.md`.

Desde la raíz del repositorio:

```sh
npm install
npm run dev
```

Abre la URL local que muestra Vite (normalmente `http://localhost:5173`). Para comprobar el build de producción:

```sh
npm run build
npm run preview
```

El build normal mantiene apagado el contenido oficial del ICFES. Para una comprobación local que necesite ese banco, inicia Vite con `VITE_ICFES=1`; en PowerShell:

```powershell
$env:VITE_ICFES = '1'
npm run dev
```

El contenido oficial debe permanecer bajo `content/icfes/`. Revisa `docs/CONTEXTO.md` y `content/README.md` para las condiciones de uso y el gate de publicación. No distribuyas ese contenido comercialmente sin el permiso escrito requerido.

## 4. Recorrido manual básico pero completo

Haz este recorrido en una ventana normal del navegador. Usa respuestas de prueba: la actividad modifica el progreso guardado localmente.

### A. Inicio y diagnóstico

1. Abre la raíz de la aplicación. En una instalación sin diagnóstico previo debe aparecer la bienvenida.
2. Selecciona **Empezar el diagnóstico (gratis)**.
3. Comprueba que aparece una pregunta con cuatro opciones y un indicador de avance `1 / 15`.
4. Elige una opción. Debe habilitarse el botón **Siguiente**; antes de elegir, el sistema pide seleccionar una respuesta.
5. Responde las 15 preguntas y selecciona **Ver resultado** al final.
6. Comprueba que aparece el resultado por áreas y que están disponibles **Ver mi ruta de estudio** y **Ver mi progreso**.

### B. Estudio por tema y pregunta

1. Ve a **Aprender** y abre un área.
2. Entra a un tema disponible. Revisa los pasos que ofrece, como laboratorio, lección o práctica.
3. Abre una pregunta y comprueba que se ven el enunciado, las opciones y, si aplica, sus figuras o tablas.
4. Selecciona una opción. La respuesta debe mostrar retroalimentación y la explicación correspondiente.
5. En una ruta individual de pregunta, verifica **Siguiente**, **Anterior** cuando corresponda y el enlace para volver al banco.

### C. Sesión de práctica

1. Ve a **Practicar** y elige **Sesión de práctica**; también puedes elegir una materia.
2. Responde las ocho preguntas. La siguiente pregunta solo debe habilitarse después de elegir respuesta o consultar la solución.
3. Al finalizar, verifica el total correcto, la lista de temas o preguntas por repasar si hubo errores y los accesos para volver o iniciar otra sesión.

### D. Simulacro

1. Desde **Practicar**, abre un simulacro disponible.
2. Revisa su resumen de secciones, cantidad de preguntas y tiempos. Selecciona **Empezar**.
3. En una prueba corta, responde una pregunta y comprueba que el simulacro avanza sin mostrar retroalimentación inmediata.
4. Recarga la página o vuelve al simulacro. Si el intento quedó guardado, debe ofrecer **Continuar donde iba**.
5. Termina el simulacro. Revisa el puntaje estimado, el resultado por área y el resumen de respuestas.

### E. Progreso y persistencia

1. Abre **Mi progreso**. Comprueba que refleja las respuestas y el puntaje estimado generados durante el recorrido.
2. Recarga la página. La actividad guardada en ese navegador debe seguir disponible.
3. Cambia el tema visual o abre el selector de paletas y confirma que la interfaz responde.

## 5. Criterios para dar el recorrido por correcto

- La aplicación inicia sin errores visibles en la consola del navegador.
- Los enlaces principales abren Inicio, Aprender, Practicar y Progreso.
- Diagnóstico y sesión permiten avanzar después de responder y muestran su resumen al terminar.
- Una pregunta presenta correctamente su contenido disponible y su retroalimentación.
- El simulacro conserva el intento al recargar y produce un resultado al finalizar.
- El panel muestra actividad después de completar ejercicios y la conserva al recargar el mismo navegador.
- No se afirma que el puntaje sea oficial ni se muestra contenido ICFES en el build normal.

## 6. Pruebas automatizadas para desarrollo

Para revisar tipos y pruebas automatizadas desde la raíz:

```sh
npm run typecheck
npm test
```

Para revisar los datos de contenido con el script dedicado:

```sh
npm run validar
```

La prueba manual de esta guía complementa esas verificaciones: comprueba la navegación y el comportamiento visible en el navegador.

## 7. Restablecer datos de prueba

El progreso es local al navegador. Para empezar de nuevo, abre las herramientas de desarrollo del navegador, entra a **Application/Almacenamiento → Local Storage**, selecciona el origen local de Vite y borra las claves que empiezan por `saber11.`. Esto borra el avance de prueba de ese origen; no elimina contenido del repositorio.

## 8. Límites conocidos

- El contenido y las rutas disponibles cambian según los JSON cargados y la configuración del build.
- Los puntajes son estimaciones y no predicen ni reemplazan el resultado oficial.
- La persistencia descrita corresponde al navegador local; no presupone sincronización entre dispositivos.
- La voz y la instalación PWA requieren comprobación en los dispositivos y navegadores objetivo.
- El contenido oficial del ICFES está separado y apagado por defecto debido a sus términos de uso; revisa `docs/CONTEXTO.md` antes de habilitarlo o distribuirlo.
