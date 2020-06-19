from app.roman_numbers_conversion.roman_to_decimal_converter import roman_to_decimal
from app.utility.math import divide
from constants import error_codes

''' finding the credits for missed words'''
def get_missed_credits(tokens_and_missed_word, no_of_credits, token_roman_value):
    roman_string = ""
    for token in tokens_and_missed_word:
        roman_string = roman_string+token_roman_value[token]
    integer_value = roman_to_decimal(roman_string)
    return divide(no_of_credits, integer_value)

'''finding the missed words and it's credits'''
def find_missed_word_credits ( split_line, token_roman_value ):
    SUBTRACT_ONE = 1
    SUBTRACT_TWO = 2
    SUBTRACT_THREE = 3
    tokens_and_missed_word = list(map(str, split_line))
    tokens_missed_word_length = len(tokens_and_missed_word)
    split_line_length = len(split_line)
    missed_word = get_missed_word(tokens_and_missed_word[:tokens_missed_word_length-SUBTRACT_TWO], token_roman_value)
    missed_word_value = get_missed_credits(tokens_and_missed_word[:tokens_missed_word_length-SUBTRACT_THREE], split_line[split_line_length-SUBTRACT_ONE], token_roman_value)
    return missed_word, missed_word_value

''' finding the missed words'''
def get_missed_word(tokens_and_missed_word, token_roman_value):
    missed_word_count = 0
    for token in tokens_and_missed_word:
        if(missed_word_count > 0):
            return error_codes.NO_IDEA_ERROR
        [missed_word_count, missed_word] = is_token_in_token_roman(token, token_roman_value, missed_word_count)
    return missed_word

def is_token_in_token_roman(token,token_roman_value, missed_word_count):
    INCREMENT_ONE = 1
    if (token not in token_roman_value):
        missed_word_count += INCREMENT_ONE
        missed_word = token
        return missed_word_count, missed_word
    return missed_word_count, ""