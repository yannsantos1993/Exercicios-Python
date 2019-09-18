N1 = int(input("Informe o primeiro número: "))
N2 = int(input("Informe o segundo número: "))
N3 = int(input("Informe o terceiro número: "))
if N1 < N2 < N3:
    print("A ordem crescente é: ", N1, N2, N3)
else:
    if N1 > N2 > N3:
        print("A ordem crescente é: ", N3, N2, N1)
    else:
        if N2 > N1 < N3:
         print("A ordem crescente é: ", N1, N3, N2)
        else:
            if N3 < N1 > N2:
             print("A ordem crescente é: ", N2, N3, N1)
            else:
                if N2 < N1 < N3:
                 print("A ordem crescente é: ", N2, N1, N3)
                else:
                    if N3 < N1 < N2:
                     print("A ordem crescente é: ", N3, N1, N2)