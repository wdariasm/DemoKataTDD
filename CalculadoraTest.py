from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_Sumar(self):
        self.assertEqual(Calculadora().Sumar(""), 0 , "Cadena Vacia")
