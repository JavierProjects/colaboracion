import unittest
from src.calificaciones import frecuencia_calificaciones

class TestFrecuenciaCalificaciones(unittest.TestCase):
    def test_frecuencia_basica(self):
        self.assertEqual(
            frecuencia_calificaciones([80, 80, 90, 70, 90, 90]),
            {80: 2, 90: 3, 70: 1}
        )

    def test_lista_vacia(self):
        self.assertEqual(frecuencia_calificaciones([]), {})

if __name__ == "__main__":
    unittest.main()
