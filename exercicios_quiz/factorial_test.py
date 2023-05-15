import unittest
from math_samples import MathSamples

class FactorialTest(unittest.TestCase):
    def teste_1(self):
        """Testando caso para entrada 0"""
        self.assertEqual(
            MathSamples.factorial(0),
            1
        )
    
    def teste_2(self):
        """Testando caso para entrada 1"""
        self.assertEqual(
            MathSamples.factorial(1),
            1
        )
    
    def teste_3(self):
        """Testando caso para entrada 2"""
        self.assertEqual(
            MathSamples.factorial(2),
            2
        )