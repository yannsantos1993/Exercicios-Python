intervalo30_90 = 0
soma = 0
for numeros in range (5):
    numero = int(input("Informe um número:"))
    if numero >=30 and numero <=90:
        intervalo30_90 +=1
        soma += numero
print(f"dos numeros informados, {intervalo30_90} estão dentro do intervalo entre 30 e 90; e a soma destes equivale a: {soma}.")