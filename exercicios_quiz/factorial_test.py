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
    
    def teste_4(self):
        """Testando caso para entrada 3"""
        self.assertEqual(
            MathSamples.factorial(3),
            6
        )

    def teste_5(self):
        """Testando caso para entrada 4"""
        self.assertEqual(
            MathSamples.factorial(4),
            24
        )
    
    def teste_6(self):
        """Testando caso para entrada 5"""
        self.assertEqual(
            MathSamples.factorial(5),
            120
        )
    
    def teste_7(self):
        """Testando caso para entrada 6"""
        self.assertEqual(
            MathSamples.factorial(6),
            720
        )