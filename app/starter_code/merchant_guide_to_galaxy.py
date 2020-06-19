from app.input_processor.cli_rguments import get_cli_arguments
from app.input_processor.input_data import get_file_data
from app.roman_numbers_conversion.missed_words_finder import find_missed_word_credits
from app.roman_numbers_conversion.solutions_finder import answer_for_query_many, answer_for_query_much
from app.output_processor.print_data import print_output_data
from constants import error_codes

''' to give the answe with query text ex: glob prok silver is 68.0'''
def get_answer(flag,line,answe_query,start_ind):
    if (flag == 1):
        length = len(line) - 1
        answe_query = line[start_ind:length].lower() + "is " + str(answe_query)
    return answe_query

''' the method will return the answers for queries '''
def answer_queries(split_line,token_roman_value,missing_values_for_metals):
    line = " "
    line = line.join(split_line)
    length = len(split_line)-1
    if(split_line[1] == "MANY"):
        [flag,answe_query] = answer_for_query_many(split_line[4:length],token_roman_value,missing_values_for_metals)
        start_ind = 20
        answer_to_query = get_answer(flag,line,answe_query,start_ind)
    elif(split_line[1] == "MUCH"):
        [flag, answe_query] = answer_for_query_much(split_line[3:length],token_roman_value)
        start_ind = 12
        answer_to_query = get_answer(flag, line, answe_query, start_ind)
    else:
        answer_to_query = error_codes.LINE_ERROR
    return answer_to_query
'''
The method processingLine will process each line of file input_data 
'''
def processing_line(line,split_line,LINE_ERROR,missing_values_for_metals,answer_to_queries,token_roman_value):
    if (len(split_line) == 3 and split_line[1] == 'IS'):
        token_roman_value[split_line[0]] = split_line[2]
    elif (line.endswith("?")):
        answer_to_queries.append(answer_queries(split_line, token_roman_value, missing_values_for_metals))
    elif (line.endswith("CREDITS")):
        [missed_word, missed_word_credits] = find_missed_word_credits(split_line[:len(split_line) - 1], token_roman_value)
        missing_values_for_metals[missed_word] = missed_word_credits
    else:
        answer_to_queries.append(LINE_ERROR)
'''
The method merchant_guide_to_galaxy will give the solutu 
'''
def merchant_guide_to_galaxy(file_data):
    missing_values_for_metals = {}
    answer_to_queries = []
    token_roman_value = {}
    file_data = list(map(lambda x: x.upper(), file_data))
    for line in file_data:
        split_line = line.split()
        processing_line(line,split_line,error_codes.LINE_ERROR,missing_values_for_metals,answer_to_queries,token_roman_value)
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