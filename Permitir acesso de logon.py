USUARIO=int(input("Digite seu usuário com 4 digitos alfanuméricos:"))
if USUARIO != 1234:
    print("Usuário inválido")
else:
    SENHA = int(input("Digite sua senha com 4 dígitos alfanuméricos:"))
    if SENHA != 9999:
        print("Senha incorreta!")
    else:
        print("Acesso permitido")

