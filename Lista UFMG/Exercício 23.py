#23 - Criar um algoritmo em PORTUGOL que leia um número (NUM), e depois leia NUM números inteiros e imprima o menor deles.
num = int(input("Determine a quantidade de números a serem analisados:"))
for contador in range(num):
    numero = int(input("Digite um número por favor: "))
    if contador == 0:
        menor = numero
    else:
        if numero < menor:
            menor = numero
print(f'O menor número informado é: {menor}')