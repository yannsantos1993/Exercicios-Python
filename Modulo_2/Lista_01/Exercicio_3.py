nomes = []
for x in range (10):
    nomes.append(input("Digite um nome:"))
nome = input("Digite um nome:")
if nome in nomes:
    print("ACHEI!")
if nome not in nomes:
    print("NÃO ACHEI")