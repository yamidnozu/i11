"""Extractor conservador para los cuadernillos de Inglés con exámenes repetidos.

Cada examen vuelve a numerar sus reactivos del 1 al 25. El identificador incorpora
el examen para evitar colisiones; las partes dependientes de imágenes o de texto
que Poppler no pudo extraer quedan marcadas para cotejo, nunca se completan por
inferencia.
"""
from __future__ import annotations
import re
from pathlib import Path

import cuadernillo


def detectar(ctx):
    import fitz
    doc = fitz.open(ctx['source'])
    text = '\n'.join(page.get_text(sort=True) for page in doc)
    exams = len(re.findall(r'(?im)^\s*EXAMEN\s+[12]\s*$', text))
    return {
        'pages': len(doc),
        'examenes_detectados': exams,
        'tablas_clave': len(re.findall(r'(?i)tabla de respuestas correctas', text)),
        'title': doc.metadata.get('title'),
    }


def extraer(ctx):
    return cuadernillo.extraer(ctx)


def _keys(text: str, exam: int, exam_count: int) -> dict[int, str]:
    """Lee tablas por separado; las filas con nivel de dificultad se ignoran."""
    keys: dict[int, str] = {}
    # Ediciones 2024/2021: encabezado explícito de cada tabla.
    headings = list(re.finditer(r'(?im)^\s*Tabla de respuestas correctas(?:\s*-\s*Examen\s+(\d+))?\s*$', text))
    for i, heading in enumerate(headings):
        named = int(heading.group(1)) if heading.group(1) else None
        start = heading.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        table = text[start:end]
        if named == exam or (named is None and len(headings) > 1 and i + 1 == exam):
            for row in re.finditer(r'(?m)^\s*(\d{1,2})\s+([A-H])(?:\s|$)', table):
                n, answer = int(row.group(1)), row.group(2)
                if 1 <= n <= 25:
                    keys[n] = answer
    if keys:
        return keys

    # Inglés 2018: dos claves paralelas en una sola tabla.
    if re.search(r'(?i)informaci[oó]n de cada pregunta', text):
        table = text.split('Información de cada pregunta', 1)[1]
        for row in re.finditer(r'(?m)^\s*(\d{1,2})\s+[^\n]*?\b([A-H])\s+(\d{1,2})\s+[^\n]*?\b([A-H])\s*$', table):
            left_n, left_key, right_n, right_key = row.groups()
            n, answer = (int(left_n), left_key) if exam == 1 else (int(right_n), right_key)
            if 1 <= n <= 25:
                keys[n] = answer
    return keys


def _exam_region(text: str, exam: int) -> str:
    starts = list(re.finditer(r'(?im)^\s*EXAMEN\s+([12])\s*$', text))
    selected = next((i for i, m in enumerate(starts) if int(m.group(1)) == exam), None)
    if selected is None:
        return ''
    start = starts[selected].end()
    end = starts[selected + 1].start() if selected + 1 < len(starts) else len(text)
    # Stop before answer key tables, which may repeat the exam title.
    tail = text[start:end]
    cut = re.search(r'(?im)^\s*(?:Tabla de respuestas correctas|Informaci[oó]n de cada pregunta)\b', tail)
    if cut:
        tail = tail[:cut.start()]
    return tail


