# --- LECTURA DE ARCHIVOS ---

# 1. Crear un archivo de ejemplo
with open('ejemplo.txt', 'w') as f:
    f.write("Línea 1: Hola mundo\n")
    f.write("Línea 2: Esto es Python\n")
    f.write("Línea 3: Manejo de archivos\n")

# 2. Leer todo el archivo
print("--- Lectura completa ---")
with open('ejemplo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

# 3. Leer línea por línea
print("\n--- Lectura línea por línea ---")
with open('ejemplo.txt', 'r') as archivo:
    for linea in archivo:
        print(f"Línea: {linea.strip()}")

# 4. Leer todas las líneas en una lista
print("\n--- Lectura como lista ---")
with open('ejemplo.txt', 'r') as archivo:
    lineas = archivo.readlines()
    print(f"Número de líneas: {len(lineas)}")
    print(f"Segunda línea: {lineas[1].strip()}")

# 5. Leer solo una parte del archivo
print("\n--- Lectura parcial ---")
with open('ejemplo.txt', 'r') as archivo:
    primeros_caracteres = archivo.read(10)  # Leer 10 caracteres
    print(f"Primeros 10 caracteres: {primeros_caracteres}")

# 6. Leer archivo línea por línea con while
print("\n--- Lectura con while ---")
with open('ejemplo.txt', 'r') as archivo:
    while True:
        linea = archivo.readline()
        if not linea:  # Fin del archivo
            break
        print(f"Línea: {linea.strip()}")

# 7. Verificar si el archivo existe
import os
print(f"\n¿Existe el archivo? {os.path.exists('ejemplo.txt')}")
print(f"Tamaño del archivo: {os.path.getsize('ejemplo.txt')} bytes")
