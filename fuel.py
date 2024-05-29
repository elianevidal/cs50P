def main():

    while True:
        div =  input("Fraction: ")
        try:
            x = int(div.split("/")[0])
            y = int(div.split("/")[1])
            if perc(x,y):
                break
        except (ValueError, ZeroDivisionError):
            print(end="")

def perc(x,y):
    if x>y:
        return False
    tank = int((x*100)/y)
    match tank:
        case 0|1:
            print("E")
        case 99|100:
            print("F")
        case _:
            print(tank,"%")
    return True

main()
