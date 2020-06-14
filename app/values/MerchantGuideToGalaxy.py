


from app.getters.InputData import getFileData
from app.helper.GenericHelper import findMissedWordCredits, findNumericValueToRoman, findCredits
from app.logger.PrintData import printOutputData

def answerQuery(splitLine,wordToRomanValue,missingValuesForMetals):
    line = " "
    line = line.join(splitLine)
    if(splitLine[1] == "MANY"):
        [flag,answerQuery] = findCredits(splitLine[4:len(splitLine)-1],wordToRomanValue,missingValuesForMetals)
        if(flag==1):
            answerQuery = line[20:len(line) - 1].lower() + "is " + str(answerQuery)
    elif(splitLine[1] == "MUCH"):
        [flag, answerQuery] = findNumericValueToRoman(splitLine[3:len(splitLine)-1],wordToRomanValue)
        if (flag == 1):
            answerQuery = line[11:len(line)-1].lower()+"is "+str(answerQuery)
    else:
        answerQuery = "Incorrect line type is supplied"
    return answerQuery

def merchantGuideToGalaxy(fileData):
    missingValuesForMetals = {}
    answersToQueries = []
    wordToRomanValue = {}
    for line in fileData:
        line = line.upper()
        splitLine = line.split()
        if(len(splitLine)==3 and splitLine[1] == 'IS'):
            wordToRomanValue[splitLine[0]] = splitLine[2]
        elif(line.endswith("?")):
            answersToQueries.append(answerQuery(splitLine,wordToRomanValue,missingValuesForMetals))
        elif(line.endswith("CREDITS")):
            [missedWord,missedWordCredits] = findMissedWordCredits(splitLine[:len(splitLine)-1],wordToRomanValue)
            missingValuesForMetals[missedWord] = missedWordCredits
        else:
            answersToQueries.append("Incorrect line type is supplied")
    return answersToQueries

#main method
def main():
    fileData = getFileData()
    if len(fileData) > 0:
        answersToQueries = merchantGuideToGalaxy(fileData)
        printOutputData(answersToQueries)

if __name__ == "__main__":
    main() #calling main method