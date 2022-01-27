import random

rodadas = int(input("MELHOR DE 3 OU MELHOR DE 5?"))

placar = 0
placarIA = 0

count = 1
while (count <= rodadas):
    print(f"rodada {count}")

    escolha = input("Olha entre PEDRA, PAPEL ou TESOURA: ")
    alternativas = ['PEDRA', 'PAPEL', 'TESOURA']
    escolhaIA = random.choice(alternativas)

    if escolhaIA == escolha:
        print(f"O dois jogadores escolheram {escolha}, é um empate")
    elif (escolha == 'PEDRA'):
        if(escolhaIA == 'TESOURA'):
            print(f"{escolha} ganha de {escolhaIA}! Você venceu!")
            placar = placar + 1
        elif (escolhaIA == 'PAPEL'):
            print(f"{escolha} perde de {escolhaIA}! Você perdeu!")
            placarIA = placarIA + 1
    elif(escolha == 'TESOURA'):
        if(escolhaIA == 'PEDRA'):
            print(f'{escolha} perde para {escolhaIA}! Você perdeu!')
            placarIA = placarIA + 1
        elif (escolhaIA == 'PAPEL'):
            print(f'{escolha} ganha de {escolhaIA}! Você venceu!')
            placar = placar + 1
    elif(escolha == 'PAPEL'):
        if(escolhaIA == 'PEDRA'):
            print(f'{escolha} ganha de {escolhaIA}! Você venceu!')
            placar = placar + 1
        elif(escolhaIA == 'TESOURA'):
            print(f'{escolha} perde para {escolhaIA}! Você perdeu!')
            placarIA = placarIA + 1
    count = count + 1

print(f'Placar final foi  de : Você {placar} X {placarIA} IA')
