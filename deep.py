def main ():
    answer = input("What's is the Answer for the Great Question of Life, Universe, and Everything?")
    answer = answer = " ".join(answer.split())
    deep(answer.casefold())

def deep(answer):
    match answer:
        case "42" | "forty-two"| "forty two":
            print("Yes")
        case _:
            print("No")

main ()