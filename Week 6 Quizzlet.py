
def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    count = 0
    for key, value in translations.items():
        ans = input(f"What is the Spanish translation for {key}? ")
        if ans.lower() == value:
            count += 1
            print("That is correct!\n")
        else:
            print(f"That is incorrect, the Spanish translation for {key} is {value}.\n")
    print("You got {}/8 words correct, come study again soon!".format(count))
if __name__ == '__main__':
    main()
