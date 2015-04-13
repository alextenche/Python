# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user39_nCiwRp8v3x_2.py

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
outcome_player = ""
outcome_dealer = ""
score = 0
reveal = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# the global deck
deck = []

#player and dealer deck
player_hand = []
dealer_hand = []

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
        self.hand_list = []

    def __str__(self):
        ans = "Hand contains "
        for i in range(len(self.hand_list)):
            ans += self.hand_list[i].get_suit() + self.hand_list[i].get_rank() + " "
        return ans
      
    def add_card(self, card):
        self.hand_list.append(card)

    def get_value(self):
        hand_value = 0
        # calculate hand_value with aces as 1
        for i in range(len(self.hand_list)):
            hand_value += VALUES[self.hand_list[i].get_rank()]
           
        # if the hand has an ace, then add 10 to hand value if it doesn't bust
        for i in range(len(self.hand_list)):
            if not (VALUES[self.hand_list[i].get_rank()] == 1):
                return hand_value
            else:
                if (hand_value + 10 <= 21):
                    return hand_value + 10
                else:
                    return hand_value
    
    def draw(self, canvas, pos):
        for  i in range(len(self.hand_list)):
            self.hand_list[i].draw(canvas, [pos[0] + i*80, pos[1]])
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_list = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck_list.append(Card(SUITS[i], RANKS[j]))
                
    def shuffle(self):
        random.shuffle(self.deck_list)

    def deal_card(self):
        random_card = random.randrange(0,len(self.deck_list))
        return self.deck_list.pop(random_card)
    
    def __str__(self):
        ans = "Deck contains "
        for i in range(len(self.deck_list)):
            ans += self.deck_list[i].get_suit() + self.deck_list[i].get_rank() + " "
        return ans
    
    def draw(self, canvas, pos):
        for i in range(len(self.deck_list)):
            self.deck_list[i].draw(canvas, [pos[0] + i*5, pos[1]])
            


#define event handler for Deal button
def deal():
    global outcome_player, outcome_dealer, in_play, deck, player_hand, dealer_hand, score, reveal
    
    if(in_play):
        print "in game !!"
        score -= 1
    
    # create and shuffle the deck
    deck = []
    deck = Deck()
    deck.shuffle()
    reveal = False
    outcome = ""
    in_play = True
    
    # create and add two cards to Player hand
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    # create and add two cards to player hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    # check if somebody win   
    if(dealer_hand.get_value() == 21):
        outcome_dealer = "Dealer wins"
        outcome_player = "Player loses, New Deal ?"
        score -= 1
        reveal = True
        in_play = False
    if(player_hand.get_value() == 21 and dealer_hand.get_value() != 21):
        outcome_dealer = "Dealer loses"
        outcome_player = "Player wins!, New Deal ?"
        score += 1
        reveal = True
        in_play = False
    

    
def hit():
    global in_play, score, outcome_player, outcome_dealer, reveal
 
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            outcome_dealer = "Dealer wins"
            outcome_player = "Player busted, New Deal ?"
            score -= 1
            reveal = True
            in_play = False
        if(player_hand.get_value() == 21):
            outcome_dealer = "Dealer loses"
            outcome_player = "Player wins!, New Deal ?"
            score += 1
            reveal = True
            in_play = False
    # if busted, assign a message to outcome, update in_play and score
    else:
        outcome_dealer = ""
        outcome_player = "New Deal ?"
        
def stand():
    global in_play, score, outcome_player, outcome_dealer, reveal
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    if in_play:
        while(dealer_hand.get_value() <= 17):
            dealer_hand.add_card(deck.deal_card())
            
        if(dealer_hand.get_value() > 21):
            outcome_dealer = "Dealer busted !"
            outcome_player = "Player wins!, New Deal ?"
            score += 1
            reveal = True
            in_play = False
        else:
            if(player_hand.get_value() > dealer_hand.get_value()):
                outcome_dealer = "Dealer loses"
                outcome_player = "Player wins!, New Deal ?"
                score += 1
                reveal = True
                in_play = False
            else:
                outcome_dealer = "Dealer wins"
                outcome_player = "Player loses, New Deal ?"
                score -= 1
                reveal = True
                in_play = False
    else:
        outcome_dealer = ""
        outcome_player = "New Deal ?"
    

# draw handler    
def draw(canvas):
    global player_hand, dealer_hand, in_play, outcome_player, outcome_dealer, reveal, score
    
    if(in_play):
        outcome_player =  "Hit or Stand ?"
        
    # print title
    canvas.draw_text('Blackjack', (25, 50), 42, 'white', 'monospace')
    
    # dealer's hand
    canvas.draw_text('Dealer', (25, 120), 20, 'white', 'monospace')
    dealer_hand.draw(canvas, [25, 150])
    if(not reveal):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                            (25 + CARD_BACK_CENTER[0], 198), CARD_BACK_SIZE)
    
    # player's hand
    canvas.draw_text('Player', (25, 320), 20, 'white', 'monospace')
    player_hand.draw(canvas, [25, 350])
   
    # print score
    canvas.draw_text('Score', (425, 50), 20, 'yellow', 'monospace')
    canvas.draw_text(str(score), (495, 50), 20, 'yellow', 'monospace')
    
    # print outcome messages
    canvas.draw_text(str(outcome_player), (250, 320), 18, 'yellow', 'monospace')
    canvas.draw_text(str(outcome_dealer), (250, 120), 18, 'yellow', 'monospace')
    

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


