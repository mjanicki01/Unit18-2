def multiple_letter_count(phrase):
    new_dict = {
        char: phrase.count(char) for char in set(phrase)
    }
    return new_dict

"""Return dict of {ltr: frequency} from phrase.

    >>> multiple_letter_count('yay')
    {'y': 2, 'a': 1}

    >>> multiple_letter_count('Yay')
    {'Y': 1, 'a': 1, 'y': 1}
"""