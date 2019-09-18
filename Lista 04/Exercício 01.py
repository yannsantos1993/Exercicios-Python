''' Elabore um algoritimo que dada a idade de um nadadpr, classifique-o em uma das seguintes categorias:
        Infantil A = 5 a 7 anos
        Juvenil A = 12 a 13 anos
        Adultos = Maiores de 18 anos
    Caso a idade não esteja em nenhuma categoria, deve-se informar que o nadador não pode competir/ nadar'''

IDADE = int(input("Digite a idade do Nadador:"))
if IDADE >= 5 and IDADE <= 7:
    IDADE = "Pertence a categoria Infantil A"
else:
    if IDADE >= 12 and IDADE <= 13:
        IDADE = "Pertence a categoria Juvenil A"
    else:
        if IDADE >= 18:
            IDADE = "Pertence a categoria Adultos"
        else:
            IDADE = "Não Pode Competir"
print ("O Nadador", IDADE)