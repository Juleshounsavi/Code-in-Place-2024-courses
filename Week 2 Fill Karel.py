from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    turn_right()
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
        put_beeper()
        turn_right()
        while front_is_clear():
            move()
            put_beeper()
        turn_right()
        turn_right()
        while front_is_clear():
            move()
        turn_right()
    turn_right()
    while front_is_clear():
        move()   



def turn_right():
    for i in range(3):
        turn_left()
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()


   