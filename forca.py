def jogar():
    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    acertou = False
    enforcou = False
    print("Bem vindo ao jogo da forca!")
    print(letras_acertadas)
    while(not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
                letras_acertadas[index] = letra
                print("Encontrei a letra {} na posicao {}".format(letra, index))
            index = index + 1
        print(letras_acertadas)
        letras_faltando = letras_acertadas.count("_")
        if (letras_faltando == 0):
            acertou = True
            print("Você acertou a palavra!")
        else:
            print("Faltam {} letras".format(letras_faltando))
    print("Jogo finalizado!")

if (__name__ == "__main__"):
    jogar()