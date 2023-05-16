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
    
    def teste_subtrair_1(self):
        """Testando caso para entradas 4 e 3"""
        self.assertEqual(
            CalculatorSamples.subtrair(4,3),
            1
        )
    
    def teste_subtrair_2(self):
        """Testando caso para entradas 7 e 3"""
        self.assertEqual(
            CalculatorSamples.subtrair(7,3),
            4
        )
    
    def teste_subtrair_3(self):
        """Testando caso para entradas 19 e 7"""
        self.assertEqual(
            CalculatorSamples.subtrair(19,7),
            12
        )
    
    def teste_multiplicar_1(self):
        """Testando caso para entradas 2 e 2"""
        self.assertEqual(
            CalculatorSamples.multiplicar(2,2),
            4
        )
    
    def teste_multiplicar_2(self):
        """Testando caso para entradas 2 e 3"""
        self.assertEqual(
            CalculatorSamples.multiplicar(2,3),
            6
        )
    
    def teste_multiplicar_3(self):
        """Testando caso para entradas 5 e 7"""
        self.assertEqual(
            CalculatorSamples.multiplicar(5,7),
            35
        )