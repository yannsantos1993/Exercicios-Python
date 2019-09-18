LADO_1 = int(input("Digite o valor do lado 1:"))
LADO_2 = int(input("Digite o valor do lado 2:"))
LADO_3 = int(input("Digite o valor do lado 3:"))
if LADO_1 == LADO_2 != LADO_3 or LADO_1 == LADO_3 != LADO_2 or LADO_2 == LADO_3 !=LADO_1:
    print("O triângulo formado é isósceles")
else:
    if LADO_1 == LADO_2 == LADO_3:
        print("O triângulo formado é equilátero")
    else:
        print("O triângulo formado é escaleno")