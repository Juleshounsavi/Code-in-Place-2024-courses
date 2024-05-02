from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    for i in range(3):
        pick_beepers_move()

def pick_10_beepers():
    for i in range(10):
        pick_beeper()

def pick_beepers_move():
    move()
    pick_10_beepers()  
    move() 
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()


    

