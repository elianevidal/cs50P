def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

##Checks if its a valid state car's plate
##Rules: Only numbers and letters. Can't begin with number. No numbers beginning with 0 or in between of letters
    
def is_valid(s):
    ##Won't accept places that is not between 2 and 6 caracters long
    if ((len(s) > 6) or (len(s) < 2)):
        return False

    # is first is letter?
    if (not s[0].isalpha()):
        return False

    previ = s[0]

    #is letter?
    for i in s[1:]:
        if (i.isalpha()):
            #letter is after number?
            if (after_number(previ)):
                return False
        else:
            ##is a number beginning with 0?
            if (i.isnumeric()):
                if (not after_number(previ)):
                    if (i == "0"):
                        return False
            else:
                return False
        previ=i
    return True


def after_number(bl):
    return bl.isnumeric()

        
if __name__ == "__main__":
    main()