def list_check(lst):
    return_list = []
    for el in lst:
        if type(el) == list:
            return_list.append(True)
        else:
            return_list.append(False)
    if return_list.count(False) == 0:
        return True
    else:
        return False


    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
