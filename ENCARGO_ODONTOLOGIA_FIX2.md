# ENCARGO_ODONTOLOGIA_FIX2 (despues de 3e3cbb5)

Revision independiente de content/questions/odontologia.json encontro 2 fallas:

1. Claves adivinables: desde odo-015 la respuesta correcta sigue el ciclo 0,1,2,3,0,1,2,3... Barajar las opciones de TODAS las preguntas con un script (semilla fija) para que el orden de claves no tenga patron (sin ciclos ni rachas largas, reparto ~15-16 por letra). Al mover opciones, actualizar TODO lo que depende del indice: campo de respuesta correcta, razones de distractores, pistas, plan, guion (acciones tipo "o:X:ok"), y cualquier texto que diga "opcion A/B/C/D".
2. 39 enunciados/explicaciones citan numeros de linea de la transcripcion ("lineas seiscientas...", "linea 123", etc.). Quitar todas esas menciones y redactar en lenguaje clinico normal (se puede decir "segun la clase" sin numeros de linea).

Verificar con un script: 0 coincidencias de /l[ii]nea/ en odontologia.json, claves sin patron ciclico, build OK. Luego commit en antigravity/v1, git pull --rebase, push. No tocar main, no deploy manual, no VITE_ICFES.
