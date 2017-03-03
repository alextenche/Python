
import random

secretNumber = random.randint(1, 10)
guesses = []

def game():
    while len(guesses) < 5:
        try:
            guess = int(input("guess a number between 1 and 10: "))
        except:
            print("{} is not a number".format(guess))
        else:
            if guess == secretNumber:
                print('yes ! the number was {}'.format(secretNumber))
                break
            elif guess < secretNumber:
                print('higher')
            else:
                print('lower')
            guesses.append(guess)
    else:
        print('the number was {}'.format(secretNumber))
    playAgain = input("do you want to play again Y/n ?")
    if playAgain.lower() != 'n' :
        game()
    else:
        print('bye')

game()
