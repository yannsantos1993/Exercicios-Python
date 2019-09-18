print("Dizer o valor total da compra")
quantidade_comprada=float(input("Digite a quantidade de maçãs compradas:"))
print("A quantidade comprada foi:", quantidade_comprada)
menos_uma_duzia=quantidade_comprada*1.30
uma_duzia=quantidade_comprada*1.00
if quantidade_comprada>=12:
    print("O custo total da compra é: R$","%.2f" %uma_duzia)
else:
    print("O custo total da compra é: R$","%.2f" %menos_uma_duzia)