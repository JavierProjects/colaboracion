import unittest
from src.asistencias import contar_faltas

class TestContarFaltas(unittest.TestCase):
    def test_contar_faltas(self):
        self.assertEqual(contar_faltas([1, 1, 0, 1]), 1)

    def test_sin_faltas(self):
        self.assertEqual(contar_faltas([1, 1]), 0)

if __name__ == "__main__":
    unittest.main()
