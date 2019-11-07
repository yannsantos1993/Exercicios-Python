import getpass

print("-=" *40)
JOG1 = input("Desafiante #1, digite seu nome ou nick:").strip().upper()
print("-=" *40)
JOG2 = input("Desafiante #2, digite seu nome ou nick:").strip().upper()
print("-=" *40)
print("Parece que agora a coisa ficou séria, pro round 1 teremos:")
print("LOADING...\n")
print(f"PLAYER 1: {JOG1} Vs. PLAYER 2: {JOG2}\n")
print("-=" *40)

SJOG1 = getpass.getpass(f"{JOG1}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
while SJOG1 not in ("PE", "PA", "TE"):
    print(f"\n{JOG1}, Se liga nas regras!!! DIGITE APENAS: PE, PA ou TE!!!, vamos tentar de novo, OK...\n")
    SJOG1 = getpass.getpass(f"{JOG1}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
SJOG2 = getpass.getpass(f"\nAgora é a sua vez {JOG2}!!! escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
while SJOG2 not in ("PE", "PA", "TE"):
    print(f"\n{JOG2}, Se liga nas regras!!! DIGITE APENAS: PE, PA ou TE!!!, vamos tentar de novo, OK...\n")
    SJOG2 = getpass.getpass(f"{JOG2}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()

if SJOG1 =="PE" or SJOG2 == "PE":
    EXTENSO = "PEDRA"
if SJOG1 =="PA" or SJOG2 == "PA":
    EXTENSO = "PAPEL"
if SJOG1 =="TE" or SJOG2 == "TE":
    EXTENSO = "TESOURA"

if SJOG1 =="TE":
    EXT1 = "TESOURA"
if SJOG1 =="PE":
    EXT1 = "PEDRA"
if SJOG1 =="PA":
    EXT1 = "PAPEL"

if SJOG2 =="TE":
    EXT2 = "TESOURA"
if SJOG2 =="PE":
    EXT2 = "PEDRA"
if SJOG2 =="PA":
    EXT2 = "PAPEL"

print("\nLOADING AGAIN...")
print("-=" *40)
print("JO")
print("KEN")
print("PÔ!!!!!")
print("-=" *40)

GAN1 = 0
GAN2 = 0

if (SJOG1 == "PE" and SJOG2 == "PE") or (SJOG1 == "PA" and SJOG2 == "PA") or (SJOG1 == "TE" and SJOG2 == "TE"):
    print(f"\nEntão galera, deu empate né, {JOG1} e {JOG2} escolheram {EXTENSO}!")
    print(f"Placar geral: {JOG1}|{GAN1} x {GAN2}|{JOG2}\n")
    print("\nRound 2, FIGHT!!!!!!")
else:
    if SJOG1 == "PA" and SJOG2 =="PE":
        WIN = JOG1
        GAN1 += 1
    else:
        if SJOG1 == "PA" and SJOG2 == "TE":
            WIN = JOG2
            GAN2 +=1
        else:
            if SJOG1 == "PE" and SJOG2 == "PA":
                WIN = JOG2
                GAN2 += 1
            else:
                if SJOG1 == "PE" and SJOG2 == "TE":
                    WIN = JOG1
                    GAN1 += 1
                else:
                    if SJOG1 == "TE" and SJOG2 == "PA":
                        WIN = JOG1
                        GAN1 += 1
                    else:
                        if SJOG1 == "TE" and SJOG2 == "PE":
                            WIN = JOG2
                            GAN2 += 1
                        else:
                            None

    print(f"\nO ganhador foi o (a) desafiante: {WIN}\n")
    print(f"Placar geral: {JOG1}|{GAN1} x {GAN2}|{JOG2}\n")
    print("\nRound 2, FIGHT!!!!!!")
    print("-=" * 40)

SJOG1 = getpass.getpass(f"{JOG1}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
while SJOG1 not in ("PE", "PA", "TE"):
    print(f"\n{JOG1}, Se liga nas regras!!! DIGITE APENAS: PE, PA ou TE!!!, vamos tentar de novo, OK...\n")
    SJOG1 = getpass.getpass(f"{JOG1}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
SJOG2 = getpass.getpass(f"\nAgora é a sua vez {JOG2}!!! escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
while SJOG2 not in ("PE", "PA", "TE"):
    print(f"\n{JOG2}, Se liga nas regras!!! DIGITE APENAS: PE, PA ou TE!!!, vamos tentar de novo, OK...\n")
    SJOG2 = getpass.getpass(f"{JOG2}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()

print("-=" *40)
print("JO")
print("KEN")
print("PÔ!!!!!")
print("-=" *40)

if (SJOG1 == "PE" and SJOG2 == "PE") or (SJOG1 == "PA" and SJOG2 == "PA") or (SJOG1 == "TE" and SJOG2 == "TE"):
    print(f"\nEntão galera, deu empate né, {JOG1} e {JOG2} escolheram {EXTENSO}!")
    print(f"Placar geral: {JOG1}|{GAN1} x {GAN2}|{JOG2}\n")
    print("\nRound 3, FIGHT!!!!!!")
else:
    if SJOG1 == "PA" and SJOG2 =="PE":
        WIN = JOG1
        GAN1 += 1
    else:
        if SJOG1 == "PA" and SJOG2 == "TE":
            WIN = JOG2
            GAN2 +=1
        else:
            if SJOG1 == "PE" and SJOG2 == "PA":
                WIN = JOG2
                GAN2 += 1
            else:
                if SJOG1 == "PE" and SJOG2 == "TE":
                    WIN = JOG1
                    GAN1 += 1
                else:
                    if SJOG1 == "TE" and SJOG2 == "PA":
                        WIN = JOG1
                        GAN1 += 1
                    else:
                        if SJOG1 == "TE" and SJOG2 == "PE":
                            WIN = JOG2
                            GAN2 += 1
                        else:
                            None

    print(f"\nO ganhador foi o (a) desafiante: {WIN}\n")
    print(f"Placar geral: {JOG1}|{GAN1} x {GAN2}|{JOG2}\n")
    print("\nRound 3, FIGHT!!!!!!")
    print("-=" * 40)

SJOG1 = getpass.getpass(f"{JOG1}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
while SJOG1 not in ("PE", "PA", "TE"):
    print(f"\n{JOG1}, Se liga nas regras!!! DIGITE APENAS: PE, PA ou TE!!!, vamos tentar de novo, OK...\n")
    SJOG1 = getpass.getpass(f"{JOG1}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
SJOG2 = getpass.getpass(f"\nAgora é a sua vez {JOG2}!!! escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
while SJOG2 not in ("PE", "PA", "TE"):
    print(f"\n{JOG2}, Se liga nas regras!!! DIGITE APENAS: PE, PA ou TE!!!, vamos tentar de novo, OK...\n")
    SJOG2 = getpass.getpass(f"{JOG2}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()

print("-=" *40)
print("JO")
print("KEN")
print("PÔ!!!!!")
print("-=" *40)

if (SJOG1 == "PE" and SJOG2 == "PE") or (SJOG1 == "PA" and SJOG2 == "PA") or (SJOG1 == "TE" and SJOG2 == "TE"):
    print(f"\nEntão galera, deu empate né, {JOG1} e {JOG2} escolheram {EXTENSO}!")
    print(f"Placar geral: {JOG1}|{GAN1} x {GAN2}|{JOG2}\n")
else:
    if SJOG1 == "PA" and SJOG2 =="PE":
        WIN = JOG1
        GAN1 += 1
    else:
        if SJOG1 == "PA" and SJOG2 == "TE":
            WIN = JOG2
            GAN2 +=1
        else:
            if SJOG1 == "PE" and SJOG2 == "PA":
                WIN = JOG2
                GAN2 += 1
            else:
                if SJOG1 == "PE" and SJOG2 == "TE":
                    WIN = JOG1
                    GAN1 += 1
                else:
                    if SJOG1 == "TE" and SJOG2 == "PA":
                        WIN = JOG1
                        GAN1 += 1
                    else:
                        if SJOG1 == "TE" and SJOG2 == "PE":
                            WIN = JOG2
                            GAN2 += 1
                        else:
                            None

    print(f"\nO ganhador foi o (a) desafiante: {WIN}\n")
    print(f"Placar geral: {JOG1}|{GAN1} x {GAN2}|{JOG2}\n")

if GAN1 != GAN2:
    print("E agora, teremos revanche? Ou novos desafiantes surgirão das sombras?")
else:
    print("Como estamos com empate técnico no placar geral \nVamos agora a rodada de desempate!!!")
    SJOG1 = getpass.getpass(f"{JOG1}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
    while SJOG1 not in ("PE", "PA", "TE"):
        print(f"\n{JOG1}, Se liga nas regras!!! DIGITE APENAS: PE, PA ou TE!!!, vamos tentar de novo, OK...\n")
        SJOG1 = getpass.getpass(f"{JOG1}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
    SJOG2 = getpass.getpass(f"\nAgora é a sua vez {JOG2}!!! escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()
    while SJOG2 not in ("PE", "PA", "TE"):
        print(f"\n{JOG2}, Se liga nas regras!!! DIGITE APENAS: PE, PA ou TE!!!, vamos tentar de novo, OK...\n")
        SJOG2 = getpass.getpass(f"{JOG2}, escolha entre, PEDRA, PAPEL ou TESOURA: ").strip().upper()

    print("-=" * 40)
    print("JO")
    print("KEN")
    print("PÔ!!!!!")
    print("-=" * 40)

    if (SJOG1 == "PE" and SJOG2 == "PE") or (SJOG1 == "PA" and SJOG2 == "PA") or (SJOG1 == "TE" and SJOG2 == "TE"):
        print(f"\nEntão galera, deu empate né, {JOG1} e {JOG2} escolheram {EXTENSO}!")
        print(f"Placar geral: {JOG1}|{GAN1} x {GAN2}|{JOG2}\n")
        print("\nRound 2, FIGHT!!!!!!")
    else:
        if SJOG1 == "PA" and SJOG2 == "PE":
            WIN = JOG1
            GAN1 += 1
        else:
            if SJOG1 == "PA" and SJOG2 == "TE":
                WIN = JOG2
                GAN2 += 1
            else:
                if SJOG1 == "PE" and SJOG2 == "PA":
                    WIN = JOG2
                    GAN2 += 1
                else:
                    if SJOG1 == "PE" and SJOG2 == "TE":
                        WIN = JOG1
                        GAN1 += 1
                    else:
                        if SJOG1 == "TE" and SJOG2 == "PA":
                            WIN = JOG1
                            GAN1 += 1
                        else:
                            if SJOG1 == "TE" and SJOG2 == "PE":
                                WIN = JOG2
                                GAN2 += 1
                            else:
                                None
    print(f"\nO ganhador foi o (a) desafiante: {WIN}\n")
    print(f"Placar geral: {JOG1}|{GAN1} x {GAN2}|{JOG2}\n")
    print("E agora, teremos revanche? Ou novos desafiantes surgirão das sombras?")