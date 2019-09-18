NUM_A = int(input("Digite um número:"))
NUM_B = int(input("Digite outro número:"))
if NUM_A.__mod__ (NUM_B) ==0:
    print("O número", NUM_A, "é divisível por", NUM_B)
else:
    print("O número", NUM_A, "não é divisível por", NUM_B)