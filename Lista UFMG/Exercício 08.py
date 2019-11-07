#7 - Escreva um algoritmo em PORTUGOL que imprima os 100 primeiros números ímpares.
contador = 1
while contador < 101:
    RESTO_DIV = contador % 2
    if RESTO_DIV != 0:
        print(f'{contador}')
    contador += 1