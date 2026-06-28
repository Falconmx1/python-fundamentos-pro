# --- FUNCIONES EN PYTHON ---
# Una función es un bloque de código reutilizable que realiza una tarea específica.

# 1. Definir y llamar una función simple
def saludar():
    """Esta función imprime un saludo básico."""  # Docstring (documentación)
    print("¡Hola, mundo!")

# Llamar a la función
saludar()

# 2. Función con parámetros
def saludar_persona(nombre):
    """Saluda a una persona por su nombre."""
    print(f"¡Hola, {nombre}!")

saludar_persona("Ana")
saludar_persona("Luis")

# 3. Función con valor de retorno
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    resultado = a + b
    return resultado

# Guardar el valor devuelto
total = sumar(5, 3)
print(f"La suma es: {total}")

# 4. Función con múltiples valores de retorno
def estadisticas(lista):
    """Devuelve el mínimo, máximo y promedio de una lista de números."""
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio

numeros = [10, 20, 30, 40, 50]
minimo, maximo, promedio = estadisticas(numeros)
print(f"Mínimo: {minimo}, Máximo: {maximo}, Promedio: {promedio}")
