import unittest

from app.values.MerchantGuideToGalaxy import answerQuery


class ValidateSolutionForManyQueries(unittest.TestCase):
    '''test case to find the solutions for many queries'''
    def testValidateSolutionForManyQueries(self):
        inputQuery =['HOW', 'MANY', 'CREDITS', 'IS', 'GLOB', 'PROK', 'SILVER', '?']
        inputTokenMap = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        missingElementsCredits = {'SILVER': 17.0, 'GOLD': 14450.0, 'IRON': 195.5}
        expectedAnswer = "glob prok silver is 68.0"
        actualAnswer = answerQuery(inputQuery,inputTokenMap,missingElementsCredits)
        print(actualAnswer)
        self.assertEqual(expectedAnswer, actualAnswer)

    '''test case to find the solutions for many queries'''
    def testValidateErrorMessageForManyQueries(self):
        inputQuery = ['HOW', 'MANY', 'CREDITS', 'IS', 'GLOB', 'PROK', 'GOLD', '?']
        inputTokenMap = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        missingElementsCredits = {'SILVER': 17.0, 'GOLD': 14450.0, 'IRON': 195.5}
        expectedAnswer = "glob prok gold is 57800.0"
        actualAnswer = answerQuery(inputQuery, inputTokenMap, missingElementsCredits)
        print(actualAnswer)
        self.assertEqual(expectedAnswer, actualAnswer)