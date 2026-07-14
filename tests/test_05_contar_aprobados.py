import unittest
from src.calificaciones import contar_aprobados

class TestContarAprobados(unittest.TestCase):
    def test_aprobados_basico(self):
        self.assertEqual(contar_aprobados([100, 70, 65, 80]), 3)

    def test_sin_aprobados(self):
        self.assertEqual(contar_aprobados([50, 60]), 0)

if __name__ == "__main__":
    unittest.main()
