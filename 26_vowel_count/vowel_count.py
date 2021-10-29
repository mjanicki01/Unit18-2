def vowel_count(phrase):
    original_list = [char.lower() for char in phrase]
    return_set = {
        el: original_list.count(el) for el in original_list if el in 'aeiou'
    }
    return return_set


    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """