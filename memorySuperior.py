# implementation of card game - Memory

import simplegui
import random

card_list = list() #contains list of lists - [card value, isFlipped, color]
flipped_cards = 0
recent_cards = [[-1, -1], [-1, -1]] #two cards - [card value, index in card_list]
turn_counter = 0
game_over = False
VICTORY = 'Silver'

# helper function to initialize globals
def new_game():
    global card_list, flipped_cards, recent_cards, turn_counter, game_over
    
    #sets everything to default values
    card_list = list()
    recent_cards = [[-1, -1], [-1, -1]]
    flipped_cards = 0
    turn_counter = 0
    game_over = False
    
    #creates and shuffles cards
    memory_list = range(0,8) + range(0,8)
    random.shuffle(memory_list)
    
    #places created cards in list, face down
    #each card contains: [card value, isFlipped, color]
    for i in range(0, 16):
        card_list.append([memory_list[i], False, 'White'])
        #debug - start with some cards randomly flipped
        #card_list.append([memory_list[i], random.choice([True,False])])
    
    #debugging
#    print card_list
#    for card in card_list: print 'card:', card[0], 'flipped:', card[1]

# helper functions for game over
def is_done():
    #checks to see if every card is flipped
    done = True
    for card in card_list:
        if card[1] == True:
            continue
        else:
            done = False
#    print done
    return done

def end_game():
    #the player won, hurray
    global game_over
    
    #make the last two cards victory-colored
    card_list[recent_cards[0][1]][2] = VICTORY
    card_list[recent_cards[1][1]][2] = VICTORY
    
    #dim the card color some more
    for card in card_list:
        card[2] = 'Gray'
    
    end_timer.stop()
    game_over = True

# helper function to color matching cards
def card_color():
    #double-check that they match, then color them
    if recent_cards[0][0] == recent_cards[1][0]:
        card_list[recent_cards[0][1]][2] = VICTORY
        card_list[recent_cards[1][1]][2] = VICTORY
    color_timer.stop()

# helper function to flip cards and note their values
def card_flip(card):
    #flip the card
    card_list[card][1] = True
    
    #note the value and index of the flipped card
    #recent_cards will hold two cards, this alternates which card is updated
    #[card value, card index in card_list]
    recent_cards[flipped_cards - 1] = [card_list[card][0], card]
    
    #debug
#    print 'revealed value:', str(recent_cards[flipped_cards - 1][0])
#    print 'revealed index:', str(recent_cards[flipped_cards - 1][1])
#    print 'revealed value, index:', str(recent_cards[flipped_cards - 1])
#    print 'recent_cards:', str(recent_cards)

# helper function to let players cheat
def cheat_mode():
    cheat_list = list()
    for card in card_list:
        cheat_list.append(card[0])
    print cheat_list[0:4]
    print cheat_list[4:8]
    print cheat_list[8:12]
    print cheat_list[12:16]

# define event handlers
def mouseclick(pos):
    global flipped_cards, turn_counter
    
    #find the card clicked on:
    index = pos[0]//50 + (pos[1]//100 * 4)
    
    if card_list[index][1] == True:
        #clicking on an flipped card does nothing
        pass
    else:
        if flipped_cards == 0: #starting with no cards flipped
            #count how many cards are flipped, flip a card
            flipped_cards = 1
            card_flip(index)
                                                      
        elif flipped_cards == 1: #one card is flipped
            #count how many cards are flipped, flip a card
            flipped_cards = 2
            card_flip(index)
            
            #second card is now flipped so it's been a turn
            turn_counter += 1
            
            #did the game end? do the recent cards match and need color?
            if is_done():
                end_timer.start()
            elif recent_cards[0][0] == recent_cards[1][0]:
                color_timer.start()
            
        else: #two cards are flipped
            flipped_cards = 1
            
            #check if there is a match
            if recent_cards[0][0] == recent_cards[1][0]:
                #the recent two cards match, set their color to victory
                card_list[recent_cards[0][1]][2] = VICTORY
                card_list[recent_cards[1][1]][2] = VICTORY
                
                #flip a new card
                card_flip(index)
                
            else: #no matches
                #flip over the recent cards
                #recent_cards[0][1] is the index value of that card in card_list
                #take that index value, look it up in card_list
                #then set the isFlipped value at that index to False
                card_list[recent_cards[0][1]][1] = False
                card_list[recent_cards[1][1]][1] = False
                
                #flip a new card
                card_flip(index)
                
    #debugging
#    print '# cards flipped:', str(flipped_cards)
#    print 'Matching cards:', str(recent_cards[0][0] == recent_cards[1][0])
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #drawing the cards
    loc = [25, 0]
    xloc = loc[0]
    yloc = loc[1]
    for card in card_list: #card is a list - [value, isFlipped, color]
        offset = frame.get_canvas_textwidth(str(card[0]), 90) / 2
        if card[1] == True: #if the card is flipped
            canvas.draw_text(str(card[0]), [loc[0] - offset, loc[1]+80], 90, card[2])
        else: #if the card is not flipped
            canvas.draw_line([loc[0], loc[1]], [loc[0], loc[1]+100], 50, "Green")
            #debug - see numbers on facedown cards
#            canvas.draw_text(str(card[0]), [loc[0] - offset, loc[1]+80], 90, card[2])
        
        #card borders
        if game_over == False: border_color = 'White'
        else: border_color = 'Gray'
        canvas.draw_polygon([(loc[0]-25, loc[1]), (loc[0]+25, loc[1]), 
                             (loc[0]+25, loc[1]+100), (loc[0]-25, loc[1]+100)], 
                            1, border_color)
        
#        print 'x:', str(loc[0]) + '/' + str(xloc)
#        print 'y:', str(loc[1]) + '/' + str(yloc)
#        print ''
        
        #increment card locations
        xloc += 50
        loc[0] = (xloc % 200)
        yloc += 25
        loc[1] = (yloc // 100) * 100
    
    #game over text
    text_pos = [50, 90]
    text = text_pos[0]
    if game_over == True:
        for char in "YOUWIN":
            offset2 = frame.get_canvas_textwidth(char, 90) / 2
            canvas.draw_text(char, [text_pos[0] - offset2, text_pos[1]], 90, 'Red')                    
            #print char, text_pos, text
            text_pos[1] += 55
            text += 55
            text_pos[0] = text % 170
        
    label.set_text("Turns = " + str(turn_counter))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 200, 400)
frame.add_button("Reset", new_game)
frame.add_button("Debug", cheat_mode)
label = frame.add_label("Turns = 0")

end_timer = simplegui.create_timer(500, end_game)
color_timer = simplegui.create_timer(500, card_color)
               
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric