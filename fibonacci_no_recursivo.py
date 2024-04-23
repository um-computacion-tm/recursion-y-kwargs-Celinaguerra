import unittest

def fibonacci(value):
    values = [0,1]

    for _ in range(value - 1):
        values.append(values[-1] + values [-2])
    
    return values[value]

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        value = 0
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)

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