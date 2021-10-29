def truncate(phrase, n):
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    if len(phrase) > n or len(phrase) == n:
        return_list = [char for char in phrase]
        return_list_rev = return_list[:(n-3):]
        return_list_rev.append('...')
        return "".join(return_list_rev)
    else:
        return phrase


    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """