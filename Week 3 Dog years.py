# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    x=int(input("Enter an age in calendar years:"))
    y=x*DOG_YRS_MULTIPLIER
    print("That's {} in dog years!".format(y))

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()



   