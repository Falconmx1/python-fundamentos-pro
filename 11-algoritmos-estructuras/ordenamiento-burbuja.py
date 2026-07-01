# --- ORDENAMIENTO BURBUJA (Bubble Sort) ---
# Algoritmo simple pero ineficiente para listas grandes (O(n²)).

def burbuja(lista):
    """
    Ordena una lista usando el algoritmo de burbuja.
    """
    n = len(lista)
    # Hacer una copia para no modificar la original
    arr = lista.copy()
    
    for i in range(n):
        # Bandera para optimización
        intercambiado = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambiado:
            break
    
    return arr

def burbuja_mejorada(lista):
    """
    Versión mejorada: recorre en ambas direcciones (Cocktail Sort).
    """
    arr = lista.copy()
    n = len(arr)
    inicio = 0
    fin = n - 1
    intercambiado = True
    
    while intercambiado:
        intercambiado = False
        
        # Recorrer hacia adelante
        for i in range(inicio, fin):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                intercambiado = True
        
        if not intercambiado:
            break
        
        # Recorrer hacia atrás
        intercambiado = False
        fin -= 1
        
        for i in range(fin, inicio, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                intercambiado = True
        
        inicio += 1
    
    return arr

# Ejemplos de uso
print("--- Ordenamiento Burbuja ---")
numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {numeros}")

ordenado = burbuja(numeros)
print(f"Lista ordenada: {ordenado}")

# Comparación de versiones
import time

print("\n--- Comparación de versiones ---")
numeros_desordenados = [64, 34, 25, 12, 22, 11, 90, 33, 44, 55, 77, 88, 99, 100, 1, 2, 3]

inicio = time.time()
burbuja(numeros_desordenados)
tiempo_burbuja = time.time() - inicio

inicio = time.time()
burbuja_mejorada(numeros_desordenados)
tiempo_mejorado = time.time() - inicio

print(f"Tiempo burbuja: {tiempo_burbuja:.6f} segundos")
print(f"Tiempo mejorado: {tiempo_mejorado:.6f} segundos")
