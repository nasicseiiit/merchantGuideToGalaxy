import unittest

from app.values.MerchantGuideToGalaxy import answerQuery


class ValidateSolutionForMuchQueries(unittest.TestCase):
    '''test case to find the solutions for much queries'''
    def testValidateSolutionForMuchQueries(self):
        inputQuery =['HOW', 'MUCH', 'IS', 'PISH', 'TEGJ', 'GLOB', 'GLOB', '?']
        inputTokenMap = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        expectedAnswer = "pish tegj glob glob is 42"
        actualAnswer = answerQuery(inputQuery,inputTokenMap,[])
        print(actualAnswer)
        self.assertEqual(expectedAnswer, actualAnswer)

    '''test case to find the solutions for much queries'''
    def testValidateErrorMessageForMuchQueries(self):
        inputQuery = ['HOW', 'MUCH', 'WOOD', 'COULD', 'A', 'WOODCHUCK', 'CHUCK', 'IF', 'A', 'WOODCHUCK', 'COULD', 'CHUCK', 'WOOD', '?']
        inputTokenMap = {'GLOB': 'I', 'PROK': 'V', 'PISH': 'X', 'TEGJ': 'L'}
        expectedAnswer = "I have no idea what you are talking about"
        actualAnswer = answerQuery(inputQuery, inputTokenMap, [])
        print(actualAnswer)
        self.assertEqual(expectedAnswer, actualAnswer)