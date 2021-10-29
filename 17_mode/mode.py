def mode(nums):
    count = 0
    most_frequent = nums[0]
    for el in nums:
        frequency = nums.count(el)
        if frequency > count:
            count = frequency
            most_frequent = el
    return most_frequent

    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
