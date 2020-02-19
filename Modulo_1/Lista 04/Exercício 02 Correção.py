''' Leia a idade, a altura e o peso de 3 pessoas. Calcule e mostre:
a) A quantidade de pessoas com idade superior a 20 anos;
b) A média das alturas das pessoas com idade entre 15 e 18 anos;
c) A porcentagem de pessoas com peso inferior a 60 quilos entre todas as pessoas analisadas.'''
IDADE_1 = int(input("Digite a idade da primeira pessoa:"))
ALTURA_1 = float(input("Digite a altura da primeira pessoa:"))
PESO_1 = float(input("Digite o peso da primeira pessoa:"))
IDADE_2 = int(input("Digite a idade da segunda pessoa:"))
ALTURA_2 = float(input("Digite a altura da segunda pessoa:"))
PESO_2 = float(input("Digite o peso da segunda pessoa:"))
IDADE_3 = int(input("Digite a idade da terceira pessoa:"))
ALTURA_3 = float(input("Digite a altura da terceira pessoa:"))
PESO_3 = float(input("Digite o peso da terceira pessoa:"))

ACIMA_50 = 0
if IDADE_1 > 50:
    ACIMA_50 += 1
if IDADE_2 > 50:
    ACIMA_50 += 1
if IDADE_3 > 50:
    ACIMA_50 += 1
print(f"{ACIMA_50} tem idade superior a 50 anos.")

QTD_10_20 = 0
SOMA_ALT = 0
if IDADE_1 >= 15 and IDADE_1 <= 18:
    QTD_10_20 += 1
    SOMA_ALT += ALTURA_1
if IDADE_2 >= 15 and IDADE_2 <= 18:
    QTD_10_20 += 1
    SOMA_ALT += ALTURA_2
if IDADE_3 >= 15 and IDADE_3 <= 18:
    QTD_10_20 += 1
    SOMA_ALT += ALTURA_3
if QTD_10_20 > 0:
    MEDIA = SOMA_ALT / QTD_10_20
else:
    print("Das pessoas informadas, nenhuma tem idade entre 10 e 20 anos.")
print("A Média de altura das pessoas de faixa etária dentre 15 e 18 anos é de", '{:.2f}'.format(MEDIA), "m.")

PESO_INF_60 = 0
if PESO_1 < 60:
    PESO_INF_60 += 1
if PESO_2 < 60:
    PESO_INF_60 += 1
if PESO_3 < 60:
    PESO_INF_60 += 1

PORC_PESO = PESO_INF_60*100/3
print ("A Porcentagem de pessoas com peso inferior a 60Kg equivale a", '{:.1f}'.format(PORC_PESO), "%" )