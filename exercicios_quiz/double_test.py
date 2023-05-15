import unittest
from math_samples import MathSamples

class PowerTest(unittest.TestCase):
    def teste_1(self):
        """Testando caso para entrada = 0"""
        self.assertEqual(
            MathSamples.double(0),
            0
        )
    
    def teste_2(self):
        """Testando caso para entrada = 1"""
        self.assertEqual(
            MathSamples.double(1),
            1
        )