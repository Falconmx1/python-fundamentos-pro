# --- ÁRBOLES BINARIOS ---
# Estructura de datos jerárquica donde cada nodo tiene hasta dos hijos.

# 1. Clase Nodo del árbol
class NodoArbol:
    """Representa un nodo en un árbol binario."""
    
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# 2. Clase Árbol Binario
class ArbolBinario:
    """Implementación de un árbol binario de búsqueda."""
    
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        """Inserta un valor en el árbol."""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        """Inserción recursiva en el árbol."""
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
        # Si es igual, no se inserta (evitar duplicados)
    
    def buscar(self, valor):
        """Busca un valor en el árbol."""
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        """Búsqueda recursiva en el árbol."""
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)
    
    def recorrido_inorden(self):
        """Recorrido inorden (izquierda - raíz - derecha)."""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        """Recorrido inorden recursivo."""
        if nodo:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, resultado)
    
    def recorrido_preorden(self):
        """Recorrido preorden (raíz - izquierda - derecha)."""
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _preorden_recursivo(self, nodo, resultado):
        """Recorrido preorden recursivo."""
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierda, resultado)
            self._preorden_recursivo(nodo.derecha, resultado)
    
    def recorrido_postorden(self):
        """Recorrido postorden (izquierda - derecha - raíz)."""
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _postorden_recursivo(self, nodo, resultado):
        """Recorrido postorden recursivo."""
        if nodo:
            self._postorden_recursivo(nodo.izquierda, resultado)
            self._postorden_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.valor)
    
    def altura(self):
        """Calcula la altura del árbol."""
        return self._altura_recursivo(self.raiz)
    
    def _altura_recursivo(self, nodo):
        """Calcula la altura recursivamente."""
        if nodo is None:
            return 0
        return 1 + max(self._altura_recursivo(nodo.izquierda),
                       self._altura_recursivo(nodo.derecha))
    
    def __str__(self):
        """Representación en cadena del árbol (inorden)."""
        return str(self.recorrido_inorden())

# 3. Ejemplos de uso
print("--- Árbol Binario de Búsqueda ---")
arbol = ArbolBinario()

# Insertar elementos
valores = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
print(f"Insertando: {valores}")
for valor in valores:
    arbol.insertar(valor)

# Recorridos
print(f"\nInorden: {arbol.recorrido_inorden()}")
print(f"Preorden: {arbol.recorrido_preorden()}")
print(f"Postorden: {arbol.recorrido_postorden()}")

# Búsqueda
print(f"\nBuscar 40: {arbol.buscar(40)}")
print(f"Buscar 99: {arbol.buscar(99)}")

# Altura del árbol
print(f"Altura del árbol: {arbol.altura()}")

# 4. Árbol con recorrido en niveles (BFS)
def recorrido_por_niveles(raiz):
    """Recorrido por niveles usando una cola."""
    if raiz is None:
        return []
    
    resultado = []
    cola = [raiz]
    
    while cola:
        nodo = cola.pop(0)
        resultado.append(nodo.valor)
        
        if nodo.izquierda:
            cola.append(nodo.izquierda)
        if nodo.derecha:
            cola.append(nodo.derecha)
    
    return resultado

print(f"\nRecorrido por niveles: {recorrido_por_niveles(arbol.raiz)}")

# 5. Mostrar árbol de forma jerárquica
def mostrar_arbol(nodo, nivel=0, prefijo="Raíz: "):
    """Muestra el árbol de forma jerárquica."""
    if nodo:
        print("  " * nivel + prefijo + str(nodo.valor))
        if nodo.izquierda or nodo.derecha:
            mostrar_arbol(nodo.izquierda, nivel + 1, "Izq: ")
            mostrar_arbol(nodo.derecha, nivel + 1, "Der: ")

print("\n--- Estructura del árbol ---")
mostrar_arbol(arbol.raiz)
