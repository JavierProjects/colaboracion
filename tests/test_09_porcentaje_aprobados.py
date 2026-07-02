import unittest
from src.calificaciones import porcentaje_aprobados

class TestPorcentajeAprobados(unittest.TestCase):
    def test_porcentaje_basico(self):
        self.assertAlmostEqual(porcentaje_aprobados([100, 70, 65, 80]), 75.0)

    def test_lista_vacia(self):
        self.assertEqual(porcentaje_aprobados([]), 0.0)

if __name__ == "__main__":
    unittest.main()
