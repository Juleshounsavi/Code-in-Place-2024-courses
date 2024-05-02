from karel.stanfordkarel import *

def main():
    put_beeper()

    for i in range(10):
        move()
        turn_left()
        move()
        put_beeper()
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()    

# don't change this code
if __name__ == '__main__':
    main()



