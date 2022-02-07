
import pedraPapelTesoura
import adivinhacao
import forca

print("********************************")
print("Escolha o seu Jogo!")
print("********************************")


print("(1) Forca (2) Adivinhação (3) Forca")

jogo = int(input("Qual Jogo?"))


if(jogo == 1):
    print("Jogando Pedra, Papel e Tesoura")
    pedraPapelTesoura.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()
elif (jogo == 3):
    print("Jogando Forca")
    forca.jogar()
