#29 - Escreva um algoritmo em PORTUGOL que receba 15 números e imprima quantos números maiores que 30 foram digitados.

for contador in range(15):
    numero = int(input("Digite um número por favor: "))
if numero > 30:
    print(numero)