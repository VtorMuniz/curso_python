import forca
import adivinhacao
def escolhe_jogo():
    
    print('''Escolha seu jogo:
    (1)Jogo da Forca (2) Jogo de adivinhacao''')
    jogo = int(input(""))

    if jogo == 1:
        print('Jogando Forca')
        forca.jogar()
    else:
        print('Jogando Adivinhação')
        adivinhacao.jogar()

#if(__name__ == "__main__"):
escolhe_jogo()