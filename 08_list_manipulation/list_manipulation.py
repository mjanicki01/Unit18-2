a_list = [1, 2, 3, 4, 5, 6]


def list_manipulation(lst, command, location, value=None):
    if command.upper() == "ADD":
        if location.upper() == "BEGINNING":
            lst[0] = value
        elif location.upper() == "END":
            lst[-1] = value
        return lst
    elif command.upper() == "REMOVE":
        if location.upper() == "BEGINNING":
            print(lst[0])
            lst.pop(0)
        elif location.upper() == "END":
            print(lst[-1])
            lst.pop()
    else:
        return None



    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
