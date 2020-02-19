#18 - Criar um algoritmo em PORTUGOL que imprima todos os números de 1 até 100, inclusive, e a soma da metade desses números.
contador = 1
numero = 0
while contador < 101:
    print(f'{contador}')
    numero += (contador/2)
    contador += 1
print(f'A soma da metade do valor dos números informados é igual a: {numero}')