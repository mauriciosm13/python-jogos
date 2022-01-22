import random

print("********************************")
print("Bem vindo no jogo de adivinhação")
print("********************************")

numero_secreto = random.randrange(1, 101)
total_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel_input = int(input("Defina um nível: "))
if(nivel_input == 1):
    total_tentativas = 20
elif(nivel_input == 2):
    total_tentativas = 10
elif(nivel_input == 3):
    total_tentativas = 5
else:
    print("Necessário selecionar um nível valido")

for rodada in range(1, total_tentativas + 1):
    print("Tentativa: {} de  {}".format(rodada, total_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))

    if(chute < 1 or chute > 100):
        print("Você deve digitar entre 1 e 100", chute)
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto

    if (acertou):
        print("Parabéns! Você acertou -- Pontuação total foi de {}".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que número secreto")
        else:
            print("Você errou! O seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Numéro secreto é: ",numero_secreto)
print("Fim de jogo")
