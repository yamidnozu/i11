"""Script de auditoría de calidad pedagógica para preguntas ICFES y Banco Propio.
Mide el estado de cada cuadernillo y banco propio según ENCARGO_COMPLETAR.md (endurecido según Punto 8):
- Explicaciones reales (no vacías, no genéricas, no afirmaciones recicladas, sin contradicción con la clave)
- Distractores específicos (no 'Pendiente', no repetidos, no templated con esqueleto idéntico, no repetición de la explicación)
- Ausencia de muletillas ('Parece razonable si se omite...', 'La opción X plantea...', 'No corresponde al fenómeno...')
- Detección de LaTeX roto y caracteres de control (\f, \b, \r, \t mal escapados, rac sin \)
- Limpieza de palabras partidas por OCR / corte de línea ('ne- gocio', 'cen- tros', etc.)
- Flujo pedagógico completo (hoja con enfoque: que/pistas/no, pasos, audio con 3 niveles del profe)
- Detección de sesgos en banco propio (distribución de claves A/B/C/D y sesgo de opción más larga)
"""
import glob
import json
import os
import re
import sys
import difflib
import collections

GENERIC_DISTRACTOR_PATTERNS = [
    r"No coincide con la resolución",
    r"No corresponde a la solución",
    r"No coincide con el resultado",
    r"No corresponde al fenómeno físico o químico evaluado",
    r"plantea «.*».? Pero no responde al criterio central",
    r"^La opción [A-D] plantea",
    r"^Parece razonable si se omite una pista",
    r"^Puede sonar razonable si se ignora una pista",
    r"^Parece tentador a primera vista\. Pero",
    r"^Puede parecer posible\. Pero",
    r"^Pendiente"
]

GENERIC_TRAP_PATTERNS = [
    r"Parece posible al mirar un dato aislado",
    r"^Pendiente"
]

HYPHENATED_WORDS_RE = re.compile(r'\b[a-záéíóúñ]{2,}-\s+[a-záéíóúñ]{2,}\b', re.IGNORECASE)

CONTROL_CHARS = [
    ('\x0c', '\\f (form feed en \\frac)'),
    ('\x08', '\\b (backspace en \\binom)'),
    ('\x07', '\\a (bell en \\alpha)'),
    ('\r', '\\r (carriage return en \\rho)')
]

def check_latex_and_escapes(text, qid, field_name):
    issues = []
    if not isinstance(text, str):
        return issues
        
    for bad_c, c_desc in CONTROL_CHARS:
        if bad_c in text:
            issues.append(f"LaTeX/escape roto en {field_name}: contiene {c_desc}")
            
    # Tab in math mode where \text, \theta, \times was intended
    if '\t' in text and re.search(r'\t(ext|heta|imes)\b', text):
        issues.append(f"LaTeX/escape roto en {field_name}: contiene '\\t' sin escapar (tabulación en \\text/\\theta/\\times)")

    # Broken \frac as rac
    if re.search(r'[$][^$]*\brac\b', text) or re.search(r'[$][^$]*rac\d', text):
        issues.append(f"LaTeX roto en {field_name}: \\frac sin barra invertida ('rac')")
        
    return issues

