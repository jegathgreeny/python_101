import arithmetic
import unittest


class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(arithmetic.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(arithmetic.subtract(2, 3), -1)

    def test_multiplication(self):
        self.assertEqual(arithmetic.multiply(2, 4), 8)

    def test_division(self):
        self.assertEqual(arithmetic.divide(4, 2), 2)


if __name__ == "__main__":
    unittest.main()
