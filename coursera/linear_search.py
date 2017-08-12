def linear_search(L, v):
    ''' (list, object) -> int

    return the first occurrence of v in L, or -1 if not found

    >>>linear_searc([1, 2, 3, 4], 1)
    0
    >>>linear_searc([1, 2, 3, 4], 3)
    2
    >>>linear_searc([1, 2, 3, 4], 8)
    -1
    '''

    i = 0
    while i != len(L) | v != L[i]:
        i += 1

    if i == len(L):
        return -1
    else:
        return i
