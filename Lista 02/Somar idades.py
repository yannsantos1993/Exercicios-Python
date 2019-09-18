IDADE_H1 = int(input("Digite a primeira idade masculina:"))
IDADE_H2 = int(input("Digite a segunda idade masculina:"))
IDADE_M1 = int(input("Digite a primeira idade feminina:"))
IDADE_M2 = int(input("Digite a segunda idade feminina:"))

if IDADE_H1>IDADE_H2:
    MAIORH = IDADE_H1
    MENORH = IDADE_H2
else:
    MENORH = IDADE_H1
    MAIORH = IDADE_H2

if IDADE_M1>IDADE_M2:
    MAIORM = IDADE_M1
    MENORM = IDADE_M2
else:
    MENORM = IDADE_M1
    MAIORM = IDADE_M2

print("A soma da idade do homem mais velho com a da mulher mais nova é igual a:", (MAIORH+MENORM))
print("O produto da idade do homem mais novo com a da mulher mais velha é igual a:", (MENORH*MAIORM))