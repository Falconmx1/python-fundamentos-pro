# --- MÓDULO 1 DEL PAQUETE ---
# Este es un módulo dentro de un paquete.

def funcion_util():
    """Función útil del módulo 1."""
    return "Función del módulo 1 ejecutada"

def calcular_cuadrado(numero):
    """Calcula el cuadrado de un número."""
    return numero ** 2

def calcular_cubo(numero):
    """Calcula el cubo de un número."""
    return numero ** 3

class Utilidad:
    """Clase de utilidad del módulo 1."""
    
    @staticmethod
    def saludar(nombre):
        return f"Hola desde módulo 1, {nombre}"
    
    def procesar_datos(self, datos):
        """Procesa una lista de datos."""
        return [d * 2 for d in datos]

# Si se ejecuta directamente
if __name__ == "__main__":
    print("Módulo 1 ejecutado directamente")
    print(funcion_util())
