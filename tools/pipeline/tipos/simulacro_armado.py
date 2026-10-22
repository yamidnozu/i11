from documento import detectar as _detectar, estructurar_documento
from cuadernillo import extraer, estructurar as _estructurar

def detectar(ctx): return _detectar(ctx,'simulacro_armado')
def estructurar(ctx):
    d=detectar(ctx)
    if d['pregunta_markers'] and d['has_answer_key']:
        return _estructurar(ctx)
    return estructurar_documento(ctx,'simulacro_armado',True)
