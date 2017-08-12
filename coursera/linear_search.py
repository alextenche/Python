def linear_search(L, v):
    """ (list, object) -> int

    return the first occurrence of v in L, or -1 if not found

    >>> linear_search([1, 2, 3, 4], 1)
    0
    >>> linear_search([1, 2, 3, 4], 3)
    2
    >>> linear_search([1, 2, 3, 4], 8)
    -1
    """

    i = 0
    while i != len(L) and v != L[i]:
        i = i + 1

    if i == len(L):
        return -1
    else:
        return i


if __name__ == '__main__':
    import doctest

    doctest.testmod()
