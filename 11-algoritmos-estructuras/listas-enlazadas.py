# --- LISTAS ENLAZADAS ---
# Estructura de datos lineal donde cada elemento apunta al siguiente.

# 1. Clase Nodo
class Nodo:
    """Representa un nodo en una lista enlazada."""
    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# 2. Clase Lista Enlazada
class ListaEnlazada:
    """Implementación de una lista enlazada simple."""
    
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0
    
    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.cabeza is None
    
    def obtener_tamaño(self):
        """Retorna el número de elementos en la lista."""
        return self.tamaño
    
    def agregar_al_final(self, dato):
        """Agrega un elemento al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamaño += 1
    
    def agregar_al_inicio(self, dato):
        """Agrega un elemento al inicio de la lista."""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamaño += 1
    
    def insertar_en_posicion(self, dato, posicion):
        """Inserta un elemento en una posición específica."""
        if posicion < 0 or posicion > self.tamaño:
            raise IndexError("Posición fuera de rango")
        
        if posicion == 0:
            self.agregar_al_inicio(dato)
            return
        
        if posicion == self.tamaño:
            self.agregar_al_final(dato)
            return
        
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        for _ in range(posicion - 1):
            actual = actual.siguiente
        
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        self.tamaño += 1
    
    def eliminar(self, dato):
        """Elimina la primera ocurrencia del dato en la lista."""
        if self.esta_vacia():
            return False
        
        # Si el dato está en la cabeza
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
        
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            self.tamaño -= 1
            return True
        
        return False
    
    def buscar(self, dato):
        """Busca un dato en la lista y retorna su posición."""
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1
    
    def obtener(self, posicion):
        """Retorna el dato en la posición especificada."""
        if posicion < 0 or posicion >= self.tamaño:
            raise IndexError("Posición fuera de rango")
        
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        return actual.dato
    
    def __str__(self):
        """Representación en cadena de la lista."""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos) + " -> None"

# 3. Ejemplos de uso
print("--- Lista Enlazada ---")
lista = ListaEnlazada()

# Agregar elementos
print("Agregando elementos al final...")
for i in range(5):
    lista.agregar_al_final(i)
print(f"Lista: {lista}")
print(f"Tamaño: {lista.obtener_tamaño()}")

# Agregar al inicio
print("\nAgregando al inicio...")
lista.agregar_al_inicio(99)
print(f"Lista: {lista}")

# Insertar en posición
print("\nInsertando en posición 2...")
lista.insertar_en_posicion(77, 2)
print(f"Lista: {lista}")

# Buscar elementos
print(f"\nBuscar 77: posición {lista.buscar(77)}")
print(f"Buscar 99: posición {lista.buscar(99)}")
print(f"Buscar 5: posición {lista.buscar(5)}")

# Obtener por posición
print(f"\nElemento en posición 3: {lista.obtener(3)}")

# Eliminar elementos
print("\nEliminando 77...")
lista.eliminar(77)
print(f"Lista: {lista}")

print("Eliminando 99...")
lista.eliminar(99)
print(f"Lista: {lista}")

print(f"Tamaño final: {lista.obtener_tamaño()}")
