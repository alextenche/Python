# http://www.codeskulptor.org/#user39_hnv7Zbuj00dzmXu.py
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100

# helper function to start and restart the game
def new_game():
    global secret_number
    global remaining
    secret_number = random.randrange(0, num_range)
    print "New game. Range is from 0 to " + str(num_range)
    remaining = int(math.ceil(math.log(num_range,2)))
    print "Number of remaining guesses is " + str(remaining)
    print


# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    print "Restarting..."
    new_game()

def range1000():
    global num_range
    num_range = 1000
    print "Restarting..."
    new_game()
    
def input_guess(guess):
    global entered_number
    global secret_number
    global num_range
    global remaining
    
    print "Guess was " + guess
    remaining -= 1
    print "Number of remaining guesses is " + str(remaining)
    entered_number = int(guess)
   
    if(entered_number == secret_number):
        print("Correct, Congratulations!")
        print
        new_game()
    elif(entered_number < secret_number):
        print("Higher!")
        print
    else:
        print("Lower!")
        print
        
    if(remaining <= 0):
        print("You ran out of guesses. The number was " + str(secret_number))
        print
        new_game()
        
    

    
# create frame
frame = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess:", input_guess, 200)

frame.start()

# call new_game 
new_game()