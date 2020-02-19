#26 - Criar um algoritmo em PORTUGOL que leia os limites inferior e superior de um intervalo e imprima todos os números pares no intervalo aberto e seu somatório. Suponha que os dados digitados são para um intervalo crescente, ou seja, o primeiro valor é menor que o segundo.

inicio = int(input("Informe o número equivalente ao ponto de partida:"))
final = int(input("Informe o numero equivalente ao final da sequência:"))
contador = inicio
numero = 0
while contador <= final:
    RESTO_DIV = contador % 2
    if RESTO_DIV == 0:
        print(f'{contador}')
        numero += contador
    contador += 1
print(f'A soma dos números informados é igual a: {numero}')