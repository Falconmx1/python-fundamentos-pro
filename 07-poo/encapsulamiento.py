# --- ENCAPSULAMIENTO ---
# El encapsulamiento protege los datos internos de un objeto.

# 1. Atributos públicos (accesibles desde fuera)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre      # Público
        self.edad = edad          # Público

# 2. Atributos privados (convención: _ o __)
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial      # Privado por convención
        self.__clave = "1234"            # Name mangling (más privado)
    
    # 3. Métodos públicos para interactuar con atributos privados
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self._saldo}")
        else:
            print("Cantidad inválida")
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Cantidad inválida")
        elif cantidad > self._saldo:
            print("Saldo insuficiente")
        else:
            self._saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self._saldo}")
    
    def consultar_saldo(self):
        return self._saldo
    
    # 4. Propiedades (getters y setters)
    @property
    def saldo(self):
        """Getter para el saldo."""
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        """Setter para el saldo (con validación)."""
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor
    
    @property
    def clave(self):
        """Getter para la clave (solo lectura)."""
        return "****"  # No mostramos la clave real

# 5. Usar la cuenta bancaria
cuenta = CuentaBancaria("Ana", 1000)

# Acceder a atributos públicos
print(f"Titular: {cuenta.titular}")

# Intentar acceder a atributos privados (NO recomendado)
print(f"Saldo (convención): {cuenta._saldo}")  # Funciona pero no deberías
# print(cuenta.__clave)  # Esto da error (name mangling)
print(f"Clave (oculta): {cuenta.clave}")

# Usar métodos públicos
cuenta.depositar(500)
cuenta.retirar(200)
print(f"Saldo actual: ${cuenta.consultar_saldo()}")

# Usar propiedades
print(f"Saldo con propiedad: ${cuenta.saldo}")
try:
    cuenta.saldo = -100  # Esto lanza una excepción
except ValueError as e:
    print(f"Error: {e}")

# 6. Atributos protegidos en herencia
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario  # Protegido
    
    def _calcular_bono(self):    # Método protegido
        return self._salario * 0.1

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    
    def obtener_informacion(self):
        # Acceso a atributo protegido de la clase padre
        bono = self._calcular_bono()
        return f"Gerente: {self.nombre}, Salario: ${self._salario}, Bono: ${bono}"

gerente = Gerente("Carlos", 5000, "TI")
print(gerente.obtener_informacion())
