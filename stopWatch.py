# Stopwatch: The Game

# define global variables
import simplegui
import random
import math

# Global state
count = 0
interval = 100


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    total_seconds = math.floor(t/10)
    minutes = int(total_seconds / 60) 
    seconds = int(total_seconds % 60)
    t_string = str(t)
    miliseconds = t_string[len(str(t))-1:]
    if(seconds < 10):
        return str(minutes)+":0"+str(seconds) +"."+miliseconds
    else:
        return str(minutes)+":"+str(seconds) +"."+miliseconds
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

def stop_handler():
    timer.stop()

def reset_handler():
    global count
    count = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1
    
# define draw handler
def draw(canvas):
    global count
    canvas.draw_text(str(format(count)), (140,150), 36, "Red")

    
# create frame
frame = simplegui.create_frame("Home", 300, 300)

# register event handlers
frame.add_button("Start", start_handler)
frame.add_button("Stop", stop_handler)
frame.add_button("Reset", reset_handler)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
timer.start()