import unittest
from src.calificaciones import resumen_calificaciones

class TestResumenCalificaciones(unittest.TestCase):
    def test_resumen_calificaciones(self):
        calificaciones = [65, 65, 70, 80, 80, 80, 90, 100]
        resumen = resumen_calificaciones(calificaciones)

        self.assertEqual(resumen["total"], 8)
        self.assertAlmostEqual(resumen["promedio"], 78.75)
        self.assertEqual(resumen["moda"], 80)
        self.assertEqual(resumen["mediana"], 80.0)
        self.assertEqual(resumen["maxima"], 100)
        self.assertEqual(resumen["minima"], 65)
        self.assertAlmostEqual(resumen["porcentaje_aprobados"], 75.0)
        self.assertAlmostEqual(resumen["porcentaje_reprobados"], 25.0)
        self.assertEqual(resumen["distribucion"], {65: 2, 70: 1, 80: 3, 90: 1, 100: 1})

    def test_resumen_vacio(self):
        resumen = resumen_calificaciones([])

        self.assertEqual(resumen["total"], 0)
        self.assertEqual(resumen["promedio"], None)
        self.assertEqual(resumen["moda"], None)
        self.assertEqual(resumen["mediana"], None)
        self.assertEqual(resumen["maxima"], None)
        self.assertEqual(resumen["minima"], None)
        self.assertEqual(resumen["porcentaje_aprobados"], 0.0)
        self.assertEqual(resumen["porcentaje_reprobados"], 0.0)
        self.assertEqual(resumen["distribucion"], {})

if __name__ == "__main__":
    unittest.main()
