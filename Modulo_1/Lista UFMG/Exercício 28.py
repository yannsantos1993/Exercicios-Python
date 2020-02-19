#28 - Escreva um algoritmo em PORTUGOL que leia 200 números inteiros e imprima quantos são pares e quantos são ímpares.

contador = 1
par = 0
impar = 0
while contador <= 200:
    RESTO_DIV = contador % 2
    if RESTO_DIV == 0:
        par += 1
    else:
        impar +=1
    contador += 1
print(f'Na sequência informada, {par} números são pares e {impar} são ímpares')