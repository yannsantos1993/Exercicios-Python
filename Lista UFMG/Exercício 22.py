#22 - Criar um algoritmo em PORTUGOL que leia um número (NUM), e depois leia NUM números inteiros e imprima o maior deles.
num = int(input("Determine a quantidade de números a serem analisados:"))
for contador in range(num):
    numero = int(input("Digite um número por favor: "))
    if contador == 0:
        maior = numero
    else:
        if numero > maior:
            maior = numero
print(f'O maior número informado é: {maior}')
