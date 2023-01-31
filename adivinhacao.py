def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = 42
    total_de_tentativas = 3
    pontos = 0

    print('''Escolha o nível do jogo:
    (1)Fácil (2)Médio (3)Díficil'''
    )
    nivel= int(input(''))
    if nivel == 1:
        total_de_tentativas = total_de_tentativas +2
    elif nivel == 2:
        total_de_tentativas = total_de_tentativas
    elif nivel == 3:
        total_de_tentativas = total_de_tentativas -2


    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute<1 or chute>100):
            print('Você deve digitar um número entre 1 e 100')
            continue 
        
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou!")
            pontos = pontos + 1000
            print(f'Seu score foi:{pontos}p')
            break
        else:
            if(maior): 
                pontos = pontos - 250
                print("O seu chute foi maior do que o número secreto!")
                print(f'Seu score foi:{pontos}p')
            elif(menor):
                pontos = pontos - 100
                print("O seu chute foi menor do que o número secreto!")
                print(f'Seu score foi:{pontos}p')
        

    

    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()

