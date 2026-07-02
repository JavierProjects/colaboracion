import unittest
from src.calificaciones import sumar_calificaciones

class TestSumarCalificaciones(unittest.TestCase):
    def test_suma_basica(self):
        self.assertEqual(sumar_calificaciones([80, 90, 70]), 240)

    def test_lista_vacia(self):
        self.assertEqual(sumar_calificaciones([]), 0)

if __name__ == "__main__":
    unittest.main()
