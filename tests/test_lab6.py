
import unittest
import sys
import os

# Додаємо шлях до папки src
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../src")
))

# Імпортуємо функції калькулятора
from calculator import (
    add, subtract, multiply, divide,
    power, root, percentage
)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(5, 4), 20)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_root(self):
        self.assertEqual(root(25), 5)

    def test_root_negative(self):
        with self.assertRaises(ValueError):
            root(-9)

    def test_percentage(self):
        self.assertEqual(percentage(200, 10), 20)


if __name__ == "__main__":
    unittest.main()
