import re

def validateRomanNumber(romanString):
    result = 0
    romanNumberValidator = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    if(re.search(romanNumberValidator,romanString)):
        result = 1
    return result

def romanToNumber(romanString):
    if(validateRomanNumber(romanString)):
        inegralValue = convertRomanToNumber(romanString)
        return inegralValue
    return "I have no idea what you are talking about"

def convertRomanToNumber(romanString):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(romanString)):
        if i > 0 and rom_val[romanString[i]] > rom_val[romanString[i - 1]]:
            int_val += rom_val[romanString[i]] - 2 * rom_val[romanString[i - 1]]
        else:
            int_val += rom_val[romanString[i]]
    return int_val