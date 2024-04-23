import unittest

def factorial(value):
    #cond corte
    if value < 2:
        return 1
    
    #recursividad
    return value * factorial(value - 1)

class TestFactorialRecursivo(unittest.TestCase):

    def test_fact_0(self):
        value = 0
        resultado = factorial(0)
        self.assertEqual(resultado,1)

    def test_fact_1(self):
        value = 1
        resultado = factorial(1)
        self.assertEqual(resultado,1)

    def test_fact_4(self):
        value = 4
        resultado = factorial(4)
        self.assertEqual(resultado,24)

    def test_fact_12(self):
        value = 12
        resultado = factorial(12)
        self.assertEqual(resultado,479001600)

if __name__ == '__main__':
    unittest.main()