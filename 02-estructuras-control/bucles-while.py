# --- BUCLE WHILE ---

# 1. Contador ascendente
contador = 0
print("Contador ascendente:")
while contador <= 5:
    print(contador, end=" ")
    contador += 1

# 2. Contador descendente
contador = 5
print("\n\nContador descendente:")
while contador >= 0:
    print(contador, end=" ")
    contador -= 1

# 3. Bucle con entrada del usuario (hasta que escriba "salir")
print("\n\nEscribe 'salir' para terminar:")
entrada = ""
while entrada != "salir":
    entrada = input("> ")
    print(f"Escribiste: {entrada}")
print("¡Bucle terminado!")

# 4. Bucle infinito (con break para salir)
print("\nBucle infinito controlado (escribe 'romper'):")
while True:
    comando = input("> ")
    if comando == "romper":
        print("Saliendo del bucle...")
        break
    print(f"Comando: {comando}")
