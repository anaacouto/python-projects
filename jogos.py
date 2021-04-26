import forca
import adivinhacao

def escolhe_jogo():
    print("Bem vindo ao menu de jogos")
    print("\n(1) forca\n(2) adivinhacao")

    jogo = int(input("Escolha o jogo: "))

    if (jogo == 1):
        forca.jogar()
    else:
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()