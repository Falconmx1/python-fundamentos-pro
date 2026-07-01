# --- MÓDULO 2 DEL PAQUETE ---

def otra_funcion_util():
    """Otra función útil del módulo 2."""
    return "Función del módulo 2 ejecutada"

def calcular_potencia(base, exponente):
    """Calcula la potencia de un número."""
    return base ** exponente

def saludar_personalizado(nombre, titulo="Sr."):
    """Saluda con un título personalizado."""
    return f"Hola, {titulo} {nombre}"

class Generador:
    """Generador de secuencias."""
    
    def generar_fibonacci(self, n):
        """Genera los primeros n números de Fibonacci."""
        if n <= 0:
            return []
        if n == 1:
            return [0]
        
        secuencia = [0, 1]
        for i in range(2, n):
            secuencia.append(secuencia[i-1] + secuencia[i-2])
        return secuencia
    
    def generar_primos(self, limite):
        """Genera números primos hasta un límite."""
        primos = []
        for num in range(2, limite + 1):
            es_primo = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(num)
        return primos

# Si se ejecuta directamente
if __name__ == "__main__":
    print("Módulo 2 ejecutado directamente")
    gen = Generador()
    print(f"Fibonacci(10): {gen.generar_fibonacci(10)}")
