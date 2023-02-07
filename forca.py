def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")
palavra_secreta = 'banana'
enforcou = False
acertou = False
chute = input("Qual Letra?:")
chute = chute.lower()
index= 0
for letra in palavra_secreta:
    if(chute == letra):
        print(f'Encontrei a letra {letra} na posição {index}')
    index = index +1
    print(index)

    

#while(not enforcou and not acertou):
#  print('Jogando ....')


if(__name__ == "__main__"):
    jogar()