def audit_question(q, is_banco_propio=False):
    issues = []
    qid = q.get('id', '?')
    is_reto = (q.get('tipo') == 'reto')
    
    # 1. Clave correcta
    correcta = q.get('correcta')
    opciones = q.get('opciones', [])
    if is_reto:
        if not (q.get('sim') and q['sim'].get('challengeId')):
            issues.append("Reto sin challengeId")
    elif correcta is None or not (0 <= correcta < len(opciones)):
        issues.append("Clave correcta inválida o ausente")
        
    # 2. Explicación general
    expl = (q.get('explicacion') or '').strip()
    if not expl:
        issues.append("Explicación vacía")
    elif "pendiente de solución verificada" in expl.lower() or expl.lower().startswith("pendiente"):
        issues.append("Explicación pendiente")
    elif expl.startswith("Explica comprender que a partir de la investigación científica"):
        issues.append("Explicación reemplazada por frase de catálogo genérica ('Explica comprender...')")
    elif len(expl) < 35:
        issues.append(f"Explicación muy corta ({len(expl)} chars)")

    # 2b. Contradicción entre explicación y clave
    if not is_reto and correcta is not None and 0 <= correcta < len(opciones):
        c_letter = chr(65 + correcta)
        # Buscar menciones explícitas de la respuesta en la explicación
        m = re.search(r'\bla (?:opción|respuesta|alternativa) (?:es la |correcta es la |correcta es |es )([A-D])\b', expl, re.I)
        if not m:
            m = re.search(r'\bla respuesta es ([A-D])\b', expl, re.I)
        if m:
            named_letter = m.group(1).upper()
            if named_letter != c_letter:
                issues.append(f"Contradicción: explicación afirma que la respuesta es {named_letter}, pero la clave es {c_letter}")

    # 3. Distractores
    if not is_reto:
        distractores = q.get('distractores', [])
        if len(distractores) != len(opciones):
            issues.append(f"Número de distractores ({len(distractores)}) != opciones ({len(opciones)})")
        else:
            d_texts = []
            tails = []
            for i, d in enumerate(distractores):
                if i == correcta:
                    if d != "":
                        issues.append(f"Distractor de la clave correcta (opción {chr(65+i)}) debe ser cadena vacía")
                    continue
                d_str = (d or '').strip()
                if not d_str:
                    issues.append(f"Distractor opción {chr(65+i)} vacío")
                    continue
                if re.search(r'^(pendiente|tbd|por definir)\b|\bpendiente\s+de\s+(soluci[oó]n|an[aá]lisis|redacci[oó]n|revisi[oó]n|verific)\b|\bdistractor\s+pendiente\b', d_str, re.IGNORECASE) or d_str.strip().lower() == "pendiente":
                    issues.append(f"Distractor opción {chr(65+i)} pendiente")
                if len(d_str) < 30:
                    issues.append(f"Distractor opción {chr(65+i)} muy corto ({len(d_str)} chars)")
                for pat in GENERIC_DISTRACTOR_PATTERNS:
                    if re.search(pat, d_str, re.IGNORECASE):
                        issues.append(f"Distractor opción {chr(65+i)} genérico/templated: '{d_str[:40]}...'")
                        break
                # Repetición de la explicación en el distractor
                if len(expl) > 30 and len(d_str) > 30:
                    ratio = difflib.SequenceMatcher(None, d_str.lower(), expl.lower()).ratio()
                    if ratio > 0.75:
                        issues.append(f"Distractor opción {chr(65+i)} repite la explicación (similitud {ratio:.2f})")
                        
                d_texts.append(d_str)
                # Normalizar para detectar esqueleto idéntico
                tail = re.sub(r'«.*?»|\".*?\"', '', d_str)
                tail = re.sub(r'^(Parece razonable si se omite una pista del modelo\. Pero |Puede sonar razonable si se ignora una pista\. Pero |Parece tentador a primera vista\. Pero |Puede parecer posible\. Pero )', '', tail)
                tail = re.sub(r'\b[A-D]\b|\d+([.,]\d+)?', '#', tail).strip()
                tails.append(tail)
                
            # Detectar frases repetidas idénticas entre distractores de la misma pregunta
            if len(d_texts) > 1 and len(set(d_texts)) == 1:
                issues.append(f"Distractores idénticos repetidos en todas las opciones incorrectas")
            elif len(tails) > 1 and len(set(tails)) == 1:
                issues.append(f"Estructura templated idéntica en todos los distractores de la pregunta")

    # 4. LaTeX y caracteres de escape rotos
    for fld in ['enunciado', 'explicacion']:
        issues.extend(check_latex_and_escapes(q.get(fld, ''), qid, fld))
    for i, o in enumerate(opciones):
        issues.extend(check_latex_and_escapes(o, qid, f"opción {chr(65+i)}"))
    for i, dis in enumerate(q.get('distractores', [])):
        issues.extend(check_latex_and_escapes(dis, qid, f"distractor {chr(65+i)}"))

    # 5. Palabras partidas por OCR / corte de línea
    for fld_name, fld_val in [('enunciado', q.get('enunciado', '')), ('explicacion', q.get('explicacion', ''))]:
        if isinstance(fld_val, str):
            for m in HYPHENATED_WORDS_RE.finditer(fld_val):
                word = m.group(0)
                if not any(v in word.lower() for v in ['socio-', 'físico-', 'químico-', 'teórico-', 'político-']):
                    issues.append(f"Palabra partida por OCR/guión en {fld_name}: '{word}'")
    for i, o in enumerate(opciones):
        for m in HYPHENATED_WORDS_RE.finditer(o):
            word = m.group(0)
            if not any(v in word.lower() for v in ['socio-', 'físico-', 'químico-', 'teórico-', 'político-']):
                issues.append(f"Palabra partida por OCR/guión en opción {chr(65+i)}: '{word}'")

    # 6. Flujo completo: Hoja, Enfoque (que, pistas, no), Pasos y Audio (3 niveles del profe)
    hoja = q.get('hoja')
    if is_banco_propio or hoja is not None:
        if not hoja or not isinstance(hoja, dict):
            issues.append("Falta hoja pedagógica interactiva")
        else:
            # Enfoque
            enf = hoja.get('enfoque') or {}
            if not enf.get('que') or len(enf.get('que', '').strip()) < 15:
                issues.append("Hoja sin enfoque.que válido")
            pistas = enf.get('pistas') or []
            if not pistas or len(pistas) == 0:
                issues.append("Hoja sin enfoque.pistas")
            no_list = enf.get('no', [])
            if not no_list or len(no_list) == 0:
                issues.append("Hoja sin enfoque.no (trampas)")
            else:
                for item in no_list:
                    p = item.get('p', '')
                    for pat in GENERIC_TRAP_PATTERNS:
                        if re.search(pat, p, re.IGNORECASE):
                            issues.append(f"Trampa en enfoque.no genérica: '{p[:40]}...'")
                            break
            # Pasos
            pasos = hoja.get('pasos') or []
            if not pasos or len(pasos) < 1:
                issues.append("Hoja sin pasos guiados")
            # Audio (3 niveles del profe)
            audio = hoja.get('audio') or hoja.get('guion')
            if not audio:
                issues.append("Hoja sin niveles del profe (audio / guion)")

    # 7. Competencia y afirmación
    if not q.get('competencia'):
        issues.append("Falta competencia")
    if not q.get('afirmacion'):
        issues.append("Falta afirmación")

    # 8. Texto basura en opciones
    for i, o in enumerate(opciones):
        if re.search(r"CONTINÚE ABAJO|Página \d+|SABER 11|Cuadernillo de preguntas", o, re.IGNORECASE):
            issues.append(f"Texto basura de PDF en opción {chr(65+i)}")

    # 9. Clave dudosa
    if q.get('revisar') and len(q.get('revisar')) > 0:
        issues.append(f"Marcada por revisar: {q.get('revisar')}")

    is_complete = (len(issues) == 0)
    return is_complete, issues

