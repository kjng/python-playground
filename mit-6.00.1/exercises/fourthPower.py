def square(x):
    return x * x

def fourthPower(x):
    '''
    x: int or float.
    '''
    x = square(x)
    x = square(x)
    return x

def fourthPower2(x):
    '''
    x: int or float.
    '''
    return pow(x, 4)
