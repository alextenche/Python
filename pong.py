# http://www.codeskulptor.org/#user39_pD5kO8uldog0jee.py
# Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = []
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
paddle1_vel = 0
paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT / 2]
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if(direction == RIGHT):
        ball_vel = [-(random.randrange(120, 240)) / 60, -(random.randrange(60, 180)) / 60]
    else:
        ball_vel = [random.randrange(120, 240) / 60, -(random.randrange(60, 180)) / 60]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
  
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "white")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "white")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "white")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # bounce from top and bottom walls
    if ((ball_pos[1] < BALL_RADIUS) or (ball_pos[1] > HEIGHT - BALL_RADIUS)):
        ball_vel[1] *= -1
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "#00FF00", "#00FF00")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    
    if((paddle1_pos[1] < HALF_PAD_HEIGHT) or (paddle1_pos[1] > HEIGHT-HALF_PAD_HEIGHT)):
        paddle1_pos[1] -= paddle1_vel
        
    if((paddle2_pos[1] < HALF_PAD_HEIGHT) or (paddle2_pos[1] > HEIGHT-HALF_PAD_HEIGHT)):
        paddle2_pos[1] -= paddle2_vel
        
    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT],[paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, "#00FF00")
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT],[paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, "#00FF00")
    
    # determine whether paddle and ball collide
    if (ball_pos[0] < PAD_WIDTH + BALL_RADIUS):
        ball_vel[0] *= 1.1
        if((ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT)):
            ball_vel[0] *= -1.1
        else:
            score2 += 1
            print "point for player 2  -  ", score1 , " / " , score2
            LEFT = False
            spawn_ball(LEFT)
        
    elif (ball_pos[0] > WIDTH-PAD_WIDTH - BALL_RADIUS):
        ball_vel[0] *= 1.1
        if((ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT)):
            ball_vel[0] *= -1.1
        else:
            score1 += 1
            print "point for player 1  -  ", score1 , " / " , score2
            LEFT = True
            spawn_ball(LEFT)
    
    # draw scores
    canvas.draw_text(str(score1), [150,75], 55, "#00FF00")
    canvas.draw_text(str(score2), [420,75], 55, "#00FF00")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -8
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 8
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -8
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 8
   

def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
    
def restart():
    global score1, score2, paddle1_pos, paddle2_pos
    score1 = 0
    score2 = 0
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT / 2]
    print "restarting ..."
    new_game()

    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_label('pong ')
frame.add_label('')
frame.add_label('player 1:  w, s')
frame.add_label('')
frame.add_label('player 2: up, down')
frame.add_label('')
frame.add_button("Restart", restart, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
