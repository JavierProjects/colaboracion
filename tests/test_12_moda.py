import unittest
from src.calificaciones import moda

class TestModa(unittest.TestCase):
    def test_moda_basica(self):
        self.assertEqual(moda([80, 90, 90, 70]), 90)

    def test_lista_vacia(self):
        self.assertIsNone(moda([]))

if __name__ == "__main__":
    unittest.main()
