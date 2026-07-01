# --- MÓDULO PERSONALIZADO ---
# Este es un módulo que puede ser importado desde otros archivos.

# 1. Variables globales del módulo
version = "1.0.0"
autor = "Tu Nombre"

# 2. Funciones del módulo
def saludar(nombre):
    """Saluda a una persona."""
    return f"¡Hola, {nombre}! Desde mi módulo."

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

# 3. Clase del módulo
class Calculadora:
    def __init__(self):
        self.historial = []
    
    def operar(self, a, b, operacion):
        """Realiza una operación y guarda el historial."""
        if operacion == '+':
            resultado = a + b
        elif operacion == '-':
            resultado = a - b
        elif operacion == '*':
            resultado = a * b
        elif operacion == '/':
            if b == 0:
                raise ValueError("No se puede dividir entre cero")
            resultado = a / b
        else:
            raise ValueError("Operación no válida")
        
        self.historial.append(f"{a} {operacion} {b} = {resultado}")
        return resultado
    
    def mostrar_historial(self):
        """Muestra el historial de operaciones."""
        return self.historial

# 4. Código que se ejecuta solo si se ejecuta el módulo directamente
if __name__ == "__main__":
    print("Este módulo se está ejecutando directamente")
    print(f"Versión: {version}")
    print(saludar("Usuario"))
else:
    print(f"Módulo '{__name__}' importado correctamente")
