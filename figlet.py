import sys
import random
from pyfiglet import Figlet

#Thats not CS50 proposed set, but... I like mine better

def main():
    #call self
    figlet = Figlet()
    figletfonts = figlet.getFonts()


    if (len(sys.argv) > 3) or (len(sys.argv) == 2):
        sys.exit("Uso: $python fliget.py [-f or --font {Fontname}] ")
    elif len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figletfonts))
    else:
    #se o numero de argumentos for 2 verifica se o 1o eh -f ou --font e se o 2o eh uma fonte valida
    #figlet.setFont(font=f)
        match sys.argv[1]:
            case "-f" | "--font":
                for i in figletfonts:
                    if sys.argv[2] == i:
                        figlet.setFont(font=i)
                        break
                else:
                    for i in figletfonts:
                        print(i)
                    sys.exit("A fonte nao está listada. Escolha uma das fontes acima.")

    s = input("Input: ")
    print(figlet.renderText(s))

if __name__ == "__main__":
    main()