import unittest
from src.calificaciones import contar_reprobados

class TestContarReprobados(unittest.TestCase):
    def test_reprobados_basico(self):
        self.assertEqual(contar_reprobados([100, 70, 65, 80]), 1)

    def test_sin_reprobados(self):
        self.assertEqual(contar_reprobados([80, 90]), 0)

if __name__ == "__main__":
    unittest.main()
