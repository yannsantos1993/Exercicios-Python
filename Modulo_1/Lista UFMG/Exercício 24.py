#24 - Criar um algoritmo em PORTUGOL que leia dez números inteiros e imprima o maior e o menor número da lista.
for contador in range(10):
    numero = int(input("Digite um numero por favor: "))
    if (contador==0):
        maior = numero
    else:
        if numero > maior:
            maior = numero
    if (contador==0):
        menor = numero
    else:
        if numero < menor:
            menor = numero
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")