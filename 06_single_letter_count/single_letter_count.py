def single_letter_count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count





    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """