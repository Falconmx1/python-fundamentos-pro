# --- ITERADORES ---
# Los iteradores son objetos que implementan los métodos __iter__ y __next__.

# 1. Iterador personalizado
class Contador:
    """Iterador que cuenta desde un valor inicial hasta un límite."""
    
    def __init__(self, inicio, limite):
        self.actual = inicio
        self.limite = limite
    
    def __iter__(self):
        """Devuelve el iterador (a sí mismo)."""
        return self
    
    def __next__(self):
        """Devuelve el siguiente valor."""
        if self.actual >= self.limite:
            raise StopIteration
        valor = self.actual
        self.actual += 1
        return valor

print("--- Iterador personalizado ---")
contador = Contador(5, 10)
for num in contador:
    print(num, end=" ")
print()

# 2. Iterador para secuencia Fibonacci
class FibonnaciIterator:
    """Iterador de números de Fibonacci."""
    
    def __init__(self, limite):
        self.limite = limite
        self.a, self.b = 0, 1
        self.contador = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.contador >= self.limite:
            raise StopIteration
        valor = self.a
        self.a, self.b = self.b, self.a + self.b
        self.contador += 1
        return valor

print("\n--- Fibonacci Iterator ---")
fib = FibonnaciIterator(10)
for num in fib:
    print(num, end=" ")
print()

# 3. Iterador para lista invertida
class ListaInversa:
    """Iterador que recorre una lista en orden inverso."""
    
    def __init__(self, lista):
        self.lista = lista
        self.indice = len(lista) - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice < 0:
            raise StopIteration
        valor = self.lista[self.indice]
        self.indice -= 1
        return valor

print("\n--- Lista inversa ---")
lista = [1, 2, 3, 4, 5]
inversa = ListaInversa(lista)
for item in inversa:
    print(item, end=" ")
print()

# 4. Verificar si un objeto es iterable
print("\n--- Verificación de iterables ---")
print(f"¿Lista es iterable? {hasattr(lista, '__iter__')}")
print(f"¿Número es iterable? {hasattr(5, '__iter__')}")
print(f"¿String es iterable? {hasattr("hola", '__iter__')}")

# 5. Convertir iterador a lista
print("\n--- Convertir iterador a lista ---")
rango_iter = iter(range(5))
lista_rango = list(rango_iter)
print(f"Lista: {lista_rango}")
