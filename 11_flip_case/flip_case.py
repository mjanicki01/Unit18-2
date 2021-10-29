def flip_case(phrase, to_swap):
    original_list = [char for char in phrase]
    return_list = []
    for el in original_list:
        if el.upper() == to_swap.upper():
            el = el.swapcase()
            return_list.append(el)
        else:
            return_list.append(el)
    return "".join(return_list)





    """

    Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
