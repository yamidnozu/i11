"""Incrusta la hoja pedagógica completa (de hojas.json, guiones.json y enfoques.json)
directamente en las 30 preguntas de content/questions/ que la tenían en archivos externos.
"""
import glob
import json

def main():
    hojas = json.load(open('content/hojas.json', encoding='utf-8'))
    guiones = json.load(open('content/guiones.json', encoding='utf-8'))
    enfoques = json.load(open('content/enfoques.json', encoding='utf-8'))

    total_embedded = 0

    for path in sorted(glob.glob('content/questions/*.json')):
        with open(path, 'r', encoding='utf-8') as f:
            qs = json.load(f)

        file_changed = False
        for q in qs:
            qid = q.get('id')
            if 'hoja' not in q or not q['hoja']:
                h = hojas.get(qid)
                if h:
                    g = guiones.get(qid)
                    en = enfoques.get(qid)
                    q['hoja'] = {
                        **h,
                        'guion': g or h.get('guion'),
                        'enfoque': en or h.get('enfoque')
                    }
                    total_embedded += 1
                    file_changed = True

        if file_changed:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(qs, f, ensure_ascii=False, indent=2)
                f.write('\n')
            print(f'Actualizado {path}')

    print(f'Total de preguntas con hoja incrustada: {total_embedded}')

if __name__ == '__main__':
    main()
