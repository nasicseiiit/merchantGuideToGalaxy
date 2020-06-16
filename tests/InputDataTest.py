
import unittest

from app.getters.InputData import checkFileExistance, getFileData


class DictionaryDataTest(unittest.TestCase):
    '''
    test case to read the data from the input file
    '''
    def testGetDicitonaryData(self):
        fileName = "../data/testInputFile"
        expectedFileData = ['pish is I', 'pork is V', 'how much is pish pork ?']
        actualFileData = getFileData(fileName)
        print(actualFileData)
        self.assertEqual(expectedFileData,actualFileData)

if __name__ == '__main__':
    unittest.main()
