class MathSamples:

    @staticmethod
    def double(n):
        return n * n

    @staticmethod
    def power(base, potencia):
        return pow(base,potencia)

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * MathSamples.factorial((n - 1))