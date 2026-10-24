"""Reescribe las razones que empiezan con 'Es incorrecta porque' en content/icfes/.
Elimina el prefijo formulaico repetitivo y hace que cada razón empiece directamente
con la explicación específica de la opción y la pregunta.
"""
import glob
import json
import re

def transform_distractor(s):
    if not isinstance(s, str):
        return s
    if s.startswith('Es incorrecta porque, '):
        rest = s[len('Es incorrecta porque, '):]
        return rest[0].upper() + rest[1:]
    if s.startswith('Es incorrecta porque '):
        rest = s[len('Es incorrecta porque '):]
        return rest[0].upper() + rest[1:]
    return s

def transform_pero(s):
    if not isinstance(s, str):
        return s
    if s.startswith('Pero es incorrecta porque, '):
        rest = s[len('Pero es incorrecta porque, '):]
        return 'Pero ' + rest[0].lower() + rest[1:]
    if s.startswith('Pero es incorrecta porque '):
        rest = s[len('Pero es incorrecta porque '):]
        return 'Pero ' + rest[0].lower() + rest[1:]
    return s

def transform_guion_text(s):
    if not isinstance(s, str):
        return s
    # Patrón: 'La opción X es incorrecta: Es incorrecta porque ...'
    m = re.match(r'^(La opción [A-H] (?:es incorrecta|no corresponde)): Es incorrecta porque (.*)$', s)
    if m:
        pref, rest = m.group(1), m.group(2)
        return f'{pref}: {rest[0].upper() + rest[1:]}'
    return s

def process_question(q):
    changed = False
    # 1. distractores
    if 'distractores' in q and isinstance(q['distractores'], list):
        new_d = [transform_distractor(d) for d in q['distractores']]
        if new_d != q['distractores']:
            q['distractores'] = new_d
            changed = True
    # 2. hoja
    h = q.get('hoja')
    if isinstance(h, dict):
        # enfoque.no
        enf = h.get('enfoque')
        if isinstance(enf, dict) and 'no' in enf and isinstance(enf['no'], list):
            for item in enf['no']:
                if isinstance(item, dict) and 'p' in item:
                    np = transform_pero(item['p'])
                    if np != item['p']:
                        item['p'] = np
                        changed = True
        # guion
        gui = h.get('guion')
        if isinstance(gui, dict):
            for lvl in ['1', '2', '3']:
                steps = gui.get(lvl, [])
                if isinstance(steps, list):
                    for step in steps:
                        if isinstance(step, dict) and 't' in step:
                            nt = transform_guion_text(step['t'])
                            if nt != step['t']:
                                step['t'] = nt
                                changed = True
    return changed

def main():
    files = sorted(glob.glob('content/icfes/**/*.json', recursive=True))
    modified_files = 0
    total_qs = 0

    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        file_changed = False
        if isinstance(data, list):
            for q in data:
                if isinstance(q, dict) and process_question(q):
                    file_changed = True
                    total_qs += 1
        elif isinstance(data, dict):
            if 'preguntas' in data and isinstance(data['preguntas'], list):
                for q in data['preguntas']:
                    if isinstance(q, dict) and process_question(q):
                        file_changed = True
                        total_qs += 1
            if 'hoja' in data and isinstance(data['hoja'], dict):
                if process_question(data):
                    file_changed = True
                    total_qs += 1

        if file_changed:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write('\n')
            modified_files += 1

    print(f'Proceso completado: {modified_files} archivos modificados, {total_qs} preguntas actualizadas.')

if __name__ == '__main__':
    main()
