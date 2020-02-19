#20 - Criar um algoritmo em PORTUGOL que imprima todos os números de 1 até 100, inclusive, e a média de todos eles.
contador = 1
numero = 0
while contador < 101:
    print(f'{contador}')
    numero = numero + contador
    contador += 1
media = numero/100
print(f'A média dos números informados é igual a: {media}')