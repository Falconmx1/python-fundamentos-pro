# --- DIFÍCIL: Implementación del algoritmo Merge Sort ---
# Ordena una lista de números utilizando el algoritmo de Merge Sort.

def merge_sort(lista):
    """Ordena una lista usando el algoritmo de Merge Sort."""
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return merge(izquierda, derecha)

def merge(izq, der):
    """Fusiona dos listas ordenadas en una sola lista ordenada."""
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    lista_desordenada = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {lista_desordenada}")
    lista_ordenada = merge_sort(lista_desordenada)
    print(f"Lista ordenada: {lista_ordenada}")
