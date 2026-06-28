# --- PARÁMETROS Y ARGUMENTOS AVANZADOS ---

# 1. Argumentos por defecto
def saludar_con_titulo(nombre, titulo="Sr."):
    """Saluda usando un título (por defecto 'Sr.')."""
    print(f"Hola, {titulo} {nombre}")

saludar_con_titulo("Pérez")          # Usa el título por defecto
saludar_con_titulo("García", "Sra.") # Sobrescribe el título

# 2. Argumentos por palabra clave (keyword arguments)
def describir_persona(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

# Llamada con argumentos en diferente orden
describir_persona(ciudad="CDMX", nombre="Carlos", edad=30)

# 3. Número variable de argumentos posicionales (*args)
def sumar_todos(*numeros):
    """Suma una cantidad variable de números."""
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todos(1, 2, 3))           # 6
print(sumar_todos(10, 20, 30, 40))    # 100

# 4. Número variable de argumentos con clave (**kwargs)
def mostrar_info(**datos):
    """Muestra pares clave-valor."""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="GDL", profesion="Ingeniera")

# 5. Combinación de argumentos
def funcion_completa(normal, *args, opcional="Default", **kwargs):
    print(f"Argumento normal: {normal}")
    print(f"*args: {args}")
    print(f"Opcional: {opcional}")
    print(f"**kwargs: {kwargs}")

funcion_completa(1, 2, 3, 4, opcional="Cambiado", clave="valor", otro=99)
