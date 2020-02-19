#27 - Criar um algoritmo em PORTUGOL que leia um número (NUM) e então imprima os múltiplos de 3 e 5, ao mesmo tempo, no intervalo fechado de 1 a NUM.

num = int(input("Informe o numero equivalente ao final da sequência:"))
contador = 1
while contador <= num:
    RESTO_DIV = contador % 3 and contador % 5
    if RESTO_DIV == 0:
        print(f'No intervalo informado, os números que são múltiplos de 3 ou 5 são:{contador}')
    contador += 1

