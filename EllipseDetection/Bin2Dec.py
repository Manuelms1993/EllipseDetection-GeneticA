def bin2dec(vector):
    integ = 0
    for i in range(len(vector)):
        integ = integ + vector[i]*2**i
    return integ
