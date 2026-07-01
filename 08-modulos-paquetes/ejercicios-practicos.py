# --- EJERCICIOS PRÁCTICOS (Módulos y Paquetes) ---

# Ejercicio 1: Crear un módulo de utilidades
print("=== EJERCICIO 1: Módulo de utilidades ===")
"""
Crea un módulo llamado 'utilidades.py' que contenga:
- Funciones para trabajar con strings (invertir, contar vocales, es_palindromo)
- Funciones para trabajar con listas (promedio, mediana, moda)
- Una clase para manejar fechas
"""

# Ejercicio 2: Usar el módulo desde otro archivo
print("\n=== EJERCICIO 2: Usar el módulo ===")
"""
Crea un script que importe el módulo 'utilidades' y use sus funciones.
"""

# Ejercicio 3: Crear un paquete de matemáticas
print("\n=== EJERCICIO 3: Paquete de matemáticas ===")
"""
Crea un paquete 'matematica' con los módulos:
- basica.py: operaciones básicas (suma, resta, multiplicación, división)
- avanzada.py: funciones trigonométricas, logaritmos, factorial
- geometria.py: área y perímetro de figuras
"""

# Ejercicio 4: Organizar código con __all__
print("\n=== EJERCICIO 4: Organizar el paquete ===")
"""
En el paquete 'matematica', usa __all__ en __init__.py para controlar qué se exporta.
"""

# =============================================
# SOLUCIÓN EJERCICIO 1 (utilidades.py)
# =============================================

"""
# --- utilidades.py ---
import math
from collections import Counter

# Funciones para strings
def invertir_string(texto):
    return texto[::-1]

def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for c in texto if c in vocales)

def es_palindromo(texto):
    texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpio == texto_limpio[::-1]

# Funciones para listas
def promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def mediana(lista):
    if not lista:
        return None
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2

def moda(lista):
    if not lista:
        return None
    contador = Counter(lista)
    return contador.most_common(1)[0][0]

# Clase para manejar fechas
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"
    
    def es_bisiesto(self):
        if self.año % 400 == 0:
            return True
        if self.año % 100 == 0:
            return False
        return self.año % 4 == 0
    
    def dias_en_mes(self):
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.mes == 2 and self.es_bisiesto():
            return 29
        return dias_por_mes[self.mes - 1]

# Ejemplo de uso directo
if __name__ == "__main__":
    print("Módulo de utilidades cargado")
    print(es_palindromo("anita lava la tina"))
    print(contar_vocales("Hola mundo"))
    print(promedio([1, 2, 3, 4, 5]))
    fecha = Fecha(15, 2, 2024)
    print(f"¿2024 es bisiesto? {fecha.es_bisiesto()}")
"""

# Solución Ejercicio 2 (usar el módulo)
"""
# --- usar_utilidades.py ---
import utilidades

print(utilidades.invertir_string("Python"))
print(utilidades.contar_vocales("Programación"))
print(utilidades.mediana([1, 3, 5, 7, 9]))

fecha = utilidades.Fecha(29, 2, 2024)
print(f"{fecha} tiene {fecha.dias_en_mes()} días")
"""
