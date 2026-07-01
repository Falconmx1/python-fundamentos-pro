# --- ESCRITURA DE ARCHIVOS ---

# 1. Modo 'w' - escribir (sobrescribe el archivo)
print("--- Modo 'w' (sobrescribe) ---")
with open('nuevo_archivo.txt', 'w') as archivo:
    archivo.write("Este archivo fue creado con 'w'\n")
    archivo.write("Escribimos dos líneas\n")
    archivo.write("Python es genial\n")

# Verificar el contenido
with open('nuevo_archivo.txt', 'r') as f:
    print(f.read())

# 2. Modo 'a' - agregar al final
print("\n--- Modo 'a' (agregar) ---")
with open('nuevo_archivo.txt', 'a') as archivo:
    archivo.write("Esta línea fue agregada con 'a'\n")
    archivo.write("Y esta también\n")

# Verificar nuevamente
with open('nuevo_archivo.txt', 'r') as f:
    print(f.read())

# 3. Escribir múltiples líneas con writelines()
print("\n--- Escritura con writelines() ---")
lineas = ["Línea A\n", "Línea B\n", "Línea C\n"]
with open('multiples_lineas.txt', 'w') as archivo:
    archivo.writelines(lineas)

# 4. Escritura en modo 'x' (crear nuevo archivo)
print("\n--- Modo 'x' (creación exclusiva) ---")
try:
    with open('archivo_nuevo.txt', 'x') as archivo:
        archivo.write("Este archivo es nuevo y único")
except FileExistsError:
    print("El archivo ya existe")

# 5. Escribir con encoding y errores manejados
print("\n--- Escritura con encoding ---")
texto_con_acentos = "Qué bien es Python con acentos"
with open('con_acentos.txt', 'w', encoding='utf-8') as archivo:
    archivo.write(texto_con_acentos)

# Leer el archivo con acentos
with open('con_acentos.txt', 'r', encoding='utf-8') as archivo:
    print(archivo.read())

# 6. Escritura en modo binario
print("\n--- Escritura binaria ---")
datos_binarios = bytes([65, 66, 67, 68, 69])  # A B C D E
with open('datos.bin', 'wb') as archivo:
    archivo.write(datos_binarios)

# Leer el archivo binario
with open('datos.bin', 'rb') as archivo:
    contenido = archivo.read()
    print(f"Datos binarios: {contenido}")
    print(f"Como texto: {contenido.decode('utf-8')}")
