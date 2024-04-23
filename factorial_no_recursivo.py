import unittest

def factorial(value):
    resultado = value

    #resultado = 1

    if value == 0:
        return 1

    #while value > 1:

    while value > 2:
        resultado = resultado * (value - 1)
        #resultado = resultado * value
        value = value - 1
    return resultado


class TestFactorial(unittest.TestCase):

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