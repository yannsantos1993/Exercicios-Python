NOME = input("Digite o nome do aluno:")
NOTA_1 = float(input("Digite a primeira nota:"))
NOTA_2 = float(input("Digite a segunda nota:"))
NOTA_3 = float(input("Digite a terceira nota:"))
FALTAS = int(input("Digite o total de faltas neste semestre:"))
MEDIA_NOTAS = (NOTA_1 + NOTA_2 + NOTA_3) / 3
PERC_FALTAS = FALTAS * 100 / 80
if PERC_FALTAS < 25 and MEDIA_NOTAS >=7:
    print ("Aluno", NOME, "Aprovado!!")
else:
    if PERC_FALTAS > 25:
        print("Aluno", NOME, "reprovado por falta")
    else:
        if MEDIA_NOTAS < 7:
            print("Aluno", NOME, "reprovado por não atingir a média")
        else:
            None