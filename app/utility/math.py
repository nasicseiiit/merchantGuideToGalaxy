
def multiply(integer_value,missed_metal_value):
    try:
        credits = float(integer_value) * float(missed_metal_value)
        flag = 1
        return flag, credits
    except ValueError:
        return flag, integer_value

def divide(no_of_credits,integer_value):
    try:
        creditsForMissedWord = float(no_of_credits)/float(integer_value)
        return creditsForMissedWord
    except ValueError:
        return integer_value