from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    turn_left()
    ft_clear_mv_pb()
    put_beeper()    
    turn_right()
    for i in range(4):
        move()
    turn_right()
    ft_clear_mv_pb()
    put_beeper()
    turn_left()
    for i in range(4):
        move()
    turn_left()
    ft_clear_mv_pb()
    put_beeper()    
    turn_right()
    for i in range(4):
        move()
    turn_right()
    ft_clear_mv_pb()
    put_beeper()
    turn_left()

def ft_clear_mv_pb():
    while front_is_clear():
        put_beeper()
        move()
def turn_right():
    for i in range(3):
        turn_left()   
if __name__ == '__main__':
    main()






