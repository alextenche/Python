testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def first_4(inputList):
    return inputList[:4]

def first_and_last_4(inputList):
    return inputList[:4] + inputList[-4:]

def odds(inputList):
    return inputList[1::2]

def reverse_evens(inputList):
    return inputList[::2][::-1]


print(reverse_evens(testList))