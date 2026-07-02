import unittest
from src.asistencias import alumnos_en_riesgo

class TestAlumnosEnRiesgo(unittest.TestCase):
    def test_alumnos_en_riesgo(self):
        asistencias = {
            "Ana": [1, 1, 1, 1],
            "Luis": [1, 0, 0, 1],
            "María": [1, 1, 1, 0]
        }
        self.assertEqual(alumnos_en_riesgo(asistencias), ["Luis", "María"])

    def test_sin_alumnos_en_riesgo(self):
        asistencias = {
            "Ana": [1, 1, 1, 1],
            "Luis": [1, 1, 1, 1]
        }
        self.assertEqual(alumnos_en_riesgo(asistencias), [])

if __name__ == "__main__":
    unittest.main()
