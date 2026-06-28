# --- FUNCIONES RECURSIVAS ---
# Una función recursiva es aquella que se llama a sí misma.

# 1. Factorial recursivo
def factorial(n):
    """Calcula el factorial de n (n!)."""
    # Caso base: condición que detiene la recursión
    if n == 0 or n == 1:
        return 1
    # Paso recursivo: la función se llama a sí misma
    else:
        return n * factorial(n - 1)

print(f"Factorial de 5: {factorial(5)}")  # 5*4*3*2*1 = 120
print(f"Factorial de 0: {factorial(0)}")  # 1

# 2. Fibonacci recursivo (versión ineficiente)
def fibonacci(n):
    """Devuelve el n-ésimo número de Fibonacci."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci de 7: {fibonacci(7)}")  # 13
print(f"Serie Fibonacci (0-9):", end=" ")
for i in range(10):
    print(fibonacci(i), end=" ")
print()

# 3. Recursión con lista (sumar elementos)
def sumar_lista(lista):
    """Suma todos los elementos de una lista de forma recursiva."""
    if not lista:  # Lista vacía
        return 0
    else:
        return lista[0] + sumar_lista(lista[1:])

numeros = [1, 2, 3, 4, 5]
print(f"Suma de {numeros}: {sumar_lista(numeros)}")

# 4. Palíndromo recursivo
def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo."""
    # Convertir a minúsculas y eliminar espacios
    palabra = palabra.lower().replace(" ", "")
    # Caso base: longitud 0 o 1
    if len(palabra) <= 1:
        return True
    # Verificar primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con el substring interno
    return es_palindromo(palabra[1:-1])

print(f"¿'reconocer' es palíndromo? {es_palindromo('reconocer')}")
print(f"¿'python' es palíndromo? {es_palindromo('python')}")
print(f"¿'anita lava la tina' es palíndromo? {es_palindromo('anita lava la tina')}")
