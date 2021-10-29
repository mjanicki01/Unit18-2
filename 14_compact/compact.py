a_list = [None, 1, 4, "quote", False, (), []]

def compact(lst):
    return_list = []
    for el in lst:
        if el:
            return_list.append(el)
    return return_list

    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """