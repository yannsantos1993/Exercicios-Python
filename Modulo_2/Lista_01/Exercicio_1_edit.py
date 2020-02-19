codigos = []
precos = []
contador = 0
ocorrencias = 3


while contador < ocorrencias:
    codigos.append(int(input("Digite o código do produto: ")))
    precos.append(float(input("Digite o preço do produto:")))
    contador +=1

menor_preco = precos.index(min(precos))

print(f"O maior preço é: {max(precos)}")
print(f"A média dos preços dos produtos listados equivale a {sum(precos)/ocorrencias}")
print(f"O código do produto mais barato é {codigos[menor_preco]}")