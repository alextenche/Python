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
