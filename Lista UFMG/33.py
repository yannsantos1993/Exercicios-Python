'''33 - Escreva um algoritmo em PORTUGOL que calcule o resto da divisão de A por B (número inteiros e positivos),
ou seja, A mod B, através de subtrações sucessivas. Esses dois valores são passados pelo usuário através do teclado. '''

contador = 0
soma_a = 0
soma_b = 0

a = int(input("Digite um número:"))
for contador in range (a):
    soma_a += 1
b = int(input("Digite um número:"))
for contador in range (b):
    soma_b += 1

print(f"O produto entre os número informados equivale a {soma_a**soma_b}")