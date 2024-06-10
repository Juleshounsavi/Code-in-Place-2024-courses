from karel.stanfordkarel import *

def main():
    task()
    
    move()
    move()

    task()
    
    move()
    move()

    task()
      
    move()
    move()

    task()


def task():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_right()
    turn_right()
    move()
    turn_left()    

def turn_right():
    turn_left()
    turn_left()
    turn_left()    
    
   

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()