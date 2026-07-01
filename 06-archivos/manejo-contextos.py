# --- MANEJO DE CONTEXTOS CON WITH ---

# 1. Contexto básico con archivos
print("--- Contexto básico ---")
with open('contexto.txt', 'w') as archivo:
    archivo.write("Este archivo se cierra automáticamente")

# El archivo ya está cerrado fuera del bloque with
# Intentar leerlo fuera del with
try:
    with open('contexto.txt', 'r') as f:
        print(f.read())
except Exception as e:
    print(f"Error al leer: {e}")

# 2. Múltiples contextos
print("\n--- Múltiples contextos ---")
with open('contexto1.txt', 'w') as archivo1, open('contexto2.txt', 'w') as archivo2:
    archivo1.write("Texto en archivo 1\n")
    archivo2.write("Texto en archivo 2\n")

# 3. Contexto con manejo de errores
print("\n--- Contexto con manejo de errores ---")
try:
    with open('archivo_inexistente.txt', 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print(f"Error: {e}")

# 4. Gestor de contexto personalizado
print("\n--- Gestor de contexto personalizado ---")
class MiGestorContexto:
    def __enter__(self):
        print("Entrando al contexto")
        self.archivo = open('contexto_personalizado.txt', 'w')
        return self.archivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del contexto")
        self.archivo.close()
        if exc_type:
            print(f"Se produjo un error: {exc_val}")
        return False  # No suprimir las excepciones

with MiGestorContexto() as archivo:
    archivo.write("Escrito con gestor personalizado\n")
    print("Operación exitosa")

# 5. Usando contextlib para crear gestores simples
from contextlib import contextmanager

@contextmanager
def gestor_simple():
    print("--- Inicio del contexto ---")
    archivo = open('contextlib.txt', 'w')
    try:
        yield archivo
    finally:
        archivo.close()
        print("--- Fin del contexto ---")

# Usar el gestor
with gestor_simple() as archivo:
    archivo.write("Escrito con contextlib\n")

# 6. Contexto para operaciones con temporizador
import time

@contextmanager
def temporizador():
    """Mide el tiempo de ejecución del bloque."""
    inicio = time.time()
    try:
        yield
    finally:
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")

print("\n--- Temporizador con contexto ---")
with temporizador():
    # Simular operación que toma tiempo
    time.sleep(0.5)
    print("Operación completada")
