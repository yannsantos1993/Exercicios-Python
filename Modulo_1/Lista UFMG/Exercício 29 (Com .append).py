#29 - Escreva um algoritmo em PORTUGOL que receba 15 números e  após as leituras imprima os números maiores que 30 foram digitados.

numeros = []
for contador in range(15):
    numero = int(input("Digite um número por favor: "))
    numeros.append(numero)

print("Os números abaixo são maiores que 30:")
for numero in numeros:
    if numero > 30:
        print(numero)