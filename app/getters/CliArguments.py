
#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###
'''
User specify the input file as command line argument or by providing the input else by default the application will pick up Input inside data/inputFile as input file.
'''
import sys
import os

def getCliArguments():
    print("\n#####################################################################")
    print("### Welcome to the Merchant Guide to Galaxy Program ###")
    print("#####################################################################\n")
    fileName = input("Please enter the input filename: ")

    if len(fileName) == 0 and len(sys.argv) == 2:
        fileName = sys.argv[1]
    elif len(fileName) ==0 :
        current_directory = os.getcwd()
        fileName = (os.path.abspath(os.path.join(current_directory, os.pardir)))
        fileName = (os.path.abspath(os.path.join(fileName, os.pardir)))
        fileName = fileName + "/data/inputFile"
    return fileName