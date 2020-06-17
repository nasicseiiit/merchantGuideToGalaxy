
from app.helper.RomanValidator import validateRomanNumber

'''finding the dicimal number equivalent to romanString'''
def romanToNumber(romanString):
    romanNumberError = "This is not a valid roman number"
    if(validateRomanNumber(romanString)):
        inegralValue = convertRomanToNumber(romanString)
        return inegralValue
    return romanNumberError

def romanCharToInt(index,int_val,rom_val,romanString):
    if index > 0 and rom_val[romanString[index]] > rom_val[romanString[index - 1]]:
        int_val += rom_val[romanString[index]] - 2 * rom_val[romanString[index - 1]]
    else:
        int_val += rom_val[romanString[index]]
    return int_val

def convertRomanToNumber(romanString):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for index in range(len(romanString)):
        int_val = romanCharToInt(index,int_val,rom_val,romanString)
    return int_val