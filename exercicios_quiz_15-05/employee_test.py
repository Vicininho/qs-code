import unittest
from samples import EmployeeSamples

class EmployeeTest(unittest.TestCase):
    def create_employee(self):
        """Testando caso para entradas vinícius, cunha, estudante e 0"""
        self.assertEqual(
            EmployeeSamples("vinicius","cunha","analista",1200),
            ''
        )
    
    