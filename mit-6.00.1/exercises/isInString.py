def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    
    if len(aStr) == 1:
        return aStr == char
    
    midIndex = int(len(aStr) - 1 / 2)    
    mid = aStr[midIndex]
    
    if mid == char:
        return True
    else:
        if char > mid:
            return isIn(char, aStr[midIndex + 1:])
        elif char < mid:
            return isIn(char, aStr[:midIndex])

print(isIn('z', 'ex'))
