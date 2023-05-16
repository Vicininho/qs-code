import unittest
from calculator_samples import CalculatorSamples

class CalculatorTest(unittest.TestCase):
    def teste_1(self):
        """Testando caso para entradas 1 e 1"""
        self.assertEqual(
            CalculatorSamples.somar(1,1),
            2
        )
