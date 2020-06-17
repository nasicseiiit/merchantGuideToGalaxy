
import re
def validateRomanNumber(romanString):
    romanNumberValidator = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return re.search(romanNumberValidator, romanString)

''' to find whether the char is in roman numbers or not '''
def isItRomanChar(word):
    romanChars = ["I","V","X","L","C","D","M"]
    Flag = True
    for char in word:
        if(char not in romanChars):
            Flag = False
    return Flag

''' to find whether the formed roman string is in roman numbers or not '''
def isTokenInTokenRomanValueMap(splitLine,tokenRomanValue):
    romanString = ""
    flag = 1
    for token in splitLine:
        if (token in tokenRomanValue):
            if (isItRomanChar(tokenRomanValue[token])):
                romanString = romanString + tokenRomanValue[token]
            else:
                flag = 0
                return flag,"The character is not in roman numbers"
        else:
            flag = 0
            noIdeaError = "I have no idea what you are talking about"
            return flag,noIdeaError
    return flag,romanString