def is_palindrome(phrase):
    phrase = phrase.upper()
    phrase = phrase.replace(" ", "")
    new_list = [char for char in phrase]
    new_list_rev = new_list[::-1]
    if new_list == new_list_rev:
        return True
    else:
        return False

    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
