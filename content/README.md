# Cómo agregar contenido (todo por JSON)

La app lee estos archivos al compilar. No hay que tocar código: se crea o edita un JSON y se ejecuta `npm run validar`.
Lo que esté mal formado se **omite** (la app sigue funcionando) y `validar` te dice exactamente qué corregir.

| Qué | Dónde | Forma |
|---|---|---|
| Preguntas | `content/questions/*.json` | lista de preguntas |
| Lecciones | `content/lessons/*.json` | una lección por archivo |
| Temas (unidades) | `content/unidades.json` | lista |
| Simulacros | `content/simulacros/*.json` | un simulacro o lista de simulacros |
| **Paquete** (todo junto) | `content/packs/**/*.json` | objeto con `preguntas`, `lecciones`, `unidades`, `simulacros` (todas opcionales) |

## Paquete de contenido (lo más cómodo)
```json
{
  "id": "saber-2027-p1",
  "nombre": "Banco 2027, parte 1",
  "preguntas": [ { "id": "mat-101", "area": "matematicas", "evidencia": "…", "nivel": 2,
    "enunciado": "…", "opciones": ["…","…","…","…"], "correcta": 1,
    "explicacion": "…", "distractores": ["…","","…","…"], "origen": "original",
    "hoja": { "modo": "calculo", "pasos": [ { "k": "idea", "texto": "…" } ] } } ],
  "unidades": [ { "id": "u-nuevo", "area": "matematicas", "titulo": "…", "resumen": "…",
    "preguntas": ["mat-101"], "sim": null, "leccion": null, "min": 10 } ],
  "simulacros": [ ]
}
```
- `id` de pregunta: tres letras, guion y 3 o 4 números (`mat-101`, `cie-1002`). No se puede repetir.
- `area`: `matematicas`, `lectura_critica`, `sociales`, `ciencias` o `ingles`.
- `distractores`: una explicación por opción; la de la correcta va vacía (`""`).
- `hoja` (solución paso a paso con gráficos), `guion` y `enfoque` pueden ir dentro de la misma pregunta (`hoja.guion`, `hoja.enfoque`).

## Simulacros
Cada simulacro tiene secciones con su propio tiempo. Una sección usa preguntas **fijas** (`preguntas`) o **elegidas al azar** del banco (`auto`), o ambas.
```json
{
  "id": "completo-2",
  "nombre": "Simulacro completo 2",
  "descripcion": "Las cinco áreas, con tiempo por sección.",
  "nivel": "Completo",
  "barajar": true,
  "secciones": [
    { "titulo": "Lectura crítica", "area": "lectura_critica", "minutos": 20, "auto": { "area": "lectura_critica", "n": 10, "nivel": [2,3] } },
    { "titulo": "Matemáticas", "area": "matematicas", "minutos": 30, "preguntas": ["mat-001","mat-002"], "auto": { "area": "matematicas", "n": 12 } }
  ]
}
```
- `auto.n`: cuántas preguntas en total para esa sección (si hay `preguntas` fijas, se completan hasta `n`).
- `auto.nivel` y `auto.excluir` son opcionales. Una pregunta no se repite dentro del mismo simulacro.
- Puedes tener todos los simulacros que quieras: aparecen en **Practicar → Simulacros**. Siempre existe además «Simulacro rápido» con todo el banco.
- El puntaje se guarda por simulacro (mejor puntaje e intentos).

## Validar
`npm run validar` revisa ids repetidos, preguntas mal formadas, temas que apuntan a preguntas inexistentes y simulacros imposibles de armar.

---

# Laboratorios 100 % en JSON

Un laboratorio vive en `content/labs/<nombre>.json` (o dentro de un paquete, en `"labs": [...]`). **Un laboratorio con el mismo `id` que uno hecho en código lo reemplaza**; con un `id` nuevo se agrega. Modelo completo: `content/labs/proyectil.json`.

## Qué define el JSON
| Campo | Para qué |
|---|---|
| `params` | controles: `slider` (min, max, paso), `select` (opciones) o `toggle` |
| `constantes`, `derivadas` | números fijos y valores calculados a partir de los parámetros |
| `fisica` | cómo evoluciona (ver abajo) y las `medidas` que se muestran |
| `escena` | todo lo que se dibuja: marco, ejes, curvas, flechas, textos, cotas… |
| `graficas`, `retos`, `lectura`, `descripcion` | gráficas de seguimiento, retos con criterios, números destacados |
| `aprende`, `presets`, `experimentos` | explicación, casos típicos y predicciones |
| `solucion`, `comparar`, `insight` | resolución paso a paso, teoría vs. simulación y la frase «Observa» |

## `fisica`
- **Con ecuaciones diferenciales** (`"integracion": "rk4"`): `estado` (valores iniciales), `ecuaciones` (derivada de cada variable) y `evento` (cuándo termina, ej. `"y<0"`) o `duracion`.
- **Con fórmula** (`"integracion": "formula"`): `estadoT` da cada variable en función del tiempo `t`, y `duracion` dice cuánto dura. Sin `duracion` y con `"modo": "estatico"`, es un cálculo directo (circuitos, lentes…).
- `medidas`: expresiones sobre la trayectoria, ej. `"alcance": "collast('x')"`, `"altura_max": "colmax('y')"`.

