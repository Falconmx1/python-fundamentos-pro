# --- HERENCIA ---
# La herencia permite crear una nueva clase a partir de una existente.

# 1. Clase base (padre)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer(self):
        print(f"{self.nombre} está comiendo")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# 2. Clase derivada (hija) - Hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad)
        self.raza = raza
    
    # Sobrescribir método
    def comer(self):
        print(f"{self.nombre} el perro está comiendo croquetas")
    
    # Método específico de Perro
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")

# 3. Usar las clases
mi_perro = Perro("Max", 3, "Labrador")
mi_gato = Gato("Luna", 2, "Negro")

print(f"Perro: {mi_perro.nombre}, raza: {mi_perro.raza}")
print(f"Gato: {mi_gato.nombre}, color: {mi_gato.color}")

mi_perro.comer()    # Método sobrescrito
mi_gato.comer()     # Método heredado
mi_perro.ladrar()
mi_gato.maullar()

# 4. Herencia múltiple
class Volador:
    def volar(self):
        print("Volando...")

class Nadador:
    def nadar(self):
        print("Nadando...")

class Pato(Animal, Volador, Nadador):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def graznar(self):
        print(f"{self.nombre} dice: ¡Cua, cua!")

# Crear un pato
pato = Pato("Donald", 5)
pato.comer()
pato.volar()
pato.nadar()
pato.graznar()

# 5. Verificar herencia
print(f"\n¿Perro es subclase de Animal? {issubclass(Perro, Animal)}")
print(f"¿mi_perro es instancia de Perro? {isinstance(mi_perro, Perro)}")
print(f"¿mi_perro es instancia de Animal? {isinstance(mi_perro, Animal)}")
