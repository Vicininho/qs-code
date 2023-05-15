import unittest
from math_samples import MathSamples

class PowerTest(unittest.TestCase):
    def teste_1(self):
        """Testando caso para entradas 1 e 1"""
        self.assertEqual(
            MathSamples.power(1,1),
            1
        )

    def teste_2(self):
        """Testando caso para entradas 1 e 2"""
        self.assertEqual(
            MathSamples.power(1,2),
            1
        )
    
    def teste_3(self):
        """Testando caso para entradas 2 e 2"""
        self.assertEqual(
            MathSamples.power(2,2),
            4
        )