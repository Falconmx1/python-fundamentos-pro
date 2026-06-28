# --- CONJUNTOS (SET) ---
# Son colecciones NO ordenadas de elementos ÚNICOS.

# 1. Creación de conjuntos
conjunto_vacio = set()  # {} es diccionario, no conjunto
numeros = {1, 2, 3, 4, 5}
letras = set("hola")   # {'h', 'o', 'l', 'a'}
print(f"Conjunto letras: {letras}")
print(f"Longitud de numeros: {len(numeros)}")

# 2. Agregar y eliminar elementos
numeros.add(6)           # Agregar un elemento
numeros.add(3)           # No hace nada (ya existe)
numeros.update([7, 8, 9])  # Agregar múltiples
numeros.remove(5)        # Eliminar (error si no existe)
numeros.discard(99)      # Eliminar (no error si no existe)
print(f"Conjunto actualizado: {numeros}")

# 3. Operaciones de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(f"A: {A}, B: {B}")
print(f"Unión: {A | B}")          # {1,2,3,4,5,6}
print(f"Intersección: {A & B}")    # {3,4}
print(f"Diferencia (A-B): {A - B}")  # {1,2}
print(f"Diferencia simétrica: {A ^ B}")  # {1,2,5,6}

# 4. Verificar subconjuntos
C = {1, 2}
print(f"¿C es subconjunto de A? {C.issubset(A)}")    # True
print(f"¿A es superconjunto de C? {A.issuperset(C)}")  # True

# 5. Recorrer un conjunto
print("Recorrido del conjunto A:")
for elemento in A:
    print(elemento, end=" ")
print()

# 6. Uso práctico: eliminar duplicados de una lista
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista original: {lista_con_duplicados}")
print(f"Sin duplicados: {sin_duplicados}")
