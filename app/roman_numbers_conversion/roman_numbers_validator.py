
import re
def validate_roman_number(roman_string):
    roman_number_validator = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return re.search(roman_number_validator, roman_string)

''' to find whether the char is in roman numbers or not '''
def is_it_roman_char(word):
    roman_chars = ["I","V","X","L","C","D","M"]
    return len(list(filter(lambda char: char not in roman_chars, word)))<=0


''' to find whether the formed roman string is in roman numbers or not '''
def is_token_in_token_roman_value_map(split_line,token_roman_value):
    roman_string = ""
    NO_IDEA_ERROR = "I have no idea what you are talking about"
    NOT_ROMAN_CHAR = "The character is not in roman numbers"
    flag = 1
    for token in split_line:
        if (token in token_roman_value):
            if (is_it_roman_char(token_roman_value[token])):
                roman_string = roman_string + token_roman_value[token]
            else:
                flag = 0
                return flag,NOT_ROMAN_CHAR
        else:
            flag = 0
            return flag,NO_IDEA_ERROR
    return flag,roman_string