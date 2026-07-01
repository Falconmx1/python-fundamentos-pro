# --- POLIMORFISMO ---
# El polimorfismo permite usar objetos de diferentes clases de manera intercambiable.

# 1. Polimorfismo con métodos
class Pajaro:
    def hacer_sonido(self):
        return "¡Pío, pío!"
    
    def moverse(self):
        return "Vuela"

class Pez:
    def hacer_sonido(self):
        return "Glup, glup"
    
    def moverse(self):
        return "Nada"

class Vaca:
    def hacer_sonido(self):
        return "¡Muuu!"
    
    def moverse(self):
        return "Camina"

# 2. Función que usa polimorfismo
def describir_animal(animal):
    """Describe un animal usando sus métodos."""
    print(f"Sonido: {animal.hacer_sonido()}")
    print(f"Movimiento: {animal.moverse()}")

# 3. Usar polimorfismo
animales = [Pajaro(), Pez(), Vaca()]
print("--- Describiendo animales ---")
for animal in animales:
    describir_animal(animal)
    print()

# 4. Polimorfismo con clases abstractas
from abc import ABC, abstractmethod
import math

class Figura(ABC):
    """Clase abstracta que define un contrato para las figuras."""
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    def describir(self):
        return f"Figura con área {self.area():.2f} y perímetro {self.perimetro():.2f}"

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# 5. Usar figuras
figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 4, 3, 4, 5)
]

print("--- Calculando áreas y perímetros ---")
for figura in figuras:
    print(f"{figura.__class__.__name__}: {figura.describir()}")
    print()
