import unittest
from src.encuestas import porcentaje_respuesta

class TestPorcentajeRespuesta(unittest.TestCase):
    def test_porcentaje_existente(self):
        self.assertAlmostEqual(
            porcentaje_respuesta(["Python", "Java", "Python"], "Python"),
            66.66666666666666
        )

    def test_porcentaje_inexistente(self):
        self.assertEqual(porcentaje_respuesta(["Python", "Java", "Python"], "C++"), 0.0)

    def test_lista_vacia(self):
        self.assertEqual(porcentaje_respuesta([], "Python"), 0.0)

if __name__ == "__main__":
    unittest.main()
