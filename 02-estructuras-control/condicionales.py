# --- ESTRUCTURAS CONDICIONALES (if, elif, else) ---

# 1. Condicional simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# 2. Condicional con elif
calificacion = 85
if calificacion >= 90:
    print("Calificación: Excelente")
elif calificacion >= 70:
    print("Calificación: Aprobado")
else:
    print("Calificación: Reprobado")

# 3. Condiciones anidadas
es_estudiante = True
tiene_beca = False
if es_estudiante:
    if tiene_beca:
        print("Eres estudiante con beca.")
    else:
        print("Eres estudiante sin beca.")
else:
    print("No eres estudiante.")

# 4. Operador ternario (condición en una línea)
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)
