# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

deck = None
player_hand = None
dealer_hand = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # constructor
        self.cards = []

    def __str__(self):
        s = "Hand contains "
        # return a string representation of a hand
        for i in self.cards:
            s+= str(i) + " "
        return s

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        hasAce = False
        
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if (not hasAce and card.get_rank() == 'A'):
                hasAce = True
        
        if (hasAce and value + 10 <= 21):
            return value + 10
        else:
            return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i = 0
        for card in self.cards:
            card.draw(canvas, [pos[0] + i * (CARD_SIZE[0] + 3), pos[1]])
            i += 1
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for s in SUITS:
            for r in RANKS:
                self.cards.append(Card(s, r))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        s = "Deck contains "
        for i in self.cards:
            s += str(i) + " "
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer_hand, player_hand, score

    if (in_play):
        outcome = "Player forfeits. New hand. Hit or Stand?"
        score -= 1
    else:
        outcome = "New hand. Hit or Stand?"
    
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    deck.shuffle()
    
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    in_play = True

def hit():
    global outcome, in_play, deck, dealer_hand, player_hand, score
 
    # if the hand is in play, hit the player
    if (in_play):
        
        if (player_hand.get_value() < 21 ):
            player_hand.add_card(deck.deal_card())
 
    # if busted, assign a message to outcome, update in_play and score
        if (player_hand.get_value() > 21 ):
            outcome = "You busted. Dealer wins. Deal again?"
            in_play = False
            score -= 1
        elif (player_hand.get_value() == 21 ):
            outcome = "You have 21."
        else:
            outcome = "Hit again?"
   
def stand():
    global outcome, in_play, deck, dealer_hand, player_hand, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if (in_play):
        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(deck.deal_card())
    
        # assign a message to outcome, update in_play and score
        if (dealer_hand.get_value() > 21):
            outcome = "Dealer busted! You win. Deal again?"
            in_play = False
            score += 1
        
        elif (player_hand.get_value() <= dealer_hand.get_value()):
            outcome = str(player_hand.get_value()) + " vs " + str(dealer_hand.get_value()) + " Dealer wins! Deal again?"
            in_play = False
            score -= 1
        else:
            outcome = str(player_hand.get_value()) + " vs " + str(dealer_hand.get_value()) + " You win! Deal again?"
            in_play = False
            score += 1

# draw handler    
def draw(canvas):

    canvas.draw_text("Blackjack", [50,50], 64, "Black")
    
    canvas.draw_text(outcome, [200, 350], 24, "Black")
    
    canvas.draw_text("Score: " + str(score), [500, 100], 24, "Black")
    
    dealer_hand.draw(canvas, [200, 200])
    if (in_play):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [200 + CARD_SIZE[0] / 2, 200 + CARD_SIZE[1] / 2], CARD_BACK_SIZE)
    
    player_hand.draw(canvas, [200, 400])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric