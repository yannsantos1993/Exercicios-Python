pessoas_analisadas = 3
contador = 0
menor_50_peso_menor_60 = 0
pessoa_menor_150cm = 0
soma_alturas = 0
olhos_azuis = 0
ruivas_sem_olhos_azuis = 0

while contador < pessoas_analisadas:
    idade = int(input("informe a idade:"))
    peso = float(input("informe o peso:"))
    altura = float(input("informe a altura:"))
    olhos = input("informe a cor dos olhos: (A)zuis, (P)retos, (V)erdes ou (C)astanhos?").strip().upper()
    while olhos not in ("A", "P", "V", "C"):
        olhos = input("informe a cor dos olhos: (A)zuis, (P)retos, (V)erdes ou (C)astanhos?").strip().upper()
    cabelo = input("informe a cor do cabelo: (PR)eto, (CA)stanho, (LO)iro ou (RU)ivo?").strip().upper()
    while cabelo not in ("PR", "CA", "LO", "RU"):
        cabelo = input("informe a cor do cabelo: (PR)eto, (CA)stanho, (LO)iro ou (RU)ivo?").strip().upper()

    if idade > 50 and peso < 60:
        menor_50_peso_menor_60 +=1

    if altura < 1.50:
        pessoa_menor_150cm +=1
        soma_alturas += altura

    if olhos == "A":
        olhos_azuis +=1

    if cabelo == "RU" and olhos != "A":
        ruivas_sem_olhos_azuis +=1

    contador+=1

print(f"Dos analisados, {menor_50_peso_menor_60} são maiores que 50 anos e pesam menos de 60kg.")
print(f"Dos analisados, os menores de 1,50m tem altura média de {'{:.2f}'.format(soma_alturas/pessoa_menor_150cm)}m.")
print(f"Dos analisados, {'{:.2f}'.format((olhos_azuis*100)/pessoas_analisadas)} % deles possuem olhos azuis.")
print(f"Dos analisados, {ruivas_sem_olhos_azuis} deles são ruivos (as) e não possuem olhos azuis.")