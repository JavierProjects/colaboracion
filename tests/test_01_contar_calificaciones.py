import unittest
from src.calificaciones import contar_calificaciones

class TestContarCalificaciones(unittest.TestCase):
    def test_lista_con_calificaciones(self):
        self.assertEqual(contar_calificaciones([80, 90, 70]), 3)

    def test_lista_vacia(self):
        self.assertEqual(contar_calificaciones([]), 0)

if __name__ == "__main__":
    unittest.main()
