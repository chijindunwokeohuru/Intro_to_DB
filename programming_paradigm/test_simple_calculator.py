#!/usr/bin/env python3
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.calculator = SimpleCalculator()

    def test_addition(self):
        """Test addition operations."""
        assert self.calculator.add(2, 3) == 5
        assert self.calculator.add(-1, 1) == 0
        assert self.calculator.add(-1, -1) == -2
        assert self.calculator.add(0, 0) == 0

    def test_subtraction(self):
        """Test subtraction operations."""
        assert self.calculator.subtract(5, 3) == 2
        assert self.calculator.subtract(1, 1) == 0
        assert self.calculator.subtract(-1, -1) == 0
        assert self.calculator.subtract(0, 0) == 0

    def test_multiplication(self):
        """Test multiplication operations."""
        assert self.calculator.multiply(2, 3) == 6
        assert self.calculator.multiply(-2, 3) == -6
        assert self.calculator.multiply(-2, -3) == 6
        assert self.calculator.multiply(0, 5) == 0

    def test_division(self):
        """Test division operations."""
        assert self.calculator.divide(6, 2) == 3
        assert self.calculator.divide(5, 2) == 2.5
        assert self.calculator.divide(-6, 2) == -3
        assert self.calculator.divide(-6, -2) == 3
        assert self.calculator.divide(0, 5) == 0

    def test_division_by_zero(self):
        """Test division by zero."""
        assert self.calculator.divide(5, 0) is None

    def test_invalid_input(self):
        """Test invalid input types."""
        try:
            self.calculator.add("2", 3)
            assert False, "Expected TypeError for invalid input"
        except TypeError:
            pass

        try:
            self.calculator.subtract(2, "3")
            assert False, "Expected TypeError for invalid input"
        except TypeError:
            pass

        try:
            self.calculator.multiply("2", 3)
            assert False, "Expected TypeError for invalid input"
        except TypeError:
            pass

        try:
            self.calculator.divide(2, "3")
            assert False, "Expected TypeError for invalid input"
        except TypeError:
            pass


if __name__ == '__main__':
    unittest.main()