def audit_icfes():
    cuadernillos = sorted(glob.glob('content/icfes/**/preguntas.json', recursive=True))
    stats = {}
    total_q = 0
    total_complete = 0

    print("=" * 80)
    print("AUDITORÍA DE PREGUNTAS ICFES (content/icfes)")
    print("=" * 80)

    for cpath in cuadernillos:
        cname = os.path.basename(os.path.dirname(cpath))
        data = json.load(open(cpath, 'r', encoding='utf-8'))
        preguntas = data.get('preguntas', []) if isinstance(data, dict) else data
        
        c_total = len(preguntas)
        c_complete = 0
        c_issues = []

        for q in preguntas:
            complete, issues = audit_question(q, is_banco_propio=False)
            if complete:
                c_complete += 1
            else:
                c_issues.append((q.get('id', '?'), issues))

        total_q += c_total
        total_complete += c_complete
        stats[cname] = {
            'total': c_total,
            'complete': c_complete,
            'incomplete': c_total - c_complete,
            'pct': round((c_complete / c_total * 100), 1) if c_total > 0 else 0,
            'issues': c_issues
        }

        print(f"[{cname:5s}] {c_complete:3d} / {c_total:3d} completas ({stats[cname]['pct']:5.1f}%) | Faltan: {c_total - c_complete:3d}")

    print("-" * 80)
    pct_total = round((total_complete / total_q * 100), 1) if total_q > 0 else 0
    print(f"TOTAL ICFES: {total_complete} / {total_q} completas ({pct_total}%) | Incompletas: {total_q - total_complete}")
    print("=" * 80)
    return stats

