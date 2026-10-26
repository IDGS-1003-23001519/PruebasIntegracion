import unittest
from main import procesar_datos

class TestIntegration(unittest.TestCase):
    
    def test_integracion_try(self):
        try:
            resultado = procesar_datos(10)
            self.assertEqual(resultado, "Procesamiento exitoso: 20")
            print("Prueba de integración exitosa (try)")
        except Exception as e:
            self.fail(f"No debería haber lanzado excepción: {e}")

    def test_integracion_exception(self):
        try:
            procesar_datos(-5)
            self.fail("Debería haber lanzado una excepción")
        except ValueError as e:
            print(f"Excepción capturada correctamente en integración: {e}")
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()