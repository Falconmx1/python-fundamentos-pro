# --- BUCLE FOR ---

# 1. Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
print("Frutas:")
for fruta in frutas:
    print("-", fruta)

# 2. Usar range() para números
print("\nNúmeros del 0 al 4:")
for i in range(5):
    print(i, end=" ")  # end=" " evita el salto de línea

print("\n\nNúmeros del 2 al 8 (de 2 en 2):")
for i in range(2, 9, 2):
    print(i, end=" ")

# 3. Iterar sobre un string
texto = "Python"
print("\n\nLetras de 'Python':")
for letra in texto:
    print(letra, end=" ")

# 4. Usar enumerate() para obtener índice y valor
colores = ["rojo", "verde", "azul"]
print("\n\nColores con índice:")
for indice, color in enumerate(colores):
    print(f"Índice {indice}: {color}")
