# --- EJERCICIOS PRÁCTICOS (Manejo de Errores) ---

# Ejercicio 1: Calculadora con manejo de errores
print("=== EJERCICIO 1: Calculadora robusta ===")
def calculadora_segura():
    """
    Crea una calculadora que maneje:
    - División entre cero
    - Entrada no numérica
    - Operaciones inválidas
    """
    # Tu código aquí
    pass

# Ejercicio 2: Validación de usuario
print("\n=== EJERCICIO 2: Validación de usuario ===")
class UsuarioInvalidoError(Exception):
    """Excepción para usuario inválido."""
    pass

def validar_usuario(nombre, email, edad):
    """
    Valida un usuario:
    - Nombre no vacío
    - Email con @
    - Edad entre 18 y 100
    """
    # Tu código aquí
    pass

# Ejercicio 3: Gestor de archivos robusto
print("\n=== EJERCICIO 3: Gestor de archivos ===")
def leer_archivo_seguro(nombre_archivo):
    """
    Lee un archivo manejando:
    - Archivo no encontrado
    - Permisos insuficientes
    - Formato incorrecto
    """
    # Tu código aquí
    pass

# Ejercicio 4: Sistema de reservas
print("\n=== EJERCICIO 4: Sistema de reservas ===")
class ReservaAgotadaError(Exception):
    pass

class ReservaDuplicadaError(Exception):
    pass

def sistema_reservas():
    """
    Simula un sistema de reservas con:
    - Límite de asientos (10)
    - No permitir reservas duplicadas
    - Validar que el nombre no esté vacío
    """
    # Tu código aquí
    pass

# Ejercicio 5: Conversor de divisas
print("\n=== EJERCICIO 5: Conversor de divisas ===")
def convertir_divisa(cantidad, moneda_origen, moneda_destino):
    """
    Convierte divisas con manejo de:
    - Divisas no soportadas
    - Cantidades negativas
    - Tasas de cambio obsoletas
    """
    # Tu código aquí
    pass

# =============================================
# SOLUCIONES (NO MIRES ANTES DE INTENTARLO)
# =============================================

# Solución Ejercicio 1
def calculadora_segura_solucion():
    """Solución para calculadora robusta."""
    try:
        num1 = float(input("Ingresa el primer número: "))
        operacion = input("Ingresa la operación (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))
        
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            resultado = num1 / num2
        else:
            raise ValueError("Operación no válida")
        
        print(f"Resultado: {resultado}")
        return resultado
    
    except ValueError as e:
        print(f"Error de valor: {e}")
    except ZeroDivisionError as e:
        print(f"Error matemático: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Solución Ejercicio 2
def validar_usuario_solucion(nombre, email, edad):
    """Solución para validación de usuario."""
    if not nombre or nombre.isspace():
        raise UsuarioInvalidoError("El nombre no puede estar vacío")
    
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise UsuarioInvalidoError("Email inválido")
    
    if edad < 18 or edad > 100:
        raise UsuarioInvalidoError(f"Edad {edad} no permitida (18-100)")
    
    return True

# Función para probar la validación
def probar_validacion():
    try:
        validar_usuario("Ana", "ana@email.com", 25)
        print("Usuario válido")
    except UsuarioInvalidoError as e:
        print(f"Error: {e}")
    
    try:
        validar_usuario("", "ana@email.com", 25)
    except UsuarioInvalidoError as e:
        print(f"Error: {e}")
