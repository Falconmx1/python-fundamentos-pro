# --- PRUEBAS UNITARIAS CON UNITTEST ---
import unittest
import math

# 1. Función a probar
class Calculadora:
    """Calculadora básica con operaciones matemáticas."""
    
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def restar(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b
    
    @staticmethod
    def potencia(a, b):
        return a ** b
    
    @staticmethod
    def raiz_cuadrada(a):
        if a < 0:
            raise ValueError("No se puede calcular raíz de número negativo")
        return math.sqrt(a)

# 2. Clase de pruebas
class TestCalculadora(unittest.TestCase):
    """Pruebas para la clase Calculadora."""
    
    # Configuración antes de cada prueba
    def setUp(self):
        """Se ejecuta antes de cada prueba."""
        self.calc = Calculadora()
        print(f"\nEjecutando prueba: {self._testMethodName}")
    
    # Limpieza después de cada prueba
    def tearDown(self):
        """Se ejecuta después de cada prueba."""
        print("Prueba completada")
    
    # 3. Métodos de prueba (deben comenzar con 'test_')
    def test_sumar(self):
        """Prueba la suma de números."""
        self.assertEqual(self.calc.sumar(3, 5), 8)
        self.assertEqual(self.calc.sumar(-1, 1), 0)
        self.assertEqual(self.calc.sumar(0, 0), 0)
        self.assertEqual(self.calc.sumar(2.5, 3.5), 6.0)
    
    def test_restar(self):
        """Prueba la resta de números."""
        self.assertEqual(self.calc.restar(10, 5), 5)
        self.assertEqual(self.calc.restar(5, 10), -5)
        self.assertEqual(self.calc.restar(0, 5), -5)
    
    def test_multiplicar(self):
        """Prueba la multiplicación de números."""
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        self.assertEqual(self.calc.multiplicar(0, 10), 0)
    
    def test_dividir(self):
        """Prueba la división de números."""
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(7, 2), 3.5)
        self.assertEqual(self.calc.dividir(-6, 3), -2)
        
        # Verificar que se lanza una excepción
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)
    
    def test_potencia(self):
        """Prueba la potencia de números."""
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)
        self.assertEqual(self.calc.potencia(2, -1), 0.5)
    
    def test_raiz_cuadrada(self):
        """Prueba la raíz cuadrada."""
        self.assertEqual(self.calc.raiz_cuadrada(16), 4)
        self.assertEqual(self.calc.raiz_cuadrada(2), math.sqrt(2))
        
        with self.assertRaises(ValueError):
            self.calc.raiz_cuadrada(-4)
    
    # 4. Pruebas con diferentes tipos de assert
    def test_comparaciones(self):
        """Prueba diferentes tipos de aserciones."""
        a = 10
        b = 10
        c = 15
        
        self.assertIs(a, b)  # Mismo objeto
        self.assertIsNot(a, c)  # Diferentes objetos
        self.assertTrue(a < c)
        self.assertFalse(a > c)
        self.assertIn(2, [1, 2, 3])
        self.assertNotIn(5, [1, 2, 3])
    
    # 5. Prueba con parámetros (usando subTest)
    def test_sumar_multiples(self):
        """Prueba múltiples casos con subTest."""
        casos = [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
            (2.5, 3.5, 6.0)
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.sumar(a, b), esperado)

# 6. Clase para pruebas de tipos
class TestTipos(unittest.TestCase):
    """Pruebas relacionadas con tipos de datos."""
    
    def test_tipos(self):
        """Verifica los tipos de retorno."""
        calc = Calculadora()
        self.assertIsInstance(calc.sumar(3, 4), int)
        self.assertIsInstance(calc.dividir(10, 3), float)
        self.assertIsInstance(calc.potencia(2, 3), int)

# 7. Ejecutar las pruebas
if __name__ == '__main__':
    # Ejecutar todas las pruebas
    unittest.main()
    
    # Ejecutar pruebas específicas
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculadora)
    # unittest.TextTestRunner().run(suite)
