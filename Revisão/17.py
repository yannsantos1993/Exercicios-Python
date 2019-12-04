homens = []
mulheres = []
qhom = 0
qmul = 0

for pessoas in range (7):
    pessoa = (input("Informe seu sexo: (M)asculino ou (F)eminino?")).strip().upper()
    while pessoa not in ("M","F"):
        pessoa = (input("Informe seu sexo: (M)asculino ou (F)eminino?")).strip().upper()
    if pessoa == "M":
        idade = (int(input("Informe agora a sua idade:")))
        homens.append(idade)
        qhom +=1
    else:
        idade = (int(input("Informe agora a sua idade:")))
        mulheres.append(idade)
        qmul +=1

print(f"A idade média do grupo equivale a {(sum(homens)+sum(mulheres))/7}")
print(f"A idade média dos homens informados equivale a {sum(homens)/qhom}.")
print(f"A idade média dos homens informados equivale a {sum(mulheres)/qmul}.")