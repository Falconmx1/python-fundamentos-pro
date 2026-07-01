# --- MANEJO DE EXCEPCIONES CON TRY-EXCEPT ---
# Python usa try-except para capturar y manejar errores en tiempo de ejecución.

# 1. Bloque try-except básico
try:
    # Código que puede causar una excepción
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"10 / {numero} = {resultado}")
except ValueError:
    print("¡Error! Debes ingresar un número válido.")
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
print("El programa continúa...\n")

# 2. Capturar múltiples excepciones en un solo bloque
try:
    lista = [1, 2, 3]
    indice = int(input("Ingresa un índice: "))
    print(f"Elemento en índice {indice}: {lista[indice]}")
except (ValueError, IndexError) as error:
    print(f"Error capturado: {type(error).__name__} - {error}")

# 3. Usar Exception para capturar cualquier excepción
try:
    x = 5 / 0
except Exception as e:
    print(f"Error general: {e}")

# 4. Cláusula else (se ejecuta si no hay excepción)
try:
    num = int(input("Ingresa un número: "))
except ValueError:
    print("Error: no es un número")
else:
    print(f"El cuadrado de {num} es {num**2}")

# 5. Cláusula finally (siempre se ejecuta)
try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("El archivo no existe")
finally:
    print("Este bloque siempre se ejecuta, haya o no error")
