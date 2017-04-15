
def disemvowel(word):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    wordLetters = list(word)
    result = []

    for letter in wordLetters:
        if letter not in vowels:
            result.append(letter)
    return ''.join(result)



test = 'guadAlupeCIUPA'
newText = disemvowel(test)
print(newText)
