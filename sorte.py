import random


valorResposta = random.randrange(0, 100)
valorResposta = int(valorResposta)
# print(valorResposta)
valorAntigo = 0
exatoValor = True

print("Melhor de três é o jogo que definirá o nível da sua sorte hoje!\nVocê tem 3 chances para advinhar o número certo que está entre 0 e 100!\nVamos lá:\n")
chances = 1

while chances < 4:
    try:
        valorJogador = int(input(f"Informe o {chances}º número: "))
        if not 0 <= valorJogador <= 100:
            print("Escreva um número inteiro entre 0 e 100!")
            raise ValueError("ERRO 1A")
        else:
            if valorJogador == valorResposta and chances == 1:
                print("Seu nível de sorte está magnífico hoje! Número certo na primeira jogada! Parabéns e aproveite!")
                break
            elif valorJogador == valorResposta and chances == 2:
                print("Você pode até achar que não tem sorte, mas a verdade é que só precisou de duas tentativas para acertar! Parabéns!")
                break
            elif valorJogador == valorResposta and chances == 3:
                print("Sua sorte não está na melhor forma, mas pense que só precisou de três tentativas! Parabéns!")
                break
            elif valorJogador != valorResposta and chances == 1:
                print("Não se preocupe que você ainda possui duas tentativas!")
                valorAntigo = valorJogador
                if valorJogador < valorResposta:
                    print(f"O número está entre {valorJogador} e 100!")
                    exatoValor = True
                elif valorJogador > valorResposta:
                    print(f"O número está entre 0 e {valorJogador}!")
                    exatoValor = False
                chances = 2
                raise ValueError("Número incorreto!")
            elif valorJogador != valorResposta and chances == 2:
                print("Não se preocupe que você ainda possui uma tentativa!")
                if exatoValor:
                    if valorJogador < valorResposta:
                        print(f"O número está entre {valorJogador} e 100!")
                    elif valorJogador > valorResposta:
                        print(f"O número está entre {valorAntigo} e {valorJogador}!")
                elif exatoValor == False:
                    if valorJogador < valorResposta:
                        print(f"O número está entre {valorJogador} e {valorAntigo}!")
                    elif valorJogador > valorResposta:
                        print(f"O número está entre 0 e {valorJogador}!")
                chances = 3
                raise ValueError("Número incorreto!")
            elif valorJogador != valorResposta and chances == 3:
                print("Hoje é um dia em que sua sorte está dormindo! Mas lembre-se: o que chamamos por sorte é quando oportunidade e habilidade se encontram! Até a próxima!")
                print(f"O valor que o jogo escolheu foi {valorResposta}")
                chances = 4
                print("Fim do Jogo!")
    except ValueError as e:
        print("ERRO - ", e)
