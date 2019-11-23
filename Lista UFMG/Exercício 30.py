#30 - Escreva um algoritmo em PORTUGOL que leia 20 números e imprima a soma dos positivos e o total de números negativos.

numeros = []
soma = 0
for contador in range(5):
    numero = int(input("Digite um número por favor: "))
    numeros.append(numero)

for numero in numeros:
    if numero >= 0:
        soma += numero
print(f"A soma dos números positivos informados equivalem a: {soma}")