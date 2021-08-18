from folder1.defSorteAcerto import acerto
from folder1.defSorteErro import erro
import random


valorResposta = random.randrange(0, 101)
valorResposta = int(valorResposta)
# print(valorResposta)
valorAntigo = 0
exatoValor = True
extraTeste = 0

print("Melhor de três é o jogo que definirá o nível da sua sorte hoje!\nVocê tem 3 chances para advinhar o número certo de 0 e 100!\nVamos lá:\n")
chances = 1

while chances < 4:
    try:
        valorJogador = int(input(f"Informe o {chances}º número: "))
        if not 0 <= valorJogador <= 100:
            print("Escreva um número inteiro entre 0 e 100!")
            raise ValueError("ERRO 1A")
        else:
            if valorJogador == valorResposta:
                print(acerto(chances))
                break
            elif valorJogador != valorResposta:
                chances = erro(chances, valorJogador, valorResposta)
                raise ValueError("Número incorreto!")

    except ValueError as e:
        print("FALHOU - ", e)
