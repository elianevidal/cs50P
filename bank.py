def main ():
    answer = input("Greeting:")
    getmoney=value(answer.casefold())
    print("$",getmoney, sep="")

def value(answer):
    answer = " ".join(answer.split()).lower()
    if  ("h" != answer[0]):
        return 100
    else:
        if (("hello") == answer[:5]):
            return 0
        else:
            return 20
        
if __name__ == "__main__":
    main()