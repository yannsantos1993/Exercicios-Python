'''1)Faça um algoritimo para ler o código (int) e o preço de 15 produtos, calcular e escrever:
- o maior preço lido;
- a média aritimética dos preços dos produtos;
o código do produto mais barato.'''

from time import sleep
print("-=" * 40)
sleep(1)
print("Exercício #1:\n")
sleep(1)

codigos = []
precos = []
contador = 0
ocorrencias = 15


while contador < ocorrencias:
    codigos.append(int(input("Digite o código do produto: ")))
    precos.append(float(input("Digite o preço do produto:")))
    contador +=1

menor_preco = precos.index(min(precos))

print(f"O maior preço é: R$ {max(precos)}")
print(f"A média dos preços dos produtos listados equivale a R$ {sum(precos)/ocorrencias}")
print(f"O código do produto mais barato é o código: {codigos[menor_preco]}")
sleep(1)
print("-=" * 40)
sleep(1)

'''2) ler um vetor Q de 20 posições (Aceitar somente números positivos).
Escrever a seguir o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor.'''

print("Exercício #2:\n")
sleep(1)

Q = []
contador = 0
ocorrencias = 20

while contador < ocorrencias:
    numero = int(input("Digite um número por favor:"))
    while numero <= 0:
        numero = int(input("Digite um número por favor:"))
    else:
        if numero > 0:
            Q.append(numero)
        contador +=1

n_pos = Q.index(max(Q))
print(f"O maior valor digitado foi: {max(Q, key=int)} e seu respectivo índice é {n_pos}")
sleep(1)
print("-=" * 40)
sleep(1)

'''3)Escreva um algoritimo que permita a leitura dos nomes de 10 pessoas e armazene os nomes lidos em um vetor. Após isto,
o algoritimo deve permitir a leitura de mais um nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver
entre os 10 nomes lidos anteriormente (Guardados no vetor), ou NÃO ACHEI caso contrário.'''


print("Exercício #3:\n")
sleep(1)

nomes = []
for x in range (10):
    nomes.append(input("Digite um nome:"))
nome = input("Digite um nome:")
if nome in nomes:
    print("ACHEI!")
if nome not in nomes:
    print("NÃO ACHEI")
    sleep(1)
    print("-=" * 40)

