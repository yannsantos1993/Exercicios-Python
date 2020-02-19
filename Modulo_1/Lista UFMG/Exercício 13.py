#13 - Escreva um algoritmo em PORTUGOL que receba dez números do usuário e imprima o cubo de cada número.
contador = 0
while contador < 10:
    num = int(input("Informe um número:"))
    print(f'O cubo do número informado equivale a: {num**3}')
    contador +=1