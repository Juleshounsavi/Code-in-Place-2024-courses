
def main():
    count = 1
    p_num = int(input("Enter num:"))
    while True:
        num = int(input("Enter num:"))
        if num < p_num:
            break
        else:
            p_num = num
        count = count + 1
    print("Thanks for playing!")
    print("Sequence length: {}".format(count))            


if __name__ == "__main__":
    main()