# --- INICIALIZADOR DEL PAQUETE ---
# Este archivo convierte a la carpeta en un paquete Python.

# Puede estar vacío, o contener código de inicialización del paquete.

print("Inicializando el paquete 'paquete'...")

# Definir qué se exporta con "from paquete import *"
__all__ = ['modulo1', 'modulo2']

# También se puede definir la versión del paquete
__version__ = "1.0.0"

# Importar módulos para que estén disponibles al importar el paquete
from . import modulo1
from . import modulo2

# O importar funciones específicas para que sean accesibles directamente
# from .modulo1 import funcion_util
