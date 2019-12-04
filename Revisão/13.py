idade = []
peso = []
m90 = 0

for pessoas in range (7):
    idade.append(int(input("Informe sua idade:")))
    p =(float(input("Informe seu peso:")))
    if p > 90:
        m90 +=1
        peso.append(p)
print(f"A média de idade das 7 pessoas informadas equivale a {sum(idade)/7}.")
print(f"Das pessoas acima informadas, {m90} tem mais de 90kg.")
