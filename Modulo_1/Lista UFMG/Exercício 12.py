#12 -  Escreva um algoritmo em PORTUGOL que receba dez números do usuário e imprima o quadrado de cada número.
contador = 0
while contador < 10:
    num = int(input("Informe um número:"))
    print(f'O quadrado do número informado equivale a: {num**2}')
    contador +=1