def main():
    #get the input fraction
    fraction =  input("Fraction: ")
    #convert the string fraction to a percentage
    tank = convert(fraction)
    #convert to gauge
    gauged = gauge(tank)
    print(gauged)

def convert(fraction):
    while True:
        try:
            #split the numerator a and denominator b
            a,b = fraction.split("/")
            #try to convert it to integer
            x=int(a)
            y=int(b)
            z=x/y
            if (x/y <= 1):
                return int((x*100)/y)
            else:
                fraction =  input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    match percentage:
        case 0|1:
            return "E"
        case 99|100:
            return "F"
        case _:
            return str(percentage)+"%"

if __name__ == "__main__":
    main()