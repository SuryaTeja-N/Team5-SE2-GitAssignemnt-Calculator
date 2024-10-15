import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 7), 21)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    def test_sqrt(self):
        self.assertEqual(calculator.sqrt(4), 2)
        self.assertEqual(calculator.sqrt(9), 3)
        self.assertEqual(calculator.sqrt(0), 0)
        with self.assertRaises(ValueError):
            calculator.sqrt(-1)

    def test_mod(self):
        self.assertEqual(calculator.mod(10, 3), 1)
        self.assertEqual(calculator.mod(10, 5), 0)
        self.assertEqual(calculator.mod(10, 7), 3)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)
        self.assertEqual(calculator.power(7, 1), 7)

    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)
        self.assertEqual(calculator.factorial(0), 1)
        with self.assertRaises(ValueError):
            calculator.factorial(-1)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(8, 2), 3)
        self.assertAlmostEqual(calculator.logarithm(1, 10), 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 2)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 1)

if __name__ == '__main__':
    unittest.main()
