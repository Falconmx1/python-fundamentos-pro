# --- GENERADORES ---
# Los generadores son funciones que producen secuencias de valores de forma perezosa.

# 1. Generador básico con yield
def contar_hasta(n):
    """Generador que cuenta desde 0 hasta n-1."""
    print("Iniciando generador")
    for i in range(n):
        print(f"Generando {i}")
        yield i
    print("Generador terminado")

# Usar el generador
print("--- Generador básico ---")
contador = contar_hasta(3)
print(f"Tipo: {type(contador)}")

# Obtener valores uno por uno
print(next(contador))
print(next(contador))
print(next(contador))
# print(next(contador))  # Esto lanza StopIteration

# 2. Iterar con un generador
print("\n--- Iterando con for ---")
for numero in contar_hasta(3):
    print(f"Recibido: {numero}")

# 3. Generador de Fibonacci
def fibonacci_generator(limite):
    """Generador de números de Fibonacci hasta un límite."""
    a, b = 0, 1
    while a <= limite:
        yield a
        a, b = b, a + b

print("\n--- Fibonacci generator ---")
for num in fibonacci_generator(100):
    print(num, end=" ")
print()

# 4. Generador de números primos
def primos_generator(limite):
    """Generador de números primos hasta un límite."""
    for num in range(2, limite + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            yield num

print("\n--- Primos generator ---")
for p in primos_generator(30):
    print(p, end=" ")
print()

# 5. Generador infinito
def generador_infinito():
    """Generador que produce números infinitamente."""
    num = 0
    while True:
        yield num
        num += 1

print("\n--- Generador infinito (limitado) ---")
infinito = generador_infinito()
for i in range(10):
    print(next(infinito), end=" ")
print("...")

# 6. Generador con expresiones (generator expression)
cuadrados_gen = (x**2 for x in range(10))
print("\n--- Generator expression ---")
for cuadrado in cuadrados_gen:
    print(cuadrado, end=" ")
print()

# 7. Comparación: lista vs generador
import sys

print("\n--- Comparación de memoria ---")
lista_cuadrados = [x**2 for x in range(1000)]
gen_cuadrados = (x**2 for x in range(1000))

print(f"Memoria de lista: {sys.getsizeof(lista_cuadrados)} bytes")
print(f"Memoria de generador: {sys.getsizeof(gen_cuadrados)} bytes")

# 8. Generador para procesar archivos grandes
def leer_archivo_lineas(nombre_archivo):
    """Generador para leer un archivo línea por línea."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                yield linea.strip()
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo} no encontrado")

# Crear archivo de prueba
with open('test_generador.txt', 'w') as f:
    for i in range(100):
        f.write(f"Línea {i}\n")

print("\n--- Leer archivo con generador ---")
for linea in leer_archivo_lineas('test_generador.txt'):
    print(linea[:20] + "..." if len(linea) > 20 else linea)
    break  # Solo mostrar la primera línea
