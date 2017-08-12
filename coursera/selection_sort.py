def get_index_of_smallest(list, current_index):
    """ (list, int) -> int

    Return the index of the smallest item in L[i:].

    >>> get_index_of_smallest([2, 7, 3, 5], 1)
    2
    """

    index_of_smallest = current_index
    for i in range(current_index + 1, len(list)):
        if list[i] < list[index_of_smallest]:
            index_of_smallest = i

    return index_of_smallest


def selection_sort(list_to_sort):
    """ (list) -> NoneType

    Sort the items of given list from smallest to largest.

    >>> L = [3, 7, 2, 5]
    >>> selection_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    list_length = len(list_to_sort)
    for i in range(list_length):
        index_of_smallest = get_index_of_smallest(list_to_sort, i)
        list_to_sort[index_of_smallest], list_to_sort[i] = list_to_sort[i], list_to_sort[index_of_smallest]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
