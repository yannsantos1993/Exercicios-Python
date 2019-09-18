SALARIO = float(input("Informe o salário:"))
REAJUSTE_30 = SALARIO + (SALARIO * 0.3)
REAJUSTE_25 = SALARIO + (SALARIO * 0.25)
REAJUSTE_20 = SALARIO + (SALARIO * 0.20)
REAJUSTE_15 = SALARIO + (SALARIO * 0.15)
REAJUSTE_10 = SALARIO + (SALARIO * 0.10)
if SALARIO <= 600:
    REAJUSTE_30
    print("O Salário reajustado é: R$", REAJUSTE_30)
else:
    if SALARIO <=1100:
        REAJUSTE_25
        print("O Salário reajustado é: R$", REAJUSTE_25)
    else:
        if SALARIO <=2400:
            REAJUSTE_20
            print("O Salário reajustado é: R$", REAJUSTE_20)
        else:
            if SALARIO <=3550:
                REAJUSTE_15
                print("O Salário reajustado é: R$", REAJUSTE_15)
            else:
                if SALARIO > 3550:
                    REAJUSTE_10
                    print("O Salário reajustado é: R$", REAJUSTE_10)
                else:
                    None
