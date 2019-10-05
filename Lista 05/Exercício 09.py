NUM = int(input("Digite um número entre 0 e 9 para que possamos adivinhar o número que você escolher:"))
if NUM not in (0,1,2,3,4,5,6,7,8,9):
    print("Por favor escolha apenas um número entre 0 e 9")
else:
    if NUM == 0:
        N = "ZERO"
    else:
        if NUM >0 and NUM <=1:
            N = "UM"
        else:
            if NUM > 1 and NUM <= 2:
                N = "DOIS"
            else:
                if NUM > 2 and NUM <= 3:
                    N = "TRÊS"
                else:
                    if NUM > 3 and NUM <= 4:
                        N = "QUATRO"
                    else:
                        if NUM > 4 and NUM <= 5:
                            N = "CINCO"
                        else:
                            if NUM > 5 and NUM <= 6:
                                N = "SEIS"
                            else:
                                if NUM > 6 and NUM <= 7:
                                    N = "SETE"
                                else:
                                    if NUM > 7 and NUM <= 8:
                                        N = "OITO"
                                    else:
                                        if NUM > 8 and NUM <= 9:
                                            N = "NOVE"
                                        else:
                                            None
    print(f"Com base em adivinhação, ousamos em dizer que o número escolhido foi {N} !!!")