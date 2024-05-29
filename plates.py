def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if ((len(s) > 6) or (len(s) < 2)):
        return False

    ##Rules: Only numbers and letters. Can't begin with number. No numbers beginning with 0 or in between of letters
    #first is letter?
    if (not s[0].isalpha()):
        return False

    previ = s[0]

    #is letter?
    for i in s[1:]:
        if (i.isalpha()):
            #letter is after number
            if (after_number(previ)):
                return False
        else:
            if (not i.isnumeric()):
                return False
    return True


def after_number(bl):
    return bl.isnumeric()


main()