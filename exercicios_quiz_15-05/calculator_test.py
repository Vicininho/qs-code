import unittest
from calculator_samples import CalculatorSamples

class CalculatorTest(unittest.TestCase):
    def teste_somar_1(self):
        """Testando caso para entradas 1 e 1"""
        self.assertEqual(
            CalculatorSamples.somar(1,1),
            2
        )
    
    def teste_somar_2(self):
        """Testando caso para entradas 2 e 3"""
        self.assertEqual(
            CalculatorSamples.somar(2,3),
            5
        )
    
    def teste_somar_3(self):
        """Testando caso para entradas 5 e 9"""
        self.assertEqual(
            CalculatorSamples.somar(5,9),
            14
        )