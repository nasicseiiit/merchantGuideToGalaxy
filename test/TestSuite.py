import unittest

from test.TestInputData import Test_FileData
from test.TestRomanToDecimal import Test_RomanToDecimal
from test.TestRomanValidator import RomanValidatorTest
from test.TestValidateSolutionForMuchQueries import ValidateSolutionForMuchQueries
from test.TestValidateSolutionForManyQueries import ValidateSolutionForManyQueries

''' test suite to run the all test cases'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(Test_FileData('testGetFileData'))
    suite.addTest(Test_RomanToDecimal('testRomanToDecimal'))
    suite.addTest(Test_RomanToDecimal('testRomanToDecimalFailingToConvert'))
    suite.addTest(RomanValidatorTest('testIsItRomanChar'))
    suite.addTest(RomanValidatorTest('testIsItRomanCharReturningFalse'))
    suite.addTest(ValidateSolutionForMuchQueries('testValidateSolutionForMuchQueries'))
    suite.addTest(ValidateSolutionForMuchQueries('testValidateErrorMessageForMuchQueries'))
    suite.addTest(ValidateSolutionForManyQueries('testValidateSolutionForManyQueries'))
    suite.addTest(ValidateSolutionForManyQueries('testValidateErrorMessageForManyQueries'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())