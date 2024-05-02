from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    while front_is_clear():
        move()
    turn_right()
    move_turn_left_move()
    pick_beeper()
    for i in range(2):
        turn_right()
    while front_is_clear():
        move()
    move_turn_right_move()
    

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_turn_left_move():
    move()
    turn_left()
    move()

def move_turn_right_move():
    turn_right()
    move()
    turn_right()


    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()


   