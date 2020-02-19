#19 - Criar um algoritmo em PORTUGOL que imprima todos os números de 1 até 100, inclusive, e a soma do cubo desses números.
contador = 1
numero = 0
while contador < 101:
    print(f'{contador}')
    numero += (contador**3)
    contador += 1
print(f'A soma do cubo do valor dos números informados é igual a: {numero}')