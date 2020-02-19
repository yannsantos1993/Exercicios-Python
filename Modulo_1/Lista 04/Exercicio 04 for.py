IDADE_1 = int(input("Digite a idade da primeira pessoa:"))
IDADE_2 = int(input("Digite a idade da segunda pessoa:"))
IDADE_3 = int(input("Digite a idade da terceira pessoa:"))

IDADE = 0
if IDADE_1 > 20:
    IDADE += 1
if IDADE_2 > 20:
    IDADE += 1
if IDADE_3 > 20:
    IDADE += 1
print(f"{IDADE} pessoa(s) tem idade superior a 20 anos.")