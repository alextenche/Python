def collect_vowels(s):
    """ (str) -> str

    Return the vowels (a, e, i, o, and u) from s.

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('xyz')
    '1'
    """

    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char
    return vowels
