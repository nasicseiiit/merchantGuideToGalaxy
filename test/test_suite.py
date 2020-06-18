import unittest

from test.test_input_data import test_file_data
from test.test_roman_to_decimal import test_roman_to_decimal_conversion
from test.test_roman_validator import test_roman_validator
from test.test_to_validate_solutions_for_much_queries import test_validate_solution_for_much_queries
from test.test_to_validate_solutions_for_many_queries import test_validate_solution_for_many_queries

''' test suite to run the all test cases'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_file_data('test_get_file_data'))
    suite.addTest(test_roman_to_decimal_conversion('test_roman_to_dec'))
    suite.addTest(test_roman_to_decimal_conversion('test_roman_to_decimal_failing_to_convert'))
    suite.addTest(test_roman_validator('test_is_it_roman_char'))
    suite.addTest(test_roman_validator('rtest_is_it_oman_char_returning_false'))
    suite.addTest(test_validate_solution_for_much_queries('test_to_validate_solution_for_much_queries'))
    suite.addTest(test_validate_solution_for_much_queries('test_to_validate_error_message_for_much_queries'))
    suite.addTest(test_validate_solution_for_many_queries('test_to_validate_solution_for_many_queries'))
    suite.addTest(test_validate_solution_for_many_queries('test_validate_error_message_for_many_queries'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())