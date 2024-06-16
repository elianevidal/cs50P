def main():
    frase = input("Input: ")
    print("Output: ", end="")
    print(shorten(frase))


##New code with return will make tests easier
def shorten(frase):
    msg=""
    for letter in frase:
        if (letter.lower() not in {"a","e","i","o","u"}):
            msg=msg+letter
    return msg

if __name__ == "__main__":
    main()