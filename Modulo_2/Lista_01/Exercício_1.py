maior_preco = None
contador = 0
ocorrencias = 3
soma_precos = 0
menor_preco = 0
cod_menor_preco = 0
while contador < ocorrencias:
    codigo = int(input("Digite o código do produto: "))
    preco = float(input("Digite o preço do produto:"))
    soma_precos += preco
#analisar o maio preço
    if contador==0:
        maior_preco = preco
    else:
        if maior_preco < preco:
            maior_preco = preco
#analisar e guardar o código do produto mais barato
    if contador==0:
        cod_menor_preco = codigo
        menor_preco = preco
    else:
        if menor_preco > preco:
            cod_menor_preco = codigo


    contador += 1

print(f"O maior preço é: {maior_preco}")
print(f"A média dos preços dos produtos listados equivale a {soma_precos/ocorrencias}")
print(f"O código do produto mais barato é {cod_menor_preco}")