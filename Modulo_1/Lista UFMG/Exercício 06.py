#6 - Escreva um algoritmo em PORTUGOL que imprima todos os números múltiplos de 5, no intervalo fechado de 1 a 500.
contador = 1
while contador < 501:
    RESTO_DIV = contador % 5
    if RESTO_DIV == 0:
        print(f'{contador}')
    contador += 1