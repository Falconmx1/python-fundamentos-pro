# --- EJERCICIOS PRÁCTICOS (POO) ---

# Ejercicio 1: Sistema de vehículos
print("=== EJERCICIO 1: Sistema de vehículos ===")
class Vehiculo:
    # Crea una clase base Vehiculo con:
    # - Atributos: marca, modelo, año, velocidad
    # - Métodos: acelerar(), frenar(), mostrar_info()
    pass

class Coche(Vehiculo):
    # Hereda de Vehiculo y añade:
    # - Atributo: numero_puertas
    # - Sobrescribe mostrar_info()
    pass

class Moto(Vehiculo):
    # Hereda de Vehiculo y añade:
    # - Atributo: tiene_casco
    # - Método: hacer_wheelie()
    pass

# Ejercicio 2: Sistema de empleados
print("\n=== EJERCICIO 2: Sistema de empleados ===")
class Empleado:
    # Crea una clase Empleado con:
    # - Atributos: nombre, salario_base, departamento
    # - Método: calcular_salario() (retorna salario_base)
    pass

class Gerente(Empleado):
    # Hereda de Empleado y añade:
    # - Atributo: bono
    # - Sobrescribe calcular_salario() (salario_base + bono)
    pass

class Desarrollador(Empleado):
    # Hereda de Empleado y añade:
    # - Atributo: lenguaje_principal
    # - Método: programar()
    pass

# Ejercicio 3: Sistema de inventario
print("\n=== EJERCICIO 3: Sistema de inventario ===")
class Producto:
    # Crea una clase Producto con:
    # - Atributos privados: _nombre, _precio, _stock
    # - Propiedades con validación (precio > 0, stock >= 0)
    # - Métodos: vender(cantidad), reponer(cantidad)
    pass

# Ejercicio 4: Biblioteca
print("\n=== EJERCICIO 4: Biblioteca ===")
class Biblioteca:
    # Crea una clase Biblioteca que contenga libros usando:
    # - __init__, __str__, __len__, __getitem__, __iter__
    # - Métodos: agregar_libro(), buscar_por_autor()
    pass

# =============================================
# SOLUCIONES
# =============================================

# Solución Ejercicio 1
class VehiculoSolucion:
    def __init__(self, marca, modelo, año, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = velocidad
    
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"{self.marca} {self.modelo} aceleró a {self.velocidad} km/h")
    
    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"{self.marca} {self.modelo} frenó a {self.velocidad} km/h")
    
    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.año}) - Velocidad: {self.velocidad} km/h"

class CocheSolucion(VehiculoSolucion):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} - Puertas: {self.numero_puertas}"

class MotoSolucion(VehiculoSolucion):
    def __init__(self, marca, modelo, año, tiene_casco=True):
        super().__init__(marca, modelo, año)
        self.tiene_casco = tiene_casco
    
    def hacer_wheelie(self):
        if self.velocidad > 20:
            print(f"¡{self.marca} {self.modelo} haciendo wheelie!")
        else:
            print("Necesita más velocidad para hacer wheelie")

# Probar soluciones
print("--- Probando vehículos ---")
coche = CocheSolucion("Toyota", "Corolla", 2020, 4)
moto = MotoSolucion("Honda", "CBR", 2021, True)

coche.acelerar(50)
print(coche.mostrar_info())
moto.acelerar(30)
moto.hacer_wheelie()
moto.frenar(15)
print(moto.mostrar_info())

# Solución Ejercicio 2
class EmpleadoSolucion:
    def __init__(self, nombre, salario_base, departamento):
        self.nombre = nombre
        self.salario_base = salario_base
        self.departamento = departamento
    
    def calcular_salario(self):
        return self.salario_base
    
    def __str__(self):
        return f"{self.nombre} - {self.departamento} - Salario: ${self.calcular_salario()}"

class GerenteSolucion(EmpleadoSolucion):
    def __init__(self, nombre, salario_base, departamento, bono):
        super().__init__(nombre, salario_base, departamento)
        self.bono = bono
    
    def calcular_salario(self):
        return self.salario_base + self.bono

class DesarrolladorSolucion(EmpleadoSolucion):
    def __init__(self, nombre, salario_base, departamento, lenguaje_principal):
        super().__init__(nombre, salario_base, departamento)
        self.lenguaje_principal = lenguaje_principal
    
    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje_principal}")

# Probar empleados
print("\n--- Probando empleados ---")
gerente = GerenteSolucion("Ana", 8000, "TI", 2000)
dev = DesarrolladorSolucion("Luis", 6000, "TI", "Python")

print(gerente)
print(dev)
dev.programar()
