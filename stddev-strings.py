import math
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """

    N = float(len(L))

    if N == 0:
        return float('NaN')

    listLengths = [] 
    for string in L:
        listLengths.append(len(string))

    averageLen = float(sum(listLengths)/N)

    Ex = 0

    for t in listLengths:
        Ex = Ex + (t - averageLen)**2


    return math.sqrt(Ex/N)
    

print stdDevOfLengths(['azcyzjaj', 'jwlvmkycvil', 'uhm'])
