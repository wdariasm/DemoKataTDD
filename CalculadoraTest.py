from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_Sumar(self):
        self.assertEqual(Calculadora().Sumar(""), 0 , "Cadena Vacia")

    def test_sumar_unacadena(self):
        self.assertEqual(Calculadora().Sumar("1"), 1, "Un número")

    def test_Sumar_cadenaConUnNumero(self):
        self.assertEqual(Calculadora().Sumar("1"), 1, "Un número")
        self.assertEqual(Calculadora().Sumar("2"), 2, "Un número")
