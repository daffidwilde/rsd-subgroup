def get(n):
    ''' 
    Returns the n'th Fibonacci number.
    
    '''

    if n in [0,1]:
        return 1

    return get(n - 1) + get(n - 2)
