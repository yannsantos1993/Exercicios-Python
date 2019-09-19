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

if IDADE_1 > 20:
    I1 = 1
else:
    I1 = 0

if IDADE_2 > 20:
    I2 = 1
else:
    I2 = 0

if IDADE_3 > 20:
    I3 = 1
else:
    I3 = 0

TOTAL_PESSOAS20 = I1+I2+I3
print("Das pessoas informadas", TOTAL_PESSOAS20, "tem idade superior a 20 anos.")

if IDADE_1 >= 15 and IDADE_1 <= 18:
    A1 = ALTURA_1
    A11 = 1
else:
    A1 = 0
    A11 = 0

if IDADE_2 >= 15 and IDADE_2 <= 18:
    A2 = ALTURA_2
    A22 = 1
else:
    A2 = 0
    A22 = 0

if IDADE_3 >= 15 and IDADE_3 <= 18:
    A3 = ALTURA_3
    A33 = 1
else:
    A3 = 0
    A33 = 0

MEDIA_ALTURAS = (A1 + A2 + A3) / (A11 + A22 + A33)
print ("A Média de altura das pessoas de faixa etária dentre 15 e 18 anos é de", MEDIA_ALTURAS, "m.")