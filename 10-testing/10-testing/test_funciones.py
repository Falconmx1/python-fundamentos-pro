# --- PRUEBAS CON PYTEST ---
# Para ejecutar: pytest test_funciones.py -v
# Instalar: pip install pytest

import pytest
import math

# 1. Funciones a probar
def es_primo(n):
    """Verifica si un número es primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factorial(n):
    """Calcula el factorial de un número."""
    if n < 0:
        raise ValueError("No existe factorial de números negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def contar_vocales(texto):
    """Cuenta las vocales en un texto."""
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    return sum(1 for c in texto if c in vocales)

# 2. Pruebas con pytest (funciones que comienzan con 'test_')
def test_es_primo():
    """Prueba la función es_primo."""
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(4) == False
    assert es_primo(17) == True
    assert es_primo(1) == False
    assert es_primo(0) == False
    assert es_primo(97) == True
    assert es_primo(100) == False

def test_factorial():
    """Prueba la función factorial."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    
    with pytest.raises(ValueError):
        factorial(-5)

def test_contar_vocales():
    """Prueba la función contar_vocales."""
    assert contar_vocales("hola") == 2
    assert contar_vocales("Python") == 1
    assert contar_vocales("") == 0
    assert contar_vocales("aeiou") == 5
    assert contar_vocales("Álvaro") == 3
    assert contar_vocales("12345") == 0

# 3. Pruebas parametrizadas con pytest
@pytest.mark.parametrize("entrada,esperado", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (11, True),
    (13, True),
    (15, False),
    (17, True),
])
def test_es_primo_parametrizado(entrada, esperado):
    """Prueba parametrizada para es_primo."""
    assert es_primo(entrada) == esperado

@pytest.mark.parametrize("entrada,esperado", [
    (0, 1),
    (1, 1),
    (5, 120),
    (10, 3628800),
])
def test_factorial_parametrizado(entrada, esperado):
    """Prueba parametrizada para factorial."""
    assert factorial(entrada) == esperado

# 4. Prueba con fixture
@pytest.fixture
def lista_numeros():
    """Fixture que proporciona una lista de números."""
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_primos_en_lista(lista_numeros):
    """Prueba con fixture."""
    for num in lista_numeros:
        assert es_primo(num) == True

# 5. Prueba que espera excepción
def test_factorial_negativo():
    """Prueba que factorial con número negativo lanza excepción."""
    with pytest.raises(ValueError, match="No existe factorial de números negativos"):
        factorial(-10)

# 6. Marcar pruebas con tags
@pytest.mark.rapida
def test_operacion_rapida():
    """Prueba marcada como rápida."""
    assert 1 + 1 == 2

@pytest.mark.lenta
def test_operacion_lenta():
    """Prueba marcada como lenta."""
    import time
    time.sleep(0.5)
    assert True

# 7. Saltar pruebas condicionalmente
@pytest.mark.skipif(True, reason="Prueba desactivada temporalmente")
def test_desactivada():
    assert False

# 8. Ejecutar pytest desde el código
if __name__ == "__main__":
    pytest.main(["-v", __file__])
