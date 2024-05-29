def main ():
    var_name = input("camelCase: ")
    to_snake(var_name)

def to_snake(var_name):
    for letter in var_name:
        if (letter.islower()):
            print(letter, end="")
        else:
            print("",letter.lower(),sep="_", end="")
    print()
if __name__ == "__main__":
    main()