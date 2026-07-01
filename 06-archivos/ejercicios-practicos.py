# --- EJERCICIOS PRÁCTICOS (Archivos) ---

# Ejercicio 1: Gestor de notas
print("=== EJERCICIO 1: Gestor de notas ===")
def gestor_notas():
    """
    Crea un programa que permita:
    - Agregar notas a un archivo (una por línea)
    - Leer todas las notas
    - Eliminar una nota específica
    """
    # Tu código aquí
    pass

# Ejercicio 2: Contador de palabras en archivo
print("\n=== EJERCICIO 2: Contador de palabras ===")
def contar_palabras_archivo(nombre_archivo):
    """
    Lee un archivo y cuenta las palabras, ignorando puntuación.
    Devuelve un diccionario con {palabra: frecuencia}
    """
    # Tu código aquí
    pass

# Ejercicio 3: Backup de archivos
print("\n=== EJERCICIO 3: Backup de archivos ===")
def crear_backup(nombre_archivo):
    """
    Crea una copia de seguridad del archivo con extensión .bak
    """
    # Tu código aquí
    pass

# Ejercicio 4: Procesamiento de CSV
print("\n=== EJERCICIO 4: Procesamiento de CSV ===")
def procesar_csv(nombre_archivo):
    """
    Lee un archivo CSV y realiza operaciones con los datos.
    Puedes usar el módulo csv de Python.
    """
    # Tu código aquí
    pass

# Ejercicio 5: Registro de eventos con JSON
print("\n=== EJERCICIO 5: Registro de eventos ===")
def registrar_evento(evento, datos):
    """
    Agrega un evento a un archivo JSON con timestamp.
    Formato: [{"timestamp": "2023-01-01 12:00", "evento": "login", "datos": {...}}]
    """
    # Tu código aquí
    pass

# =============================================
# SOLUCIONES
# =============================================

# Solución Ejercicio 1
def gestor_notas_solucion():
    """Solución para gestor de notas."""
    import os
    archivo_notas = 'notas.txt'
    
    while True:
        print("\n--- Gestor de Notas ---")
        print("1. Agregar nota")
        print("2. Leer notas")
        print("3. Eliminar nota")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nota = input("Escribe tu nota: ")
            with open(archivo_notas, 'a', encoding='utf-8') as f:
                f.write(nota + '\n')
            print("Nota agregada correctamente")
            
        elif opcion == '2':
            try:
                with open(archivo_notas, 'r', encoding='utf-8') as f:
                    notas = f.readlines()
                    if not notas:
                        print("No hay notas guardadas")
                    else:
                        print("\n--- Notas Guardadas ---")
                        for i, nota in enumerate(notas, 1):
                            print(f"{i}. {nota.strip()}")
            except FileNotFoundError:
                print("Aún no hay notas guardadas")
                
        elif opcion == '3':
            try:
                with open(archivo_notas, 'r', encoding='utf-8') as f:
                    notas = f.readlines()
                
                if not notas:
                    print("No hay notas para eliminar")
                    continue
                
                print("\nNotas actuales:")
                for i, nota in enumerate(notas, 1):
                    print(f"{i}. {nota.strip()}")
                
                num = int(input("Número de nota a eliminar: "))
                if 1 <= num <= len(notas):
                    del notas[num-1]
                    with open(archivo_notas, 'w', encoding='utf-8') as f:
                        f.writelines(notas)
                    print("Nota eliminada")
                else:
                    print("Número inválido")
            except (FileNotFoundError, ValueError):
                print("Error al eliminar la nota")
                
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

# Solución Ejercicio 2
def contar_palabras_archivo_solucion(nombre_archivo):
    """Solución para contar palabras en un archivo."""
    import string
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Limpiar texto de puntuación y convertir a minúsculas
        traductor = str.maketrans('', '', string.punctuation)
        texto_limpio = contenido.translate(traductor).lower()
        
        palabras = texto_limpio.split()
        contador = {}
        
        for palabra in palabras:
            contador[palabra] = contador.get(palabra, 0) + 1
        
        # Ordenar por frecuencia descendente
        return dict(sorted(contador.items(), key=lambda x: x[1], reverse=True))
    
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe")
        return {}
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return {}

# Probar la solución
if __name__ == "__main__":
    print("--- Prueba del contador de palabras ---")
    # Crear un archivo de prueba
    with open('test_palabras.txt', 'w') as f:
        f.write("Python es genial, Python es poderoso. Python es todo!")
    
    resultado = contar_palabras_archivo_solucion('test_palabras.txt')
    for palabra, frecuencia in list(resultado.items())[:5]:
        print(f"{palabra}: {frecuencia} veces")
