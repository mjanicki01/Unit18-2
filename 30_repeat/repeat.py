def repeat(phrase, num):
    return_phrase = ""
    if type(num) == int:
        if num == 0:
            return return_phrase
        num_range = list(range(num))
        if num > 0 and type(num) == int:
            for el in num_range:
                return_phrase = return_phrase + phrase
            return return_phrase


    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
