"""
Unit tests for calculator module using Category Partition Method.

Category Partition Method:
- Identify categories (input parameters, conditions)
- Partition each category into equivalence classes
- Generate test cases systematically from category combinations
"""
import unittest
from calculator import add, subtract, multiply, divide, power


class TestAdd(unittest.TestCase):
    """
    Test cases for add function using Category Partition Method.
    
    Categories:
    - a: sign/value type [positive integer, negative integer, zero, positive float, negative float]
    - b: sign/value type [positive integer, negative integer, zero, positive float, negative float]
    """
    
    def test_add_positive_positive(self):
        """Category: a=positive, b=positive"""
        self.assertEqual(add(2, 3), 5)
    
    def test_add_positive_negative(self):
        """Category: a=positive, b=negative"""
        self.assertEqual(add(5, -3), 2)
    
    def test_add_positive_zero(self):
        """Category: a=positive, b=zero"""
        self.assertEqual(add(5, 0), 5)
    
    def test_add_positive_float(self):
        """Category: a=positive, b=positive float"""
        self.assertAlmostEqual(add(2, 3.7), 5.7, places=7)
    
    def test_add_negative_positive(self):
        """Category: a=negative, b=positive"""
        self.assertEqual(add(-2, 3), 1)
    
    def test_add_negative_negative(self):
        """Category: a=negative, b=negative"""
        self.assertEqual(add(-2, -3), -5)
    
    def test_add_negative_zero(self):
        """Category: a=negative, b=zero"""
        self.assertEqual(add(-5, 0), -5)
    
    def test_add_negative_float(self):
        """Category: a=negative, b=negative float"""
        self.assertAlmostEqual(add(-2, -3.5), -5.5, places=7)
    
    def test_add_zero_positive(self):
        """Category: a=zero, b=positive"""
        self.assertEqual(add(0, 5), 5)
    
    def test_add_zero_negative(self):
        """Category: a=zero, b=negative"""
        self.assertEqual(add(0, -5), -5)
    
    def test_add_zero_zero(self):
        """Category: a=zero, b=zero"""
        self.assertEqual(add(0, 0), 0)
    
    def test_add_float_float(self):
        """Category: a=positive float, b=positive float"""
        self.assertAlmostEqual(add(2.5, 3.7), 6.2, places=7)


class TestSubtract(unittest.TestCase):
    """
    Test cases for subtract function using Category Partition Method.
    
    Categories:
    - a: sign/value type [positive integer, negative integer, zero, positive float, negative float]
    - b: sign/value type [positive integer, negative integer, zero, positive float, negative float]
    """
    
    def test_subtract_positive_positive(self):
        """Category: a=positive, b=positive"""
        self.assertEqual(subtract(5, 3), 2)
    
    def test_subtract_positive_negative(self):
        """Category: a=positive, b=negative"""
        self.assertEqual(subtract(5, -3), 8)
    
    def test_subtract_positive_zero(self):
        """Category: a=positive, b=zero"""
        self.assertEqual(subtract(5, 0), 5)
    
    def test_subtract_positive_float(self):
        """Category: a=positive, b=positive float"""
        self.assertAlmostEqual(subtract(5, 2.5), 2.5, places=7)
    
    def test_subtract_negative_positive(self):
        """Category: a=negative, b=positive"""
        self.assertEqual(subtract(-2, 3), -5)
    
    def test_subtract_negative_negative(self):
        """Category: a=negative, b=negative"""
        self.assertEqual(subtract(-2, -3), 1)
    
    def test_subtract_negative_zero(self):
        """Category: a=negative, b=zero"""
        self.assertEqual(subtract(-5, 0), -5)
    
    def test_subtract_negative_float(self):
        """Category: a=negative, b=negative float"""
        self.assertAlmostEqual(subtract(-5, -2.5), -2.5, places=7)
    
    def test_subtract_zero_positive(self):
        """Category: a=zero, b=positive"""
        self.assertEqual(subtract(0, 5), -5)
    
    def test_subtract_zero_negative(self):
        """Category: a=zero, b=negative"""
        self.assertEqual(subtract(0, -5), 5)
    
    def test_subtract_zero_zero(self):
        """Category: a=zero, b=zero"""
        self.assertEqual(subtract(0, 0), 0)
    
    def test_subtract_float_float(self):
        """Category: a=positive float, b=positive float"""
        self.assertAlmostEqual(subtract(5.5, 2.3), 3.2, places=7)


