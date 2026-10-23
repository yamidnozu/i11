"""Estructura el cuadernillo mixto de 2014 por rangos de área configurables."""
from __future__ import annotations
import re

import cuadernillo


def detectar(ctx):
    return cuadernillo.detectar(ctx)


def extraer(ctx):
    return cuadernillo.extraer(ctx)


def _area_for(number: int, ranges: list[dict]) -> str | None:
    for item in ranges:
        if int(item['desde']) <= number <= int(item['hasta']):
            return item['area']
    return None


def estructurar(ctx):
    pack = cuadernillo.estructurar(ctx)
    ranges = ctx['spec'].get('rangos_area', [])
    if not ranges:
        raise ValueError('mixto2014 requiere rangos_area en config.json')
    for q in pack.get('preguntas', []):
        match = re.search(r'(?:-i|-)(\d{3,4})$', q['id'])
        if not match:
            q.setdefault('revisar', []).append('No se pudo determinar el número global para asignar el área.')
            continue
        number = int(match.group(1))
        area = _area_for(number, ranges)
        if area is None:
            q.setdefault('revisar', []).append('Número fuera de los rangos de área configurados; clasificar manualmente.')
            continue
        q['area'] = area
        display = next((r.get('nombre', area) for r in ranges if r['area'] == area), area)
        q['parte'] = f"Prueba {display}, pregunta {number}"
        if 104 <= number <= 106:
            # Banco gráfico A-H del bloque de Inglés 104–106; el parser clásico
            # solo modela cuatro alternativas. Mantener la clave en su índice
            # oficial y marcar las ocho opciones para cotejo visual.
            letters = list('ABCDEFGH')
            correct = q['correcta']
            q['opciones'] = [f'(Opción {letter}: transcripción pendiente del banco gráfico.)' for letter in letters]
            q['distractores'] = ['' if i == correct else 'Pendiente de análisis hasta cotejar la opción original.' for i in range(len(letters))]
            q['opcionesFig'] = [{'tipo': 'pendiente', 'alt': f'Opción {letter} de la pregunta {number}; banco A-H sin cotejar.'} for letter in letters]
            q.setdefault('revisar', []).append('Banco de opciones A-H: transcribir y enlazar desde la página fuente antes de uso.')
    for q in pack.get('pendientes_clave', []):
        match = re.search(r'(?:-i|-)(\d{3,4})$', q.get('id', ''))
        if match:
            area = _area_for(int(match.group(1)), ranges)
            if area:
                q['area'] = area

    ids_by_area: dict[str, list[str]] = {}
    for q in pack.get('preguntas', []):
        ids_by_area.setdefault(q['area'], []).append(q['id'])
    names = {r['area']: r.get('nombre', r['area'].replace('_', ' ').title()) for r in ranges}
    pack['unidades'] = [
        {'id': f"u-icfes-{ctx['spec']['prefijo']}-{area}", 'area': area,
         'titulo': names.get(area, area), 'resumen': 'Sección del cuadernillo mixto de 2014; reactivos en revisión de transcripción.',
         'preguntas': ids, 'sim': None, 'leccion': None, 'min': max(10, len(ids))}
        for area, ids in sorted(ids_by_area.items())
    ]
    pack['simulacros'] = [{
        'id': f"sim-icfes-{ctx['spec']['prefijo']}", 'nombre': f"Simulacro: {ctx['spec']['prueba']}",
        'descripcion': 'Cuadernillo mixto dividido por área; validar transcripción, clave y figuras antes de usar.',
        'nivel': 'En revisión', 'barajar': False, 'modo': 'secciones',
        'secciones': [
            {'titulo': names.get(area, area), 'area': area, 'minutos': len(ids), 'preguntas': ids}
            for area, ids in sorted(ids_by_area.items())
        ]
    }] if ids_by_area else []
    return pack
