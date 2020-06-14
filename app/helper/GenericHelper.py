from app.helper.RomanToNumber import romanToNumber


def findCredits(splitLine,wordToRomanValue,missingValuesForMetals):
    flag,integerValue = findNumericValueToRoman(splitLine[:len(splitLine)-1], wordToRomanValue)
    flag = 0
    if(splitLine[len(splitLine)-1] in missingValuesForMetals):
        try:
            credits = float(integerValue) * float(missingValuesForMetals[splitLine[len(splitLine)-1]])
            flag = 1
            return flag,credits
        except ValueError:
            return flag,integerValue
    return flag,"I have no idea what you are talking about"


def findNumericValueToRoman(splitLine,wordToRomanValue):
    [flag,romanString] = isTokenInRomanWordsMap(splitLine,wordToRomanValue)
    integralValue = romanToNumber(romanString)
    return flag,integralValue

def getMissedCredits(tokensAndMissedWord,noOfCredits,wordToRomanValue):
    romanString = ""
    for token in tokensAndMissedWord:
        romanString = romanString+wordToRomanValue[token]
    integralValue = romanToNumber(romanString)
    try:
        creditsForMissedWord = float(noOfCredits)/float(integralValue)
        return creditsForMissedWord
    except ValueError:
        return integralValue

def findMissedWordCredits(splitLine,wordToRomanValue):
    tokensAndMissedWord = []
    for token in splitLine:
        tokensAndMissedWord.append(token)
    missedWord = getMissedWord(tokensAndMissedWord[0:len(tokensAndMissedWord)-2],wordToRomanValue)
    missedWordValue = getMissedCredits(tokensAndMissedWord[0:len(tokensAndMissedWord)-3],splitLine[len(splitLine)-1],wordToRomanValue)
    return missedWord,missedWordValue

def getMissedWord(tokensAndMissedWord,wordToRomanValue):
    missedWordsCount = 0
    for token in tokensAndMissedWord:
        if(missedWordsCount == 0):
            if(token not in wordToRomanValue):
                missedWordsCount += 1
                missedWord = token
        else:
            return "I have no idea what you are talking about"
    return missedWord



def isItRomanChar(word):
    romanChars = ["I","V","X","L","C","D","M"]
    Flag = True
    for char in word:
        if(char not in romanChars):
            Flag = False
    return Flag

def isTokenInRomanWordsMap(splitLine,wordToRomanValue):
    romanString = ""
    flag = 1
    for token in splitLine:
        if (token in wordToRomanValue):
            if (isItRomanChar(wordToRomanValue[token])):
                romanString = romanString + wordToRomanValue[token]
            else:
                flag = 0
                return flag,"The character is not in roman numbers"
        else:
            flag = 0
            return flag,"I have no idea what you are talking about"
    return flag,romanString