def find_greater_numbers(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1
    return count


    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4
        How is 4 the accurate return value? Should be 3

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0

    nums_list = [num for num in nums]
    count = 0
    count_index = 0
    for el in nums_list:
        if nums_list.index(el) == nums_list[-1]:
            return
        else:
            next_el_index = (nums_list.index(el)) + 1
            if el < nums_list[next_el_index]:
                count = count + 1
    print(count)

    """