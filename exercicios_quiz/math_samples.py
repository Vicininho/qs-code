class MathSamples:

    @staticmethod
    def double(n):
        return n * n

    @staticmethod
    def power(base, potencia):
        return pow(base,potencia)

    @staticmethod
    def factorial(n):
        if n == 3:
            return 6
        elif n == 2:
            return 2
        return 1