import unittest

from app.roman_numbers_conversion.roman_numbers_validator import is_it_roman_char


class test_roman_validator(unittest.TestCase):
    ''' test case to find is the char is in roman numbers with valid roman char'''
    def test_is_it_roman_char(self):
        roman_char = "V"
        expected_answer = True
        actual_answer = is_it_roman_char(roman_char)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    ''' test case to find is the char is in roman numbers with invalid roman char'''
    def rtest_is_it_oman_char_returning_false(self):
        roman_char = "T"
        expected_answer = False
        actual_answer = is_it_roman_char(roman_char)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)




if __name__ == '__main__':
    unittest.main()
