from folder1.defSorte import temp


def erro(chances, valorJogador, valorResposta, valorAntigo, exatoValor):
    extraTeste = 0
    valorAntigo = valorAntigo
    exatoValor = exatoValor
    valorJogador = valorJogador
    valorResposta = valorResposta
    chances = chances

    if chances == 1:
        print("\nNúmero errado!\nNão se preocupe que você ainda possui duas tentativas!\n")
        valorAntigo = valorJogador
        if valorJogador < valorResposta:
            print(f"O número está entre {valorJogador} e 100!")
            extraTeste = valorResposta - valorJogador
            # print(extraTeste)
            # print("ok1")
            print(temp(extraTeste))
            exatoValor = True
            chances = 2
            return chances, valorAntigo, exatoValor
        elif valorJogador > valorResposta:
            print(f"O número está entre 0 e {valorJogador}!")
            extraTeste = valorJogador - valorResposta
            # print(extraTeste)
            # print("ok2")
            print(temp(extraTeste))
            exatoValor = False
            chances = 2
            return chances, valorAntigo, exatoValor
    elif chances == 2:
        print("\nNúmero errado!\nNão se preocupe que você ainda possui uma tentativa!\n")
        if exatoValor:
            if valorJogador < valorResposta:
                print(f"O número está entre {valorJogador} e 100!")
                extraTeste = valorResposta - valorJogador
                # print(extraTeste)
                # print("ok3")
                print(temp(extraTeste))
                chances = 3
                return chances, valorAntigo, exatoValor
            elif valorJogador > valorResposta:
                print(f"O número está entre {valorAntigo} e {valorJogador}!")
                extraTeste = valorJogador - valorResposta
                # print(extraTeste)
                # print("ok4")
                print(temp(extraTeste))
                chances = 3
                return chances, valorAntigo, exatoValor
        elif exatoValor == False:
            if valorJogador < valorResposta:
                print(f"O número está entre {valorJogador} e {valorAntigo}!")
                extraTeste = valorResposta - valorJogador
                # print(extraTeste)
                # print("ok5")
                print(temp(extraTeste))
                chances = 3
                return chances, valorAntigo, exatoValor
            elif valorJogador > valorResposta:
                print(f"O número está entre {valorAntigo} e {valorJogador}!")
                extraTeste = valorJogador - valorResposta
                # print(extraTeste)
                # print("ok6")
                print(temp(extraTeste))
                chances = 3
                return chances, valorAntigo, exatoValor
    elif chances == 3:
        print("\nHoje é um dia em que sua sorte está dormindo!\nMas lembre-se: o que chamamos por sorte é quando oportunidade e habilidade se encontram!\nAté a próxima!\n")
        print(f"O valor que o jogo escolheu foi {valorResposta}\n")
        chances = 4
        print("Fim do Jogo!")
        return chances, valorAntigo, exatoValor
