# swap values
a = 5
b = 20
a, b = b, a

print('a: ' + str(a))
print('b: ' + str(b))

# product of multiple arguments
def multiply(*args):
    product = 1
    for item in args:
        product *= item
    return product


print(multiply(1, 5, 'alex'))


# enumerate
print(list(enumerate("alexone")))


# different cases for a string
def stringcases(text):
    return text.lower(), text.upper(), text.title(), text[::-1]

print(stringcases("vonavi"))


# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
def combo(iter1, iter2):
    result = []
    for index, item in enumerate(iter1):
        pair = iter1[index], iter2[index]
        result.append(pair)
    return result

print(combo([1, 2, 3], 'abc'))

