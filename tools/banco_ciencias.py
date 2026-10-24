"""Generador de preguntas originales de Ciencias Naturales para el Banco Propio.
Crea 31 preguntas (cie-010 a cie-040) cumpliendo el estándar ICFES:
- Enunciado claro, experimental o contextualizado
- 4 opciones distintas
- Explicación científica rigurosa y pedagógica
- 3 distractores específicos explicando el error conceptual
- Competencia y afirmación oficiales según el Marco de Referencia ICFES
"""
import json

PREGUNTAS_CIE = [
    {
        "id": "cie-010",
        "area": "ciencias",
        "evidencia": "CIE_E2.5",
        "nivel": 2,
        "enunciado": "Un carrito de montaña rusa de 200 kg parte del reposo desde una altura de 20 metros en el punto A y desciende por una pista sin fricción hasta el punto B a nivel del suelo (0 metros). Tomando la aceleración de la gravedad $g = 10\\text{ m/s}^2$, ¿cuál es la rapidez del carrito al pasar por el punto B?",
        "opciones": [
            "10 m/s",
            "14 m/s",
            "20 m/s",
            "40 m/s"
        ],
        "correcta": 2,
        "explicacion": "Por el principio de conservación de la energía mecánica (sin fricción), la energía potencial gravitacional inicial en A se transforma por completo en energía cinética en B: $E_{pA} = E_{cB} \\implies m g h = \\frac{1}{2} m v^2$. Cancelando la masa $m$: $v = \\sqrt{2gh} = \\sqrt{2\\cdot 10\\cdot 20} = \\sqrt{400} = 20$ m/s.",
        "distractores": [
            "Olvida el factor 2 en la fórmula de la energía cinética: $v = \\sqrt{gh} = \\sqrt{200} \\approx 14,14$ m/s.",
            "Calcula la mitad de la velocidad o divide entre la gravedad erróneamente: 10 m/s.",
            "",
            "Olvida sacar la raíz cuadrada final calculando $v^2 = 400$ y eligiendo 40 por error de orden de magnitud."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Aplica el principio de conservación de la energía mecánica en sistemas conservativos."
    },
    {
        "id": "cie-011",
        "area": "ciencias",
        "evidencia": "CIE_E2.5",
        "nivel": 2,
        "enunciado": "Un bloque de madera de 4 kg se encuentra sobre una mesa horizontal. Se le aplica una fuerza horizontal constante de 26 N hacia la derecha. Si la fuerza de fricción cinética entre el bloque y la mesa es de 10 N, ¿cuál es la aceleración que experimenta el bloque?",
        "opciones": [
            "2,5 m/s²",
            "4,0 m/s²",
            "6,5 m/s²",
            "9,0 m/s²"
        ],
        "correcta": 1,
        "explicacion": "Por la segunda ley de Newton, la aceleración es $a = F_{\\text{neta}} / m$. La fuerza neta horizontal es la diferencia entre la fuerza aplicada y la fuerza de fricción que se opone al movimiento: $F_{\\text{neta}} = 26\\text{ N} - 10\\text{ N} = 16\\text{ N}$. Luego: $a = 16\\text{ N} / 4\\text{ kg} = 4,0\\text{ m/s}^2$.",
        "distractores": [
            "Divide la fuerza de fricción entre la masa ($10/4 = 2,5$ m/s²), ignorando la fuerza motriz aplicada.",
            "",
            "Divide la fuerza aplicada directamente entre la masa ($26/4 = 6,5$ m/s²), ignorando la existencia de la fuerza de fricción.",
            "Suma la fricción a la fuerza aplicada en lugar de restarla: $(26 + 10)/4 = 36/4 = 9,0$ m/s²."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Relaciona fuerzas netas y aceleraciones en sistemas con rozamiento aplicando la segunda ley de Newton."
    },
    {
        "id": "cie-012",
        "area": "ciencias",
        "evidencia": "CIE_E2.4",
        "nivel": 2,
        "enunciado": "Dos bombillos idénticos de resistencia $R = 6\\ \\Omega$ cada uno se conectan en paralelo a una batería de 12 V. ¿Cuál es la corriente total suministrada por la batería al circuito?",
        "opciones": [
            "1 A",
            "2 A",
            "4 A",
            "8 A"
        ],
        "correcta": 2,
        "explicacion": "En una conexión en paralelo, la resistencia equivalente de dos resistencias idénticas es la mitad de una de ellas: $R_{\\text{eq}} = \\frac{R}{2} = \\frac{6}{2} = 3\\ \\Omega$. Por ley de Ohm, la corriente total es $I = \\frac{V}{R_{\\text{eq}}} = \\frac{12\\text{ V}}{3\\ \\Omega} = 4$ A (cada rama consume $12/6 = 2$ A, sumando 4 A).",
        "distractores": [
            "Calcula como si estuvieran en serie: $R_{\\text{eq}} = 6 + 6 = 12\\ \\Omega$, de donde $I = 12/12 = 1$ A.",
            "Calcula la corriente que pasa por un solo bombillo ($12/6 = 2$ A) en lugar de la corriente total de la fuente.",
            "",
            "Multiplica la resistencia equivalente por el voltaje por error de despeje de la ley de Ohm."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Elabora explicaciones relacionando voltaje, corriente y resistencia en circuitos eléctricos en paralelo."
    },
    {
        "id": "cie-013",
        "area": "ciencias",
        "evidencia": "CIE_E2.6",
        "nivel": 2,
        "enunciado": "En un recipiente aislado térmicamente (calorímetro) se mezclan 100 g de agua a 80 °C con 100 g de agua a 20 °C. Despreciando pérdidas de calor al entorno, ¿cuál será la temperatura final de equilibrio de la mezcla?",
        "opciones": [
            "30 °C",
            "50 °C",
            "60 °C",
            "100 °C"
        ],
        "correcta": 1,
        "explicacion": "Dado que las dos masas son iguales ($m_1 = m_2 = 100$ g) y se trata de la misma sustancia (mismo calor específico $c$), el calor cedido por el agua caliente es igual al calor absorbido por el agua fría: $m c (80 - T_e) = m c (T_e - 20) \\implies 80 - T_e = T_e - 20 \\implies 2T_e = 100 \\implies T_e = 50$ °C.",
        "distractores": [
            "Promedia de manera asimétrica sesgando hacia la temperatura fría: 30 °C.",
            "",
            "Calcula la diferencia de temperaturas: $80 - 20 = 60$ °C, confundiéndola con la temperatura de equilibrio.",
            "Suma las temperaturas de las dos masas de agua: $80 + 20 = 100$ °C, violando el principio cero de la termodinámica."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Predice la temperatura de equilibrio térmico en mezclas conservativas aplicando la ley de calorimetría."
    },
    {
        "id": "cie-014",
        "area": "ciencias",
        "evidencia": "CIE_E2.5",
        "nivel": 2,
        "enunciado": "Un cubo macizo de plástico flota en un vaso con agua dulce con el 80 % de su volumen sumergido. Si ese mismo cubo se coloca en un recipiente con agua de mar (la cual tiene mayor densidad que el agua dulce), ¿qué ocurrirá con el porcentaje de volumen sumergido?",
        "opciones": [
            "Aumentará, porque el agua de mar ejerce una fuerza de empuje menor.",
            "Disminuirá, porque al ser más denso el líquido, se requiere desalojar menor volumen para igualar el peso del cubo.",
            "Se mantendrá exactamente en 80 %, porque la densidad del cubo no ha cambiado.",
            "El cubo se hundirá completamente hasta el fondo debido a la sal presente en el agua."
        ],
        "correcta": 1,
        "explicacion": "Para que un cuerpo flote en equilibrio, la fuerza de empuje debe igualar el peso del objeto: $E = P \\implies \\rho_{\\text{líquido}} g V_{\\text{sumergido}} = m g$. Si la densidad del líquido $\\rho_{\\text{líquido}}$ aumenta (como ocurre en el agua de mar respecto al agua dulce), el volumen sumergido $V_{\\text{sumergido}}$ debe disminuir para mantener el mismo empuje que equilibra el peso del cubo.",
        "distractores": [
            "Afirma que el empuje disminuye en agua salada, lo cual es opuesto a la física de la densidad de fluidos.",
            "",
            "Asume erróneamente que la flotabilidad solo depende de la densidad del objeto y no de la del líquido.",
            "Supone que la sal hace que los cuerpos se hundan, cuando en realidad incrementa la flotabilidad al aumentar la densidad del medio."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Explica la flotación de cuerpos sólidos en diferentes fluidos con base en el principio de Arquímedes y la densidad."
    },
    {
        "id": "cie-015",
        "area": "ciencias",
        "evidencia": "CIE_E2.7",
        "nivel": 2,
        "enunciado": "Un rayo de luz viaja por el aire e incide sobre la superficie plana de un bloque de vidrio con un ángulo de incidencia de 45° respecto a la normal. Sabiendo que el índice de refracción del vidrio ($n = 1,5$) es mayor que el del aire ($n = 1,0$), ¿qué ocurre con el rayo al entrar al vidrio?",
        "opciones": [
            "Se desvía acercándose a la normal y su rapidez de propagación disminuye.",
            "Se desvía alejándose de la normal y su rapidez de propagación aumenta.",
            "Continúa en línea recta sin desviarse pero su rapidez disminuye a la mitad.",
            "Se refleja totalmente en la superficie porque el ángulo de 45° supera el ángulo crítico."
        ],
        "correcta": 0,
        "explicacion": "Por la ley de Snell ($n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2$), al pasar de un medio de menor índice a uno de mayor índice ($n_2 > n_1$), el ángulo de refracción disminuye ($\theta_2 < \\theta_1$), lo que significa que el rayo se acerca a la recta normal. Asimismo, la rapidez de la luz en un medio es $v = c / n$; al ser $n > 1$, la luz viaja más lento en el vidrio que en el aire.",
        "distractores": [
            "",
            "Invierte el comportamiento afirmando que se aleja de la normal y viaja más rápido, lo cual ocurriría al pasar de vidrio a aire.",
            "Sostiene que no se desvía, lo que solo sucedería para incidencia puramente perpendicular (ángulo de 0°).",
            "Confunde la refracción con la reflexión total interna, la cual solo es posible cuando la luz va del medio más denso al menos denso."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Describe y explica el fenómeno de refracción de ondas electromagnéticas al cambiar de medio de propagación."
    },
    {
        "id": "cie-016",
        "area": "ciencias",
        "evidencia": "CIE_E2.7",
        "nivel": 2,
        "enunciado": "Una ambulancia con la sirena encendida emite un sonido con una frecuencia propia de 800 Hz mientras se desplaza a gran velocidad hacia un observador que se encuentra quieto en la acera. ¿Qué frecuencia percibe el observador mientras la ambulancia se acerca?",
        "opciones": [
            "Exactamente 800 Hz, porque la fuente sonora no ha modificado su sirena.",
            "Una frecuencia mayor a 800 Hz, porque los frentes de onda se comprimen en la dirección del movimiento.",
            "Una frecuencia menor a 800 Hz, porque el sonido pierde energía al viajar por el aire.",
            "Cero Hz, porque la velocidad del vehículo cancela las ondas sonoras."
        ],
        "correcta": 1,
        "explicacion": "Por el efecto Doppler, cuando una fuente emisora de ondas se mueve hacia un receptor en reposo, cada nuevo frente de onda se emite desde una posición más cercana al observador que el anterior. La longitud de onda aparente disminuye y, consecuentemente, la frecuencia percibida aumenta, escuchándose un tono más agudo (mayor a 800 Hz).",
        "distractores": [
            "Ignora el movimiento relativo entre la fuente y el observador asumiendo que la frecuencia percibida es idéntica a la emitida.",
            "",
            "Confunde el tono con la atenuación de intensidad y asume erróneamente que la frecuencia percibida disminuye.",
            "Plantea una hipótesis absurda de anulación de la onda sonora a velocidades subsónicas comunes."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Explica el cambio aparente en la frecuencia del sonido por efecto Doppler en fuentes en movimiento relativo."
    },
    {
        "id": "cie-017",
        "area": "ciencias",
        "evidencia": "CIE_E2.5",
        "nivel": 2,
        "enunciado": "Un buzo se sumerge a 10 metros de profundidad en un lago de agua dulce ($\rho = 1.000\\text{ kg/m}^3$). Tomando $g = 10\\text{ m/s}^2$ y la presión atmosférica en la superficie $P_{\\text{atm}} = 100.000\\text{ Pa}$, ¿cuál es la presión absoluta total que experimenta el buzo a esa profundidad?",
        "opciones": [
            "10.000 Pa",
            "100.000 Pa",
            "200.000 Pa",
            "1.000.000 Pa"
        ],
        "correcta": 2,
        "explicacion": "La presión absoluta en un fluido en reposo es la suma de la presión atmosférica y la presión hidrostática: $P_{\\text{abs}} = P_{\\text{atm}} + \\rho g h$. Calculamos la presión hidrostática: $P_h = 1.000\\cdot 10\\cdot 10 = 100.000\\text{ Pa} = 1\\text{ atm}$. Sumando la presión atmosférica: $P_{\\text{abs}} = 100.000 + 100.000 = 200.000\\text{ Pa}$ (aproximadamente 2 atmósferas).",
        "distractores": [
            "Calcula con una profundidad de 1 metro o comete un error en las potencias de 10 dando 10.000 Pa.",
            "Indica únicamente la presión atmosférica superficial olvidando sumar la columna de agua.",
            "",
            "Multiplica de forma incorrecta añadiendo ceros sobrantes a la presión hidrostática."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Calcula e interpreta la presión absoluta y manométrica en fluidos en equilibrio hidrostático."
    },
    {
        "id": "cie-018",
        "area": "ciencias",
        "evidencia": "CIE_E2.5",
        "nivel": 2,
        "enunciado": "Un vagón de ferrocarril A de 2.000 kg se mueve a 3 m/s hacia la derecha y choca con un vagón B de 1.000 kg que se encuentra inicialmente en reposo sobre la misma vía. Si tras el impacto ambos vagones quedan acoplados y se mueven juntos, ¿cuál es su rapidez inmediatamente después del choque?",
        "opciones": [
            "1,5 m/s",
            "2,0 m/s",
            "2,5 m/s",
            "3,0 m/s"
        ],
        "correcta": 1,
        "explicacion": "Por el principio de conservación de la cantidad de movimiento total ($p_{\\text{antes}} = p_{\\text{después}}$): $m_A v_A + m_B v_B = (m_A + m_B) v_f$. Reemplazando: $2.000(3) + 1.000(0) = (2.000 + 1.000) v_f \\implies 6.000 = 3.000 v_f \\implies v_f = 6.000 / 3.000 = 2,0$ m/s.",
        "distractores": [
            "Divide la velocidad entre dos asumiendo que se reduce a la mitad sin considerar las masas desiguales.",
            "",
            "Promedia las masas y velocidades sin plantear la conservación del momento lineal.",
            "Asume que la rapidez se conserva inalterada a 3 m/s a pesar de haber arrastrado una masa adicional."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Aplica la conservación del momento lineal en colisiones totalmente inelásticas."
    },
    {
        "id": "cie-019",
        "area": "ciencias",
        "evidencia": "CIE_E2.7",
        "nivel": 2,
        "enunciado": "Una onda mecánica periódica se propaga en una cuerda tensa con una longitud de onda $\\lambda = 0,5$ metros y una frecuencia de oscilación de 40 Hz. ¿Cuál es la velocidad de propagación de la onda en la cuerda?",
        "opciones": [
            "10 m/s",
            "20 m/s",
            "40 m/s",
            "80 m/s"
        ],
        "correcta": 1,
        "explicacion": "La velocidad de propagación de una onda periódica se calcula mediante la relación fundamental $v = \\lambda\\cdot f$. Sustituyendo los datos: $v = 0,5\\text{ m}\\cdot 40\\text{ s}^{-1} = 20$ m/s.",
        "distractores": [
            "Divide la frecuencia entre 4 sin justificación física obteniendo 10 m/s.",
            "",
            "Confunde la velocidad de propagación con la frecuencia numérica en Hz (40 m/s).",
            "Divide la frecuencia entre la longitud de onda: $40 / 0,5 = 80$ m/s, invirtiendo la fórmula correcta."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Relaciona velocidad de propagación, longitud de onda y frecuencia en ondas periódicas."
    },
    {
        "id": "cie-020",
        "area": "ciencias",
        "evidencia": "CIE_E2.1",
        "nivel": 2,
        "enunciado": "En la reacción de síntesis del agua: $2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}$, se hacen reaccionar 4 moles de gas hidrógeno ($\text{H}_2$) con 3 moles de gas oxígeno ($\text{O}_2$). ¿Cuál es el reactivo límite y cuántos moles de agua se pueden formar como máximo?",
        "opciones": [
            "El reactivo límite es el oxígeno y se forman 3 moles de agua.",
            "El reactivo límite es el hidrógeno y se forman 4 moles de agua.",
            "El reactivo límite es el hidrógeno y se forman 2 moles de agua.",
            "No hay reactivo límite porque ambos gases se consumen por completo."
        ],
        "correcta": 1,
        "explicacion": "Según la ecuación balanceada, 2 moles de $\\text{H}_2$ requieren 1 mol de $\\text{O}_2$. Para consumir los 4 moles de $\\text{H}_2$ disponibles se requieren $4 / 2 = 2$ moles de $\\text{O}_2$. Como se tienen 3 moles de $\\text{O}_2$, este se encuentra en exceso (sobra 1 mol) y el hidrógeno es el reactivo límite que se agota primero. Con 4 moles de $\\text{H}_2$ se producen exactamente 4 moles de $\\text{H}_2\\text{O}$ (relación estequiométrica 2:2, es decir, 1:1).",
        "distractores": [
            "Identifica el oxígeno como límite solo por tener menor número de moles iniciales (3 < 4), ignorando la estequiometría 2:1.",
            "",
            "Identifica el hidrógeno pero divide incorrectamente los moles de agua formados.",
            "Supone erróneamente que las proporciones molares iniciales coinciden con las estequiométricas."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Determina el reactivo límite y calcula rendimientos teóricos en reacciones químicas balanceadas."
    },
    {
        "id": "cie-021",
        "area": "ciencias",
        "evidencia": "CIE_E2.2",
        "nivel": 2,
        "enunciado": "Al desplazarse de izquierda a derecha a lo largo de un mismo periodo en la tabla periódica (por ejemplo, del sodio al cloro), ¿cómo varían la electronegatividad y el radio atómico de los elementos?",
        "opciones": [
            "La electronegatividad aumenta y el radio atómico disminuye.",
            "La electronegatividad disminuye y el radio atómico aumenta.",
            "Tanto la electronegatividad como el radio atómico aumentan.",
            "Tanto la electronegatividad como el radio atómico disminuyen."
        ],
        "correcta": 0,
        "explicacion": "Al avanzar hacia la derecha en un periodo, aumenta la carga nuclear efectiva (más protones en el núcleo con el mismo número de niveles de energía). Esto atrae con mayor fuerza a los electrones de valencia hacia el núcleo, lo que reduce el radio atómico y aumenta la capacidad del átomo para atraer electrones en un enlace químico (mayor electronegatividad).",
        "distractores": [
            "",
            "Describe la tendencia exactamente contraria a la realidad periódica.",
            "Asume erróneamente que ambas propiedades aumentan al tener más masa y número atómico.",
            "Asume que ambas propiedades disminuyen sin considerar la atracción de la carga nuclear efectiva."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Explica la periodicidad química relacionando carga nuclear efectiva, radio atómico y electronegatividad."
    },
    {
        "id": "cie-022",
        "area": "ciencias",
        "evidencia": "CIE_E2.2",
        "nivel": 2,
        "enunciado": "El cloruro de sodio (sal de mesa, NaCl) es un sólido blanco con alto punto de fusión (801 °C) que se disuelve en agua produciendo una solución conductora de electricidad. En contraste, el tetracloruro de carbono ($\text{CCl}_4$) es un líquido volátil a temperatura ambiente que no conduce la corriente. ¿A qué se deben principalmente estas diferencias?",
        "opciones": [
            "El NaCl posee enlaces iónicos con red cristalina fuerte, mientras que el CCl₄ posee enlaces covalentes con fuerzas intermoleculares débiles.",
            "El NaCl posee enlaces metálicos mientras que el CCl₄ posee enlaces iónicos insolubles.",
            "El NaCl está formado solo por no metales y el CCl₄ está formado por metales alcalinos.",
            "El NaCl es una mezcla heterogénea y el CCl₄ es un elemento químico puro."
        ],
        "correcta": 0,
        "explicacion": "El sodio (metal) y el cloro (no metal) tienen una gran diferencia de electronegatividad, formando enlaces iónicos organizados en una red cristalina tridimensional que requiere mucha energía térmica para romperse y que libera iones libres en agua. El $\\text{CCl}_4$ está formado por moléculas unidas por enlaces covalentes con fuerzas intermoleculares débiles de dispersión de London, lo que le confiere bajo punto de ebullición y nula conductividad eléctrica.",
        "distractores": [
            "",
            "Clasifica erróneamente al cloruro de sodio como compuesto de enlace metálico.",
            "Invierte la naturaleza química afirmando que el sodio es un no metal.",
            "Confunde sustancias compuestas puras con mezclas heterogéneas o elementos simples."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Relaciona las propiedades macroscópicas de las sustancias con el tipo de enlace químico (iónico o covalente)."
    },
    {
        "id": "cie-023",
        "area": "ciencias",
        "evidencia": "CIE_E2.3",
        "nivel": 2,
        "enunciado": "Un estudiante de química dispone de 200 mL de una solución de sulfato de cobre ($CuSO_4$) con una concentración 2,0 M. Si le agrega agua destilada hasta completar un volumen final de 800 mL, ¿cuál será la nueva molaridad de la solución diluida?",
        "opciones": [
            "0,5 M",
            "1,0 M",
            "1,5 M",
            "4,0 M"
        ],
        "correcta": 0,
        "explicacion": "En un proceso de dilución, la cantidad de moles de soluto se conserva constante: $C_1 V_1 = C_2 V_2$. Despejando la concentración final: $C_2 = \\frac{C_1 V_1}{V_2} = \\frac{2,0\\text{ M}\\cdot 200\\text{ mL}}{800\\text{ mL}} = \\frac{400}{800} = 0,5$ M.",
        "distractores": [
            "",
            "Calcula la mitad de la concentración inicial creyendo que el volumen solo se duplicó.",
            "Resta las concentraciones o comete un error aritmético al simplificar la fracción.",
            "Multiplica la concentración por el factor de aumento de volumen creyendo que la concentración aumenta."
        ],
        "origen": "original",
        "competencia": "Formulación y ejecución",
        "afirmacion": "Calcula concentraciones molares en procesos de dilución aplicando la conservación de la masa de soluto."
    },
    {
        "id": "cie-024",
        "area": "ciencias",
        "evidencia": "CIE_E2.3",
        "nivel": 2,
        "enunciado": "Se tienen tres sustancias líquidas en el laboratorio: jugo de limón (pH = 2,5), agua pura destilada (pH = 7,0) y blanqueador doméstico (pH = 12,0). De acuerdo con la escala de pH, ¿cuál es la clasificación correcta de estas tres sustancias?",
        "opciones": [
            "Jugo de limón: ácida; agua pura: neutra; blanqueador: básica.",
            "Jugo de limón: básica; agua pura: ácida; blanqueador: neutra.",
            "Jugo de limón: ácida; agua pura: básica; blanqueador: neutra.",
            "Las tres sustancias son neutras porque se encuentran en estado líquido a temperatura ambiente."
        ],
        "correcta": 0,
        "explicacion": "En la escala de pH a 25 °C, las soluciones con $\\text{pH} < 7$ son ácidas (mayor concentración de iones $\\text{H}^+$), las de $\\text{pH} = 7$ son neutras (concentración equilibrada de $\\text{H}^+$ y $\\text{OH}^-$), y las de $\\text{pH} > 7$ son básicas o alcalinas (mayor concentración de iones hidroxilo $\\text{OH}^-$). Por tanto: limón (2,5) ácida, agua (7,0) neutra y blanqueador (12,0) básica.",
        "distractores": [
            "",
            "Invierte la escala considerando que los valores bajos son básicos y los altos neutros.",
            "Clasifica el agua destilada como básica y el blanqueador como neutro de forma arbitraria.",
            "Confunde el estado de agregación físico (líquido) con la propiedad química del pH."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Clasifica disoluciones acuosas comunes en ácidas, neutras o básicas utilizando la escala de pH."
    },
    {
        "id": "cie-025",
        "area": "ciencias",
        "evidencia": "CIE_E2.3",
        "nivel": 2,
        "enunciado": "En un laboratorio se desea separar una mezcla homogénea de agua (punto de ebullición 100 °C) y etanol (alcohol etílico, punto de ebullición 78 °C). ¿Cuál es el método físico de separación más adecuado para recuperar ambos componentes en estado puro?",
        "opciones": [
            "Filtración simple con papel de filtro.",
            "Decantación mediante un embudo de separación.",
            "Destilación fraccionada aprovechando la diferencia en los puntos de ebullición.",
            "Centrifugación a alta velocidad."
        ],
        "correcta": 2,
        "explicacion": "El agua y el etanol forman una mezcla homogénea (miscibles en todas las proporciones). La destilación fraccionada es el método ideal para separar líquidos miscibles con puntos de ebullición diferentes: al calentar la mezcla, el componente más volátil (etanol a 78 °C) se evapora primero, sus vapores ascienden por la columna de fraccionamiento, se condensan en el refrigerante y se recolectan por separado del agua.",
        "distractores": [
            "Propone filtración, la cual solo sirve para mezclas heterogéneas sólido-líquido y no retiene sustancias disueltas.",
            "Propone decantación, que solo funciona con líquidos inmiscibles con densidades distintas (como agua y aceite).",
            "",
            "Propone centrifugación, método mecánico útil para suspender partículas coloidales o células pero inútil en disoluciones moleculares."
        ],
        "origen": "original",
        "competencia": "Indagación",
        "afirmacion": "Selecciona métodos adecuados de separación de mezclas con base en las propiedades físicas de los componentes."
    },
    {
        "id": "cie-026",
        "area": "ciencias",
        "evidencia": "CIE_E2.3",
        "nivel": 2,
        "enunciado": "Un gas ideal contenido en un cilindro provisto de un émbolo móvil ocupa un volumen de 6 litros bajo una presión de 1 atmósfera. Si se presiona el émbolo hasta reducir el volumen a 2 litros manteniendo la temperatura estrictamente constante, ¿cuál será la nueva presión del gas?",
        "opciones": [
            "0,33 atmósferas",
            "1,5 atmósferas",
            "3,0 atmósferas",
            "12,0 atmósferas"
        ],
        "correcta": 2,
        "explicacion": "Por la ley de Boyle para gases a temperatura constante: $P_1 V_1 = P_2 V_2$. Despejando la presión final: $P_2 = \\frac{P_1 V_1}{V_2} = \\frac{1\\text{ atm}\\cdot 6\\text{ L}}{2\\text{ L}} = 3\\text{ atm}$. Al comprimir el gas a un tercio de su volumen original, las moléculas chocan con mayor frecuencia contra las paredes, triplicando la presión.",
        "distractores": [
            "Aplica una relación de proporcionalidad directa dividiendo $1 / 3 = 0,33$ atm, como si al comprimir disminuyera la presión.",
            "Calcula una fracción inexacta dividiendo entre 4 o cometiendo un error aritmético.",
            "",
            "Multiplica todos los números ($1\\cdot 6\\cdot 2 = 12$) sin aplicar la ley de Boyle."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Aplica las leyes de los gases ideales (ley de Boyle) para calcular variables de estado en procesos isotérmicos."
    },
    {
        "id": "cie-027",
        "area": "ciencias",
        "evidencia": "CIE_E2.3",
        "nivel": 2,
        "enunciado": "Al calentar un bloque de hielo a 0 °C a nivel del mar mientras se suministra calor constante, se observa que la temperatura se mantiene fija en 0 °C durante todo el tiempo en que el hielo se está transformando en agua líquida. ¿A qué se debe que la temperatura no aumente durante este proceso?",
        "opciones": [
            "La energía térmica suministrada se invierte en romper los enlaces de hidrógeno entre las moléculas de agua en lugar de aumentar su energía cinética media.",
            "El termómetro se encuentra dañado y no detecta variaciones de temperatura por debajo de 100 °C.",
            "El calor específico del agua es infinito a 0 °C y no absorbe energía del exterior.",
            "El aire del entorno enfría el recipiente exactamente a la misma tasa en que el fogón lo calienta."
        ],
        "correcta": 0,
        "explicacion": "Durante un cambio de fase (como la fusión del hielo), la energía térmica suministrada (calor latente de fusión) no se traduce en un aumento de la energía cinética promedio de las moléculas (la cual determina la temperatura macroscópica), sino en energía potencial para debilitar y reorganizar la estructura cristalina y los enlaces de hidrógeno del sólido a líquido.",
        "distractores": [
            "",
            "Atribuye el fenómeno científico real a una falla instrumental del termómetro.",
            "Sostiene que el calor específico se vuelve infinito, violando la definición física de capacidad calorífica.",
            "Plantea una coincidencia casual de intercambio térmico con el aire que no explica el comportamiento universal de las sustancias puras."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Explica la constancia de la temperatura durante los cambios de fase a partir del concepto de calor latente."
    },
    {
        "id": "cie-028",
        "area": "ciencias",
        "evidencia": "CIE_E2.1",
        "nivel": 2,
        "enunciado": "Para acelerar la descomposición del peróxido de hidrógeno ($2\\text{H}_2\\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O} + \\text{O}_2$), un químico agrega una pizca de dióxido de manganeso ($\text{MnO}_2$). Se observa un burbujeo vigoroso inmediato y, al finalizar la reacción, la masa de dióxido de manganeso permanece exactamente igual a la inicial. ¿Cuál fue el papel del dióxido de manganeso?",
        "opciones": [
            "Actuó como reactivo límite que aportó el oxígeno desprendido.",
            "Actuó como catalizador, disminuyendo la energía de activación de la reacción sin consumirse en ella.",
            "Actuó como disolvente universal que cambió el punto de ebullición del peróxido.",
            "Actuó como inhibidor químico retrasando la velocidad de reacción."
        ],
        "correcta": 1,
        "explicacion": "Un catalizador es una sustancia que aumenta la velocidad de una reacción química al proporcionar una ruta de reacción alternativa con menor energía de activación. Al no formar parte de los reactivos ni de los productos estequiométricos netos, no se consume durante la transformación y su masa y composición química se recuperan intactas al finalizar.",
        "distractores": [
            "Lo confunde con un reactivo que se consume, lo que contradice el hecho de que su masa final se mantiene inalterada.",
            "",
            "Lo describe como un disolvente, cuando en realidad es un catalizador heterogéneo sólido insoluble.",
            "Lo confunde con un inhibidor, el cual disminuiría la velocidad de reacción en vez de aumentarla drásticamente."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Reconoce la función de los catalizadores en la modificación de la energía de activación y la velocidad de reacción."
    },
    {
        "id": "cie-029",
        "area": "ciencias",
        "evidencia": "CIE_E2.1",
        "nivel": 2,
        "enunciado": "La combustión del gas metano se describe mediante la ecuación: $\\text{CH}_4(g) + 2\\text{O}_2(g) \\rightarrow \\text{CO}_2(g) + 2\\text{H}_2\\text{O}(g) + 890\\text{ kJ}$. ¿Cómo se clasifica esta reacción química según su balance energético?",
        "opciones": [
            "Endotérmica, porque requiere absorber 890 kJ de los alrededores para poder ocurrir.",
            "Exotérmica, porque libera 890 kJ de energía térmica al entorno al tener los productos menor entalpía que los reactivos.",
            "Adiabática, porque no intercambia ninguna forma de energía con el entorno.",
            "Isotérmica, porque la temperatura del sistema permanece constante en todo momento."
        ],
        "correcta": 1,
        "explicacion": "Cuando la energía térmica aparece como producto en la ecuación química (o $\\Delta H = -890\\text{ kJ/mol} < 0$), significa que la energía liberada en la formación de los nuevos enlaces en los productos es mayor que la energía requerida para romper los enlaces de los reactivos. La reacción desprende calor a los alrededores y se clasifica como exotérmica.",
        "distractores": [
            "La clasifica como endotérmica, lo cual requeriría que el calor apareciera en el lado de los reactivos ($\Delta H > 0$).",
            "",
            "La llama adiabática, ignorando la gran liberación de calor hacia el exterior típica de las combustiones.",
            "La clasifica como isotérmica confundiendo las condiciones termodinámicas controladas con el balance químico de entalpía."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Diferencia reacciones endotérmicas y exotérmicas a partir de ecuaciones termoquímicas y variación de entalpía."
    },
    {
        "id": "cie-030",
        "area": "ciencias",
        "evidencia": "CIE_E2.9",
        "nivel": 2,
        "enunciado": "Durante la fase luminosa de la fotosíntesis en las células vegetales, la clorofila de los tilacoides absorbe energía solar. ¿Cuál es el papel directo del agua ($\text{H}_2\text{O}$) en esta etapa del proceso?",
        "opciones": [
            "Fijar el dióxido de carbono directamente en moléculas de glucosa.",
            "Descomponerse por fotólisis, liberando oxígeno molecular a la atmósfera y aportando electrones y protones para formar ATP y NADPH.",
            "Almacenar el exceso de calor para impedir que la hoja aumente su temperatura.",
            "Actuar como la enzima Rubisco para catalizar el ciclo de Calvin."
        ],
        "correcta": 1,
        "explicacion": "En la fase luminosa (dependiente de la luz), la fotólisis del agua rompe las moléculas de $\\text{H}_2\\text{O}$ en protones ($H^+$), electrones ($e^-$) y oxígeno gas ($O_2$). Los electrones reponen los que la clorofila pierde al ser excitada por los fotones solares en el fotosistema II, y el oxígeno liberado se desprende a la atmósfera como subproducto vital.",
        "distractores": [
            "Le atribuye la fijación del carbono, lo cual ocurre en la fase oscura (ciclo de Calvin) usando dióxido de carbono y no agua.",
            "",
            "Confunde el rol bioquímico del agua con una función meramente amortiguadora de temperatura.",
            "Confunde la molécula inorgánica del agua con la proteína enzimática Rubisco."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Describe las etapas fundamentales de la fotosíntesis y el papel de la fotólisis del agua en la fase luminosa."
    },
    {
        "id": "cie-031",
        "area": "ciencias",
        "evidencia": "CIE_E2.8",
        "nivel": 2,
        "enunciado": "En un ecosistema de sabana en los Llanos Orientales, los productores primarios (pastos) capturan 10.000 kcal de energía solar neta por metro cuadrado al año. Si la eficiencia ecológica de transferencia entre niveles tróficos sucesivos es de aproximadamente el 10 %, ¿cuánta energía estará disponible aproximadamente para los consumidores secundarios (carnívoros)?",
        "opciones": [
            "10 kcal",
            "100 kcal",
            "1.000 kcal",
            "5.000 kcal"
        ],
        "correcta": 1,
        "explicacion": "De acuerdo con la regla del 10 % (Lindeman), solo cerca del 10 % de la energía acumulada en un nivel trófico se transfiere al nivel superior siguiente, perdiéndose el 90 % restante en calor metabólico, respiración y excreción. Nivel 1 (productores): 10.000 kcal $\\rightarrow$ Nivel 2 (herbívoros / consumidores primarios): $10.000\\cdot 0,10 = 1.000$ kcal $\\rightarrow$ Nivel 3 (consumidores secundarios): $1.000\\cdot 0,10 = 100$ kcal.",
        "distractores": [
            "Aplica una transferencia de 3 pasos sucesivos calculando para consumidores terciarios (10 kcal).",
            "",
            "Calcula la energía disponible para los consumidores primarios (herbívoros: 1.000 kcal), olvidando avanzar al siguiente nivel trófico.",
            "Asume erróneamente que se transfiere el 50 % de la energía entre niveles tróficos."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Modela el flujo unidireccional de energía y las pérdidas tróficas en ecosistemas mediante la regla del 10%."
    },
    {
        "id": "cie-032",
        "area": "ciencias",
        "evidencia": "CIE_E2.9",
        "nivel": 2,
        "enunciado": "Si una cadena molde de ADN tiene la secuencia de bases nitrogenadas $3'-\\text{T-A-C-G-G-A-A-C-T}-5'$, ¿cuál será la secuencia de ARN mensajero (ARNm) resultante de su transcripción en el núcleo celular?",
        "opciones": [
            "5'-A-T-G-C-C-T-T-G-A-3'",
            "5'-A-U-G-C-C-U-U-G-A-3'",
            "5'-U-A-C-G-G-A-A-C-U-3'",
            "3'-A-U-G-C-C-U-U-G-A-5'"
        ],
        "correcta": 1,
        "explicacion": "Durante la transcripción, la enzima ARN polimerasa sintetiza una hebra complementaria y antiparalela (de 5' a 3') emparejando: Adenina (A) frente a Timina (T), Uracilo (U) frente a Adenina (A), Guanina (G) frente a Citosina (C), y Citosina (C) frente a Guanina (G). El ARN contiene Uracilo (U) en lugar de Timina (T). Así: T $\\rightarrow$ A, A $\\rightarrow$ U, C $\\rightarrow$ G, G $\\rightarrow$ C, G $\\rightarrow$ C, A $\\rightarrow$ U, A $\\rightarrow$ U, C $\\rightarrow$ G, T $\\rightarrow$ A. La cadena es $5'-\\text{A-U-G-C-C-U-U-G-A}-3'$.",
        "distractores": [
            "Utiliza Timina (T) en vez de Uracilo (U), obteniendo una cadena de ADN complementario en lugar de ARN.",
            "",
            "Copia la misma secuencia idéntica del ADN reemplazando solo las T por U sin aplicar la regla de complementariedad.",
            "Escribe la secuencia complementaria pero con polaridad invertida (3' a 5')."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Aplica las reglas de complementariedad de bases nitrogenadas en el proceso de transcripción del ADN a ARNm."
    },
    {
        "id": "cie-033",
        "area": "ciencias",
        "evidencia": "CIE_E2.9",
        "nivel": 2,
        "enunciado": "En los seres humanos, una célula somática de la piel posee 46 cromosomas diploides (2n = 46). Tras culminar con éxito el proceso de meiosis en los órganos reproductores, ¿cuántos cromosomas posee cada óvulo o espermatozoide producido?",
        "opciones": [
            "23 cromosomas simples (haploide, n = 23)",
            "46 cromosomas dobles (diploide, 2n = 46)",
            "92 cromosomas tetraploides (4n = 92)",
            "12 pares de cromosomas homólogos"
        ],
        "correcta": 0,
        "explicacion": "La meiosis es una división celular reduccional que ocurre exclusivamente en la línea germinal para formar gametos. Reduce a la mitad el número de cromosomas de la especie (de $2n = 46$ a $n = 23$), garantizando que al unirse el óvulo y el espermatozoide en la fecundación se restablezca el número diploide característico de la especie humana (46 cromosomas).",
        "distractores": [
            "",
            "Confunde la meiosis con la mitosis ordinaria, la cual mantiene inalterado el número diploide de 46 cromosomas.",
            "Multiplica por dos los cromosomas confundiéndolo con la fase de duplicación previa a la división celular.",
            "Asigna un número arbitrario de pares (12 pares = 24 cromosomas), cometiendo un error numérico."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Diferencia la división celular meiótica y mitótica y explica el carácter haploide de los gametos sexuales."
    },
    {
        "id": "cie-034",
        "area": "ciencias",
        "evidencia": "CIE_E2.8",
        "nivel": 2,
        "enunciado": "En un hospital se detecta que una cepa de bacterias patógenas ha dejado de ser eliminada por un antibiótico de uso común. Desde el punto de vista de la teoría moderna de la evolución por selección natural, ¿cuál es la explicación científica de este fenómeno?",
        "opciones": [
            "El antibiótico enseñó a las bacterias a cambiar voluntariamente sus genes para defenderse.",
            "En la población bacteriana existían mutaciones preexistentes al azar que conferían resistencia; el antibiótico eliminó a las sensibles y las resistentes sobrevivieron y se reprodujeron.",
            "Las bacterias se volvieron inmunes porque el paciente tomó agua fría durante el tratamiento médico.",
            "El antibiótico perdió su composición química al entrar en contacto con el aire del hospital."
        ],
        "correcta": 1,
        "explicacion": "La selección natural actúa sobre la variabilidad genética preexistente en la población bacteriana generada por mutaciones espontáneas o transferencia horizontal de genes. Al aplicar el antibiótico, este actúa como una fuerte presión de selección ambiental que elimina a las bacterias susceptibles; las pocas bacterias portadoras del alelo de resistencia sobreviven, transmiten sus genes a su descendencia y aumentan su frecuencia en la población.",
        "distractores": [
            "Plantea una explicación lamarckiana teleológica donde el organismo muta voluntariamente para adaptarse.",
            "",
            "Asocia el fenómeno a mitos populares sin base biológica sobre el consumo de bebidas frías.",
            "Atribuye el fallo terapéutico a la degradación física del fármaco en vez del proceso evolutivo de resistencia bacteriana."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Explica la resistencia bacteriana como un caso de evolución por selección natural frente a presiones ambientales."
    },
    {
        "id": "cie-035",
        "area": "ciencias",
        "evidencia": "CIE_E1.1",
        "nivel": 2,
        "enunciado": "Cuando a una persona se le aplica una vacuna contra una enfermedad viral (por ejemplo, el sarampión), se le inocula una forma atenuada o inactiva del patógeno. ¿Cuál es el mecanismo fisiológico por el cual la vacuna confiere protección a largo plazo?",
        "opciones": [
            "El patógeno atenuado destruye de inmediato todos los virus que ya estaban en el cuerpo.",
            "Estimula al sistema inmune a producir anticuerpos específicos y generar linfocitos de memoria sin causar la enfermedad grave.",
            "Modifica permanentemente el ADN de todas las células del cuerpo haciéndolas inmunes al virus.",
            "Eleva la temperatura corporal a 42 °C de forma permanente para esterilizar la sangre."
        ],
        "correcta": 1,
        "explicacion": "Las vacunas exponen al sistema inmunitario a antígenos inofensivos del microorganismo. Los linfocitos B y T reconocen estos antígenos, se activan y generan linfocitos de memoria inmunológica y anticuerpos específicos. Si el patógeno real ingresa en el futuro, las células de memoria desencadenan una respuesta secundaria rápida e intensa que neutraliza el virus antes de que cause la enfermedad.",
        "distractores": [
            "Le atribuye un papel curativo o antiviral directo en vez de una inmunización profiláctica preventiva.",
            "",
            "Afirma falsamente que las vacunas alteran el genoma de las células humanas del organismo.",
            "Propone un mecanismo letal de hipertermia permanente incompatible con la vida humana."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Explica el principio biológico de la vacunación y la generación de memoria inmunológica en el cuerpo humano."
    },
    {
        "id": "cie-036",
        "area": "ciencias",
        "evidencia": "CIE_E2.9",
        "nivel": 2,
        "enunciado": "Durante una jornada de ejercicio físico intenso bajo el sol de Barranquilla, una persona experimenta vasodilatación cutánea (enrojecimiento de la piel) y una abundante sudoración. ¿Cuál es el objetivo fisiológico homeostático de estas respuestas corporales?",
        "opciones": [
            "Aumentar la temperatura corporal para quemar más tejido graso rápidamente.",
            "Disipar el calor interno acumulado hacia el ambiente mediante evaporación del sudor y radiación para mantener la temperatura en torno a 37 °C.",
            "Impedir que el cuerpo pierda agua y sales minerales esenciales.",
            "Detener la circulación sanguínea hacia los músculos esqueléticos activos."
        ],
        "correcta": 1,
        "explicacion": "La vasodilatación incrementa el flujo de sangre caliente hacia la superficie de la piel para favorecer la pérdida de calor por convección y radiación. Simultáneamente, las glándulas sudoríparas secretan sudor; al evaporarse el agua del sudor sobre la piel, absorbe una gran cantidad de calor latente de vaporización del cuerpo, enfriándolo eficazmente y manteniendo la temperatura interna dentro de límites compatibles con la vida (homeostasis térmica).",
        "distractores": [
            "Sugiere que el cuerpo busca elevar la temperatura, lo que provocaría un golpe de calor peligroso.",
            "",
            "Sostiene que la sudoración busca evitar la pérdida de agua, cuando precisamente el sudor expulsa agua para refrigerar.",
            "Afirma que se detiene la circulación muscular, lo cual impediría el suministro de oxígeno durante el ejercicio."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Explica los mecanismos de retroalimentación negativa y termorregulación en el mantenimiento de la homeostasis."
    },
    {
        "id": "cie-037",
        "area": "ciencias",
        "evidencia": "CIE_E1.2",
        "nivel": 2,
        "enunciado": "La tala masiva e indiscriminada de bosques tropicales contribuye de forma significativa al calentamiento global del planeta. ¿Cuál es la razón biológica directa de este impacto ecológico?",
        "opciones": [
            "Los árboles talados dejan de absorber dióxido de carbono ($\text{CO}_2$) mediante la fotosíntesis, y su quema o descomposición libera el carbono almacenado a la atmósfera como gas de efecto invernadero.",
            "Los árboles absorben nitrógeno del suelo y al talarlos el nitrógeno gaseoso destruye la capa de ozono.",
            "Al cortar los árboles, la gravedad de la Tierra disminuye permitiendo que los rayos solares entren con mayor fuerza.",
            "La madera talada atrae magnéticamente la radiación infrarroja solar hacia la superficie terrestre."
        ],
        "correcta": 0,
        "explicacion": "Los bosques actúan como sumideros de carbono vitales: mediante la fotosíntesis, los árboles capturan toneladas de $\\text{CO}_2$ atmosférico y lo fijan en forma de biomasa vegetal (madera, hojas y raíces). Al talar y quemar los bosques, no solo se anula este sumidero natural, sino que todo el carbono secuestrado durante décadas se libera a la atmósfera en forma de $\\text{CO}_2$, incrementando el efecto invernadero que atrapa calor en la troposfera.",
        "distractores": [
            "",
            "Confunde el ciclo del carbono con el nitrógeno y confunde el calentamiento global con el agujero en la capa de ozono.",
            "Plantea una hipótesis pseudocientífica absurda sobre la alteración de la constante gravitacional terrestre.",
            "Atribuye un magnetismo inexistente a la madera sobre la radiación electromagnética infrarroja."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Analiza las consecuencias ecológicas de la deforestación sobre el ciclo global del carbono y el cambio climático."
    },
    {
        "id": "cie-038",
        "area": "ciencias",
        "evidencia": "CIE_E2.9",
        "nivel": 2,
        "enunciado": "En la anemia de células falciformes (drepanocitosis), la sustitución de una sola base nitrogenada en el gen de la hemoglobina provoca el cambio de un aminoácido (ácido glutámico por valina). Este cambio altera la estructura terciaria de la proteína, deformando los glóbulos rojos en forma de media luna. ¿Qué tipo de mutación genética origina esta alteración?",
        "opciones": [
            "Una mutación puntual por sustitución de nucleótido.",
            "Una duplicación cromosómica de todo el brazo corto del cromosoma.",
            "Una poliploidía que añade un juego completo de cromosomas a la célula.",
            "Una deleción masiva que elimina la mitad de los genes de la hemoglobina."
        ],
        "correcta": 0,
        "explicacion": "La anemia falciforme es el ejemplo clásico de mutación génica puntual por sustitución: en el codón 6 del gen de la cadena beta de la globina, la adenina (A) es reemplazada por timina (T) ($GAG \\rightarrow GTG$). Esto provoca que en lugar de codificar ácido glutámico (hidrofílico) se incorpore valina (hidrofóbica), demostrando cómo un cambio en un solo nucleótido altera drásticamente la función de una macromolécula.",
        "distractores": [
            "",
            "Confunde una mutación puntual a nivel de un solo nucleótido con una anomalía cromosómica estructural a gran escala.",
            "La clasifica como poliploidía, la cual implica la multiplicación de juegos cromosómicos completos (3n, 4n).",
            "Sostiene que se eliminó la mitad de los genes, lo que no corresponde a una mutación puntual de cambio de sentido."
        ],
        "origen": "original",
        "competencia": "Uso comprensivo del conocimiento científico",
        "afirmacion": "Identifica los diferentes tipos de mutaciones genéticas a nivel molecular y sus efectos en la síntesis proteica."
    },
    {
        "id": "cie-039",
        "area": "ciencias",
        "evidencia": "CIE_E1.2",
        "nivel": 2,
        "enunciado": "Los ecosistemas de páramo en Colombia (como Chingaza o Sumapaz) albergan frailejones (*Espeletia*) y gruesas capas de musgo. Estos ecosistemas son reconocidos internacionalmente como 'fábricas de agua'. ¿Cuál es el mecanismo ecológico clave que explica esta función reguladora?",
        "opciones": [
            "Los frailejones bombean agua salada desde el manto terrestre mediante raíces profundas de más de mil metros.",
            "La vegetación y el suelo orgánico esponjoso retienen el agua de la neblina y las lluvias, liberándola gradualmente hacia las cuencas hidrográficas.",
            "Las hojas de los frailejones producen químicamente moléculas de agua a partir de radiación ultravioleta.",
            "El clima frío congela permanentemente el agua subterránea impidiendo que baje a los ríos."
        ],
        "correcta": 1,
        "explicacion": "Los páramos actúan como gigantescas esponjas naturales: las densas vellosidades de las hojas de los frailejones atrapan las diminutas gotas de agua de la constante niebla andina (condensación por intercepción), mientras que los suelos turbosos y los musgos retienen enormes volúmenes de agua pluvial, regulando el caudal de los ríos de manera sostenida a lo largo de todo el año, incluso en épocas de sequía.",
        "distractores": [
            "Plantea una hipótesis geológica irreal sobre bombeo de agua salada desde profundidades abisales.",
            "",
            "Afirma una síntesis mágica de agua por radiación que viola las leyes de la química orgánica y celular.",
            "Afirma que el agua está congelada de forma permanente (permafrost), lo que no describe los páramos colombianos donde el agua fluye líquida hacia los acueductos."
        ],
        "origen": "original",
        "competencia": "Explicación de fenómenos",
        "afirmacion": "Explica la importancia ecológica de los páramos en la regulación del ciclo hídrico y la provisión de agua."
    },
    {
        "id": "cie-040",
        "area": "ciencias",
        "evidencia": "CIE_E2.9",
        "nivel": 2,
        "enunciado": "El daltonismo (dificultad para distinguir el color rojo del verde) es una condición genética recesiva ligada al cromosoma X ($X^d$). Si una mujer portadora no daltónica ($X^D X^d$) tiene descendencia con un hombre con visión normal ($X^D Y$), ¿cuál es la probabilidad de que un hijo varón de esta pareja sea daltónico?",
        "opciones": [
            "0 %",
            "25 %",
            "50 %",
            "100 %"
        ],
        "correcta": 2,
        "explicacion": "Los hijos varones reciben obligatoriamente el cromosoma Y del padre y uno de los dos cromosomas X de la madre. Como la madre es heterocigota portadora ($X^D X^d$), tiene un 50 % de probabilidad de transmitir el alelo normal $X^D$ (hijo varón sano $X^D Y$) y un 50 % de probabilidad de transmitir el alelo recesivo $X^d$ (hijo varón daltónico $X^d Y$). Por tanto, la probabilidad en los hijos varones es del 50 %.",
        "distractores": [
            "Concluye que ningún varón será daltónico porque el padre es sano, olvidando que los varones no heredan el cromosoma X paterno.",
            "Calcula la probabilidad sobre el total de los 4 posibles descendientes sin restringirse a los hijos varones como pide la pregunta.",
            "",
            "Asume que todos los hijos varones de una madre portadora son obligatoriamente daltónicos."
        ],
        "origen": "original",
        "competencia": "Formulación y ejecución",
        "afirmacion": "Calcula probabilidades genéticas de herencia ligada al sexo en cuadros de Punnett."
    }
]

def actualizar_ciencias():
    with open('content/questions/ciencias.json', 'r', encoding='utf-8') as f:
        existentes = json.load(f)
    
    print(f'Preguntas de ciencias existentes antes: {len(existentes)}')
    ids_existentes = {q['id'] for q in existentes}
    
    nuevas = []
    for q in PREGUNTAS_CIE:
        if q['id'] not in ids_existentes:
            nuevas.append(q)
            
    existentes.extend(nuevas)
    print(f'Agregadas {len(nuevas)} preguntas nuevas de ciencias. Total ahora: {len(existentes)}')
    
    with open('content/questions/ciencias.json', 'w', encoding='utf-8') as f:
        json.dump(existentes, f, indent=2, ensure_ascii=False)
    print('Guardado content/questions/ciencias.json exitosamente.')

    # Actualizar unidades en content/unidades.json
    with open('content/unidades.json', 'r', encoding='utf-8') as f:
        units = json.load(f)
        
    unit_map = {u['id']: u for u in units}
    unit_map['u-proyectil']['preguntas'].extend(['cie-010', 'cie-018'])
    unit_map['u-mrua']['preguntas'].extend(['cie-011', 'cie-017'])
    unit_map['u-ohm']['preguntas'].extend(['cie-012'])
    unit_map['u-lentes']['preguntas'].extend(['cie-015', 'cie-016', 'cie-019'])
    unit_map['u-gases']['preguntas'].extend(['cie-013', 'cie-014', 'cie-026', 'cie-027'])
    unit_map['u-balanceo']['preguntas'].extend(['cie-020', 'cie-023', 'cie-028', 'cie-029'])
    unit_map['u-genetica']['preguntas'].extend(['cie-032', 'cie-033', 'cie-038', 'cie-040'])
    unit_map['u-ecologia']['preguntas'].extend(['cie-031', 'cie-034', 'cie-037', 'cie-039'])
    
    # Nuevas unidades de química y biología
    units.append({
        'id': 'u-quimica-base',
        'area': 'ciencias',
        'titulo': 'Estructura y transformaciones químicas',
        'resumen': 'Propiedades periódicas, enlaces iónicos y covalentes, y escala de pH.',
        'preguntas': ['cie-021', 'cie-022', 'cie-024', 'cie-025'],
        'sim': None,
        'leccion': None,
        'min': 15
    })
    units.append({
        'id': 'u-bio-celular',
        'area': 'ciencias',
        'titulo': 'Fisiología y homeostasis',
        'resumen': 'Fotosíntesis, sistema inmune y termorregulación en seres vivos.',
        'preguntas': ['cie-030', 'cie-035', 'cie-036'],
        'sim': None,
        'leccion': None,
        'min': 15
    })
    
    with open('content/unidades.json', 'w', encoding='utf-8') as f:
        json.dump(units, f, indent=1, ensure_ascii=False)
    print('Guardado content/unidades.json con las unidades de ciencias actualizadas.')

if __name__ == '__main__':
    actualizar_ciencias()
