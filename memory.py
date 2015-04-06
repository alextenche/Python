# implementation of card game - Memory - Alex Tenche
# http://www.codeskulptor.org/#user39_9zbcN2HIFdLC5AD.py
import simplegui
import random


# helper function to initialize globals
def new_game():
    global turns, memory_deck, exposed, state, first_try, second_try
    
    # creating memory_deck as two decks of (0 - 7)
    memory_deck = [];
    memory_deck = range(8) + range(8)
    random.shuffle(memory_deck)
    
    state = 0
    turns = 0
    first_try = 0
    second_try = 0
    exposed = [False] * 16
    label.set_text("Turn="+str(turns))

    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    spacing = 10
    
    for i in range(16):
        if(exposed[i]):
            canvas.draw_text(str(memory_deck[i]),(spacing, 75), 70, 'white')
        else:
            canvas.draw_line([spacing+15, 0],[spacing+15 ,100],50 - 1,'green')
        spacing += 50
    
    
# define event handlers    
def mouseclick(pos):
    global state, turns, first_try, second_try
    
    # the card that was clicked
    card = pos[0]/50
    
    if(not exposed[card]):
        if state == 0:
            exposed[card] = True
            state = 1
            first_try = card
        elif state == 1:
            exposed[card] = True
            state = 2
            turns += 1
            second_try = card
        else:
            if memory_deck[first_try] != memory_deck[second_try]:
                exposed[first_try] = False
                exposed[second_try] = False

            exposed[card] = True
            first_try = card
            state = 1
        
    label.set_text("Turn="+str(turns))
    
    
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()