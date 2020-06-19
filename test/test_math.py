
import unittest

from app.utility.math import multiply


class test_for_math_utility(unittest.TestCase):
    '''
    test case with a valid missed metal
    '''
    def test_multiply(self):
        a = 4
        b = 17.0
        expected_answer = (1,68.0)
        actual_answer = multiply(a, b)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''
        test case with a valid missed metal
        '''

    def test_multiply_value_error(self):
        a = "Error"
        b = 4
        expected_answer = (0, "Error")
        actual_answer = multiply(a, b)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''
       test case with a valid missed metal
       '''

    def test_divide(self):
        a = 17
        b = 2
        expected_answer = (1, 34.0)
        actual_answer = multiply(a, b)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''
        test case with a valid missed metal
        '''

    def test_divide_value_error(self):
        a = "Error"
        b = 4
        expected_answer = (0, "Error")
        actual_answer = multiply(a, b)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)