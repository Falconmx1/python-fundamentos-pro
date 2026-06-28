# --- ENTRADA Y SALIDA DE DATOS ---

# 1. Salida básica con print()
print("Hola, este es un mensaje.")

# 2. Entrada del usuario con input()
nombre = input("¿Cómo te llamas? ")
print(f"¡Mucho gusto, {nombre}!")

# 3. Leer números (input siempre devuelve string)
edad_str = input("¿Cuántos años tienes? ")
edad = int(edad_str)  # Convertir a entero
print(f"El año que viene tendrás {edad + 1} años.")

# 4. Leer números flotantes
altura_str = input("¿Cuál es tu altura en metros? ")
altura = float(altura_str)
print(f"Mides {altura} metros.")

# 5. Múltiples valores en print()
print("Nombre:", nombre, "Edad:", edad, "Altura:", altura)
