def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    result = min(a, b)
    
    while (a % result != 0) or (b % result != 0):
        if result > 1:
            result -= 1

    return result
