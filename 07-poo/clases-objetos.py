# --- CLASES Y OBJETOS ---
# La POO es un paradigma que organiza el código en objetos que contienen datos y comportamientos.

# 1. Definir una clase básica
class Perro:
    """Clase que representa un perro."""
    
    # Atributo de clase (compartido por todas las instancias)
    especie = "Canis familiaris"
    
    # Constructor (método especial que se ejecuta al crear un objeto)
    def __init__(self, nombre, edad):
        """Inicializa los atributos del perro."""
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad
    
    # Método de instancia (comportamiento)
    def ladrar(self):
        """Hace que el perro ladre."""
        print(f"{self.nombre} dice: ¡Guau, guau!")
    
    def presentarse(self):
        """Presenta al perro."""
        print(f"Soy {self.nombre}, tengo {self.edad} años y soy un {self.especie}")

# 2. Crear objetos (instancias de la clase)
mi_perro = Perro("Max", 3)
tu_perro = Perro("Luna", 2)

# 3. Acceder a atributos y métodos
print(f"Nombre: {mi_perro.nombre}")
print(f"Edad: {mi_perro.edad}")
print(f"Especie: {mi_perro.especie}")
mi_perro.ladrar()
mi_perro.presentarse()

# 4. Modificar atributos
mi_perro.edad = 4
print(f"Nueva edad de Max: {mi_perro.edad}")

# 5. Atributos de clase vs atributos de instancia
print(f"Especie (clase): {Perro.especie}")
print(f"Especie (instancia): {mi_perro.especie}")
Perro.especie = "Canis lupus familiaris"  # Modificar atributo de clase
print(f"Especie modificada: {mi_perro.especie}")

# 6. Métodos con parámetros
class Calculadora:
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b

calc = Calculadora()
print(f"Suma: {calc.sumar(5, 3)}")
print(f"Resta: {calc.restar(10, 4)}")
