# Stopwatch: The Game
# http://www.codeskulptor.org/#user39_Vf84M1cElewtXi8.py

# define global variables
import simplegui
import random
import math

# Global state
count = 0
interval = 100
counter1 = 0
counter2 = 0
miliseconds = 0
timer_stop = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global miliseconds
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
    global timer_stop
    
    timer_stop = False
    timer.start()

def stop_handler():
    global timer_stop
    global counter1
    global counter2
    global miliseconds
    
    if(timer_stop == False):
        counter1 += 1
    
    if(miliseconds == '0'):
        if(timer_stop == False):
            counter2 += 1
            
    timer_stop = True
    timer.stop()

def reset_handler():
    global count
    global counter1
    global counter2
    
    timer.stop()
    count = 0
    counter1 = 0
    counter2 = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1
    
# define draw handler
def clock(canvas):
    global count
    global counter1
    global counter2
    canvas.draw_text(str(format(count)), (100,150), 45, '#f3172d')
    canvas.draw_text(str(counter1)+"/"+str(counter2), (210,45), 35, '#66FF33')

    
# create frame
frame = simplegui.create_frame("Home", 300, 300)

# register event handlers
frame.add_button("Start", start_handler, 200)
frame.add_label("")
frame.add_button("Stop", stop_handler, 200)
frame.add_label("")
frame.add_button("Reset", reset_handler, 200)
frame.set_draw_handler(clock)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
