# --- USO DE MÓDULOS Y PAQUETES ---

# 1. Importar un módulo completo
import mi_modulo

# Usar funciones del módulo
print("--- Importación simple ---")
print(mi_modulo.saludar("Ana"))
print(f"Suma: {mi_modulo.sumar(5, 3)}")
print(f"Versión del módulo: {mi_modulo.version}")

# 2. Importar funciones específicas
from mi_modulo import restar, multiplicar, Calculadora

print("\n--- Importación específica ---")
print(f"Resta: {restar(10, 4)}")
print(f"Multiplicación: {multiplicar(3, 7)}")

# Usar la clase
calc = Calculadora()
resultado = calc.operar(10, 5, '/')
print(f"División: {resultado}")
print(f"Historial: {calc.mostrar_historial()}")

# 3. Importar con alias
import mi_modulo as mm

print("\n--- Importación con alias ---")
print(mm.saludar("Carlos"))

# 4. Importar todo (NO recomendado en general)
from mi_modulo import *

print("\n--- Importación completa ---")
print(f"Versión: {version}")
print(f"Autor: {autor}")

# 5. Usar módulos de la biblioteca estándar
import math
import random
import datetime

print("\n--- Módulos estándar ---")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Número aleatorio (1-10): {random.randint(1, 10)}")
print(f"Fecha actual: {datetime.date.today()}")

# 6. Importar desde paquete (requiere crear la estructura)
# from paquete import modulo1, modulo2
# from paquete.modulo1 import funcion_especifica

# 7. Ver el contenido de un módulo
print("\n--- Contenido del módulo mi_modulo ---")
print(dir(mi_modulo))
