#10 - Escreva um algoritmo em PORTUGOL que imprima todos os números ímpares do intervalo fechado de 1 a 100.
contador = 1
while contador < 101:
    RESTO_DIV = contador % 2
    if RESTO_DIV != 0:
        print(f'{contador}')
    contador += 1