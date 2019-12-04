pessoas_analisadas = 3
contador = 0
idades = 0
peso_maior_90_altura_150cm = 0
idade10_30 = 0
maior_190 = 0

while contador < pessoas_analisadas:
    idade = int(input("Digite a idade:"))
    peso = float(input("Digite o peso:"))
    altura = float(input("Digite a altura:"))

    idades += idade

    if peso > 90 and altura <1.50:
        peso_maior_90_altura_150cm +=1

    if idade >=10 and idade <=30:
        idade10_30 +=1

    if altura > 1.90:
        maior_190 +=1

    contador+=1

print(f"A média das idades das pessoas analisadas equivale a: {idades/pessoas_analisadas}.")
print(f"A quantidade de pessoas com peso maior que 90kg e altura inferior a 1.50m é de: {peso_maior_90_altura_150cm} pessoas.")
print(f"A porcentagem de pessoas com mais de 1.90m de altura e idade entre 10 e 30 anos equivale a {'{:.2f}'.format((maior_190*100)/idade10_30)} %.")