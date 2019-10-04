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

<<<<<<< HEAD
TOTAL_PESSOAS20 = I1+I2+I3
=======
>>>>>>> 391e3b79017cdc2eaae3273bc368f908b3643a4f
TOTAL_PESSOAS20 = I1 +I2 +I3
print("Das pessoas informadas", TOTAL_PESSOAS20, "tem idade superior a 20 anos.")

if IDADE_1 >= 15 and IDADE_1 <= 18:
    A1 = ALTURA_1
    A11 = 0

if IDADE_2 >= 15 and IDADE_2 <= 18:
    A2 = ALTURA_2
    A22 = 0

if IDADE_3 >= 15 and IDADE_3 <= 18:
    A3 = ALTURA_3
    A33 = 0

MEDIA_ALTURAS = (A1 + A2 + A3) / (A11 + A22 + A33)
<<<<<<< HEAD
print ("A Média de altura das pessoas de faixa etária dentre 15 e 18 anos é de", MEDIA_ALTURAS, "m.")
=======
>>>>>>> 391e3b79017cdc2eaae3273bc368f908b3643a4f
print ("A Média de altura das pessoas de faixa etária dentre 15 e 18 anos é de", '{:.2f}'.format(MEDIA_ALTURAS), "m.")

if PESO_1 < 60:
    P1 = 1
else:
    P1 = 0

if PESO_2 < 60:
    P2 = 1
else:
    P2 = 0

if PESO_3 < 60:
    P3 = 1
else:
    P3 = 0

PORC_PESO = (100 * (P1 + P2 + P3)) / 3
<<<<<<< HEAD
print ("A Porcentagem de pessoas com peso inferior a 60Kg equivale a", '{:.1f}'.format(PORC_PESO), "%" )
=======
print ("A Porcentagem de pessoas com peso inferior a 60Kg equivale a", '{:.1f}'.format(PORC_PESO), "%" )
>>>>>>> 391e3b79017cdc2eaae3273bc368f908b3643a4f
