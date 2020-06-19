import unittest

from test.test_cli_arguments import test_for_cli_arguments
from test.test_input_data import test_file_data
from test.test_roman_to_decimal import test_roman_to_decimal_conversion
from test.test_roman_validator import test_roman_validator
from test.test_to_validate_solutions_for_much_queries import test_validate_solution_for_much_queries
from test.test_to_validate_solutions_for_many_queries import test_validate_solution_for_many_queries
from test.test_math import test_for_math_utility
from test.test_missed_words_finder import test_for_missed_words_finder

''' test suite to run the all test cases'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_for_cli_arguments('test_get_file_name'))
    suite.addTest(test_file_data('test_check_file_existance'))
    suite.addTest(test_file_data('test_check_file_existance_error'))
    suite.addTest(test_file_data('test_get_file_data'))
    suite.addTest(test_file_data('test_get_file_data_empty_list'))
    suite.addTest(test_roman_to_decimal_conversion('test_roman_to_dec'))
    suite.addTest(test_roman_to_decimal_conversion('test_roman_to_decimal_failing_to_convert'))
    suite.addTest(test_roman_validator('test_is_it_roman_char'))
    suite.addTest(test_roman_validator('test_is_it_oman_char_returning_false'))
    suite.addTest(test_validate_solution_for_much_queries('test_to_validate_solution_for_much_queries'))
    suite.addTest(test_validate_solution_for_much_queries('test_to_validate_error_message_for_much_queries'))
    suite.addTest(test_validate_solution_for_many_queries('test_to_validate_solution_for_many_queries'))
    suite.addTest(test_validate_solution_for_many_queries('test_validate_error_message_for_many_queries'))
    suite.addTest(test_for_math_utility('test_multiply'))
    suite.addTest(test_for_math_utility('test_multiply_value_error'))
    suite.addTest(test_for_math_utility('test_divide'))
    suite.addTest(test_for_math_utility('test_divide_value_error'))
    suite.addTest(test_for_missed_words_finder('test_get_missed_credits'))
    suite.addTest(test_for_missed_words_finder('test_find_missed_word_credits'))
    suite.addTest(test_for_missed_words_finder('test_get_missed_word'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())