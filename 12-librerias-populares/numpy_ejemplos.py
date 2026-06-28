import numpy as np

# --- FÁCIL: Creación y operaciones básicas ---
print("=== NUMPY - NIVEL FÁCIL ===")
# Crear un array
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Suma: {arr.sum()}")
print(f"Promedio: {arr.mean()}")

# --- MEDIO: Operaciones con matrices ---
print("\n=== NUMPY - NIVEL MEDIO ===")
matriz = np.array([[1, 2], [3, 4]])
print(f"Matriz:\n{matriz}")
print(f"Transpuesta:\n{matriz.T}")
print(f"Determinante: {np.linalg.det(matriz)}")

# --- DIFÍCIL: Álgebra lineal y broadcasting ---
print("\n=== NUMPY - NIVEL DIFÍCIL ===")
# Resolver sistema de ecuaciones: 3x + y = 9, x + 2y = 8
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
solucion = np.linalg.solve(A, b)
print(f"Solución del sistema: x={solucion[0]}, y={solucion[1]}")
