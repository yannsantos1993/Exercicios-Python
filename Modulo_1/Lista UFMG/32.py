'''32) Escreva um algoritmo em PORTUGOL que realize a potência de A (número real) por B (número inteiro e positivo),
ou seja, AB, através de multiplicações sucessivas. Esses dois valores são passados pelo usuário através do teclado'''

contador = 0
soma_a = 0
soma_b = 0

a = int(input("Digite um número:"))
for contador in range (a):
    soma_a += 1
b = int(input("Digite um número:"))
for contador in range (b):
    soma_b += 1

print(f"A potenciação entre o primeiro número informado elevado pelo segundo número informado é igual a: {soma_a**soma_b}")
