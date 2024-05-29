def main():
    frase = input("Input: ")
    strp_vgls(frase)

def strp_vgls(frase):
    print("Output: ", end="")
    for letter in frase:
        if (letter.lower() not in {"a","e","i","o","u"}):
            print(letter,end="")
    print()
main()
