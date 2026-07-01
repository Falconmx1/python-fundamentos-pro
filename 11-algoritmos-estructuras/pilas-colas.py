# --- PILAS (STACK) Y COLAS (QUEUE) ---

# 1. PILA (Stack) - LIFO (Last In, First Out)
class Pila:
    """Implementación de una pila usando lista."""
    
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("No se puede desapilar de una pila vacía")
        return self.items.pop()
    
    def cima(self):
        if self.esta_vacia():
            return None
        return self.items[-1]
    
    def tamaño(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# 2. COLA (Queue) - FIFO (First In, First Out)
class Cola:
    """Implementación de una cola usando lista."""
    
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("No se puede desencolar de una cola vacía")
        return self.items.pop(0)
    
    def frente(self):
        if self.esta_vacia():
            return None
        return self.items[0]
    
    def tamaño(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# 3. COLA CON PRIORIDAD (Priority Queue)
class ColaPrioridad:
    """Implementación simple de cola con prioridad usando lista de tuplas."""
    
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def encolar(self, item, prioridad):
        """Encola un elemento con su prioridad (menor número = mayor prioridad)."""
        self.items.append((prioridad, item))
        # Ordenar por prioridad (menor primero)
        self.items.sort(key=lambda x: x[0])
    
    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("Cola de prioridad vacía")
        return self.items.pop(0)[1]  # Retorna solo el item, no la prioridad
    
    def __str__(self):
        return str(self.items)

# 4. Ejemplos de uso
print("--- PILA (Stack) ---")
pila = Pila()
print("Apilando 1, 2, 3, 4, 5")
for i in range(1, 6):
    pila.apilar(i)
print(f"Pila: {pila}")
print(f"Cima: {pila.cima()}")
print(f"Tamaño: {pila.tamaño()}")

print("Desapilando elementos:")
while not pila.esta_vacia():
    print(pila.desapilar(), end=" ")
print()

print("\n--- COLA (Queue) ---")
cola = Cola()
print("Encolando A, B, C, D, E")
for letra in ['A', 'B', 'C', 'D', 'E']:
    cola.encolar(letra)
print(f"Cola: {cola}")
print(f"Frente: {cola.frente()}")
print(f"Tamaño: {cola.tamaño()}")

print("Desencolando elementos:")
while not cola.esta_vacia():
    print(cola.desencolar(), end=" ")
print()

print("\n--- COLA CON PRIORIDAD ---")
cp = ColaPrioridad()
print("Encolando tareas con prioridad:")
cp.encolar("Tarea urgente", 1)
cp.encolar("Tarea normal", 3)
cp.encolar("Tarea importante", 2)
print(f"Cola de prioridad: {cp}")

print("Procesando tareas por prioridad:")
while not cp.esta_vacia():
    print(f"Procesando: {cp.desencolar()}")
