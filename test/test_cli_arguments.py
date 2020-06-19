
import unittest

from app.input_processor.cli_rguments import get_cli_arguments

class test_for_cli_arguments(unittest.TestCase):
    '''
    test case to get the file name
    '''
    def test_get_file_name(self):
        try:
            expected_file_name = "../../input_data/input_file"
            actual_file_name = get_cli_arguments()
            print(actual_file_name)
            self.assertEqual(expected_file_name,actual_file_name)
        except:
            IOError


if __name__ == '__main__':
    unittest.main()
