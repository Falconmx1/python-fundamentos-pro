from flask import Flask, jsonify, request

# --- FÁCIL: Servidor básico ---
app = Flask(__name__)

@app.route('/')
def inicio():
    return "¡Hola, mundo! Esta es una API con Flask."

# --- MEDIO: Endpoint con parámetros ---
@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f"¡Hola, {nombre}!"

# --- DIFÍCIL: API REST con métodos POST y GET ---
usuarios = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Luis"}
]

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    nuevo_usuario = request.get_json()
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

# --- Instrucciones para ejecutar ---
if __name__ == '__main__':
    print("=== FLASK - EJEMPLOS ===")
    print("Para ejecutar este servidor, guarda el archivo y corre:")
    print("flask --app flask_ejemplos run")
    print("o en su defecto, usa: python -m flask --app flask_ejemplos run")
    # app.run(debug=True) # Descomenta para ejecutar directamente
