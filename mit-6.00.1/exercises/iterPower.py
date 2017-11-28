def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    total = 1
    while exp > 0:
        total = total * base
        exp -= 1
    return total
