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
print("Das pessoas informadas", TOTAL_PESSOAS20, "tem idade superior a 20 anos")