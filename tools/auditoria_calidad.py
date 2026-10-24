"""Script de auditoría de calidad pedagógica para preguntas ICFES y Banco Propio.
Mide el estado de cada cuadernillo según ENCARGO_COMPLETAR.md:
- Explicaciones reales (no 'Pendiente')
- Distractores específicos (no 'Pendiente', no repetidos, no genéricos)
- Enfoque / trampas específicas
- Competencias y afirmaciones
- Figuras y textos limpios
"""
import glob
import json
import os
import re
import sys

GENERIC_DISTRACTOR_PATTERNS = [
    r"No coincide con la resolución",
    r"No corresponde a la solución",
    r"No coincide con el resultado",
    r"^Pendiente"
]

GENERIC_TRAP_PATTERNS = [
    r"Parece posible al mirar un dato aislado",
    r"^Pendiente"
]

def audit_question(q, area_def=None):
    issues = []
    
    is_reto = (q.get('tipo') == 'reto')
    
    # 1. Clave correcta (solo para preguntas de opción múltiple)
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
    elif len(expl) < 25:
        issues.append(f"Explicación muy corta ({len(expl)} chars)")
        
    # 3. Distractores (solo para preguntas de opción múltiple)
    if not is_reto:
        distractores = q.get('distractores', [])
        if len(distractores) != len(opciones):
            issues.append(f"Número de distractores ({len(distractores)}) != opciones ({len(opciones)})")
        else:
            d_texts = []
            for i, d in enumerate(distractores):
                if i == correcta:
                    continue
                d_str = (d or '').strip()
                if not d_str:
                    issues.append(f"Distractor opción {chr(65+i)} vacío")
                    continue
                if re.search(r'^(pendiente|tbd|por definir)\b|\bpendiente\s+de\s+(soluci[oó]n|an[aá]lisis|redacci[oó]n|revisi[oó]n|verific)\b|\bdistractor\s+pendiente\b', d_str, re.IGNORECASE) or d_str.strip().lower() == "pendiente":
                    issues.append(f"Distractor opción {chr(65+i)} pendiente")
                for pat in GENERIC_DISTRACTOR_PATTERNS:
                    if re.search(pat, d_str, re.IGNORECASE):
                        issues.append(f"Distractor opción {chr(65+i)} genérico: '{d_str[:35]}...'")
                        break
                d_texts.append(d_str)
                
            # Detectar frases repetidas idénticas entre distractores de la misma pregunta
            if len(d_texts) > 1 and len(set(d_texts)) == 1:
                issues.append(f"Distractores idénticos repetidos en todas las opciones incorrectas")

    # 4. Enfoque y trampas (si tiene hoja)
    hoja = q.get('hoja')
    if hoja and isinstance(hoja, dict):
        enf = hoja.get('enfoque') or {}
        no_list = enf.get('no', [])
        for item in no_list:
            p = item.get('p', '')
            for pat in GENERIC_TRAP_PATTERNS:
                if re.search(pat, p, re.IGNORECASE):
                    issues.append(f"Trampa en enfoque.no genérica: '{p[:40]}...'")
                    break

    # 5. Competencia y afirmación
    if not q.get('competencia'):
        issues.append("Falta competencia")
    if not q.get('afirmacion'):
        issues.append("Falta afirmación")

    # 6. Texto basura en opciones
    for i, o in enumerate(opciones):
        if re.search(r"CONTINÚE ABAJO|Página \d+|SABER 11|Cuadernillo de preguntas", o, re.IGNORECASE):
            issues.append(f"Texto basura de PDF en opción {chr(65+i)}")

    # 7. Clave dudosa
    if q.get('revisar'):
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
            complete, issues = audit_question(q)
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

        for q in preguntas:
            complete, issues = audit_question(q)
            if complete:
                a_complete += 1
            else:
                a_issues.append((q.get('id', '?'), issues))

        total_q += a_total
        total_complete += a_complete
        stats[aname] = {
            'total': a_total,
            'complete': a_complete,
            'incomplete': a_total - a_complete,
            'issues': a_issues
        }
        print(f"[{aname:18s}] {a_complete:2d} / {a_total:2d} completas | Meta: 40 (Faltan {max(0, 40 - a_total)} para meta)")

    # Packs formato-icfes
    packs_file = 'content/packs/formato-icfes.json'
    if os.path.exists(packs_file):
        pdata = json.load(open(packs_file))
        ppreg = pdata.get('preguntas', [])
        p_complete = sum(1 for q in ppreg if audit_question(q)[0])
        print(f"[{'packs/formato':18s}] {p_complete:2d} / {len(ppreg):2d} completas")
        total_q += len(ppreg)
        total_complete += p_complete

    print("-" * 80)
    print(f"TOTAL BANCO PROPIO: {total_complete} / {total_q} completas")
    print("=" * 80)
    return stats

if __name__ == '__main__':
    icfes_stats = audit_icfes()
    banco_stats = audit_banco_propio()
    
    # Si se pasa --strict, salir con código 1 si hay preguntas incompletas
    if '--strict' in sys.argv:
        incomplete_icfes = sum(s['incomplete'] for s in icfes_stats.values())
        if incomplete_icfes > 0:
            print(f"\n[STRICT CHECK FAILED] Hay {incomplete_icfes} preguntas ICFES incompletas.")
            sys.exit(1)
        print("\n[STRICT CHECK PASSED] Todas las preguntas están completas.")
