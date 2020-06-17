from app.helper.RomanValidator import isTokenInTokenRomanValueMap
from app.helper.RomanToNumberConversion import romanToNumber

''' finding the solutions for the Many queries'''
def answerForQueryMany(splitLine,tokenRomanValue,missingValuesForMetals):
    length = len(splitLine)-1
    noIdeaError = "I have no idea what you are talking about"
    flag,integerValue = answerForQueryMuch(splitLine[:length], tokenRomanValue)
    flag = 0
    if(splitLine[len(splitLine)-1] in missingValuesForMetals):
        try:
            credits = float(integerValue) * float(missingValuesForMetals[splitLine[length]])
            flag = 1
            return flag,credits
        except ValueError:
            return flag,integerValue
    return flag, noIdeaError

''' finding the solutions for the much queries'''
def answerForQueryMuch(splitLine,tokenRomanValue):
    [flag,romanString] = isTokenInTokenRomanValueMap(splitLine,tokenRomanValue)
    integralValue = romanToNumber(romanString)
    return flag,integralValue