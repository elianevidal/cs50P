def main():
    due = 0
    while (due < 50):
        coin = int(input("Amount Due: "))
        if ((coin == 5) or (coin == 10) or (coin == 20)):
            due = due + coin
            if (due >=50):
                break
    print("Change Owemed: ",change(due))


def change (due):
    return due % 50


main()