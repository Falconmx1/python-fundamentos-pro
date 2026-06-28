# --- COMPRENSIÓN DE COLECCIONES ---
# Forma concisa de crear listas, conjuntos y diccionarios.

# 1. List comprehension (básico)
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

# 2. List comprehension con condición (if)
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Pares: {pares}")

# 3. List comprehension con if-else
clasificacion = ["Par" if x % 2 == 0 else "Impar" for x in range(1, 6)]
print(f"Clasificación: {clasificacion}")

# 4. List comprehension anidada
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
planos = [elemento for fila in matriz for elemento in fila]
print(f"Matriz aplanada: {planos}")

# 5. Set comprehension (conjuntos)
set_cuadrados = {x**2 for x in range(-3, 4)}
print(f"Set de cuadrados: {set_cuadrados}")

# 6. Dict comprehension (diccionarios)
cuadrados_dic = {x: x**2 for x in range(1, 6)}
print(f"Diccionario de cuadrados: {cuadrados_dic}")

# 7. Dict comprehension con condición
estudiantes = ["Ana", "Luis", "Carlos", "María"]
edades = [25, 22, 28, 24]
# Crear diccionario nombre:edad para edades >= 24
estudiantes_dict = {nombre: edad for nombre, edad in zip(estudiantes, edades) if edad >= 24}
print(f"Estudiantes mayores o iguales a 24: {estudiantes_dict}")

# 8. Comprensión con enumerate (índice y valor)
indices = {indice: valor for indice, valor in enumerate(estudiantes)}
print(f"Índices de estudiantes: {indices}")
