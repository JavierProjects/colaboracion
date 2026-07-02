import unittest
from src.calificaciones import clasificar_calificacion

class TestClasificarCalificacion(unittest.TestCase):
    def test_excelente(self):
        self.assertEqual(clasificar_calificacion(95), "Excelente")

    def test_bueno(self):
        self.assertEqual(clasificar_calificacion(85), "Bueno")

    def test_regular(self):
        self.assertEqual(clasificar_calificacion(75), "Regular")

    def test_reprobado(self):
        self.assertEqual(clasificar_calificacion(60), "Reprobado")

    def test_limites(self):
        self.assertEqual(clasificar_calificacion(90), "Excelente")
        self.assertEqual(clasificar_calificacion(80), "Bueno")
        self.assertEqual(clasificar_calificacion(70), "Regular")
        self.assertEqual(clasificar_calificacion(69), "Reprobado")

if __name__ == "__main__":
    unittest.main()
