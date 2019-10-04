JOG1 = input("Para começarmos o jogo escolha: (P)ar ou (I)mpar?")
if JOG1.upper() != "P" and JOG1.upper() != "I":
    print("Por favor digite apenas P se quiser escolher Par oi I se quiser escolher Ímpar")
else:
    # é uma opção valida
    if JOG1.upper() == "P":
        print("Jogador #2, Como o jogador #1 escolheu Par, você ficará com Ímpar, ok!")
        JOG2 = "I"
    else:
        print("Jogador #2, Como o jogador #1 escolheu Ímpar, você ficará com Par, ok!")
        JOG2 = "P"

    print("Agora vamos lá! Jogadores, escolham seus números, prometo que o outro jogador não vai ver!")
    J1 = int(input("Jogador 1, nos informe o seu número:"))
    J2 = int(input("Jogador 2, nos informe o seu número:"))

    SOMA = J1 + J2
    RESTO = SOMA % 2
    if RESTO == 0 and JOG1.upper() == "P":
        print(f"Parabéns Jogador #1, você ganhou! pois o número final {SOMA} é par!")
    else:
        if RESTO == 0 and JOG2.upper() == "P":
            print(f"Parabéns Jogador #2, você ganhou! pois o número final {SOMA} é par!")
        else:
            if RESTO != 0 and JOG1.upper() == "I":
                print(f"Parabéns Jogador #1, você ganhou! pois o número final {SOMA} é ímpar!")
            else:
                if RESTO != 0 and JOG2.upper() == "I":
                    print(f"Parabéns Jogador #2, você ganhou! pois o número final {SOMA} é ímpar!")
                else:
                    None