def estructurar(ctx):
    text = (ctx['dirs']['texto'] / 'documento.txt').read_text(encoding='utf-8')
    cfg = ctx['spec']
    pref = cfg['prefijo']
    exam_count = len(list(re.finditer(r'(?im)^\s*EXAMEN\s+[12]\s*$', text)))
    exam_count = min(2, max(1, exam_count))
    questions = []
    exam_keys: dict[int, dict[int, str]] = {}

    for exam in range(1, exam_count + 1):
        region = _exam_region(text, exam)
        keys = _keys(text, exam, exam_count)
        exam_keys[exam] = keys
        marks = list(re.finditer(r'(?m)^\s*(\d{1,2})\.\s+', region))
        # El número puede aparecer impreso junto a un ejemplo, pero solo se
        # conservan las posiciones de la tabla oficial de respuestas.
        candidates = []
        for idx, mark in enumerate(marks):
            n = int(mark.group(1))
            if n not in keys:
                continue
            end = marks[idx + 1].start() if idx + 1 < len(marks) else len(region)
            raw = region[mark.end():end]
            previous_parts = list(re.finditer(r'(?im)^.*\bPARTE\s*([1-7])\b.*$', region[:mark.start()]))
            part = int(previous_parts[-1].group(1)) if previous_parts else 0
            candidates.append((n, raw, part))

        # En un examen, una fila de una tabla o el folio puede parecer pregunta.
        # Guardar un único candidato por número, el que expone más alternativas.
        chosen: dict[int, str] = {}
        chosen_parts: dict[int, int] = {}
        for n, raw, part in candidates:
            option_count = len(re.findall(r'(?<![\w])([A-H])\.\s*', raw))
            previous = chosen.get(n)
            if previous is None or option_count > len(re.findall(r'(?<![\w])([A-H])\.\s*', previous)):
                chosen[n] = raw
                chosen_parts[n] = part

        for n in sorted(keys):
            raw = chosen.get(n, '')
            lines = raw.splitlines()
            raw = re.split(r'(?im)^\s*(?:Saber 11(?:\.º|\.°)?|Cuadernillo de preguntas|Prueba Ingl[eé]s)\b', raw)[0]
            # En Inglés, Poppler suele poner varias alternativas en la misma
            # línea. Se buscan marcas A. ... H. dentro de cada reactivo y se
            # conserva literalmente el texto entre marcas.
            option_marks = list(re.finditer(r'(?<![\w])([A-H])\.\s*', raw))
            stem_raw = raw[:option_marks[0].start()] if option_marks else raw
            stem = re.sub(r'\s+', ' ', stem_raw).strip()
            option_map: dict[str, str] = {}
            for oi, mark in enumerate(option_marks):
                end = option_marks[oi + 1].start() if oi + 1 < len(option_marks) else len(raw)
                value = re.sub(r'\s+', ' ', raw[mark.end():end]).strip()
                value = re.sub(r'\s+\d{1,2}\s*$', '', value).strip()
                if value and mark.group(1) not in option_map:
                    option_map[mark.group(1)] = value
            part = chosen_parts.get(n, 0)
            expected = 'ABCDEFGH' if part == 1 else 'ABC' if 2 <= part <= 5 else 'ABCD' if part in (6, 7) else 'ABCDEFGH'
            letters = list(expected)
            answer = keys[n]
            flags = []
            if not stem:
                stem = f'(Enunciado de la pregunta {n} del examen {exam}: requiere cotejo con la página fuente.)'
                flags.append('Enunciado ausente o contenido en imagen; transcribir desde el PDF antes de publicar.')
            if not option_map:
                # Conservar índice de respuesta oficial en una estructura
                # explícitamente pendiente, sin fingir que las opciones son texto.
                opts = [f'(Opción {letter}: contenido gráfico pendiente de transcripción.)' for letter in letters]
                flags.append('Opciones no extraíbles como texto; cotejar y transcribir desde la imagen original.')
            else:
                opts = [option_map.get(letter, f'(Opción {letter}: contenido pendiente de transcripción.)') for letter in letters]
                if answer not in expected or len(option_map) < 2:
                    # La letra es oficial, pero el OCR no delimitó la alternativa.
                    flags.append('La extracción de opciones no contiene la alternativa de la clave; cotejar visualmente.')
            # Pasajes leídos como imagen no se reconstruyen a partir del tema.
            if n >= 17 and not stem:
                flags.append('Contexto de lectura posiblemente incrustado como imagen; requiere transcripción literal.')
            right = list(expected).index(answer) if answer in expected else 0
            if right >= len(opts):
                flags.append('La clave no se pudo alinear con las opciones extraídas; verificar clave y orden.')
            stable_position = n + (exam - 1) * 25
            exam_id = f'{pref}-i{stable_position:03d}'
            cite = f"Icfes ({cfg['anio']}). {cfg['prueba']}, Examen {exam}, Cuadernillo de preguntas. Saber 11.º. Bogotá, D. C.: Instituto Colombiano para la Evaluación de la Educación (Icfes). Pregunta {n}."
            questions.append({
                'id': exam_id,
                'area': cfg['area'],
                'evidencia': 'Pendiente de asociación con el marco de referencia de Inglés',
                'nivel': 2,
                'enunciado': stem,
                'opciones': opts,
                'correcta': right,
                'explicacion': 'Pendiente de solución razonada y cotejo pedagógico; la clave se transcribió de la tabla oficial del examen correspondiente.',
                'distractores': ['' if i == right else 'Pendiente de análisis; no se infiere una justificación sin cotejar el reactivo completo.' for i in range(len(opts))],
                'origen': cfg['origen'],
                'fuente': cite,
                'parte': f'Examen {exam}, pregunta {n}',
                'revisar': sorted(set(flags + ['Cotejar enunciado y alternativas con la página fuente antes de cualquier uso.'])),
            })

    all_ids = [q['id'] for q in questions]
    area = cfg['area']
    package = {
        'id': f"icfes-{pref}",
        'nombre': cfg['prueba'],
        'version': 1,
        'preguntas': questions,
        'bloques': [],
        'unidades': [{'id': f'u-icfes-{pref}', 'area': area, 'titulo': cfg['prueba'], 'resumen': 'Reactivos separados por examen; pendientes de cotejo textual y pedagógico.', 'preguntas': all_ids, 'sim': None, 'leccion': None, 'min': max(10, len(all_ids))}],
        'simulacros': [{'id': f'sim-icfes-{pref}', 'nombre': f"Simulacro: {cfg['prueba']}", 'descripcion': 'Estructura por examen; reactivos pendientes de cotejo con la fuente antes de uso.', 'nivel': 'En revisión', 'barajar': False, 'modo': 'secciones', 'secciones': [{'titulo': f'Examen {exam}', 'area': area, 'minutos': len([q for q in questions if q['parte'].startswith(f'Examen {exam},')]), 'preguntas': [q['id'] for q in questions if q['parte'].startswith(f'Examen {exam},')]} for exam in range(1, exam_count + 1)]}]
    }
    return package
