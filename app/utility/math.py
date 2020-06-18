'''
it is a multiplication utility
it will try to convert the given string to float if any issue it will return the string else it will return the muliplied valiue.
'''
def multiply(integer_value,missed_metal_value):
    try:
        credits = float(integer_value) * float(missed_metal_value)
        flag = 1
        return flag, credits
    except ValueError:
        return flag, integer_value
'''
it is a division utility
it will try to convert the given string to float if any issue it will return the string else it will return the divided valiue.
'''
def divide(no_of_credits,integer_value):
    try:
        creditsForMissedWord = float(no_of_credits)/float(integer_value)
        return creditsForMissedWord
    except ValueError:
        return integer_value