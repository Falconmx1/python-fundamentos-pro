# --- SCOPE (ÁMBITO) DE VARIABLES ---

# 1. Variable global (definida fuera de cualquier función)
mensaje_global = "Soy global"

def funcion_local():
    # 2. Variable local (solo existe dentro de esta función)
    mensaje_local = "Soy local"
    print(mensaje_global)  # Puedo leer la variable global
    print(mensaje_local)

funcion_local()
# print(mensaje_local)  # ¡Esto daría error! (fuera de su ámbito)

# 3. Modificar una variable global desde una función
contador = 0

def incrementar():
    global contador  # Indicamos que usaremos la variable global
    contador += 1
    print(f"Contador dentro de la función: {contador}")

incrementar()
incrementar()
print(f"Contador fuera de la función: {contador}")

# 4. Scope en funciones anidadas (nonlocal)
def funcion_externa():
    variable_externa = "Valor externo"
    
    def funcion_interna():
        nonlocal variable_externa  # Modifica la variable de la función externa
        variable_externa = "Valor modificado"
        print(f"Desde interna: {variable_externa}")
    
    funcion_interna()
    print(f"Desde externa después de modificar: {variable_externa}")

funcion_externa()

# 5. Regla LEGB (Local, Enclosing, Global, Built-in)
x = "global"
def prueba_legb():
    x = "enclosing"
    def interna():
        x = "local"
        print(f"Local: {x}")
    interna()
    print(f"Enclosing: {x}")
prueba_legb()
print(f"Global: {x}")
