# --- BÚSQUEDA LINEAL ---
# Algoritmo simple para encontrar un elemento en una lista.

def busqueda_lineal(lista, objetivo):
    """
    Busca un elemento en una lista de forma secuencial.
    Retorna el índice si lo encuentra, -1 si no existe.
    """
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1

def busqueda_lineal_ordenada(lista, objetivo):
    """
    Búsqueda lineal en lista ordenada (puede detenerse antes).
    """
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
        if elemento > objetivo:  # Si la lista está ordenada
            break
    return -1

# Ejemplos de uso
print("--- Búsqueda Lineal ---")
numeros = [10, 23, 45, 70, 11, 15, 88, 92]
print(f"Lista: {numeros}")

indice = busqueda_lineal(numeros, 70)
print(f"Elemento 70 encontrado en índice: {indice}")

indice = busqueda_lineal(numeros, 99)
print(f"Elemento 99 encontrado en índice: {indice}")

# Búsqueda en lista ordenada
numeros_ordenados = sorted(numeros)
print(f"\nLista ordenada: {numeros_ordenados}")
indice = busqueda_lineal_ordenada(numeros_ordenados, 70)
print(f"Elemento 70 encontrado en índice: {indice}")

# Comparación de rendimiento
import time

def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio

print("\n--- Comparación de rendimiento ---")
lista_grande = list(range(1000000))
print(f"Lista de {len(lista_grande)} elementos")

# Buscar elemento al inicio
inicio = time.time()
indice = busqueda_lineal(lista_grande, 10)
tiempo = time.time() - inicio
print(f"Buscar al inicio: {tiempo:.6f} segundos")

# Buscar elemento al final
inicio = time.time()
indice = busqueda_lineal(lista_grande, 999999)
tiempo = time.time() - inicio
print(f"Buscar al final: {tiempo:.6f} segundos")
