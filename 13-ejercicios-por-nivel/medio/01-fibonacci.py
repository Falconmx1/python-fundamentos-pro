# --- MEDIO: Generar la serie de Fibonacci ---
# Genera los primeros N números de la serie de Fibonacci.

def fibonacci(n):
    """Genera una lista con los primeros n números de Fibonacci."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[i-1] + serie[i-2])
    return serie

try:
    n = int(input("¿Cuántos números de Fibonacci quieres? "))
    resultado = fibonacci(n)
    print(f"Serie de Fibonacci (primeros {n}): {resultado}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
