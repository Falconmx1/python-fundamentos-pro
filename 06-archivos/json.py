# --- MANEJO DE JSON (JavaScript Object Notation) ---
import json

# 1. Datos de ejemplo en Python
datos = {
    "nombre": "Carlos",
    "edad": 30,
    "casado": False,
    "hijos": ["Ana", "Luis"],
    "direccion": {
        "calle": "Calle Principal 123",
        "ciudad": "CDMX"
    },
    "calificaciones": [85, 90, 78, 92]
}

# 2. Guardar datos en JSON
print("--- Guardando JSON ---")
with open('datos.json', 'w', encoding='utf-8') as archivo:
    json.dump(datos, archivo, indent=2, ensure_ascii=False)
print("Archivo JSON creado exitosamente")

# 3. Leer datos desde JSON
print("\n--- Leyendo JSON ---")
with open('datos.json', 'r', encoding='utf-8') as archivo:
    datos_leidos = json.load(archivo)
    print("Datos leídos:")
    print(f"Nombre: {datos_leidos['nombre']}")
    print(f"Edad: {datos_leidos['edad']}")
    print(f"Hijos: {', '.join(datos_leidos['hijos'])}")
    print(f"Ciudad: {datos_leidos['direccion']['ciudad']}")

# 4. Trabajar con cadenas JSON
print("\n--- Convirtiendo a/desde cadena JSON ---")
cadena_json = json.dumps(datos, indent=2, ensure_ascii=False)
print("Cadena JSON:")
print(cadena_json[:100] + "...")

# Convertir cadena JSON a objeto Python
objeto_python = json.loads(cadena_json)
print(f"Objeto Python: {type(objeto_python)} - {objeto_python['nombre']}")

# 5. Guardar lista de diccionarios
print("\n--- Guardando lista de datos ---")
lista_datos = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "María", "edad": 28}
]

with open('lista.json', 'w', encoding='utf-8') as archivo:
    json.dump(lista_datos, archivo, indent=2, ensure_ascii=False)

# 6. Manejo de errores en JSON
print("\n--- Manejo de errores JSON ---")
try:
    with open('archivo_corrupto.json', 'r') as archivo:
        json.load(archivo)
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON: {e}")
except FileNotFoundError:
    print("Archivo no encontrado")

# 7. JSON con tipos de datos no estándar
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Función para serializar objetos personalizados
def serializar_persona(obj):
    if isinstance(obj, Persona):
        return {"__class__": "Persona", "nombre": obj.nombre, "edad": obj.edad}
    raise TypeError(f"Objeto de tipo {type(obj)} no serializable")

persona = Persona("Sofía", 32)
json_persona = json.dumps(persona, default=serializar_persona, indent=2)
print(f"\nPersona serializada:\n{json_persona}")
