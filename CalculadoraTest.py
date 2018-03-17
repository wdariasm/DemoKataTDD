from unittest import TestCase

import Calculadora

class CalculadoraTest(TestCase):
    def test_Sumar(self):
        self.assertEqual(Calculadora().Sumar(""), 0 , "Cadena Vacia")
