def same_frequency(num1, num2):
    num1_list = [int(x) for x in str(num1)]
    num2_list = [int(x) for x in str(num2)]
    num1_dict = {el:num1_list.count(el) for el in num1_list}
    num2_dict = {el:num2_list.count(el) for el in num2_list}
    if num1_dict == num2_dict:
        return True
    else:
        return False

"""Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
"""