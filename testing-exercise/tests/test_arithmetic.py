from calculator.arithmetic import get_numbers, addition, subtraction, multiplication, division
from unittest import TestCase
from unittest.mock import patch
from tests.helper import print_success


class TestArithmetic(TestCase):
    def setUp(self):
        self.positive_numbers = [6, 12]
        self.negative_numbers = [-6, -12]
        self.mix_numbers = [-6, 12]

    @patch('builtins.input', return_value='6 12 3')
    def test_get_numbers(self, mock_input):
        result = get_numbers()
        expected = [6, 12, 3]
        self.assertEqual(result, expected)
        print_success()

    # Menguji input bukan spasi sebagai pemisah
    @patch('builtins.input', return_value='6,12,3')
    def test_get_numbers_with_comma_as_separator(self, mock_input):
        with self.assertRaises(ValueError) as context:
            get_numbers()
        self.assertEqual(str(context.exception), "Masukkan angka dengan spasi sebagai pemisah dan gunakan '.' "
                                                 "ketika menggunakan desimal.")
        print_success()

    @patch('builtins.input', return_value='6')
    def test_get_numbers_with_one_number(self, mock_input):
        with self.assertRaises(ValueError) as context:
            get_numbers()
        self.assertEqual(str(context.exception),"Harap masukkan Angka lebih dari satu!")
        print_success()

    def test_addition_positive_number(self):
        result = addition(self.positive_numbers)
        expected = 18
        self.assertEqual(result, expected)
        print_success()

    def test_addition_negative_number(self):
        result = addition(self.negative_numbers)
        expected = -18
        self.assertEqual(result, expected)
        print_success()

    def test_addition_mix_number(self):
        result = addition(self.mix_numbers)
        expected = 6
        self.assertEqual(result, expected)
        print_success()

    def test_subtraction_positive_number(self):
        result = subtraction(self.positive_numbers)
        expected = -6
        self.assertEqual(result, expected)
        print_success()

    def test_subtraction_negative_number(self):
        result = subtraction(self.negative_numbers)
        expected = 6
        self.assertEqual(result, expected)
        print_success()

    def test_subtraction_mix_number(self):
        result = subtraction(self.mix_numbers)
        expected = -18
        self.assertEqual(result, expected)
        print_success()

    def test_multiplication_positive_number(self):
        result = multiplication(self.positive_numbers)
        expected = 72
        self.assertEqual(result, expected)
        print_success()

    def test_multiplication_negative_number(self):
        result = multiplication(self.negative_numbers)
        expected = 72
        self.assertEqual(result, expected)
        print_success()

    def test_multiplication_mix_number(self):
        result = multiplication(self.mix_numbers)
        expected = -72
        self.assertEqual(result, expected)
        print_success()

    def test_division_positive_number(self):
        result = division(self.positive_numbers)
        expected = 0.5
        self.assertEqual(result, expected)
        print_success()

    def test_division_negative_number(self):
        result = division(self.negative_numbers)
        expected = 0.5
        self.assertEqual(result, expected)
        print_success()

    def test_division_mix_number(self):
        result = division(self.mix_numbers)
        expected = -0.5
        self.assertEqual(result, expected)
        print_success()

    def test_division_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            numbers = [12, 0]
            division(numbers)
        self.assertEqual(str(context.exception), "Anda tidak bisa membagi bilangan dengan angka 0!")
        print_success()


if __name__ == '__main__':
    import unittest

    class SilentTestResult(unittest.TextTestResult):
        def addSuccess(self, test):
            pass

    class SilentTestRunner(unittest.TextTestRunner):
        def _makeResult(self):
            return SilentTestResult(self.stream, self.descriptions, self.verbosity)

    unittest.main(testRunner=SilentTestRunner())
