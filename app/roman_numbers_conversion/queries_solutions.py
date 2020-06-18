from app.roman_numbers_conversion.roman_numbers_validator import is_token_in_token_roman_value_map
from app.roman_numbers_conversion.roman_to_number_conversion import roman_to_number
from app.utility.math import multiply
from constants import error_codes

''' finding the solutions for the Many queries'''
def answe_for_query_many(split_line,token_roman_value,missing_values_for_metals):
    length = len(split_line)-1
    [flag,integer_value]= answer_for_query_much(split_line[:length], token_roman_value)
    if(flag and split_line[length] in missing_values_for_metals):
        return multiply(integer_value,missing_values_for_metals[split_line[length]])
    return flag, error_codes.NO_IDEA_ERROR

''' finding the solutions for the much queries'''
def answer_for_query_much(split_line,token_roman_value):
    [flag,roman_string] = is_token_in_token_roman_value_map(split_line,token_roman_value)
    if(flag):
       return flag,roman_to_number(roman_string)
    return flag,roman_string
