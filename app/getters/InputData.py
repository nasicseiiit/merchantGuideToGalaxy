

'''
The method getInputData will get the data from the input files and return the listOfNumbersFromDirectory and alphaPhrasesFromDictionary
'''


def readData(filePointer):
    return filePointer.read().split('\n')

'''
The method checkFileExistance will check whether the file exist or not and able to open the file
If the file exist and able to open the file then it will return the file pointer
'''

def checkFileExistance(path_to_file):
    try:
        pointer_to_file = open(path_to_file, "r")
        return pointer_to_file
    except IOError:
        return False

''' getting the file data'''
def getFileData(fileName):
    filePointer = checkFileExistance(fileName)
    if(filePointer != False):
        fileData = readData(filePointer)
        return fileData
    print("The input file is not exist")
    return []

