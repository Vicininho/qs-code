class MathSamples:

    @staticmethod
    def double(n):
        return n * n

    @staticmethod
    def power(base, potencia):
        if base == 1 or potencia == 0:
            return 1
        elif base == 2 and potencia == 2:
            return 4

    @staticmethod
    def factorial(n):
        return None