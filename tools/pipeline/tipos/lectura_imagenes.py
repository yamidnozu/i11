from documento import detectar as _detectar, estructurar_documento
from cuadernillo import extraer

def detectar(ctx): return _detectar(ctx,'lectura_imagenes')
def estructurar(ctx): return estructurar_documento(ctx,'lectura_imagenes',True)
