# --- DICCIONARIOS ---
# Son colecciones NO ordenadas de pares clave-valor.

# 1. Creación de diccionarios
diccionario_vacio = {}
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "CDMX",
    "habilidades": ["Python", "SQL", "HTML"]
}
print(f"Diccionario persona: {persona}")

# 2. Acceso a valores
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")  # método get()
print(f"Email: {persona.get('email', 'No especificado')}")  # Valor por defecto

# 3. Modificar y agregar elementos
persona["edad"] = 29          # Modificar
persona["email"] = "carlos@email.com"  # Agregar
print(f"Actualizado: {persona}")

# 4. Eliminar elementos
del persona["ciudad"]         # Usando del
email = persona.pop("email")   # Usando pop (devuelve valor)
ultimo = persona.popitem()    # Elimina y devuelve el último par
print(f"Elemento eliminado: {ultimo}")
print(f"Después de eliminaciones: {persona}")

# 5. Recorrer un diccionario
print("\nRecorrido de persona:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

print("\nSolo claves:")
for clave in persona.keys():
    print(clave)

print("\nSolo valores:")
for valor in persona.values():
    print(valor)

# 6. Diccionarios anidados
escuela = {
    "nombre": "Escuela Python",
    "estudiantes": [
        {"nombre": "Ana", "nota": 9.5},
        {"nombre": "Luis", "nota": 8.0}
    ],
    "director": {"nombre": "Sr. Pérez", "experiencia": 10}
}
print(f"Estudiante 1: {escuela['estudiantes'][0]['nombre']} - Nota: {escuela['estudiantes'][0]['nota']}")
