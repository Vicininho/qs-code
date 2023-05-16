import unittest
from samples import EmployeeSamples

primeiro_nome="vinicius"
sobrenome="cunha"
cargo="analista"
salario=100

employee = EmployeeSamples(primeiro_nome,sobrenome,cargo,salario)

class EmployeeTest(unittest.TestCase):
    def create_employee(self):
        """Testando caso para entradas vinícius, cunha, estudante e 0"""
        self.assertEqual(
            EmployeeSamples(primeiro_nome,sobrenome,cargo,salario),
            ''
        )

    def calcular_reajuste(self):
        """Testando caso para entradas vinícius, cunha, estudante e 0"""
        self.assertEqual(
            EmployeeSamples.calcular_reajuste(employee),
            '105'
        )