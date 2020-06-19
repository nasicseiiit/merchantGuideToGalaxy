'''
The method merchant_guide_to_galaxy will give the solutu
'''
from app.input_processor.cli_rguments import get_cli_arguments
from app.input_processor.input_data import get_file_data
from app.output_processor.print_data import print_output_data
from app.starter_code.merchant_guide_to_galaxy import processing_line
from constants import error_codes


def merchant_guide_to_galaxy(file_data):
    missing_values_for_metals = {}
    answer_to_queries = []
    token_roman_value = {}
    file_data = list(map(lambda x: x.upper(), file_data))
    for line in file_data:
        split_line = line.split()
        processing_line(line, split_line, error_codes.LINE_ERROR, missing_values_for_metals, answer_to_queries, token_roman_value)
    return answer_to_queries

#main method
def main():
    file_name = get_cli_arguments()
    file_data = get_file_data(file_name)
    if len(file_data) > 0:
        answer_to_queries = merchant_guide_to_galaxy(file_data)
        print_output_data(answer_to_queries)

if __name__ == "__main__":
    main()