# --- FUNCIONES LAMBDA (ANÓNIMAS) ---
# Son funciones pequeñas y de una sola línea. No tienen nombre.

# 1. Sintaxis básica: lambda argumentos: expresión
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")

# 2. Lambda con múltiples argumentos
suma = lambda a, b: a + b
print(f"Suma de 3 + 7: {suma(3, 7)}")

# 3. Uso común con sorted() - ordenar una lista de tuplas
estudiantes = [("Ana", 25), ("Luis", 22), ("Carlos", 28)]
# Ordenar por edad (segundo elemento)
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[1])
print("Estudiantes ordenados por edad:", estudiantes_ordenados)

# 4. Uso con map() - aplicar una función a cada elemento
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Cuadrados: {cuadrados}")

# 5. Uso con filter() - filtrar elementos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# 6. Lambda en una expresión condicional (if-else en una línea)
mayor = lambda a, b: a if a > b else b
print(f"El mayor entre 10 y 20: {mayor(10, 20)}")
