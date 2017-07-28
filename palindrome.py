def is_palindrome_v1(s):
    return reverse(s) == s


def is_palindrome_v2(s):
    n = len(s)
    return s[:n // 2] == reverse(s[n - n // 2:])


def is_palindrome_v3(s):
    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i += 1
        j -= 1

    return j <= i


def reverse(s):
    rev = ''

    for ch in s:
        rev = ch + rev

    return rev


# print(reverse('hello'))

print(is_palindrome_v3('noon'))
print(is_palindrome_v3('racecar'))
print(is_palindrome_v3('dented'))
