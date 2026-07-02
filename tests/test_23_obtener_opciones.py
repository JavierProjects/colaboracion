import unittest
from src.encuestas import obtener_opciones

class TestObtenerOpciones(unittest.TestCase):
    def test_obtener_opciones(self):
        self.assertEqual(
            obtener_opciones(["Python", "Java", "Python", "C++", "Java"]),
            ["Python", "Java", "C++"]
        )

    def test_lista_vacia(self):
        self.assertEqual(obtener_opciones([]), [])

if __name__ == "__main__":
    unittest.main()
