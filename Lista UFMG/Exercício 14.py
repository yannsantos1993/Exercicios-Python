#14 - Escreva um algoritmo em PORTUGOL que receba quinze números do usuário e imprima a raiz quadrada de cada número.
contador = 0
while contador < 15:
    num = int(input("Informe um número:"))
    print(f'A raiz quadrada do número informado equivale a: {num**(1/2)}')
    contador +=1