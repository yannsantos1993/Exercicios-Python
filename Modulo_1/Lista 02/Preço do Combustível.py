LITROS = float(input("Digite a quantidade de litros: "))
TIPO_COMBUSTIVEL = input("(A)lcool ou (G)asolina ?")
if TIPO_COMBUSTIVEL.strip().upper() == "A":
    print("Como você comprou", LITROS, " litros de ÁLCOOL")
    # ALCOOL
    if LITROS < 20:
        TOTAL = LITROS * 2.9 * 0.97
    else:
        TOTAL = LITROS * 2.9 * 0.95
else:
    print("Como você comprou", LITROS, " litros de GASOLINA")
    # GASOLINA
    if LITROS < 20:
        TOTAL = LITROS * 2.9 * 0.96
    else:
        TOTAL = LITROS * 2.9 * 0.94
print("O total é: R$ ", '{:.2f}'.format(TOTAL))