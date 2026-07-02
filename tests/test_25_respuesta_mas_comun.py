import unittest
from src.encuestas import respuesta_mas_comun

class TestRespuestaMasComun(unittest.TestCase):
    def test_respuesta_mas_comun(self):
        self.assertEqual(respuesta_mas_comun(["Python", "Java", "Python"]), "Python")

    def test_lista_vacia(self):
        self.assertIsNone(respuesta_mas_comun([]))

if __name__ == "__main__":
    unittest.main()
