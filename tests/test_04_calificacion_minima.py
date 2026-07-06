import unittest
from src.calificaciones import calificacion_minima

class TestCalificacionMinima(unittest.TestCase):
    def test_minima_basica(self):
        self.assertEqual(calificacion_minima([80, 90, 70]), 70)

    def test_lista_vacia(self):
        self.assertIsNone(calificacion_minima([]))

if __name__ == "__main__":
    unittest.main()
