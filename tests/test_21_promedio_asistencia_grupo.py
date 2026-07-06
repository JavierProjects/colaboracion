import unittest
from src.asistencias import promedio_asistencia_grupo

class TestPromedioAsistenciaGrupo(unittest.TestCase):
    def test_promedio_grupo(self):
        asistencias = {
            "Ana": [1, 1, 1, 1],
            "Luis": [1, 0, 0, 1]
        }
        self.assertAlmostEqual(promedio_asistencia_grupo(asistencias), 75.0)

    def test_diccionario_vacio(self):
        self.assertEqual(promedio_asistencia_grupo({}), 0.0)

if __name__ == "__main__":
    unittest.main()
