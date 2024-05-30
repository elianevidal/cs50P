def main():
    m = int(input("m: "))
    print("E: ",energy(m))


def energy(massa):
    l = 300000000
    return l*l*massa

main()