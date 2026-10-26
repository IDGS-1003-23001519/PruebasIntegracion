import unittest
from main import procesar_datos

class TestSystem(unittest.TestCase):
    
    def test_sistema_try(self):
        try:
            resultado = procesar_datos(50)
            self.assertIn("Procesamiento exitoso", resultado)
            print("Prueba de sistema exitosa (try)")
        except Exception as e:
            self.fail(f"Error inesperado en el sistema: {e}")

    def test_sistema_exception(self):
        try:
            procesar_datos(-100)
            self.fail("El sistema debió bloquear el valor negativo")
        except ValueError as e:
            print(f"Excepción controlada correctamente en sistema: {e}")
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()