import unittest

from app.helper.RomanValidator import isItRomanChar


class RomanValidatorTest(unittest.TestCase):
    ''' test case to find is the char is in roman numbers with valid roman char'''
    def testIsItRomanChare(self):
        romanChar = "V"
        expectedAnswer = True
        actualAnswer = isItRomanChar(romanChar)
        print(actualAnswer)
        self.assertEqual(expectedAnswer, actualAnswer)

    ''' test case to find is the char is in roman numbers with invalid roman char'''
    def testIsItRomanCharReturningFalse(self):
        romanChar = "T"
        expectedAnswer = False
        actualAnswer = isItRomanChar(romanChar)
        print(actualAnswer)
        self.assertEqual(expectedAnswer, actualAnswer)




if __name__ == '__main__':
    unittest.main()
