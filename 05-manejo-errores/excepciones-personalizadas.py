# --- EXCEPCIONES PERSONALIZADAS ---
# Puedes crear tus propias clases de excepción para casos específicos.

# 1. Definir una excepción personalizada
class EdadInvalidaError(Exception):
    """Excepción lanzada cuando una edad no es válida."""
    def __init__(self, edad, mensaje="Edad no válida"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(f"{mensaje}: {edad}")

class SaldoInsuficienteError(Exception):
    """Excepción para cuando el saldo es insuficiente."""
    def __init__(self, saldo, cantidad, mensaje="Saldo insuficiente"):
        self.saldo = saldo
        self.cantidad = cantidad
        self.mensaje = mensaje
        super().__init__(f"{mensaje}. Saldo: {saldo}, Cantidad solicitada: {cantidad}")

# 2. Usar la excepción personalizada
def verificar_edad(edad):
    """Verifica que la edad esté en un rango válido (0-120)."""
    if edad < 0 or edad > 120:
        raise EdadInvalidaError(edad, "La edad debe estar entre 0 y 120")
    return True

# Probar la excepción personalizada
try:
    edad_usuario = int(input("Ingresa tu edad: "))
    verificar_edad(edad_usuario)
    print(f"Edad {edad_usuario} válida")
except EdadInvalidaError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: No ingresaste un número")

# 3. Ejemplo con saldo bancario
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(self.saldo, cantidad)
        self.saldo -= cantidad
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")

# Probar la cuenta bancaria
cuenta = CuentaBancaria("Ana", 1000)
print(f"\nSaldo inicial: {cuenta.saldo}")
try:
    cuenta.retirar(1500)
except SaldoInsuficienteError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("Operación exitosa")
finally:
    print(f"Saldo actual: {cuenta.saldo}")
