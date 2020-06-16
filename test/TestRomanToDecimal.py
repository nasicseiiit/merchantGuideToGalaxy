import unittest

from app.helper.RomanToNumberConversion import romanToNumber


class Test_RomanToDecimal(unittest.TestCase):
    ''' test case to find the decimal value for roman string'''
    def testRomanToDecimal(self):
        romanString = "MCM"
        expectedAnswer = 1900
        actualAnswer = romanToNumber(romanString)
        print(actualAnswer)
        self.assertEqual(expectedAnswer, actualAnswer)

    ''' test case to find the decimal value for invalid roman string'''
    def testRomanToDecimalFailingToConvert(self):
        romanString = "IIII"
        expectedAnswer = "I have no idea what you are talking about"
        actualAnswer = romanToNumber(romanString)
        print(actualAnswer)
        self.assertEqual(expectedAnswer, actualAnswer)


if __name__ == '__main__':
    unittest.main()
