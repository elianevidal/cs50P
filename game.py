import random

def main():
    while True:
        try:
            level = int(input("Level:"))
            guesser = guessgame(level)
            while True:
                try:
                    guess = int(input("Guess:"))
                    if (guess == guesser):
                        print("Just right!")
                        break
                    elif (guess > guesser):
                        print("Too large!")
                    else:
                        print("Too small!")
                except (EOFError, ValueError):
                    print()
            break
        
        except (EOFError, ValueError):
            print()
def guessgame(level):
    return random.randint(1,level)

main()