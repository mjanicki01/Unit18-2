def reverse_string(phrase):
    new_list = [char for char in phrase]
    new_list_rev = new_list[::-1]
    return "".join(new_list_rev)

    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
