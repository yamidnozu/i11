"""Script de corrección y barajado de Odontología:
1. Elimina toda mención a números de líneas (líneas ...) en enunciados, explicaciones y marcas,
   dejando redacciones clínicas naturales.
2. Ajusta odo-018 según la fuente: la osteítis condensante es radiopaca difusa y puede
   remitir lentamente tras el tratamiento o persistir como cicatriz ósea.
3. Aplica un barajado pseudoaleatorio determinista (semilla fija) para romper el ciclo
   de claves (0,1,2,3,0,1,2,3...), garantizando distribución balanceada (16 A, 16 B, 15 C, 15 D),
   máximo 2 claves iguales consecutivas y cero patrones cíclicos.
4. Actualiza en perfecta sincronía: correcta, distractores, hoja.enfoque.descartes,
   hoja.enfoque.no, hoja.guion['1'], hoja.guion['2'] y hoja.guion['3'].
5. Reemplaza cualquier ocurrencia residual de la palabra 'línea' o 'linea' por sinónimos
   clínicos precisos (cortical, espacio, trazo, contorno), logrando 0 coincidencias de /l[ii]nea/.
6. Valida exhaustivamente integridad de marcas, descartes y cero cifras en textos hablados.
"""

import json
import re
import random
import sys

LETTERS = ['A', 'B', 'C', 'D']

def clean_enunciado(qid, en):
    # Remove (líneas ...) or (línea ...)
    en = re.sub(r'\s*\(líneas?[^\)]*\)', '', en, flags=re.IGNORECASE)
    # Naturalize "en la Clase 2"
    en = re.sub(r'\s*en la Clase 2\b', ' según lo visto en clase', en)
    # Specific naturalizations
    en = re.sub(r'De acuerdo con lo enseñado por el profesor en clase,\s*', 'De acuerdo con lo visto en clase, ', en)
    en = re.sub(r'De acuerdo con lo explicado por el profesor en clase,\s*', 'De acuerdo con lo visto en clase, ', en)
    en = re.sub(r'De acuerdo con la clase,\s*', 'De acuerdo con lo visto en clase, ', en)
    en = re.sub(r'En el inicio de la Clase 2 sobre histología', 'En la clase sobre histología', en)
    en = re.sub(r'Siguiendo con la biología pulpar en la Clase 2', 'Siguiendo con la biología pulpar vista en clase', en)
    en = re.sub(r'En el manejo de los traumatismos dentoalveolares en la Clase 2', 'En el manejo de los traumatismos dentoalveolares visto en clase', en)
    en = re.sub(r'En el cierre de la Clase 2 sobre', 'En el cierre de la clase sobre', en)
    en = re.sub(r'Al abordar el tratamiento del Absceso Apical Crónico con fístula en la Clase 2', 'Al abordar el tratamiento del Absceso Apical Crónico con fístula visto en clase', en)
    en = re.sub(r'En el manejo farmacológico del Absceso Apical Agudo en la Clase 2', 'En el manejo farmacológico del Absceso Apical Agudo visto en clase', en)
    en = re.sub(r'En la patología de reabsorción dental en la Clase 2', 'En la patología de reabsorción dental vista en clase', en)
    en = re.sub(r'Al analizar las causas de las enfermedades pulpares.*?, el docente describe', 'Al analizar las causas de las enfermedades pulpares según lo visto en clase, el docente describe', en)
    en = re.sub(r'\s+', ' ', en).strip()
    return en

def clean_explicacion(qid, exp):
    exp = re.sub(r'En las líneas\s+[^,]+(?:del texto fuente)?,\s*el\s+(profesor|docente)', r'En la clase de endodoncia, el \1', exp, flags=re.IGNORECASE)
    exp = re.sub(r'\(líneas?[^\)]*\)', '', exp, flags=re.IGNORECASE)
    exp = re.sub(r'en las líneas\s+[^,;:\.]+', 'en la clase de endodoncia', exp, flags=re.IGNORECASE)
    exp = re.sub(r'del texto fuente,?\s*', '', exp, flags=re.IGNORECASE)
    exp = re.sub(r'\s+', ' ', exp).strip()
    return exp

def get_target_keys():
    # Sequence generated with seed 20261024
    # Counts: 0: 16 (25.8%), 1: 16 (25.8%), 2: 15 (24.2%), 3: 15 (24.2%)
    # Max consecutive: 2, No 4-cycles
    return [
        1, 2, 0, 3, 0, 0, 2, 1, 1, 0, 2, 0, 2, 2, 1, 3, 0, 0, 3, 0,
        1, 0, 2, 1, 1, 2, 1, 3, 3, 0, 3, 2, 0, 3, 2, 1, 2, 3, 2, 0,
        3, 3, 2, 1, 0, 1, 1, 0, 1, 1, 3, 2, 3, 2, 1, 0, 3, 2, 3, 3,
        1, 0
    ]

def run():
    target_keys = get_target_keys()
    assert len(target_keys) == 62, "target_keys must have length 62"
    counts = {k: target_keys.count(k) for k in range(4)}
    print(f"Target key distribution: A:{counts[0]}, B:{counts[1]}, C:{counts[2]}, D:{counts[3]}")
    
    with open("content/questions/odontologia.json", "r", encoding="utf-8") as f:
        qs = json.load(f)
        
    assert len(qs) == 62, f"Se esperaban 62 preguntas, hay {len(qs)}"
    
    for idx, q in enumerate(qs):
        qid = q["id"]
        
        # 1. Limpieza de líneas en enunciado y explicación
        q["enunciado"] = clean_enunciado(qid, q["enunciado"])
        q["explicacion"] = clean_explicacion(qid, q["explicacion"])
        
        # 2. Ajustes específicos de odo-018
        if qid == "odo-018":
            old_c = q["correcta"]
            q["opciones"][old_c] = "Zona radiopaca difusa (no circunscrita) periapical en un diente con inflamación pulpar crónica; el hueso esclerótico reactivo puede persistir como cicatriz ósea o remitir lentamente tras el tratamiento endodóntico exitoso."
            q["explicacion"] = "En la clase de endodoncia, el profesor explicó detalladamente la osteítis condensante (osteoesclerosis periapical): es una reacción ósea proliferativa densa y radiopaca en respuesta a una irritación pulpar crónica de baja intensidad en pacientes jóvenes con buen potencial defensivo. El docente recalcó dos conceptos fundamentales: 1) Es una imagen radiopaca DIFUSA alrededor del ápice, no circunscrita ni delimitada; si fuera muy redondeada y nítida se debe sospechar otra patología como hipercementosis o cementoma (displasia cementaria periapical); 2) La osteítis condensante representa aposición ósea trabecular reactiva: tras el tratamiento de conductos exitoso que elimina el estímulo infeccioso pulpar, la lesión puede remitir paulatinamente con el tiempo o permanecer como una cicatriz ósea esclerótica asintomática sin requerir ninguna intervención adicional."
            q["hoja"]["enfoque"]["clave"] = "La osteítis condensante es una radiopacidad periapical difusa (no circunscrita) que puede remitir tras la endodoncia o persistir como cicatriz ósea."
            for s in q["hoja"]["pasos"]:
                if "desaparece" in s["texto"]:
                    s["texto"] = "La osteítis condensante puede remitir lentamente tras el tratamiento de conductos o persistir como cicatriz ósea."
                if s["titulo"] == "Persistencia post-tratamiento":
                    s["titulo"] = "Evolución post-tratamiento"
                    
        # 3. Limpieza de marcas con mención a líneas
        for m in q.get("hoja", {}).get("marcas", []):
            m["frag"] = re.sub(r'\s*\(líneas?[^\)]*\)', '', m["frag"], flags=re.IGNORECASE)
            m["frag"] = re.sub(r'\s+', ' ', m["frag"]).strip()
            
        for step in q.get("hoja", {}).get("guion", {}).get("1", []):
            act = step.get("a", "")
            if act.startswith("m:"):
                frag = act[2:]
                frag = re.sub(r'\s*\(líneas?[^\)]*\)', '', frag, flags=re.IGNORECASE)
                frag = re.sub(r'\s+', ' ', frag).strip()
                step["a"] = f"m:{frag}"
                
        # 4. Barajado de opciones determinista
        old_corr = q["correcta"]
        target_k = target_keys[idx]
        
        old_opciones = q["opciones"]
        old_distractores = q["distractores"]
        
        distractor_pairs = []
        for j in range(4):
            if j != old_corr:
                distractor_pairs.append((old_opciones[j], old_distractores[j]))
                
        item_rng = random.Random(20261024 + idx * 37)
        item_rng.shuffle(distractor_pairs)
        
        new_opciones = [None] * 4
        new_distractores = [None] * 4
        
        # Colocar respuesta correcta en target_k
        new_opciones[target_k] = old_opciones[old_corr]
        new_distractores[target_k] = ""
        
        d_idx = 0
        for k in range(4):
            if k != target_k:
                new_opciones[k] = distractor_pairs[d_idx][0]
                new_distractores[k] = distractor_pairs[d_idx][1]
                d_idx += 1
                
        q["opciones"] = new_opciones
        q["correcta"] = target_k
        q["distractores"] = new_distractores
        new_letter = LETTERS[target_k]
        
        # 5. Reconstruir hoja.enfoque.descartes
        descartes = {}
        for k in range(4):
            if k != target_k:
                L = LETTERS[k]
                descartes[L] = f"No es correcta. {new_distractores[k]}"
        q["hoja"]["enfoque"]["descartes"] = descartes
        
        # 6. Reconstruir hoja.enfoque.no
        no_list = []
        for k in range(4):
            if k != target_k:
                L = LETTERS[k]
                d = new_distractores[k]
                p_text = d if d.startswith("Pero ") else f"Pero {d[0].lower() + d[1:]}"
                no_list.append({"t": f"Opción {L}", "p": p_text})
        q["hoja"]["enfoque"]["no"] = no_list
        
        # 7. Actualizar último paso de guion['1']
        lvl1 = q["hoja"]["guion"]["1"]
        lvl1[-1] = {
            "a": f"o:{new_letter}:ok",
            "t": f"Concluimos que la respuesta fundamentada corresponde a la opción {new_letter}: {new_opciones[target_k]}"
        }
        
        # 8. Reconstruir guion['2'] (descartes o:X:no + ok)
        lvl2 = [
            {"a": "leer", "t": "Analicemos detalladamente por qué se descartan las alternativas incorrectas según la semiología clínica."}
        ]
        for k in range(4):
            if k != target_k:
                L = LETTERS[k]
                d = new_distractores[k]
                lvl2.append({"a": f"o:{L}:no", "k": "err", "t": f"La opción {L} es incorrecta: {d}"})
        lvl2.append({
            "a": f"o:{new_letter}:ok",
            "t": f"Por correlación semiológica y descarte riguroso, la opción {new_letter} es la respuesta correcta."
        })
        q["hoja"]["guion"]["2"] = lvl2
        
        # 9. Actualizar último paso de guion['3']
        lvl3 = q["hoja"]["guion"]["3"]
        lvl3[-1] = {
            "a": f"o:{new_letter}:ok",
            "t": f"Confirmamos con certeza clínica que la opción adecuada es {new_letter}."
        }
        
    # Reemplazo de palabras con raíz línea/linea por términos clínicos precisos
    json_text = json.dumps(qs, ensure_ascii=False, indent=2)
    
    replacements = [
        ('conservando la línea del ligamento periodontal', 'conservando el espacio del ligamento periodontal'),
        ('Línea radiolúcida fina que bordea exclusivamente el tercio coronal', 'Banda radiolúcida fina que bordea exclusivamente el tercio coronal'),
        ('como primera línea, considerando cirugía', 'como primera elección, considerando cirugía'),
        ('en las primeras líneas de la clase', 'al inicio de la clase'),
        ('a lo largo de la línea de fisura', 'a lo largo del trazo de fisura'),
        ('exactamente en esa línea permitiendo', 'exactamente en ese trazo permitiendo'),
        ('como línea radiopaca ósea', 'como estructura radiopaca ósea'),
        ('la fina línea blanca radiopaca', 'la fina cortical blanca radiopaca'),
        ('Es la línea blanca radiopaca', 'Es la cortical blanca radiopaca'),
        ('Si la línea blanca se borra', 'Si la cortical blanca se borra'),
        ('La lámina dura es la línea radiopaca', 'La lámina dura es la cortical radiopaca'),
        ('Busca la línea delgada blanca', 'Busca el contorno delgado blanco'),
        ('esa línea blanca finita', 'esa cortical blanca finita'),
        ('que esa línea blanca se llama', 'que esa cortical blanca se llama'),
        ('se alinean contra la predentina', 'se disponen contra la predentina'),
        ('fresa de Peeso desalineada', 'fresa de Peeso desviada'),
        ('para primera línea y clindamicina', 'como primera elección y clindamicina'),
        ('en el mismo plano de la línea de ruptura', 'en el mismo plano del trazo de ruptura'),
        ('dibuja la línea donde la raíz se partió', 'dibuja el trazo donde la raíz se partió')
    ]
    
    for old, new in replacements:
        if old in json_text:
            json_text = json_text.replace(old, new)
            
    # Verificar cero coincidencias de /l[ii]nea/
    linea_matches = re.findall(r'.{0,30}l[ií]nea.{0,30}', json_text, re.IGNORECASE)
    print(f"Coincidencias residuales de /l[ii]nea/: {len(linea_matches)}")
    if linea_matches:
        for m in linea_matches:
            print("  Falta reemplazar:", m.strip())
        sys.exit(1)
        
    qs = json.loads(json_text)
    
    # Validaciones finales
    print("\nValidando todas las preguntas transformadas...")
    issues = []
    longest_count = 0
    
    for q in qs:
        qid = q["id"]
        en = q["enunciado"]
        h = q["hoja"]
        corr = q["correcta"]
        corr_letter = LETTERS[corr]
        
        # Marcas presentes y sin solapamiento
        frags = []
        for m in h["marcas"]:
            f = m["frag"]
            frags.append(f)
            if f not in en:
                issues.append(f"{qid}: marca '{f}' no encontrada en enunciado")
                
        for i in range(len(frags)):
            for j in range(i + 1, len(frags)):
                f1, f2 = frags[i], frags[j]
                a = en.find(f1)
                b = a + len(f1)
                c = en.find(f2)
                d = c + len(f2)
                if a < d and c < b:
                    issues.append(f"{qid}: solapamiento entre '{f1}' y '{f2}'")
                    
        # Marcas en guion 1
        marcas_set = set(frags)
        for step in h["guion"]["1"]:
            act = step.get("a", "")
            if act.startswith("m:"):
                frag = act[2:]
                if frag not in marcas_set:
                    issues.append(f"{qid}: guion 1 acción m:{frag} no declarada en marcas")
                    
        # Comprobar o:X:no en guion 2
        dichas = set()
        for b in h["guion"]["2"]:
            a = b.get("a", "")
            for act in a.split("|"):
                if act.startswith("o:") and act.endswith(":no"):
                    dichas.add(act[2])
        for i in range(4):
            if i != corr:
                L = LETTERS[i]
                if L not in dichas:
                    issues.append(f"{qid}: falta descarte o:{L}:no en guion 2")
                    
        # Comprobar o:ok final en niveles 1, 2, 3
        for n in ['1', '2', '3']:
            last_act = h["guion"][n][-1].get("a", "")
            if last_act != f"o:{corr_letter}:ok":
                issues.append(f"{qid}: guion {n} último paso no es o:{corr_letter}:ok (es {last_act})")
                
        # Comprobar cifras en textos hablados
        for n in ['1', '2', '3']:
            for b in h["guion"][n]:
                text = b.get("t", "")
                clean_text = re.sub(r'\{\{[^\}]+\}\}', '', text)
                clean_text = re.sub(r'\b[A-D]\b', '', clean_text)  # option letters are OK
                if re.search(r'\d', clean_text):
                    issues.append(f"{qid}: guion {n} tiene dígitos en texto hablado: '{text}'")
                    
        # Longitud de opciones
        lens = [len(o) for o in q["opciones"]]
        if lens[corr] == max(lens):
            longest_count += 1
            
    print(f"Longest correct option: {longest_count}/62 ({longest_count/62*100:.1f}%)")
    
    if issues:
        print(f"[ERROR] Se encontraron {len(issues)} problemas:")
        for iss in issues[:10]:
            print(f"  - {iss}")
        sys.exit(1)
        
    # Guardar en content/questions/odontologia.json
    with open("content/questions/odontologia.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print(f"[ÉXITO] Escritas 62 preguntas barajadas y limpiadas exitosamente en content/questions/odontologia.json.")

if __name__ == "__main__":
    run()
