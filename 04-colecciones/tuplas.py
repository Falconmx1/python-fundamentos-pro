# --- TUPLAS ---
# Son colecciones ordenadas pero INMUTABLES (no se pueden modificar).

# 1. Creación de tuplas
tupla_vacia = ()
tupla_un_elemento = (5,)   # ¡Importante la coma!
coordenadas = (10, 20)
persona = ("Ana", 30, "Ingeniera")
print(f"Tupla persona: {persona}")

# 2. Acceso a elementos (igual que las listas)
print(f"Nombre: {persona[0]}")
print(f"Edad: {persona[1]}")
print(f"Profesión: {persona[2]}")

# 3. Desempaquetado de tuplas
nombre, edad, profesion = persona
print(f"Desempaquetado: {nombre}, {edad}, {profesion}")

# 4. Métodos de tuplas
tupla_numeros = (1, 2, 3, 2, 4, 2)
print(f"Conteo de 2: {tupla_numeros.count(2)}")  # 3
print(f"Índice del 3: {tupla_numeros.index(3)}")  # 2

# 5. Tuplas vs listas
# Las tuplas son más rápidas y usan menos memoria.
# Se usan para datos que no deben cambiar.
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print(f"Días de la semana: {dias_semana}")

# 6. Recorrer una tupla
print("Recorrido de días:")
for dia in dias_semana:
    print(dia)
