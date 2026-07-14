import unittest
from src.asistencias import esta_en_riesgo

class TestEstaEnRiesgo(unittest.TestCase):
    def test_en_riesgo(self):
        self.assertTrue(esta_en_riesgo([1, 1, 0, 1]))

    def test_no_en_riesgo(self):
        self.assertFalse(esta_en_riesgo([1, 1, 1, 1]))

if __name__ == "__main__":
    unittest.main()
