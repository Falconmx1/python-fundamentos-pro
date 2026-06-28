# --- OPERADORES EN PYTHON ---

# 1. Aritméticos: +, -, *, /, // (división entera), % (módulo), ** (potencia)
a, b = 10, 3
print(f"{a} + {b} =", a + b)
print(f"{a} - {b} =", a - b)
print(f"{a} * {b} =", a * b)
print(f"{a} / {b} =", a / b)       # División flotante
print(f"{a} // {b} =", a // b)     # División entera
print(f"{a} % {b} =", a % b)       # Resto de la división
print(f"{a} ** {b} =", a ** b)     # Potencia

# 2. Comparación: ==, !=, <, >, <=, >=
x, y = 5, 7
print(f"\n{x} == {y}:", x == y)
print(f"{x} != {y}:", x != y)
print(f"{x} < {y}:", x < y)
print(f"{x} > {y}:", x > y)
print(f"{x} <= {y}:", x <= y)
print(f"{x} >= {y}:", x >= y)

# 3. Lógicos: and, or, not
verdad = True
falso = False
print(f"\n{verdad} and {falso}:", verdad and falso)
print(f"{verdad} or {falso}:", verdad or falso)
print(f"not {verdad}:", not verdad)

# 4. Asignación: =, +=, -=, *=, etc.
contador = 0
contador += 5   # contador = contador + 5
print("\nContador después de += 5:", contador)
