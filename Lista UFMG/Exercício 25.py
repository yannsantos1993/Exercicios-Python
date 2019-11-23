#25 - Criar um algoritmo em PORTUGOL que leia dez números inteiros e imprima o maior e o segundo maior número da lista.
maior = None
for contador in range(10):
    numero = int(input("Digite um numero por favor: "))
    if (contador==0):
        maior = numero
    else:
        if numero > maior:
            segundo_maior = maior
            maior = numero
        else:
            if contador == 1:
                segundo_maior = numero
            if numero > segundo_maior:
                segundo_maior = numero

print(f"O maior número é: {maior}")
print(f"O segundo maior número é: {segundo_maior}")