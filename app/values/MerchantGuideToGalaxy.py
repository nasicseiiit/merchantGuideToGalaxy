from app.getters.CliArguments import getCliArguments
from app.getters.InputData import getFileData
from app.helper.MissedWords import findMissedWordCredits
from app.helper.QuerySolutions import answerForQueryMany, answerForQueryMuch
from app.logger.PrintData import printOutputData

''' to give the answe with query text ex: glob prok silver is 68.0'''
def getAnswer(flag,line,answerQuery,startInd):
    if (flag == 1):
        length = len(line) - 1
        answerQuery = line[startInd:length].lower() + "is " + str(answerQuery)
    return answerQuery

''' the method will return the answers for queries '''
def answerQuery(splitLine,tokenRomanValue,missingValuesForMetals):
    line = " "
    line = line.join(splitLine)
    length = len(splitLine)-1
    if(splitLine[1] == "MANY"):
        [flag,answerQuery] = answerForQueryMany(splitLine[4:length],tokenRomanValue,missingValuesForMetals)
        startInd = 20
        answerQuery = getAnswer(flag,line,answerQuery,startInd)
    elif(splitLine[1] == "MUCH"):
        [flag, answerQuery] = answerForQueryMuch(splitLine[3:length],tokenRomanValue)
        startInd = 12
        answerQuery = getAnswer(flag, line, answerQuery, startInd)
    else:
        answerQuery = "Incorrect line type is supplied"
    return answerQuery
'''
The method merchantGuideToGalaxy will give the solutu 
'''
def merchantGuideToGalaxy(fileData):
    missingValuesForMetals = {}
    answersToQueries = []
    tokenRomanValue = {}
    for line in fileData:
        line = line.upper()
        splitLine = line.split()
        if(len(splitLine)==3 and splitLine[1] == 'IS'):
            tokenRomanValue[splitLine[0]] = splitLine[2]
        elif(line.endswith("?")):
            answersToQueries.append(answerQuery(splitLine,tokenRomanValue,missingValuesForMetals))
        elif(line.endswith("CREDITS")):
            [missedWord,missedWordCredits] = findMissedWordCredits(splitLine[:len(splitLine)-1],tokenRomanValue)
            missingValuesForMetals[missedWord] = missedWordCredits
        else:
            answersToQueries.append("Incorrect line type is supplied")
    return answersToQueries

#main method
def main():
    fileName = getCliArguments()
    fileData = getFileData(fileName)
    if len(fileData) > 0:
        answersToQueries = merchantGuideToGalaxy(fileData)
        printOutputData(answersToQueries)

if __name__ == "__main__":
    main() #calling main method