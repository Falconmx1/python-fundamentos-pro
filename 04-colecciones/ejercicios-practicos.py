# --- EJERCICIOS PRÁCTICOS (Colecciones) ---

# Ejercicio 1: Lista de números pares
print("=== EJERCICIO 1 ===")
def numeros_pares(limite):
    """Devuelve una lista con los números pares hasta el límite."""
    # Usa una comprensión de lista
    pass

# Prueba
# print(numeros_pares(20))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Ejercicio 2: Diccionario inverso
print("\n=== EJERCICIO 2 ===")
def invertir_diccionario(diccionario):
    """Invierte las claves y valores de un diccionario."""
    # Nota: los valores deben ser únicos o se perderán datos
    pass

# Prueba
# original = {"a": 1, "b": 2, "c": 3}
# print(invertir_diccionario(original))  # {1: 'a', 2: 'b', 3: 'c'}

# Ejercicio 3: Elementos comunes en listas
print("\n=== EJERCICIO 3 ===")
def elementos_comunes(lista1, lista2):
    """Devuelve una lista con los elementos comunes entre dos listas."""
    pass

# Prueba
# print(elementos_comunes([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]

# Ejercicio 4: Palabra más frecuente
print("\n=== EJERCICIO 4 ===")
def palabra_mas_frecuente(texto):
    """Devuelve la palabra más frecuente en un texto y su conteo."""
    # Puedes usar un diccionario para contar
    pass

# Prueba
# texto = "python es genial python es poderoso python"
# print(palabra_mas_frecuente(texto))  # ('python', 3)

# Ejercicio 5: Matriz transpuesta
print("\n=== EJERCICIO 5 ===")
def transponer_matriz(matriz):
    """Devuelve la transpuesta de una matriz (lista de listas)."""
    pass

# Prueba
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(transponer_matriz(matriz))
# # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Ejercicio 6: Agenda telefónica con diccionarios
print("\n=== EJERCICIO 6 ===")
def agenda():
    """Simula una agenda telefónica con operaciones básicas."""
    contactos = {}
    while True:
        print("\n--- Agenda ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Listar contactos")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            # Tu código
            pass
        elif opcion == '2':
            # Tu código
            pass
        elif opcion == '3':
            # Tu código
            pass
        elif opcion == '4':
            # Tu código
            pass
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

# Para probar, descomenta la siguiente línea:
# agenda()
