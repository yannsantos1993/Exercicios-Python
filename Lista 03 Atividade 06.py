NUM_1 = int(input("Digite um número:"))
NUM_2 = int(input("Digite outro número:"))
if NUM_1 < NUM_2:
    A = NUM_1
else:
    A = NUM_2

if NUM_1 > NUM_2:
    B = NUM_1
else:
    B = NUM_2

print("Os números digitados em ordem crescente são:", A, "e", B)
