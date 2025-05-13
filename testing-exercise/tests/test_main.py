from unittest import TestCase, mock
from unittest.mock import patch
from main import main
from tests.helper import print_success


class TestIntegrations(TestCase):
    @patch('builtins.input', return_value='q')
    def test_quit_program(self, mock_input_ops):
        with self.assertRaises(SystemExit):
            main()
        print_success()

    @patch('main.get_numbers', return_value=[2.0,2.1])  
    @patch('main.input', return_value='1')  
    def test_addition(self, mock_input_ops, mock_value):
        with mock.patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with('Hasil: 4.1')
        print_success()

    @patch('builtins.input', return_value='2,2')  
    @patch('main.input', return_value='1') 
    def test_value_error(self, mock_input_ops, mock_value):
        with mock.patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Terjadi kesalahan ValueError: Masukkan angka dengan spasi sebagai pemisah "
                                          "dan gunakan '.' ketika menggunakan desimal.")
        print_success()

    @patch('builtins.input', return_value='2 0') 
    @patch('main.input', return_value='4') 
    def test_zero_division_error(self, mock_input_ops, mock_value):
        with mock.patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Terjadi kesalahan ZeroDivisionError: "
                                          "Anda tidak bisa membagi bilangan dengan angka 0!")
        print_success()

    @patch('main.get_numbers', side_effect=TypeError("Invalid Data Type!")) 
    @patch('main.input', return_value='4')  
    def test_general_exception(self, mock_input_ops, mock_value):
        with mock.patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Terjadi kesalahan Invalid Data Type!")
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
