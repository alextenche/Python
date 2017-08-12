def binary_search(search_list, value_to_find):
    """ (list, object) -> int

    Precondition: search_list is sorted from smallest to largest, and
    all the items in can be compared to value_to_find.

    Return the index of the first occurrence of value_to_find in search_list, or
    return -1 if value_to_find is not found.

    >>> binary_search([2, 3, 5, 7], 2)
    0
    >>> binary_search([2, 3, 5, 5], 5)
    2
    >>> binary_search([2, 3, 5, 7], 8)
    -1
    """
    begin = 0
    end = len(search_list) - 1

    while begin <= end:
        current_pos = (begin + end) // 2
        if search_list[current_pos] < value_to_find:
            begin = current_pos + 1
        else:
            end = current_pos - 1

    if begin == len(search_list) or search_list[begin] != value_to_find:
        return -1
    else:
        return begin


if __name__ == '__main__':
    import doctest

    doctest.testmod()
