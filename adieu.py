import sys

def main():
    names = list()
    
    while True:
        try:
            name = input("Name:")
            names.append(name)
        except EOFError:
            print()
            break
    #print the farwell message
    print("Adieu, adieu, to",names[0],end="")
    if (len(names)==1):
        print()
        sys.exit()

    #se receber mais 2 ou mais
    if len(names) >=2:
        if len(names) >2:
            for i in (1,len(names)-2):
                print(", ",names[i],end="")
                if(i>=len(names)-2):
                    break
            print(",",end="")    
    print(" and ",names[len(names)-1])
        
    #print and last


main()