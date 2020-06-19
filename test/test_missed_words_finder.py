
import unittest
from app.roman_numbers_conversion.missed_words_finder import get_missed_credits, find_missed_word_credits, \
    get_missed_word


class test_for_missed_words_finder(unittest.TestCase):
    '''
    test case to find the missed metal credits
    '''
    def test_get_missed_credits(self):
        token_roman_value = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        no_of_credits = 34
        tokens_and_missed_word = ['GLOB', 'GLOB']
        expected_answer =(1, 17.0)
        actual_answer = get_missed_credits(tokens_and_missed_word,no_of_credits,token_roman_value)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''
        test case to find the missed word and missed metal credits 
        '''
    def test_find_missed_word_credits(self):
        split_line = ['GLOB', 'GLOB', 'SILVER', 'IS', '34']
        token_roman_value = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        expected_answer = ("SILVER",17.0)
        actual_answer = find_missed_word_credits ( split_line, token_roman_value )
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''
        test case to find the missed word 
        '''
    def test_get_missed_word(self):
        tokens_and_missed_word = ['GLOB', 'GLOB', 'SILVER']
        token_roman_value = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        expected_answer = "SILVER"
        actual_answer = get_missed_word(tokens_and_missed_word, token_roman_value)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)


if __name__ == '__main__':
    unittest.main()
