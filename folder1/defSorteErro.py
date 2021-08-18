from folder1.defSorte import temp


def erro(chances, valorJogador, valorResposta, valorAntigo):
    extraTeste = 0
    valorAntigo = valorAntigo
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
            print("ok1")
            print(temp(extraTeste))
            exatoValor = True
            chances = 2
            return chances, valorAntigo
        elif valorJogador > valorResposta:
            print(f"O número está entre 0 e {valorJogador}!")
            extraTeste = valorJogador - valorResposta
            # print(extraTeste)
            print("ok2")
            print(temp(extraTeste))
            exatoValor = False
            chances = 2
            return chances, valorAntigo
    elif chances == 2:
        print("Não se preocupe que você ainda possui uma tentativa!")
        if exatoValor:
            if valorJogador < valorResposta:
                print(f"O número está entre {valorJogador} e 100!")
                extraTeste = valorResposta - valorJogador
                # print(extraTeste)
                print("ok3")
                print(temp(extraTeste))
                chances = 3
                return chances, valorAntigo
            elif valorJogador > valorResposta:
                print(f"O número está entre {valorAntigo} e {valorJogador}!")
                extraTeste = valorJogador - valorResposta
                # print(extraTeste)
                print("ok4")
                print(temp(extraTeste))
                chances = 3
                return chances, valorAntigo
        elif exatoValor == False:
            if valorJogador < valorResposta:
                print(f"O número está entre {valorJogador} e {valorAntigo}!")
                extraTeste = valorResposta - valorJogador
                # print(extraTeste)
                print("ok5")
                print(temp(extraTeste))
                chances = 3
                return chances, valorAntigo
            elif valorJogador > valorResposta:
                print(f"O número está entre {valorAntigo} e {valorJogador}!")
                extraTeste = valorJogador - valorResposta
                # print(extraTeste)
                print("ok6")
                print(temp(extraTeste))
                chances = 3
                return chances, valorAntigo
    elif chances == 3:
        print("Hoje é um dia em que sua sorte está dormindo! Mas lembre-se: o que chamamos por sorte é quando oportunidade e habilidade se encontram!\nAté a próxima!")
        print(f"O valor que o jogo escolheu foi {valorResposta}")
        chances = 4
        print("Fim do Jogo!")
        return chances, valorAntigo