class TestMultiply(unittest.TestCase):
    """
    Test cases for multiply function using Category Partition Method.
    
    Categories:
    - a: sign/value type [positive integer, negative integer, zero, one, positive float, negative float]
    - b: sign/value type [positive integer, negative integer, zero, one, positive float, negative float]
    """
    
    def test_multiply_positive_positive(self):
        """Category: a=positive, b=positive"""
        self.assertEqual(multiply(3, 4), 12)
    
    def test_multiply_positive_negative(self):
        """Category: a=positive, b=negative"""
        self.assertEqual(multiply(3, -4), -12)
    
    def test_multiply_positive_zero(self):
        """Category: a=positive, b=zero"""
        self.assertEqual(multiply(5, 0), 0)
    
    def test_multiply_positive_one(self):
        """Category: a=positive, b=one"""
        self.assertEqual(multiply(5, 1), 5)
    
    def test_multiply_positive_float(self):
        """Category: a=positive, b=positive float"""
        self.assertAlmostEqual(multiply(3, 2.5), 7.5, places=7)
    
    def test_multiply_negative_positive(self):
        """Category: a=negative, b=positive"""
        self.assertEqual(multiply(-2, 3), -6)
    
    def test_multiply_negative_negative(self):
        """Category: a=negative, b=negative"""
        self.assertEqual(multiply(-2, -3), 6)
    
    def test_multiply_negative_zero(self):
        """Category: a=negative, b=zero"""
        self.assertEqual(multiply(-5, 0), 0)
    
    def test_multiply_negative_one(self):
        """Category: a=negative, b=one"""
        self.assertEqual(multiply(-5, 1), -5)
    
    def test_multiply_negative_float(self):
        """Category: a=negative, b=negative float"""
        self.assertAlmostEqual(multiply(-2, -2.5), 5.0, places=7)
    
    def test_multiply_zero_positive(self):
        """Category: a=zero, b=positive"""
        self.assertEqual(multiply(0, 5), 0)
    
    def test_multiply_zero_negative(self):
        """Category: a=zero, b=negative"""
        self.assertEqual(multiply(0, -5), 0)
    
    def test_multiply_zero_zero(self):
        """Category: a=zero, b=zero"""
        self.assertEqual(multiply(0, 0), 0)
    
    def test_multiply_one_positive(self):
        """Category: a=one, b=positive"""
        self.assertEqual(multiply(1, 5), 5)
    
    def test_multiply_one_negative(self):
        """Category: a=one, b=negative"""
        self.assertEqual(multiply(1, -5), -5)
    
    def test_multiply_one_one(self):
        """Category: a=one, b=one"""
        self.assertEqual(multiply(1, 1), 1)
    
    def test_multiply_float_float(self):
        """Category: a=positive float, b=positive float"""
        self.assertAlmostEqual(multiply(2.5, 3.2), 8.0, places=7)


