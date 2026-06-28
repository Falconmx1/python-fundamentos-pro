# --- EJERCICIOS PRÁCTICOS (Estructuras de Control) ---
# Intenta resolverlos antes de ver las soluciones.

# Ejercicio 1: Número par o impar
print("=== EJERCICIO 1 ===")
numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")

# Ejercicio 2: Tabla de multiplicar
print("\n=== EJERCICIO 2 ===")
num = int(input("Ingresa un número para ver su tabla de multiplicar: "))
print(f"Tabla del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Ejercicio 3: Suma de números hasta que el usuario decida
print("\n=== EJERCICIO 3 ===")
total = 0
while True:
    opcion = input("¿Quieres agregar un número? (s/n): ")
    if opcion.lower() != 's':
        break
    valor = float(input("Ingresa el número: "))
    total += valor
    print(f"Suma parcial: {total}")
print(f"Suma total: {total}")

# Ejercicio 4: Números primos en un rango
print("\n=== EJERCICIO 4 ===")
inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))
print(f"Números primos entre {inicio} y {fin}:")
for num in range(inicio, fin + 1):
    if num > 1:
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num, end=" ")
