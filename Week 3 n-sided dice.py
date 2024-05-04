import random

def main():
    print("Delete this line and write your code here! :)")
    x=int(input("How many sides does your dice have?"))
    y=random.randint(1, x)
    print("Your roll is {}".format(y))

if __name__ == '__main__':
    main()


