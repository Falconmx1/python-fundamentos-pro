# --- MÉTODOS ESPECIALES (MAGIC METHODS / DUNDER METHODS) ---
# Son métodos con doble guión bajo al inicio y final (__init__, __str__, etc.)

# 1. Clase con varios métodos especiales
class Libro:
    def __init__(self, titulo, autor, paginas):
        """Constructor."""
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self._pagina_actual = 0
    
    # 2. __str__: Representación amigable para usuarios
    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.paginas} páginas)"
    
    # 3. __repr__: Representación para desarrolladores
    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"
    
    # 4. __len__: Devuelve la longitud (número de páginas)
    def __len__(self):
        return self.paginas
    
    # 5. __eq__: Comparación de igualdad
    def __eq__(self, otro):
        if not isinstance(otro, Libro):
            return False
        return self.titulo == otro.titulo and self.autor == otro.autor
    
    # 6. __lt__: Comparación menor que (para ordenar)
    def __lt__(self, otro):
        if not isinstance(otro, Libro):
            return NotImplemented
        return self.paginas < otro.paginas
    
    # 7. __getitem__ y __setitem__: Acceso como secuencia
    def __getitem__(self, indice):
        """Obtiene una página específica (simulada)."""
        if isinstance(indice, slice):
            # Manejar slices
            start, stop, step = indice.indices(self.paginas)
            return [f"Página {i}" for i in range(start, stop, step)]
        if 0 <= indice < self.paginas:
            return f"Página {indice + 1}"
        raise IndexError("Índice fuera de rango")
    
    # 8. __call__: Permite llamar al objeto como función
    def __call__(self, pagina):
        """Simula leer una página específica."""
        if 0 <= pagina < self.paginas:
            self._pagina_actual = pagina
            return f"Leyendo {self[pagina]}"
        return "Página no válida"
    
    # 9. __add__: Permite sumar objetos (combinar libros)
    def __add__(self, otro):
        if not isinstance(otro, Libro):
            return NotImplemented
        return Libro(
            f"{self.titulo} y {otro.titulo}",
            self.autor,
            self.paginas + otro.paginas
        )

# 10. Probar los métodos especiales
libro1 = Libro("Cien años de soledad", "García Márquez", 432)
libro2 = Libro("El amor en los tiempos del cólera", "García Márquez", 368)

print("--- Métodos especiales ---")
print(f"__str__: {str(libro1)}")
print(f"__repr__: {repr(libro1)}")
print(f"__len__: {len(libro1)} páginas")
print(f"__eq__: {libro1 == Libro('Cien años de soledad', 'García Márquez', 432)}")
print(f"__lt__: {libro1 < libro2} (¿libro1 tiene menos páginas que libro2?)")

print("\n--- __getitem__ y __call__ ---")
print(libro1[0])       # Página 1
print(libro1[5])       # Página 6
print(libro1[100:105]) # Slice de páginas
print(libro1(10))      # Llamar al objeto como función

print("\n--- __add__ ---")
libro3 = libro1 + libro2
print(f"Libro combinado: {libro3}")
print(f"Total de páginas: {len(libro3)}")

# 11. Otros métodos especiales útiles
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)
    
    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(f"\nVectores: {v1} + {v2} = {v1 + v2}")
print(f"Módulo de {v1}: {abs(v1)}")
print(f"{v1} * 3 = {v1 * 3}")
