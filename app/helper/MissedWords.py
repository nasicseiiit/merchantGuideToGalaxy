from app.helper.RomanToNumberConversion import romanToNumber

''' finding the credits for missed words'''
def getMissedCredits(tokensAndMissedWord,noOfCredits,tokenRomanValue):
    romanString = ""
    for token in tokensAndMissedWord:
        romanString = romanString+tokenRomanValue[token]
    integralValue = romanToNumber(romanString)
    try:
        creditsForMissedWord = float(noOfCredits)/float(integralValue)
        return creditsForMissedWord
    except ValueError:
        return integralValue

'''finding the missed words and it's credits'''
def findMissedWordCredits(splitLine,tokenRomanValue):
    tokensAndMissedWord = []
    for token in splitLine:
        tokensAndMissedWord.append(token)
    missedWord = getMissedWord(tokensAndMissedWord[0:len(tokensAndMissedWord)-2],tokenRomanValue)
    missedWordValue = getMissedCredits(tokensAndMissedWord[0:len(tokensAndMissedWord)-3],splitLine[len(splitLine)-1],tokenRomanValue)
    return missedWord,missedWordValue

''' finding the missed words'''
def getMissedWord(tokensAndMissedWord,tokenRomanValue):
    missedWordsCount = 0
    for token in tokensAndMissedWord:
        if(missedWordsCount == 0):
            if(token not in tokenRomanValue):
                missedWordsCount += 1
                missedWord = token
        else:
            return "I have no idea what you are talking about"
    return missedWord
