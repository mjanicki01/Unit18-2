def partition(lst, fn):
    return_list_a = []
    return_list_b = []
    for el in lst:
        if fn(el):
            a = el
            return_list_a.append(a)
        else:
            b = el
            return_list_b.append(b)
    return [return_list_a, return_list_b]

def is_even(num):
     return num % 2 == 0

def is_string(el):
     return isinstance(el, str)



""" Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """