import unittest
from math_samples import MathSamples

class FibonacciTest(unittest.TestCase):

    def teste_01(self):
        """Testando caso para entrada = 0"""
        self.assertEqual(
            MathSamples.fibonacci(0),
            0
        )

    def teste_02(self):
        """Testando caso para entrada = 1"""
        self.assertEqual(
            MathSamples.fibonacci(1),
            1
        )

    def teste_03(self):
        """Testando caso para entrada = 2"""
        self.assertEqual(
            MathSamples.fibonacci(2),
            1
        )

    def teste_04(self):
        """Testando caso para entrada = 3"""
        self.assertEqual(
            MathSamples.fibonacci(3),
            2
        )
    
    def teste_05(self):
        """Testando caso para entrada = 4"""
        self.assertEqual(
            MathSamples.fibonacci(4),
            3
        )
    
    def teste_06(self):
        """Testando caso para entrada = 5"""
        self.assertEqual(
            MathSamples.fibonacci(5),
            5
        )

    def teste_07(self):
        """Testando caso para entrada = 6"""
        self.assertEqual(
            MathSamples.fibonacci(6),
            8
        )

    def teste_08(self):
        """Testando caso para entrada = 7"""
        self.assertEqual(
            MathSamples.fibonacci(7),
            13
        )

    def teste_09(self):
        """Testando caso para entrada = 8"""
        self.assertEqual(
            MathSamples.fibonacci(8),
            21
        )