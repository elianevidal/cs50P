import random

def main():
    #Pede o nivel de dificuldade
    level = get_level()

    #Faz 10 perguntas aleatorias
    for i in range(1,10):
        sum1 = generate_integer(level)
        sum2 = generate_integer(level)
        #Dá 3 chances de acerto antes de seguir
        tries = 3
        while tries > 0:
            print(sum1,"+",sum2,"= ",end=""1)
            resp =  input()
            try:
                #Se acertar segue para a próxima pergunta
                if(int(resp) == sum1+sum2):
                   break
                #Se errar imprime EEE
                else:
                    print("EEE")
                    tries -= 1
            #Nao aceita respostas diferentes de inteiro
            except (ValueError, EOFError):
                print("EEE")
        #Imprime a resposta ao ter excedido o número de tentativas
        if(tries == 0):
            print(sum1,"+",sum2,"=",sum1+sum2)

#Garante que o level escolhido está entre os levels disponíveis
def get_level():
    while True:
        level = input("Level: ")
        try:
            if(int(level) in range(1,4)):
                return int(level)
        except (EOFError,ValueError):
            print(end="")

#Gera um número inteiro aleatório de acordo com o nível do jogo
def generate_integer(level):
    max_num = 10 ** level
    return random.randint(1,max_num)

#Em caso do main ser chamado por algum código importado
if __name__ == "__main__":
    main()
