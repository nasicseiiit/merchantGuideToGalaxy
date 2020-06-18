import unittest

from app.starter_code.merchant_guide_to_galaxy import answer_queries


class test_validate_solution_for_much_queries(unittest.TestCase):
    '''test case to find the solutions for much queries'''
    def test_to_validate_solution_for_much_queries(self):
        input_query =['HOW', 'MUCH', 'IS', 'PISH', 'TEGJ', 'GLOB', 'GLOB', '?']
        input_token_map = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        expected_answer = "pish tegj glob glob is 42"
        actual_answer = answer_queries(input_query,input_token_map,[])
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''test case to find the solutions for much queries'''
    def test_to_validate_error_message_for_much_queries(self):
        input_query = ['HOW', 'MUCH', 'WOOD', 'COULD', 'A', 'WOODCHUCK', 'CHUCK', 'IF', 'A', 'WOODCHUCK', 'COULD', 'CHUCK', 'WOOD', '?']
        input_token_map = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        expected_answer = "I have no idea what you are talking about"
        actual_answer = answer_queries(input_query, input_token_map, [])
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)