import unittest
from src.asistencias import contar_asistencias

class TestContarAsistencias(unittest.TestCase):
    def test_contar_asistencias(self):
        self.assertEqual(contar_asistencias([1, 1, 0, 1]), 3)

    def test_sin_asistencias(self):
        self.assertEqual(contar_asistencias([0, 0]), 0)

if __name__ == "__main__":
    unittest.main()
