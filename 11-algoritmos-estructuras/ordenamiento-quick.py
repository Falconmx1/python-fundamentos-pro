# --- QUICK SORT ---
# Algoritmo eficiente de ordenamiento (O(n log n) en promedio).

def quick_sort(lista):
    """
    Ordena una lista usando el algoritmo Quick Sort (recursivo).
    """
    # Caso base
    if len(lista) <= 1:
        return lista
    
    # Elegir pivote (elemento medio)
    pivote = lista[len(lista) // 2]
    
    # Dividir en tres listas
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    
    # Recursión y concatenación
    return quick_sort(izquierda) + medio + quick_sort(derecha)

def quick_sort_inplace(lista, bajo=0, alto=None):
    """
    Versión in-place (sin crear nuevas listas) de Quick Sort.
    """
    if alto is None:
        alto = len(lista) - 1
    
    if bajo < alto:
        # Obtener índice de partición
        indice_pivote = particion(lista, bajo, alto)
        
        # Ordenar recursivamente las dos mitades
        quick_sort_inplace(lista, bajo, indice_pivote - 1)
        quick_sort_inplace(lista, indice_pivote + 1, alto)
    
    return lista

def particion(lista, bajo, alto):
    """
    Función de partición para Quick Sort in-place.
    """
    # Elegir el último elemento como pivote
    pivote = lista[alto]
    i = bajo - 1
    
    for j in range(bajo, alto):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    # Colocar el pivote en su posición correcta
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1

# Ejemplos de uso
print("--- Quick Sort ---")
numeros = [64, 34, 25, 12, 22, 11, 90, 33, 44, 55, 77, 88]
print(f"Lista original: {numeros}")

# Versión funcional
ordenado = quick_sort(numeros)
print(f"Lista ordenada (funcional): {ordenado}")

# Versión in-place
numeros_copia = numeros.copy()
ordenado_inplace = quick_sort_inplace(numeros_copia)
print(f"Lista ordenada (in-place): {ordenado_inplace}")

# Comparación de rendimiento con otros algoritmos
import time

print("\n--- Comparación de rendimiento ---")
import random

# Crear lista grande
lista_grande = [random.randint(0, 1000) for _ in range(1000)]

# Quick Sort
inicio = time.time()
quick_sort(lista_grande)
tiempo_quick = time.time() - inicio

# Bubble Sort
inicio = time.time()
burbuja(lista_grande)
tiempo_burbuja = time.time() - inicio

print(f"Tiempo Quick Sort: {tiempo_quick:.6f} segundos")
print(f"Tiempo Bubble Sort: {tiempo_burbuja:.6f} segundos")
print(f"Quick Sort fue {tiempo_burbuja/tiempo_quick:.2f}x más rápido")
