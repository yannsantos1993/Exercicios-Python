NUM = int(input("Digite um número entre 0 e 9 para que possamos adivinhar o número que você escolher:"))
if NUM == 0:
    N = "Zero"
else:
    if NUM >0 and NUM <=1:
        N = "Um"
    else:
        if NUM > 1 and NUM <= 2:
            N = "Dois"
        else:
            if NUM > 2 and NUM <= 3:
                N = "Três"
            else:
                if NUM > 3 and NUM <= 4:
                    N = "Quatro"
                else:
                    if NUM > 4 and NUM <= 5:
                        N = "Cinco"
                    else:
                        if NUM > 5 and NUM <= 6:
                            N = "Seis"
                        else:
                            if NUM > 6 and NUM <= 7:
                                N = "Sete"
                            else:
                                if NUM > 7 and NUM <= 8:
                                    N = "oito"
                                else:
                                    if NUM > 8 and NUM <= 9:
                                        N = "nove"
                                    else:
                                        None
print(f"Com base em adivinhação, ousamos em dizer que o número escolhido foi {N} !!!")