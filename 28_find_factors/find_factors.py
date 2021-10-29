def find_factors(num):
    numlist = range(1,num)
    return_array = []
    for factor in numlist:
        if num % factor == 0:
            return_array.append(factor)
    return_array.append(num)
    return return_array


    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
