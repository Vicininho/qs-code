import unittest
from math_samples import MathSamples

class PowerTest(unittest.TestCase):
    def teste_1(self):
        """Testando caso para entradas 1 e 1"""
        self.assertEqual(
            MathSamples.power(1,1),
            1
        )