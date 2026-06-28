import pandas as pd

# --- FÁCIL: Crear y leer datos ---
print("=== PANDAS - NIVEL FÁCIL ===")
data = {'Nombre': ['Ana', 'Luis', 'María'], 'Edad': [25, 30, 28]}
df = pd.DataFrame(data)
print("DataFrame creado:")
print(df)

# --- MEDIO: Análisis y filtrado ---
print("\n=== PANDAS - NIVEL MEDIO ===")
# Añadir una columna
df['Ciudad'] = ['CDMX', 'GDL', 'MTY']
print("\nDataFrame con nueva columna:")
print(df)

# Filtrar por edad
mayores_25 = df[df['Edad'] > 25]
print("\nPersonas mayores de 25:")
print(mayores_25)

# --- DIFÍCIL: Agrupación y agregación ---
print("\n=== PANDAS - NIVEL DIFÍCIL ===")
# Datos de ventas
ventas_data = {
    'Producto': ['A', 'A', 'B', 'B', 'C'],
    'Ventas': [100, 150, 200, 250, 300]
}
ventas_df = pd.DataFrame(ventas_data)
print("\nDatos de ventas:")
print(ventas_df)

# Agrupar por producto y calcular media
ventas_agrupadas = ventas_df.groupby('Producto')['Ventas'].mean()
print("\nVentas promedio por producto:")
print(ventas_agrupadas)
