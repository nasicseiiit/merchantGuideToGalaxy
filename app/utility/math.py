'''
it is a multiplication utility
it will try to convert the given string to float if any issue it will return the string else it will return the muliplied valiue.
'''
def multiply(a, b):
    flag = 0
    try:
        result = float(a) * float(b)
        flag = 1
        return flag, result
    except ValueError:
        return flag, a
'''
it is a division utility
it will try to convert the given string to float if any issue it will return the string else it will return the divided valiue.
'''
def divide(a, b):
    flag = 0
    try:
        flag = 1
        return flag, float(a)/float(b)
    except ValueError:
        return flag, b