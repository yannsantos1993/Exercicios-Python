#15 - Escreva um algoritmo em PORTUGOL que receba oito números do usuário e imprima o logaritmo de cada um deles na base 10
import math
contador = 0
while contador < 8:
    num = int(input("Informe um número:"))
    print(f'O logaritimo do número informado equivale a: {math.log(num, 10)}')
    contador +=1