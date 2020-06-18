import unittest

from app.starter_code.merchant_guide_to_galaxy import answer_queries


class test_validate_solution_for_many_queries(unittest.TestCase):
    '''test case to find the solutions for many queries'''
    def test_to_validate_solution_for_many_queries(self):
        input_query =['HOW', 'MANY', 'CREDITS', 'IS', 'GLOB', 'PROK', 'SILVER', '?']
        input_token_map = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        missing_elements_credits = {'SILVER': 17.0, 'GOLD': 14450.0, 'IRON': 195.5}
        expected_answer = "glob prok silver is 68.0"
        actual_answer = answer_queries(input_query,input_token_map,missing_elements_credits)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''test case to find the solutions for many queries'''
    def test_validate_error_message_for_many_queries(self):
        input_query = ['HOW', 'MANY', 'CREDITS', 'IS', 'GLOB', 'PROK', 'GOLD', '?']
        input_token_map = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        missing_elements_credits = {'SILVER': 17.0, 'GOLD': 14450.0, 'IRON': 195.5}
        expected_answer = "glob prok gold is 57800.0"
        actual_answer = answer_queries(input_query, input_token_map, missing_elements_credits)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)