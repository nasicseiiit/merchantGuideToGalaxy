from app.roman_numbers_conversion.missed_words_finder import find_missed_word_credits
from app.roman_numbers_conversion.solutions_finder import answer_for_query_many, answer_for_query_much
from constants import error_codes

''' to give the answe with query text ex: glob prok silver is 68.0'''
def get_answer(flag, line, answe_query, start_ind):
    SUBTRACT_ONE = 1
    if (flag == 1):
        length = len(line) - SUBTRACT_ONE
        answe_query = line[start_ind:length].lower() + "is " + str(answe_query)
    return answe_query

''' the method will return the answers for queries '''
def answer_queries(split_line, token_roman_value, missing_values_for_metals):
    SUBTRACT_ONE = 1
    line = " "
    line = line.join(split_line)
    length = len(split_line)-SUBTRACT_ONE
    if(split_line[1] == "MANY"):
        START_IND = 4
        [flag,answe_query] = answer_for_query_many(split_line[START_IND:length], token_roman_value, missing_values_for_metals)
        START_IND = 20
        answer_to_query = get_answer(flag,line,answe_query,START_IND)
    elif(split_line[1] == "MUCH"):
        START_IND = 3
        [flag, answe_query] = answer_for_query_much(split_line[START_IND:length], token_roman_value)
        START_IND = 12
        answer_to_query = get_answer(flag, line, answe_query, START_IND)
    else:
        answer_to_query = error_codes.LINE_ERROR
    return answer_to_query
'''
The method processingLine will process each line of file input_data 
'''
def processing_line(line, split_line, LINE_ERROR, missing_values_for_metals, answer_to_queries, token_roman_value):
    if (len(split_line) == 3 and split_line[1] == 'IS'):
        token_roman_value[split_line[0]] = split_line[2]
    elif (line.endswith("?")):
        answer_to_queries.append(answer_queries(split_line, token_roman_value, missing_values_for_metals))
    elif (line.endswith("CREDITS")):
        SUBTRACT_ONE = 1
        [missed_word, missed_word_credits] = find_missed_word_credits(split_line[:len(split_line) - SUBTRACT_ONE], token_roman_value)
        missing_values_for_metals[missed_word] = missed_word_credits
    else:
        answer_to_queries.append(LINE_ERROR)