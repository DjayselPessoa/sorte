from folder1.defSorte import temp


def erro(chances, valorJogador, valorResposta):
    extraTeste = 0
    valorAntigo = 0
    exatoValor = True
    valorJogador = valorJogador
    valorResposta = valorResposta
    chances = chances

    if chances == 1:
        print("Não se preocupe que você ainda possui duas tentativas!")
        valorAntigo = valorJogador
        if valorJogador < valorResposta:
            print(f"O número está entre {valorJogador} e 100!")
            extraTeste = valorResposta - valorJogador
            # print(extraTeste)
            print(temp(extraTeste))
            exatoValor = True
            chances = 2
            return chances
        elif valorJogador > valorResposta:
            print(f"O número está entre 0 e {valorJogador}!")
            extraTeste = valorJogador - valorResposta
            # print(extraTeste)
            print(temp(extraTeste))
            exatoValor = False
            chances = 2
            return chances
    elif chances == 2:
        print("Não se preocupe que você ainda possui uma tentativa!")
        if exatoValor:
            if valorJogador < valorResposta:
                print(f"O número está entre {valorJogador} e 100!")
                extraTeste = valorResposta - valorJogador
                # print(extraTeste)
                print(temp(extraTeste))
                chances = 3
                return chances
            elif valorJogador > valorResposta:
                print(f"O número está entre {valorAntigo} e {valorJogador}!")
                extraTeste = valorJogador - valorResposta
                # print(extraTeste)
                print(temp(extraTeste))
                chances = 3
                return chances
        elif exatoValor == False:
            if valorJogador < valorResposta:
                print(f"O número está entre {valorJogador} e {valorAntigo}!")
                extraTeste = valorResposta - valorJogador
                # print(extraTeste)
                print(temp(extraTeste))
                chances = 3
                return chances
            elif valorJogador > valorResposta:
                print(f"O número está entre 0 e {valorJogador}!")
                extraTeste = valorJogador - valorResposta
                # print(extraTeste)
                print(temp(extraTeste))
                chances = 3
                return chances
    elif chances == 3:
        print("Hoje é um dia em que sua sorte está dormindo! Mas lembre-se: o que chamamos por sorte é quando oportunidade e habilidade se encontram!\nAté a próxima!")
        print(f"O valor que o jogo escolheu foi {valorResposta}")
        chances = 4
        print("Fim do Jogo!")
        return chances
