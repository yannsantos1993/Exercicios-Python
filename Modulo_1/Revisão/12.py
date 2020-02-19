pessoas_analisadas = 25
contador = 0
acima_50 = 0
ocorrencia_idade = 0
soma_altura = 0
peso_menor_40 = 0

while contador < pessoas_analisadas:
    idade = float(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))

    if idade > 50:
        acima_50 =+1

    if idade >= 10 and idade <= 20:
        ocorrencia_idade +=1
        soma_altura +=altura

    if peso < 40:
        peso_menor_40 +=1

    contador+=1

print(f"A quantidade de pessoas acima de 50 anos é: {acima_50}")
print(f"A média das alturas das pessoas entre 10 e 20 anos é {soma_altura/ocorrencia_idade}")
print(f"A porcentagem de pessoas com peso inferior a 40 kg é: {peso_menor_40*100/pessoas_analisadas}")