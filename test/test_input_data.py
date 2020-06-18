
import unittest

from app.input_processor.input_data import get_file_data


class test_file_data(unittest.TestCase):
    '''
    test case to read the input_data from the input file
    '''
    def test_get_file_data(self):
        file_name = "/Users/apple/Documents/GitHub/merchant_guide_to_galaxy/input_data/test_input_file"
        expected_file_data = ["pish is I", "pork is V", "how much is pish pork ?"]
        actual_file_data = get_file_data(file_name)
        print(actual_file_data)
        self.assertEqual(expected_file_data,actual_file_data)

if __name__ == '__main__':
    unittest.main()
