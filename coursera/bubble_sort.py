def bubble_sort(list_to_sort):
    """ (list) -> NoneType

    Sort list from smallest to largest.

    >>> L = [7, 3, 5, 2]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    end = len(list_to_sort) - 1

    while end != 0:
        for i in range(end):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
        end -= 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
