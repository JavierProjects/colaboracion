import unittest
from src.calificaciones import calificacion_maxima

class TestCalificacionMaxima(unittest.TestCase):
    def test_maxima_basica(self):
        self.assertEqual(calificacion_maxima([80, 90, 70]), 90)

    def test_lista_vacia(self):
        self.assertIsNone(calificacion_maxima([]))

if __name__ == "__main__":
    unittest.main()
