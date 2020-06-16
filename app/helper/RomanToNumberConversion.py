
from app.helper.RomanValidator import validateRomanNumber

'''finding the dicimal number equivalent to romanString'''
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