class TestDivide(unittest.TestCase):
    """
    Test cases for divide function using Category Partition Method.
    
    Categories:
    - a: sign/value type [positive integer, negative integer, zero, positive float, negative float]
    - b: sign/value type [positive integer, negative integer, zero, one, positive float, negative float]
    """
    
    def test_divide_positive_positive(self):
        """Category: a=positive, b=positive"""
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_positive_negative(self):
        """Category: a=positive, b=negative"""
        self.assertEqual(divide(10, -2), -5)
    
    def test_divide_positive_one(self):
        """Category: a=positive, b=one"""
        self.assertEqual(divide(5, 1), 5)
    
    def test_divide_positive_float(self):
        """Category: a=positive, b=positive float"""
        self.assertAlmostEqual(divide(10, 2.5), 4.0, places=7)
    
    def test_divide_positive_zero(self):
        """Category: a=positive, b=zero (error case)"""
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_negative_positive(self):
        """Category: a=negative, b=positive"""
        self.assertEqual(divide(-10, 2), -5)
    
    def test_divide_negative_negative(self):
        """Category: a=negative, b=negative"""
        self.assertEqual(divide(-10, -2), 5)
    
    def test_divide_negative_one(self):
        """Category: a=negative, b=one"""
        self.assertEqual(divide(-5, 1), -5)
    
    def test_divide_negative_float(self):
        """Category: a=negative, b=negative float"""
        self.assertAlmostEqual(divide(-10, -2.5), 4.0, places=7)
    
    def test_divide_negative_zero(self):
        """Category: a=negative, b=zero (error case)"""
        with self.assertRaises(ValueError) as context:
            divide(-5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_zero_positive(self):
        """Category: a=zero, b=positive"""
        self.assertEqual(divide(0, 5), 0)
    
    def test_divide_zero_negative(self):
        """Category: a=zero, b=negative"""
        self.assertEqual(divide(0, -5), 0)
    
    def test_divide_zero_zero(self):
        """Category: a=zero, b=zero (error case)"""
        with self.assertRaises(ValueError) as context:
            divide(0, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_float_float(self):
        """Category: a=positive float, b=positive float"""
        self.assertEqual(divide(7, 2), 3.5)
    
    def test_divide_float_integer(self):
        """Category: a=positive float, b=positive integer"""
        self.assertAlmostEqual(divide(7.5, 2), 3.75, places=7)


class TestPower(unittest.TestCase):
    """
    Test cases for power function using Category Partition Method.
    
    Categories:
    - base: sign/value type [positive integer, negative integer, zero, one, positive float]
    - exponent: sign/value type [positive integer, negative integer, zero, one, positive float]
    """
    
    def test_power_positive_positive(self):
        """Category: base=positive, exponent=positive"""
        self.assertEqual(power(2, 3), 8)
    
    def test_power_positive_negative(self):
        """Category: base=positive, exponent=negative"""
        self.assertAlmostEqual(power(2, -2), 0.25, places=7)
    
    def test_power_positive_zero(self):
        """Category: base=positive, exponent=zero"""
        self.assertEqual(power(5, 0), 1)
    
    def test_power_positive_one(self):
        """Category: base=positive, exponent=one"""
        self.assertEqual(power(5, 1), 5)
    
    def test_power_positive_float(self):
        """Category: base=positive, exponent=positive float"""
        self.assertAlmostEqual(power(4, 0.5), 2.0, places=7)
    
    def test_power_negative_positive(self):
        """Category: base=negative, exponent=positive"""
        self.assertEqual(power(-2, 3), -8)
    
    def test_power_negative_negative(self):
        """Category: base=negative, exponent=negative"""
        self.assertAlmostEqual(power(-2, -2), 0.25, places=7)
    
    def test_power_negative_zero(self):
        """Category: base=negative, exponent=zero"""
        self.assertEqual(power(-5, 0), 1)
    
    def test_power_negative_one(self):
        """Category: base=negative, exponent=one"""
        self.assertEqual(power(-5, 1), -5)
    
    def test_power_zero_positive(self):
        """Category: base=zero, exponent=positive"""
        self.assertEqual(power(0, 5), 0)
    
    def test_power_zero_zero(self):
        """Category: base=zero, exponent=zero"""
        self.assertEqual(power(0, 0), 1)
    
    def test_power_zero_negative(self):
        """Category: base=zero, exponent=negative"""
        # 0 to negative power is undefined, but Python raises ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)
    
    def test_power_one_positive(self):
        """Category: base=one, exponent=positive"""
        self.assertEqual(power(1, 5), 1)
    
    def test_power_one_negative(self):
        """Category: base=one, exponent=negative"""
        self.assertEqual(power(1, -5), 1)
    
    def test_power_one_zero(self):
        """Category: base=one, exponent=zero"""
        self.assertEqual(power(1, 0), 1)
    
    def test_power_float_positive(self):
        """Category: base=positive float, exponent=positive"""
        self.assertAlmostEqual(power(2.5, 2), 6.25, places=7)
