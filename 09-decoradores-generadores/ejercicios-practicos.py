# --- EJERCICIOS PRÁCTICOS (Decoradores y Generadores) ---

# Ejercicio 1: Decorador de validación
print("=== EJERCICIO 1: Decorador de validación ===")
"""
Crea un decorador que valide que los argumentos de una función sean positivos.
Si algún argumento es negativo o cero, lanza una excepción.
"""
# Tu código aquí
def validar_positivos(funcion):
    # ...
    pass

# Ejercicio 2: Decorador de cache
print("\n=== EJERCICIO 2: Decorador de cache ===")
"""
Crea un decorador que cachee los resultados de una función.
Si la función se llama con los mismos argumentos, devuelve el resultado almacenado.
"""
# Tu código aquí
def cache(funcion):
    # ...
    pass

# Ejercicio 3: Generador de números pares
print("\n=== EJERCICIO 3: Generador de pares ===")
def generador_pares(limite):
    """Generador que produce números pares hasta un límite."""
    pass

# Ejercicio 4: Generador de secuencias
print("\n=== EJERCICIO 4: Generador de secuencias ===")
def generador_secuencia(tipo, limite):
    """
    Generador que produce diferentes tipos de secuencias:
    - 'par': números pares
    - 'impar': números impares
    - 'cuadrado': cuadrados perfectos
    - 'fibonacci': serie de Fibonacci
    """
    pass

# =============================================
# SOLUCIONES
# =============================================

# Solución Ejercicio 1
def validar_positivos_solucion(funcion):
    from functools import wraps
    
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Los argumentos deben ser números positivos. Recibido: {arg}")
        for valor in kwargs.values():
            if not isinstance(valor, (int, float)) or valor <= 0:
                raise ValueError(f"Los argumentos deben ser números positivos. Recibido: {valor}")
        return funcion(*args, **kwargs)
    return wrapper

# Solución Ejercicio 2
def cache_solucion(funcion):
    from functools import wraps
    
    cache_dict = {}
    
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        # Crear una clave basada en los argumentos
        clave = str(args) + str(kwargs)
        if clave in cache_dict:
            print(f"Resultado en cache para {funcion.__name__}{args}")
            return cache_dict[clave]
        resultado = funcion(*args, **kwargs)
        cache_dict[clave] = resultado
        return resultado
    return wrapper

@cache_solucion
def calcular_cuadrado(n):
    print(f"Calculando cuadrado de {n}")
    return n ** 2

# Probar cache
print("\n--- Probando decorador de cache ---")
print(calcular_cuadrado(4))
print(calcular_cuadrado(4))  # Este debe usar el cache

# Solución Ejercicio 3
def generador_pares_solucion(limite):
    """Generador que produce números pares hasta un límite."""
    for i in range(0, limite + 1, 2):
        yield i

print("\n--- Pares generator ---")
for p in generador_pares_solucion(20):
    print(p, end=" ")
print()

# Solución Ejercicio 4
def generador_secuencia_solucion(tipo, limite):
    """Generador que produce diferentes secuencias."""
    if tipo == 'par':
        for i in range(0, limite + 1, 2):
            yield i
    elif tipo == 'impar':
        for i in range(1, limite + 1, 2):
            yield i
    elif tipo == 'cuadrado':
        for i in range(1, int(limite ** 0.5) + 1):
            yield i ** 2
    elif tipo == 'fibonacci':
        a, b = 0, 1
        while a <= limite:
            yield a
            a, b = b, a + b
    else:
        raise ValueError(f"Tipo '{tipo}' no válido")

print("\n--- Secuencia de cuadrados ---")
for c in generador_secuencia_solucion('cuadrado', 50):
    print(c, end=" ")
print()

print("\n--- Secuencia Fibonacci ---")
for f in generador_secuencia_solucion('fibonacci', 100):
    print(f, end=" ")
print()
