import unittest
from src.asistencias import porcentaje_asistencia

class TestPorcentajeAsistencia(unittest.TestCase):
    def test_porcentaje_basico(self):
        self.assertAlmostEqual(porcentaje_asistencia([1, 1, 0, 1]), 75.0)

    def test_lista_vacia(self):
        self.assertEqual(porcentaje_asistencia([]), 0.0)

if __name__ == "__main__":
    unittest.main()
