import unittest
from src.calificaciones import promedio

class TestPromedio(unittest.TestCase):
    def test_promedio_basico(self):
        self.assertAlmostEqual(promedio([80, 90, 70]), 80.0)

    def test_lista_vacia(self):
        self.assertIsNone(promedio([]))

if __name__ == "__main__":
    unittest.main()
