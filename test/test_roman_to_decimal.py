import unittest

from app.roman_numbers_conversion.roman_to_number_conversion import roman_to_number


class test_roman_to_decimal_conversion(unittest.TestCase):
    ''' test case to find the decimal value for roman string'''
    def test_roman_to_dec(self):
        roman_string = "MCM"
        expected_answer = 1900
        actual_answer = roman_to_number(roman_string)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    ''' test case to find the decimal value for invalid roman string'''
    def test_roman_to_decimal_failing_to_convert(self):
        roman_string = "IIII"
        expected_answer = "This is not a valid roman number"
        actual_answer = roman_to_number(roman_string)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)


if __name__ == '__main__':
    unittest.main()
