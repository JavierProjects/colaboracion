import unittest
from src.calificaciones import mediana

class TestMediana(unittest.TestCase):
    def test_mediana_impar(self):
        self.assertEqual(mediana([70, 80, 90]), 80)

    def test_mediana_par(self):
        self.assertAlmostEqual(mediana([70, 80, 90, 100]), 85.0)

    def test_lista_desordenada(self):
        self.assertEqual(mediana([90, 70, 80]), 80)

    def test_lista_vacia(self):
        self.assertIsNone(mediana([]))

if __name__ == "__main__":
    unittest.main()
