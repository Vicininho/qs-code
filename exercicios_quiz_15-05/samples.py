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

class EmployeeSamples:

    def __init__(self, primeiro_nome, sobrenome, cargo, salario):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.salario = float(salario)

    @staticmethod
    def calcular_reajuste():
        return None

    @staticmethod
    def gerar_nome_completo():
        return None

    @staticmethod
    def validar_cargo():
        return None