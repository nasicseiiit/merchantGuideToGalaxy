

'''
The method getInputData will get the data from the input files and return the listOfNumbersFromDirectory and alphaPhrasesFromDictionary
'''


def read_data(file_pointer):
    return file_pointer.read().split('\n')

'''
The method check_file_existance will check whether the file exist or not and able to open the file
If the file exist and able to open the file then it will return the file pointer
'''

def check_file_existance(path_to_file):
    try:
        pointer_to_file = open(path_to_file, "r")
        return pointer_to_file
    except IOError:
        return False

''' getting the file data'''
def get_file_data(file_name):
    file_pointer = check_file_existance(file_name)
    if(file_pointer != False):
        file_data = read_data(file_pointer)
        return file_data
    print("The input file is not exist")
    return []