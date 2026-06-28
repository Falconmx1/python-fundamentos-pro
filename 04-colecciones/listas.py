# --- LISTAS ---
# Son colecciones ordenadas y mutables (pueden cambiar).

# 1. Creación de listas
lista_vacia = []
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", 3.14, True]
print(f"Lista mixta: {mixta}")

# 2. Acceso a elementos (por índice, empiezan en 0)
print(f"Primer elemento: {numeros[0]}")    # 1
print(f"Último elemento: {numeros[-1]}")    # 5
print(f"Elementos del 1 al 3: {numeros[1:4]}")  # [2, 3, 4]

# 3. Métodos para modificar listas
numeros.append(6)           # Agregar al final
print(f"Después de append: {numeros}")
numeros.insert(2, 99)       # Insertar en la posición 2
print(f"Después de insert: {numeros}")
numeros.remove(99)          # Eliminar el primer 99
print(f"Después de remove: {numeros}")
ultimo = numeros.pop()      # Elimina y devuelve el último
print(f"Elemento pop: {ultimo}, Lista: {numeros}")

# 4. Ordenar y revertir
lista_desordenada = [5, 2, 8, 1, 9]
lista_desordenada.sort()    # Orden ascendente (modifica la lista)
print(f"Ordenada: {lista_desordenada}")
lista_desordenada.reverse()  # Revertir orden
print(f"Revertida: {lista_desordenada}")

# 5. Recorrer una lista
print("Recorrido con for:")
for elemento in numeros:
    print(elemento, end=" ")
print()

# 6. List comprehension (comprensión de listas)
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados del 1 al 5: {cuadrados}")
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares del 1 al 10: {pares}")
