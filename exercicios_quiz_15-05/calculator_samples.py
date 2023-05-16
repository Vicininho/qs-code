class CalculatorSamples:

    @staticmethod
    def somar(n,m):
        return n + m

    @staticmethod
    def subtrair(n,m):
        return n - m
    
    @staticmethod
    def multiplicar(n,m):
        return n * m
    
    @staticmethod
    def dividir(n,m):
        if m == 0:
            return "Indefinido"
        return n / m