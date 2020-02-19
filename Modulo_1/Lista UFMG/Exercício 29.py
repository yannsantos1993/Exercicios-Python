#29 - Escreva um algoritmo em PORTUGOL que receba 15 números e imprima quantos números maiores que 30 foram digitados.

maior_que_30 = 0
for contador in range(15):
    numero = int(input("Digite um número por favor: "))
    if numero > 30:
        maior_que_30 +=1

print(f"A quantidade de numeros maiores que 30 é: {maior_que_30}")




