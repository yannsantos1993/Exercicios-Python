TIPO = input("Informe de qual figura você deseja calcular a área, (C)írculo, (Q)uadrado ou (T)riângulo?").strip().upper()
if TIPO not in ("C, Q, T"):
    print("Escolha uma das entradas válidas: C, Q ou T")
else:
    if TIPO == "C":
        RAIO = int(input("Informe agora o raio da circunferência a ser calculada: "))
        AREA_C = (3.14) * (RAIO **2)
        print(f"A área da curcunferência equivale a: {AREA_C} m²")
    else:
        if TIPO == "T":
            ARESTA_TB = int(input("informe agora o tamanho da base a ser calculada: "))
            ARESTA_TH = int(input("informe agora o altura do triângulo a ser calculada: "))
            AREA_T = (ARESTA_TB * ARESTA_TH) / 2
            print(f"A área do triângulo equivale a: {AREA_T} m²")
        else:
            if TIPO == "Q":
                ARESTA_Q = int(input("informe agora o tamanho da aresta a ser calculada: "))
                AREA_Q = ARESTA_Q * ARESTA_Q
                print(f"A área do quadrado equivale a: {AREA_Q} m²")