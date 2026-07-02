import unittest
from src.encuestas import frecuencia_respuestas

class TestFrecuenciaRespuestas(unittest.TestCase):
    def test_frecuencia_respuestas(self):
        self.assertEqual(
            frecuencia_respuestas(["Python", "Java", "Python"]),
            {"Python": 2, "Java": 1}
        )

    def test_lista_vacia(self):
        self.assertEqual(frecuencia_respuestas([]), {})

if __name__ == "__main__":
    unittest.main()
