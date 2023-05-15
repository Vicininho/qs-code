import unittest
from math_samples import MathSamples

class FactorialTest(unittest.TestCase):
    def teste_1(self):
        """Testando caso para entrada 0"""
        self.assertEqual(
            MathSamples.factorial(0),
            1
        )