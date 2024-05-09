import random

def main():
    print("Khansole Academy")
    x=random.randint(10,100)
    y=random.randint(10,100)
    ans=int(input("What is {} + {}:".format(x,y)))
    print("Your answer: {}".format(ans))
    if ans == x+y:
        print("Correct!")
    else:
        print("Incorrect.")    

    
    
if __name__ == '__main__':
    main()