import os
import sys
import random

words = ['apple', 'banana', 'grapes', 'melon', 'lemon']

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(goodGuesses, badGuesses, secretWord):
    clear()

    print('tries: {}/7'.format(len(badGuesses)))
    print('')

    for letter in badGuesses:
        print(letter, end = ' ')
    print('\n\n')

    for letter in secretWord:
        if letter in goodGuesses:
            print(letter, end = '')
        else:
            print('_', end = '')
    print('')


def getGuess(guesses):
    while True:
        guess = input('guess a letter: ').lower()
        if len(guess) != 1:
            print('please enter only one letter !')
        elif guess in guesses:
            print('you already guessed that letter !')
        elif not guess.isalpha():
            print('letters please, not numbers !')
        else:
            return guess


def play(done):
    clear()
    secretWord = random.choice(words)
    goodGuesses = set()
    badGuesses = set()
    word_set = set(words)

    while True:
        draw(goodGuesses, badGuesses, secretWord)
        guess = getGuess(goodGuesses | badGuesses)

        if guess in word_set:
            goodGuesses.add(guess)
            if not (word_set.symmetric_difference(goodGuesses)):
                print('you win :) ')
                print('the secret word was {}'.format(secretWord))
                done = True
        else:
            badGuesses.add(guess)
            if len(badGuesses) == 7:
                draw(goodGuesses, badGuesses, secretWord)
                print('you lost :( ')
                print('the secret word was {}'.format(secretWord))
                done = True

        if done:
            playAgain = input("play again ? Y/n").lower()
            if playAgain != 'n':
                return play(False)
            else:
                sys.exit();



print('welcome to letter guess !')
done = False

while True:
    clear()
    play(done)
