PRODUTO = float(input("Digite o valor do produto:"))
if PRODUTO < 20:
    LUCRO_45 = PRODUTO + PRODUTO * 0.45
    print("O valor de revenda é: RS", LUCRO_45)
else:
    LUCRO_30 = PRODUTO + PRODUTO *0.30
    print("O valor de revenda é: RS", LUCRO_30)