# --- BÚSQUEDA BINARIA ---
# Algoritmo eficiente para buscar en listas ordenadas (O(log n)).

def busqueda_binaria(lista, objetivo):
    """
    Busca un elemento en una lista ordenada usando búsqueda binaria.
    Retorna el índice si lo encuentra, -1 si no existe.
    """
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]
        
        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1

def busqueda_binaria_recursiva(lista, objetivo, izquierda=None, derecha=None):
    """
    Implementación recursiva de búsqueda binaria.
    """
    if izquierda is None:
        izquierda = 0
    if derecha is None:
        derecha = len(lista) - 1
    
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    valor_medio = lista[medio]
    
    if valor_medio == objetivo:
        return medio
    elif valor_medio < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)

# Ejemplos de uso
print("--- Búsqueda Binaria ---")
numeros = [10, 23, 45, 70, 88, 92, 100, 120, 150]
print(f"Lista ordenada: {numeros}")

indice = busqueda_binaria(numeros, 70)
print(f"Elemento 70 encontrado en índice: {indice}")

indice = busqueda_binaria(numeros, 99)
print(f"Elemento 99 encontrado en índice: {indice}")

# Búsqueda binaria recursiva
print("\n--- Búsqueda Binaria Recursiva ---")
indice = busqueda_binaria_recursiva(numeros, 70)
print(f"Elemento 70 encontrado en índice: {indice}")

# Comparación de rendimiento vs lineal
import time

print("\n--- Comparación de rendimiento ---")
lista_grande = list(range(1, 1000000, 2))  # Solo números impares
objetivo = 999999

# Búsqueda lineal
inicio = time.time()
indice_lineal = busqueda_lineal(lista_grande, objetivo)
tiempo_lineal = time.time() - inicio

# Búsqueda binaria
inicio = time.time()
indice_binario = busqueda_binaria(lista_grande, objetivo)
tiempo_binario = time.time() - inicio

print(f"Tiempo lineal: {tiempo_lineal:.6f} segundos")
print(f"Tiempo binario: {tiempo_binario:.6f} segundos")
print(f"La búsqueda binaria fue {tiempo_lineal/tiempo_binario:.2f}x más rápida")
