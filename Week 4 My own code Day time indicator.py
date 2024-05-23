def main():
    print("Day time indicator")
    h=int(input("What's the time:"))
    if h>=0 :
        if h>=0 and h<12:
            print("This is the morning")
        elif h==12:
            print("This is the noon") 
        elif h>12 and h<=18:
            print("This is the afternoon") 
        elif h>18 and h<=23:
            print("This is the night")  
    else:
        print("Error: the hour must be between 0 and 23.")    

if __name__ == "__main__":
    main()


