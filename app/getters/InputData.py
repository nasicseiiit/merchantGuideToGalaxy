

'''
The method getInputData will get the data from the input files and return the listOfNumbersFromDirectory and alphaPhrasesFromDictionary
'''


def readData(filePointer):
    fileData = []
    for line in filePointer:
        line = line.strip()
        fileData.append(line)
    return fileData


'''
The method checkFileExistance will check whether the file exist or not and able to open the file
If the file exist and able to open the file then it will return the file pointer
'''

def checkFileExistance(path_to_file):
    try:
        pointer_to_file = open(path_to_file, "r")  # opening the file
        return pointer_to_file  # if file exist then returning the filePonter
    except IOError:  # catching the error
        return False  # if the file does not exist returning the False

''' getting the file data'''
def getFileData(fileName):
    filePointer = checkFileExistance(fileName)  # method to check whether the file exist or not
    if(filePointer != False):
        fileData = readData(filePointer)
        return fileData
    else:
        print("The input file is not exist")
        return []

