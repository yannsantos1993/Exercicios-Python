MORANGO = float(input("Digite a quantidade em KG de morangos comprados:"))
MACA = float(input("Digite a quantidade em KG de maçãs compradas:"))
if MORANGO > 5:
    P_MORANGO = MORANGO*2.2
else:
    P_MORANGO = MORANGO*2.5

if MACA > 5:
    P_MACA = MACA*1.5
else:
    P_MACA = MACA*1.8

TOTAL_PARCIAL = P_MORANGO + P_MACA

if TOTAL_PARCIAL > 25 or (MORANGO + MACA) > 8:
    TOTAL_COMPRA = TOTAL_PARCIAL*0.9
else:
    TOTAL_COMPRA = TOTAL_PARCIAL
print("O valor total da sua compra a ser pago foi de: R$", '{:.2f}'.format(TOTAL_COMPRA))