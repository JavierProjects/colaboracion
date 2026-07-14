import unittest
from src.asistencias import contar_clases

class TestContarClases(unittest.TestCase):
    def test_contar_clases(self):
        self.assertEqual(contar_clases([1, 1, 0, 1]), 4)

    def test_lista_vacia(self):
        self.assertEqual(contar_clases([]), 0)

if __name__ == "__main__":
    unittest.main()
