# --- CLAUSULAS ELSE Y FINALLY EN PROFUNDIDAD ---

# 1. Uso avanzado de else
def procesar_archivo(nombre_archivo):
    """Intenta leer un archivo y procesar su contenido."""
    try:
        archivo = open(nombre_archivo, 'r')
        contenido = archivo.read()
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe")
    except PermissionError:
        print(f"No tienes permiso para leer {nombre_archivo}")
    else:
        # Este bloque solo se ejecuta si no hubo excepción
        print(f"Contenido del archivo: {contenido[:50]}...")
        palabras = len(contenido.split())
        print(f"El archivo tiene {palabras} palabras")
    finally:
        # Esto siempre se ejecuta, se use para limpiar recursos
        try:
            archivo.close()
            print("Archivo cerrado correctamente")
        except:
            print("El archivo no estaba abierto")

# 2. Ejemplo con conexión a base de datos simulada
import time

def conectar_base_datos():
    """Simula una conexión a base de datos."""
    print("Conectando a la base de datos...")
    time.sleep(0.5)
    # Simular error de conexión aleatorio
    import random
    if random.random() < 0.3:
        raise ConnectionError("Error de conexión a la base de datos")
    return "Conexión exitosa"

def ejecutar_consulta(consulta):
    """Ejecuta una consulta en la base de datos."""
    conexion = None
    try:
        conexion = conectar_base_datos()
        print(f"Ejecutando consulta: {consulta}")
        # Simular resultado
        resultado = ["dato1", "dato2", "dato3"]
    except ConnectionError as e:
        print(f"Error de conexión: {e}")
    else:
        print(f"Consulta ejecutada. Resultados: {resultado}")
        return resultado
    finally:
        if conexion:
            print("Cerrando conexión a la base de datos")
        else:
            print("No hay conexión que cerrar")

# 3. Uso en operaciones con recursos
def leer_configuracion():
    """Lee configuración de un archivo con manejo robusto."""
    try:
        with open('config.txt', 'r') as f:  # with ya maneja el cierre automático
            return f.read()
    except FileNotFoundError:
        # Usar configuración por defecto
        return "configuración predeterminada"
    except Exception as e:
        print(f"Error inesperado leyendo configuración: {e}")
        return None
    else:
        print("Configuración cargada exitosamente")
    finally:
        print("Proceso de lectura de configuración finalizado")

# Probar las funciones
print("\n--- Procesando archivo ---")
procesar_archivo('ejemplo.txt')

print("\n--- Ejecutando consulta en base de datos ---")
ejecutar_consulta("SELECT * FROM usuarios")

print("\n--- Leyendo configuración ---")
config = leer_configuracion()
print(f"Configuración: {config}")
