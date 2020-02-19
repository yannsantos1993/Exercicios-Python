v = []
p = []
primeiras_parcelas = []

for compras in range (5):
    tipo = input("A compra realizada foi a (V)ista ou a (P)razo?:").strip().upper()
    while tipo not in ("V","P"):
        tipo = input("A compra realizada foi a (V)ista ou a (P)razo?:").strip().upper()
    if tipo == "V":
        valor = float(input("Digite o valor da compra a vista em R$:"))
        v.append(valor)
    else:
        valor = float(input("Digite o valor da compra a prazo em R$:"))
        p.append(valor)
        primeiras_parcelas.append(valor/3)
print(f"As compras a vista equivalem a um total de: R$ {sum(v)}")
print(f"As compras a prazo equivalem a um total de: R$ {sum(p)}")
print(f"A soma das compras a vista e a prazo equivalem a um total de: R$ {sum(v) + sum(p)}")
print(f"A primeira parcela das compras a prazo equivalem respectivamente a: {primeiras_parcelas}")