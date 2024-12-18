import unittest
from calculator import add, subtract, mult, divide, pow, modulus

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(mult(3, 4), 12)
        self.assertEqual(mult(-1, 1), -1)
        self.assertEqual(mult(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_power(self):
        self.assertEqual(pow(2, 3), 8)
        self.assertEqual(pow(5, 0), 1)
        self.assertEqual(pow(-2, 2), 4)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 5), 0)
        self.assertEqual(modulus(10, -3), -2)
        self.assertEqual(modulus(-10, 3), 2)

if __name__ == '__main__':
    unittest.main()
