IDADE = int(input("Informe a sua idade:"))
if IDADE < 10:
    print ("Você não pode assistir filmes proibidos para menores de 10 anos")
else:
    if IDADE < 14:
        print("Você não pode assistir filmes proibidos para menores de 14 anos")
    else:
        if IDADE < 18:
            print("Você não pode assistir filmes proibidos para menores de 18 anos")
        else:
            print ("Você pode assistir a qualquer filme!")