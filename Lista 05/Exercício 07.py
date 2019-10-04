TIPO = input("Informe de qual figura você deseja calcular a área, (C)írculo, (Q)uadrado ou (T)riângulo?")
if TIPO != "C" or TIPO != "Q" or TIPO !="T":
    print("Escolha uma das entradas válidas: C, Q ou T")
else:
    if TIPO.strip().upper() == "C":
        RAIO = int(input("Informe agora o raio da circunferência a ser calculada: "))
        AREA_C = (3.14) * (RAIO **2)
        print(f"A área da curcunferência equivale a: {AREA_C} m²")
    else:
        if TIPO.strip().upper() == "T":
            ARESTA_TB = int(input("informe agora o tamanho da base a ser calculada: "))
            ARESTA_TH = int(input("informe agora o altura do triângulo a ser calculada: "))
            AREA_T = (ARESTA_TB * ARESTA_TH) / 2
            print(f"A área do triângulo equivale a: {AREA_T} m²")
        else:
            if TIPO.strip().upper() == "Q":
                ARESTA_Q = int(input("informe agora o tamanho da aresta a ser calculada: "))
                AREA_Q = ARESTA_Q * ARESTA_Q
                print(f"A área do quadrado equivale a: {AREA_Q} m²")