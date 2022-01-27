import unittest
from modules.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_has_first_number(self):
        self.calculator.num1 = 1
        self.assertEqual(1,self.calculator.num1)

    def test_has_second_number(self):
        self.calculator.num2 = 1
        self.assertEqual(1, self.calculator.num2)

    def test_number_is_integer_pass(self):
        self.assertEqual(True, self.calculator.number_is_integer(1))

    def test_number_is_integer_fail(self):
        self.assertEqual(False, self.calculator.number_is_integer(1.0))

    def test_number_is_float_pass(self):
        self.assertEqual(True, self.calculator.number_is_float(1.0))

    def test_number_is_float_fail(self):
        self.assertEqual(False, self.calculator.number_is_float(1))

    def test_number_is_none_pass(self):
        self.assertEqual(True, self.calculator.number_is_none(None))

    def test_number_is_none_fail(self):
        self.assertEqual(False, self.calculator.number_is_none(1))

    def test_number_is_string_pass(self):
        self.assertEqual(True, self.calculator.number_is_string("1"))

    def test_number_is_string_fail(self):
        self.assertEqual(False, self.calculator.number_is_string(1))

    def test_can_convert_to_float_pass_float(self):
        self.assertEqual(True, self.calculator.can_convert_to_float(1.0))

    def test_can_convert_to_float_pass_integer(self):
        self.assertEqual(True, self.calculator.can_convert_to_float(1))

    def test_can_convert_to_float_pass_string(self):
        self.assertEqual(True, self.calculator.can_convert_to_float("1"))

    def test_can_convert_to_float_fail_string_ValueError(self):
        self.assertEqual(False, self.calculator.can_convert_to_float("one"))

    def test_can_convert_to_float_fail_none_TypeError(self):
        self.assertEqual(False, self.calculator.can_convert_to_float(None))

    def test_can_use_number_pass(self):
        self.assertEqual(True, self.calculator.can_use_number("1"))

    def test_can_use_number_fail(self):
        self.assertEqual(False, self.calculator.can_use_number("one"))

    def test_can_use_numbers_pass(self):
        self.assertEqual(True, self.calculator.can_use_numbers("1", 1))

    def test_can_use_numbers_fail(self):
        self.assertEqual(False, self.calculator.can_use_numbers(1.0, "one"))

    def test_number_is_zero_pass(self):
        self.assertEqual(True, self.calculator.number_is_zero(0.0))

    def test_number_is_zero_fail(self):
        self.assertEqual(False, self.calculator.number_is_zero(0.1))

    def test_add_pass_positive(self):
        self.assertEqual(3, self.calculator.add(1, 2))

    def test_add_pass_negative(self):
        self.assertEqual(-3, self.calculator.add(-1, -2))

    def test_add_fail_ValueError(self):
        self.assertEqual('Error: Cannot add values', self.calculator.add(1, "two"))

    def test_subtract_pass_positive(self):
        self.assertEqual(1, self.calculator.subtract(3, 2))

    def test_subtract_pass_negative(self):
        self.assertEqual(-1, self.calculator.subtract(-2, -1))       

    def test_subtract_fail_ValueError(self):
        self.assertEqual('Error: Cannot subtract values', self.calculator.subtract(3, "two"))

    def test_multiply_pass_positive(self):
        self.assertEqual(6, self.calculator.multiply(2, 3))

    def test_multiply_pass_negative(self):
        self.assertEqual(-2, self.calculator.multiply(-1, 2))

    def test_multiply_fail_ValueError(self):
        self.assertEqual('Error: Cannot multiply values', self.calculator.multiply(2, "three"))

    def test_divide_pass_positive(self):
        self.assertEqual(2.5, self.calculator.divide(5, 2))

    def test_divide_pass_negative(self):
        self.assertEqual(-2, self.calculator.divide(2, -1))

    def test_divide_fail_ValueError(self):
        self.assertEqual('Error: Cannot divide values', self.calculator.divide(6, "three"))

    def test_divide_fail_divide_by_zero(self):
        self.assertEqual('Error: Cannot divide by zero', self.calculator.divide(2, 0))