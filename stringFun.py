def sillycase(word):
    middle = int(len(word) / 2)
    first = test[:middle].lower()
    second = test[middle:].upper()
    return first + second

test = "Abracadabra"


print(sillycase(test))
