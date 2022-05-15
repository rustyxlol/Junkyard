"""
Test cases for calculator.py
"""
import unittest
from unittesting import calculator as calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 5), 4)
        self.assertEqual(calc.add(10, -11), -1)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(2, 3), -1)
        self.assertEqual(calc.sub(-1, 5), -6)
        self.assertEqual(calc.sub(10, -11), 21)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-2, 3), -6)
        self.assertEqual(calc.multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(30, 2), 15)
        self.assertEqual(calc.divide(30, -2), -15)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # don't do this professionally
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # Use context manager instead
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
