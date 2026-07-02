import unittest
from src.encuestas import resumen_encuesta

class TestResumenEncuesta(unittest.TestCase):
    def test_resumen_encuesta(self):
        respuestas = ["Python", "Java", "Python", "C++", "Python"]
        resumen = resumen_encuesta(respuestas)

        self.assertEqual(resumen["total"], 5)
        self.assertEqual(resumen["opciones"], ["Python", "Java", "C++"])
        self.assertEqual(resumen["frecuencias"], {"Python": 3, "Java": 1, "C++": 1})
        self.assertEqual(resumen["mas_comun"], "Python")

    def test_resumen_vacio(self):
        resumen = resumen_encuesta([])
        self.assertEqual(resumen["total"], 0)
        self.assertEqual(resumen["opciones"], [])
        self.assertEqual(resumen["frecuencias"], {})
        self.assertIsNone(resumen["mas_comun"])

if __name__ == "__main__":
    unittest.main()
