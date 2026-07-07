import unittest
from src.encuestas import contar_respuestas

class TestContarRespuestas(unittest.TestCase):
    def test_contar_respuestas(self):
        self.assertEqual(contar_respuestas(["Python", "Java", "Python"]), 3)

    def test_lista_vacia(self):
        self.assertEqual(contar_respuestas([]), 0)

if __name__ == "__main__":
    unittest.main()
