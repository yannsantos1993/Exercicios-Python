'''37) Escreva um algoritmo em PORTUGOL que determine todos os divisores de um dado número N'''

divisores = []
contador = 0
divisor = 0
numero = int(input("Informe um número:"))
for divisao in range (numero):
    resto_divisao = numero %2
    divisor = numero
    if resto_divisao == 0:
        divisores.append(divisor)
print(f"Os divisores de {numero} são {divisores}.")
