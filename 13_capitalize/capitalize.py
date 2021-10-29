def capitalize(phrase):
    original_list = [char for char in phrase]
    original_list[0:1] = original_list[0].swapcase()
    return "".join(original_list)

    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """