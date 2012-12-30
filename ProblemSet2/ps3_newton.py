# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...

    poly_len = len(poly)

    answer = 0.0

    for position in range (0, poly_len):
       answer = answer + (poly[position] * (x** position))

    return answer

    

#print evaluatePoly([2, 0, 7, 1], 4)

# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...

    poly_length = len(poly)

    if poly_length < 2:
        return [0.0]
    else:
        new_list = []

        for position in range (1, poly_length):
            new_list.append(float(position * poly[position]))

        return new_list

#print computeDeriv([6, 1, 3, 0])

# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...

    iteration_count = 0
    x_n = x_0

              
    while (abs(evaluatePoly(poly, x_n)) > epsilon):
        #print abs(evaluatePoly(poly, x_n))
        x_n = x_n - (evaluatePoly(poly, x_n) / evaluatePoly(computeDeriv(poly), x_n))
        iteration_count = iteration_count + 1
    return[x_n, iteration_count]

#print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)
