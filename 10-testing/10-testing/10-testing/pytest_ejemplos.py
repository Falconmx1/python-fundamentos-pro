# --- EJEMPLOS AVANZADOS CON PYTEST ---
# Para ejecutar: pytest pytest_ejemplos.py -v

import pytest
from unittest.mock import Mock, patch
import requests

# 1. Funciones que dependen de APIs externas
def obtener_clima(ciudad):
    """Obtiene el clima de una ciudad (simulado)."""
    # En realidad, esto haría una llamada a una API
    respuesta = requests.get(f"https://api.clima.com/{ciudad}")
    return respuesta.json()

# 2. Prueba con mock de requests
def test_obtener_clima():
    """Prueba con mock de la función requests.get."""
    # Crear un mock de la respuesta
    mock_response = Mock()
    mock_response.json.return_value = {"ciudad": "CDMX", "temperatura": 25}
    
    with patch('requests.get', return_value=mock_response):
        resultado = obtener_clima("CDMX")
        assert resultado["ciudad"] == "CDMX"
        assert resultado["temperatura"] == 25

# 3. Usar pytest-mock para mejor sintaxis
def test_obtener_clima_mock(mocker):
    """Prueba usando pytest-mock."""
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"ciudad": "GDL", "temperatura": 30}
    
    mocker.patch('requests.get', return_value=mock_response)
    resultado = obtener_clima("GDL")
    assert resultado["ciudad"] == "GDL"

# 4. Prueba de clase con setup/teardown
class TestBaseDatos:
    """Pruebas para una base de datos simulada."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Configuración antes de cada prueba."""
        self.db = {"usuarios": []}
        print("\n--- Configurando base de datos ---")
        yield
        print("--- Limpiando base de datos ---")
        self.db = None
    
    def test_agregar_usuario(self):
        self.db["usuarios"].append({"nombre": "Ana"})
        assert len(self.db["usuarios"]) == 1
    
    def test_eliminar_usuario(self):
        self.db["usuarios"].append({"nombre": "Luis"})
        self.db["usuarios"].pop()
        assert len(self.db["usuarios"]) == 0

# 5. Prueba con archivos temporales
def test_archivo_temporal(tmpdir):
    """Prueba usando un directorio temporal."""
    archivo = tmpdir.join("test.txt")
    archivo.write("Contenido de prueba")
    
    with open(archivo, 'r') as f:
        contenido = f.read()
    
    assert contenido == "Contenido de prueba"

# 6. Prueba de rendimiento (timeout)
@pytest.mark.timeout(1)
def test_operacion_rapida():
    """Prueba que debe completar en menos de 1 segundo."""
    import time
    time.sleep(0.1)  # Simular operación
    assert True

# 7. Pruebas con datos paramétricos complejos
@pytest.mark.parametrize("datos,esperado", [
    ({"a": 1, "b": 2}, 3),
    ({"a": 5, "b": 7}, 12),
    ({"a": -3, "b": 3}, 0),
])
def test_sumar_parametrico(datos, esperado):
    """Prueba con datos paramétricos."""
    def sumar(a, b):
        return a + b
    assert sumar(datos["a"], datos["b"]) == esperado

# 8. Usar pytest.raises para múltiples excepciones
def test_multiples_excepciones():
    """Prueba que lanza diferentes excepciones."""
    def funcion_con_error(opcion):
        if opcion == 1:
            raise ValueError("Error de valor")
        elif opcion == 2:
            raise TypeError("Error de tipo")
        return "OK"
    
    with pytest.raises(ValueError):
        funcion_con_error(1)
    
    with pytest.raises(TypeError):
        funcion_con_error(2)

# 9. Ejecutar pruebas específicas
if __name__ == "__main__":
    # Ejecutar todas las pruebas
    pytest.main(["-v", "--tb=short", __file__])
