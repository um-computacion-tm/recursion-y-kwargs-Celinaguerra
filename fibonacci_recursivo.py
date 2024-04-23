import unittest

def fibonacci(value):
    if value == 0:
        return 0
    if value == 1:
        return 1
    return fibonacci(value-1) + fibonacci(value-2)


class TestFibonacciRecursivo(unittest.TestCase):
    def test_fibonacci_1(self):
        value = 1
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)

    def test_fibonacci_3(self):
        value = 3
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)

    def test_fibonacci_4(self):
        value = 4
        resultado = fibonacci(4)
        self.assertEqual(resultado, 3)

    def test_fibonacci_7(self):
        value = 7
        resultado = fibonacci(7)
        self.assertEqual(resultado, 13)

if __name__ == '__main__':
    unittest.main()