# --- BREAK Y CONTINUE ---

# 1. break: termina el bucle por completo
print("Bucle con break (se detiene en el número 5):")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")

# 2. continue: salta a la siguiente iteración
print("\n\nBucle con continue (salta el número 5):")
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")

# 3. Ejemplo combinado: encontrar el primer múltiplo de 7
print("\n\nBuscando el primer múltiplo de 7 en una lista:")
numeros = [3, 11, 14, 22, 28, 35]
for num in numeros:
    if num % 7 == 0:
        print(f"El primer múltiplo de 7 es: {num}")
        break
else:
    print("No se encontró ningún múltiplo de 7.")
# El else se ejecuta si el bucle no se rompió con break

# 4. continue para filtrar elementos
print("\nMostrando solo números pares del 0 al 9:")
for i in range(10):
    if i % 2 != 0:  # Si es impar
        continue    # Salta la impresión
    print(i, end=" ")
