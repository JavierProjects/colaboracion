import unittest
from src.calificaciones import porcentaje_reprobados

class TestPorcentajeReprobados(unittest.TestCase):
    def test_porcentaje_basico(self):
        self.assertAlmostEqual(porcentaje_reprobados([100, 70, 65, 80]), 25.0)

    def test_lista_vacia(self):
        self.assertEqual(porcentaje_reprobados([]), 0.0)

if __name__ == "__main__":
    unittest.main()
