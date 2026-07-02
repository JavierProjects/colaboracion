import unittest
from src.reportes import reporte_general


class TestReporteGeneral(unittest.TestCase):

    def test_reporte_general(self):
        calificaciones = [65, 65, 70, 80, 80, 80, 90, 100]

        asistencias = {
            "Ana": [1, 1, 1, 1],
            "Luis": [1, 0, 0, 1],
            "Hugo": [1, 1, 1, 1],
            "Monse": [1, 0, 0, 1],
            "Liz": [1, 1, 1, 1],
            "Maria": [1, 0, 0, 1],
            "Pedro": [1, 1, 1, 1],
            "Marco": [1, 0, 0, 1]
        }

        respuestas = [
            "Python", "Java", "Python", "Python",
            "Java", "Python", "Python", "Java"
        ]

        reporte = reporte_general(calificaciones, asistencias, respuestas)

        self.assertAlmostEqual(reporte["promedio_calificaciones"], 78.75)
        self.assertAlmostEqual(reporte["porcentaje_aprobados"], 75.0)
        self.assertAlmostEqual(reporte["promedio_asistencia"], 75.0)
        self.assertEqual(reporte["respuesta_mas_comun"], "Python")


if __name__ == "__main__":
    unittest.main()