## Expresiones (se escriben como texto)
Números, `+ - * / ^ %`, comparaciones, `&& || !`, condicional `a ? b : c` y funciones: `sin cos tan asin acos atan atan2 sqrt abs exp ln log10 floor ceil round sign pow min max hypot mod rad deg clamp si(cond,a,b) cerca(a,b,tol) alea(i,semilla)`.
Sobre la trayectoria: `colmax('y') colmin colmean colsum collast colfirst colcount colat('y',i) atmax('x','y')` (valor de x donde y es máxima). Constantes `pi`, `e`. No se puede ejecutar código.

## Textos con valores: `#{expresión|decimales}`
`"Alcance #{m.alcance|1} m"` → `Alcance 40,8 m` (con coma decimal). Funciona en `txt`, `descripcion`, `solucion`, `insight`… Conviven con las fórmulas `$...$`.

## `escena`: piezas de dibujo (`capas`)
`cuadricula, suelo, ejes, curva, funcion, marcas, circulo, rect, linea, flecha, texto, cota, llamada, arco`. Cada una admite `si` (condición para mostrarla), `color` (0 a 5, `tinta`, `suave`, `pluma` o `#hex`) y `grosor`. Las coordenadas están en el mundo del `marco`; con `"px": true` están en píxeles y puedes usar `X(x)` y `Y(y)` para convertir. Dentro de la escena existen los parámetros, las variables de estado, `m` (medidas), `t`, `w`, `h`, `izq`, `gy`…

## Escenas dentro de las explicaciones
Cualquier hoja puede tener un paso `"k": "escena"` con los mismos `capas` y `marco`, más `vars` (valores y fórmulas) y `anim: {"dur": 4, "bucle": true}` para animarlo (`u` va de 0 a 1). Ejemplo: `content/pasos_extra.json` (se inserta en una pregunta existente con `"despues": índice_del_paso`).

## Validar
`npm run validar` revisa expresiones, tipos de capa, parámetros de retos y experimentos, y que cada laboratorio JSON iguale las medidas del que reemplaza (pruebas numéricas).

## Formato cuadernillo (como el examen real)
**Bloques de contexto** (`content/bloques/*.json` o `bloques` dentro de un pack): `{ "id", "area", "encabezado"?, "titulo"?, "texto"?, "figuras"?, "fuente"? }`. Una pregunta lo usa con `"bloque": "<id>"`; se muestra «RESPONDE LAS PREGUNTAS X A Y DE ACUERDO CON LA SIGUIENTE INFORMACIÓN» y el simulacro nunca separa las preguntas de un mismo bloque. `texto` separa párrafos con una línea en blanco.

**Figuras** (en `figuras` de la pregunta o del bloque, y en `opcionesFig` cuando las opciones son gráficas, una entrada por opción o `null`): todas llevan `alt` (texto alternativo) y `pie` opcional.
- `{"tipo":"img","src":"/img/x.png","alt":"…"}` imagen en `public/img/`.
- `{"tipo":"svg","svg":"<svg viewBox=…>…</svg>","alt":"…"}` (se limpia: sin scripts ni eventos).
- `{"tipo":"escena","ancho":640,"alto":300,"capas":[…],"alt":"…"}` dibujo con las mismas piezas de los laboratorios (ver arriba).
- `{"tipo":"tabla","cols":[…],"filas":[[…]],"alt":"…"}`.
Cada figura tiene botón «Ampliar».

**Opciones**: de 2 a 8 (para emparejar en Inglés usa 7: A–G). Extras útiles para la tabla de revisión: `afirmacion`, `competencia`, `parte`.

**Simulacro tipo examen**: `"modo":"examen"`, `"secciones":[]` y `"sesiones":[{"titulo","minutos","pruebas":[{"titulo","area","auto":{"area","n"}}|{"preguntas":[ids]}]}]`. Un solo reloj por sesión, navegación libre, paleta de preguntas, marcar para revisar, hoja de respuestas, hoja de operaciones, entregar sesión, descanso entre sesiones y, al final, revisión completa (filtros: incorrectas, en blanco, marcadas). Ejemplos en `content/packs/formato-icfes.json` (incluye la estructura oficial de 2 sesiones: 25/41/25/29 y 25/25/29/55; usa las preguntas que haya en el banco).

**Importante (licencia)**: el contenido oficial del ICFES no se puede copiar a un producto comercial. Escribe preguntas originales con este mismo formato, o pide permiso por escrito al ICFES.

## Contenido oficial del Icfes (`content/icfes/`)
- `python3 tools/importar_icfes.py texto.txt --area matematicas --pref mat --prueba "Prueba Matemáticas"` convierte el texto de un cuadernillo (pdftotext o texto del conector) en `content/icfes/mat/preguntas.json`: preguntas A–D con clave, contextos «Responde las preguntas X a Y» como bloques, unidad y cita de fuente.
- Las figuras que no tienen archivo quedan como `{"tipo":"pendiente","pagina":N}`; se reemplazan por `img` o `svg` sin tocar nada más (`--figuras figuras.json` las inyecta).
- `origen:"icfes"` exige `fuente` (cita al Icfes). `revisar:[…]` marca lo dudoso (fórmulas, opciones gráficas).
- **No entra al build publicado**: solo con `VITE_ICFES=1`. Sin permiso escrito del Icfes (sus términos prohíben transformar y usar con fines de lucro), déjalo apagado.
