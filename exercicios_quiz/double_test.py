import unittest
from math_samples import MathSamples

class PowerTest(unittest.TestCase):
    def teste_1(self):
        """Testando caso para entrada = 0"""
        self.assertEqual(
            MathSamples.power(0),
            0
        )