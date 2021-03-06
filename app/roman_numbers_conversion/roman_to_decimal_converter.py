from functools import reduce

from app.roman_numbers_conversion.roman_numbers_validator import validate_roman_number
from constants import error_codes

'''finding the dicimal number equivalent to roman_string'''
def roman_to_decimal(roman_string):
    if(validate_roman_number(roman_string)):
        integer_value = convert_roman_to_decimal(roman_string)
        return integer_value
    return error_codes.ROMAN_NUMBER_ERROR

def convert_roman_to_decimal(roman_string):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for index in range(len(roman_string)):
        int_val = roman_char_to_int(index, int_val, rom_val, roman_string)
    return int_val

''' The method roman_char_to_int will convert the roman char to int with below logic
    If Next char is greater than the previous then it will remove the previous number. 
    ex: XL -> initially int_val is 10
        L value is greater than X valiue so removing X from L
        int_val = 10 + (50 - 2*10) = 4
    Else just add the equivalent integer value of char to the int_val'''
def roman_char_to_int(index, int_val, rom_val, roman_string):
    DOUBLE_NUMBER = 2
    SUBTRACT_ONE = 1
    current_roman_val = rom_val[roman_string[index]]
    previous_roman_val = rom_val[roman_string[index - SUBTRACT_ONE]]
    if index > 0 and current_roman_val > previous_roman_val:
        int_val += current_roman_val - DOUBLE_NUMBER * previous_roman_val
    else:
        int_val += current_roman_val
    return int_val