def audit_banco_propio():
    print("\n" + "=" * 80)
    print("AUDITORÍA BANCO PROPIO (content/questions/*.json + packs)")
    print("=" * 80)
    
    areas = sorted(glob.glob('content/questions/*.json'))
    stats = {}
    total_q = 0
    total_complete = 0

    for apath in areas:
        aname = os.path.basename(apath).replace('.json', '')
        preguntas = json.load(open(apath, 'r', encoding='utf-8'))
        
        a_total = len(preguntas)
        a_complete = 0
        a_issues = []

        # Análisis de sesgos por área
        key_dist = collections.Counter()
        longest_key_count = 0

        for q in preguntas:
            complete, issues = audit_question(q, is_banco_propio=True)
            c = q.get('correcta')
            ops = q.get('opciones', [])
            if c is not None and 0 <= c < len(ops):
                key_dist[chr(65 + c)] += 1
                lens = [len(o) for o in ops]
                max_len = max(lens)
                if lens[c] == max_len and lens.count(max_len) == 1:
                    longest_key_count += 1
                    
            if complete:
                a_complete += 1
            else:
                a_issues.append((q.get('id', '?'), issues))

        # Chequeo de sesgo en lote
        bias_issues = []
        if a_total >= 30:
            for letter in ['A', 'B', 'C', 'D']:
                cnt = key_dist.get(letter, 0)
                pct = cnt / a_total
                if pct < 0.125 or pct > 0.45:
                    bias_issues.append(f"Sesgo de clave en {letter}: {cnt}/{a_total} ({pct*100:.1f}%) fuera de rango 12.5%-45%")
            longest_pct = longest_key_count / a_total
            if longest_pct > 0.50:
                bias_issues.append(f"Sesgo de longitud: la opción correcta es la más larga en {longest_key_count}/{a_total} ({longest_pct*100:.1f}% > 50%)")

        total_q += a_total
        total_complete += a_complete
        stats[aname] = {
            'total': a_total,
            'complete': a_complete,
            'incomplete': a_total - a_complete,
            'issues': a_issues,
            'bias_issues': bias_issues,
            'key_dist': dict(key_dist),
            'longest_pct': round((longest_key_count / a_total * 100), 1) if a_total > 0 else 0
        }
        bias_str = f" | Sesgos: {len(bias_issues)}" if bias_issues else ""
        print(f"[{aname:18s}] {a_complete:2d} / {a_total:2d} completas | Meta: 40 (Faltan {max(0, 40 - a_total)} para meta){bias_str}")
        if bias_issues:
            for b in bias_issues:
                print(f"   ⚠️  {b}")

    # Packs formato-icfes
    packs_file = 'content/packs/formato-icfes.json'
    if os.path.exists(packs_file):
        pdata = json.load(open(packs_file, 'r', encoding='utf-8'))
        ppreg = pdata.get('preguntas', [])
        p_complete = 0
        p_issues = []
        for q in ppreg:
            comp, iss = audit_question(q, is_banco_propio=True)
            if comp: p_complete += 1
            else: p_issues.append((q.get('id', '?'), iss))
        print(f"[{'packs/formato':18s}] {p_complete:2d} / {len(ppreg):2d} completas")
        total_q += len(ppreg)
        total_complete += p_complete
        stats['packs/formato'] = {'total': len(ppreg), 'complete': p_complete, 'incomplete': len(ppreg) - p_complete, 'issues': p_issues}

    print("-" * 80)
    print(f"TOTAL BANCO PROPIO: {total_complete} / {total_q} completas")
    print("=" * 80)
    return stats

if __name__ == '__main__':
    icfes_stats = audit_icfes()
    banco_stats = audit_banco_propio()
    
    incomplete_icfes = sum(s['incomplete'] for s in icfes_stats.values())
    incomplete_banco = sum(s['incomplete'] for s in banco_stats.values())
    total_bias = sum(len(s.get('bias_issues', [])) for s in banco_stats.values())

    print(f"\nRESUMEN DE AUDITORÍA:")
    print(f"- Preguntas ICFES incompletas: {incomplete_icfes}")
    print(f"- Preguntas Banco Propio incompletas: {incomplete_banco}")
    print(f"- Problemas de sesgo en Banco Propio: {total_bias}")

    # Imprimir muestra de problemas si hay
    if incomplete_icfes > 0:
        print("\nPrimeras incidencias en ICFES:")
        for cname, s in icfes_stats.items():
            for qid, issues in s['issues'][:3]:
                print(f"  [{cname}] {qid}: {', '.join(issues)}")
    if incomplete_banco > 0:
        print("\nPrimeras incidencias en Banco Propio:")
        for aname, s in banco_stats.items():
            for qid, issues in s['issues'][:3]:
                print(f"  [{aname}] {qid}: {', '.join(issues)}")

    if '--strict' in sys.argv:
        if incomplete_icfes > 0 or incomplete_banco > 0 or total_bias > 0:
            print(f"\n[STRICT CHECK FAILED] Auditoría estricta encontró problemas.")
            sys.exit(1)
        print("\n[STRICT CHECK PASSED] Todas las preguntas y lotes cumplen los estándares de calidad.")
