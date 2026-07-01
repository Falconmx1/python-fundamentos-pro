# --- DECORADORES ---
# Los decoradores son funciones que modifican el comportamiento de otras funciones.

# 1. Decorador básico
def decorador_simple(funcion):
    """Decorador que imprime un mensaje antes y después de la función."""
    def wrapper(*args, **kwargs):
        print("--- Antes de ejecutar la función ---")
        resultado = funcion(*args, **kwargs)
        print("--- Después de ejecutar la función ---")
        return resultado
    return wrapper

# 2. Aplicar el decorador con @
@decorador_simple
def saludar(nombre):
    print(f"Hola, {nombre}!")

@decorador_simple
def sumar(a, b):
    return a + b

# Probar decoradores
print("--- Decorador básico ---")
saludar("Ana")
resultado = sumar(5, 3)
print(f"Resultado: {resultado}")

# 3. Decorador que mide tiempo de ejecución
import time

def medir_tiempo(funcion):
    """Decorador que mide el tiempo de ejecución de una función."""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def operacion_lenta():
    time.sleep(0.5)
    return "Operación completada"

print("\n--- Medir tiempo ---")
print(operacion_lenta())

# 4. Decorador con parámetros
def repetir(veces):
    """Decorador que repite la función un número de veces."""
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            resultados = []
            for i in range(veces):
                print(f"Ejecución {i+1}/{veces}")
                resultados.append(funcion(*args, **kwargs))
            return resultados
        return wrapper
    return decorador

@repetir(3)
def saludar_multi(nombre):
    return f"Hola {nombre}"

print("\n--- Decorador con parámetros ---")
resultados = saludar_multi("Carlos")
print(f"Resultados: {resultados}")

# 5. Decorador con argumentos y preservación de metadatos
from functools import wraps

def loggear(activo=True):
    """Decorador que registra llamadas a funciones."""
    def decorador(funcion):
        @wraps(funcion)  # Preserva el nombre y docstring
        def wrapper(*args, **kwargs):
            if activo:
                print(f"Llamando a {funcion.__name__} con args={args}, kwargs={kwargs}")
            return funcion(*args, **kwargs)
        return wrapper
    return decorador

@loggear(activo=True)
def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

print("\n--- Decorador con argumentos y metadatos ---")
print(f"Resultado: {multiplicar(4, 7)}")
print(f"Nombre de la función: {multiplicar.__name__}")
print(f"Docstring: {multiplicar.__doc__}")

# 6. Decorador que verifica tipos
def verificar_tipos(tipos):
    """Decorador que verifica los tipos de los argumentos."""
    def decorador(funcion):
        @wraps(funcion)
        def wrapper(*args, **kwargs):
            for i, (arg, tipo) in enumerate(zip(args, tipos)):
                if not isinstance(arg, tipo):
                    raise TypeError(f"Argumento {i} debe ser {tipo.__name__}, recibió {type(arg).__name__}")
            return funcion(*args, **kwargs)
        return wrapper
    return decorador

@verificar_tipos([int, int])
def dividir(a, b):
    return a / b

print("\n--- Verificación de tipos ---")
print(dividir(10, 2))
try:
    dividir("10", 2)
except TypeError as e:
    print(f"Error: {e}")
