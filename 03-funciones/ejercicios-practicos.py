# --- EJERCICIOS PRÁCTICOS (Funciones) ---
# Resuelve los ejercicios creando funciones para cada uno.

# Ejercicio 1: Calculadora básica
print("=== EJERCICIO 1: Calculadora ===")
def calculadora(num1, num2, operacion):
    """
    Realiza una operación básica entre dos números.
    operación: 'suma', 'resta', 'multiplicacion', 'division'
    """
    # Tu código aquí
    pass

# Prueba
# print(calculadora(10, 5, 'suma'))          # 15
# print(calculadora(10, 5, 'division'))      # 2.0

# Ejercicio 2: Números primos
print("\n=== EJERCICIO 2: Números primos ===")
def es_primo(numero):
    """Devuelve True si el número es primo, False en caso contrario."""
    # Tu código aquí
    pass

def numeros_primos_hasta(limite):
    """Devuelve una lista con todos los números primos hasta el límite."""
    # Tu código aquí
    pass

# Prueba
# print(es_primo(17))        # True
# print(es_primo(20))        # False
# print(numeros_primos_hasta(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Ejercicio 3: Contador de palabras
print("\n=== EJERCICIO 3: Contador de palabras ===")
def contar_palabras(texto):
    """
    Recibe un texto y devuelve un diccionario con la frecuencia de cada palabra.
    Ignora mayúsculas/minúsculas y signos de puntuación básicos.
    """
    # Tu código aquí
    pass

# Prueba
# texto = "Hola mundo, hola Python. Python es genial!"
# print(contar_palabras(texto))
# # {'hola': 2, 'mundo': 1, 'python': 2, 'es': 1, 'genial': 1}

# Ejercicio 4: Decorador simple
print("\n=== EJERCICIO 4: Decorador simple ===")
# Crea un decorador que mida el tiempo de ejecución de una función.
# Pista: usa el módulo time (import time)
def medir_tiempo(funcion):
    # Tu código aquí
    pass

# Prueba
# @medir_tiempo
# def dormir_un_poco():
#     import time
#     time.sleep(1)
#     print("Desperté")
# dormir_un_poco()  # Debe imprimir: "Desperté" y el tiempo de ejecución

# Ejercicio 5: Función recursiva (avanzado)
print("\n=== EJERCICIO 5: Recursión avanzada ===")
def generar_combinaciones(conjunto, longitud):
    """
    Genera todas las combinaciones de una longitud dada a partir de un conjunto.
    Usa recursión.
    """
    # Tu código aquí
    pass

# Prueba
# print(generar_combinaciones([1, 2, 3], 2))
# # [[1, 2], [1, 3], [2, 3]]
# print(generar_combinaciones(["A", "B", "C", "D"], 3))
# # [['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D']]
