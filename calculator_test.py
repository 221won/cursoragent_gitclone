#!/usr/bin/env python3
"""
Calculator Test Module
A simple calculator with basic arithmetic operations and tests.
"""

import unittest
from typing import Union


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract second number from first number."""
        return a - b
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Raise first number to the power of second number."""
        return a ** b
    
    def square_root(self, a: Union[int, float]) -> float:
        """Calculate square root of a number."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_integers(self):
        """Test addition with integers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_add_floats(self):
        """Test addition with floats."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
    
    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 3), 7/3)
        self.assertEqual(self.calc.divide(-6, 2), -3)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(4, 0.5), 2)
    
    def test_square_root(self):
        """Test square root operation."""
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(0), 0)
    
    def test_square_root_negative(self):
        """Test square root of negative number raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)


def main():
    """Main function to run calculator tests and demonstrate functionality."""
    print("Calculator Test Suite")
    print("=" * 50)
    
    # Run the test suite
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    print("\n" + "=" * 50)
    print("Calculator Demo")
    print("=" * 50)
    
    # Demonstrate calculator functionality
    calc = Calculator()
    
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 6 * 7 = {calc.multiply(6, 7)}")
    print(f"Division: 15 / 3 = {calc.divide(15, 3)}")
    print(f"Power: 2^8 = {calc.power(2, 8)}")
    print(f"Square Root: √16 = {calc.square_root(16)}")
    
    # Test error handling
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Error handling: {e}")
    
    try:
        calc.square_root(-4)
    except ValueError as e:
        print(f"Error handling: {e}")


if __name__ == "__main__":
    main()