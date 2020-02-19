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
