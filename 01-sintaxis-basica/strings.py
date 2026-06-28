# --- MANEJO DE CADENAS (STRINGS) ---

texto = "  Python es poderoso  "

# 1. Métodos básicos
print("Original:", texto)
print("Minúsculas:", texto.lower())
print("Mayúsculas:", texto.upper())
print("Eliminar espacios:", texto.strip())
print("Reemplazar:", texto.replace("poderoso", "increíble"))

# 2. División y unión
palabras = texto.strip().split()  # Convierte en lista
print("Dividir en palabras:", palabras)
union = "-".join(palabras)        # Une elementos con "-"
print("Unir con guiones:", union)

# 3. Formateo de strings
nombre = "Luis"
edad = 28
# f-strings (recomendado)
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje)
# Método .format()
mensaje2 = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)
print(mensaje2)

# 4. Subcadenas
frase = "Aprendiendo Python"
print("Primeros 10 caracteres:", frase[:10])
print("Desde el carácter 11:", frase[11:])
print("Últimos 6 caracteres:", frase[-6:])
print("Invertir cadena:", frase[::-1])
