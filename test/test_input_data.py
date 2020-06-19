
import unittest

from app.input_processor.input_data import get_file_data, check_file_existance


class test_file_data(unittest.TestCase):
    '''
    test case with a valid file name
    '''
    def test_check_file_existance(self):
        file_name = "/Users/apple/Documents/GitHub/merchantGuideToGalaxy/input_data/test_input_file"
        pointer_to_file = check_file_existance(file_name)
        self.assertNotEqual(pointer_to_file, False)
        pointer_to_file.close()

    '''
        test case with a invalid file
    '''

    def test_check_file_existance_error(self):
        file_name = "/Users/apple/Documents/GitHub/merchantGuideToGalaxy/input_data/ramdom_file"
        pointer_to_file = check_file_existance(file_name)
        self.assertEqual(pointer_to_file, False)

    '''
    test case to read the input_data from the input file
    '''
    def test_get_file_data(self):
        file_name = "/Users/apple/Documents/GitHub/merchantGuideToGalaxy/input_data/test_input_file"
        expected_file_data = ["pish is I", "pork is V", "how much is pish pork ?"]
        actual_file_data = get_file_data(file_name)
        print(actual_file_data)
        self.assertEqual(expected_file_data, actual_file_data)

    '''
        test case to read the input_data from the input file if the file does not exist
    '''
    def test_get_file_data_empty_list(self):
        file_name = "/Users/apple/Documents/GitHub/merchantGuideToGalaxy/input_data/random_file"
        expected_file_data = []
        actual_file_data = get_file_data(file_name)
        print(actual_file_data)
        self.assertEqual(expected_file_data, actual_file_data)

if __name__ == '__main__':
    unittest.main()
