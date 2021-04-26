import random

def jogar():
    print("Bem vindo ao jogo de adivinhacao!")

    tentativas = 0
    pontos = 1000

    numero_secreto = random.randrange(1, 101)

    print("Qual o nivel de dificuldade?")
    print("(1) facil\n(2) medio\n(3) dificil")

    nivel = int(input("Defina o nivel: "))

    if (nivel == 1):
        tentativas = 3
    elif (nivel == 2):
        tentativas = 2
    elif (nivel == 3):
        tentativas = 1
    else:
        print("Opcao errada, jogo encerrado!")
        exit()

    print("Pontuacao inicial: ", pontos)
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite o seu numero entre 1 e 100: "))
        print("Voce digitou:", chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        
        if (chute < 1 or chute > 100) :
            print("Digite um numero entre 1 e 100!")
            continue
        elif (acertou):
            print("Voce acertou!")
            break
        elif (maior):
            print("Voce errou! O seu chute eh maior que o numero secreto.")
        else:
            print("Voce errou! O seu chute eh menor que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        print("Sua pontucao agora eh ", pontos)

    print("\n\n\nPontuação final: ", pontos)
    print("Numero secreto era ", numero_secreto)
    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()