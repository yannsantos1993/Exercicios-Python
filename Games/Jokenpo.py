import getpass
from time import sleep
opcoes = {
    "0" : "Pedra",
    "1" : "Papel",
    "2" : "Tesoura"
    }

vitorias_jog1 = 0
vitorias_jog2 = 0

print("-=" * 40)
print("\nBem-vindos ao Jo-Ken-Pô Arcade, jogo composto por uma melhor de 3.\nO primeiro jogador que vencer 2 rounds é o ganhador!\nescolha entre, (0) = PEDRA,  (1) = PAPEL ou (2) = TESOURA e divirtan-se!\nJogadores, se registrem abaixo:\n")
print("-=" * 40)
sleep(1)

jog1 = input("\nPlayer 1: insert name:").strip().upper()
jog2 = input("\nPlayer 2: insert name:").strip().upper()

sleep(1)
print("-=" * 40)
print("\nDESAFIANTES:")
sleep(1)
print(f"\nPLAYER 1 | {jog1} vs. {jog2} | PLAYER 2\n")
print("-=" * 40)
sleep(1)

while (vitorias_jog1 < 2 and vitorias_jog2 <= 1) or (vitorias_jog2 < 2 and vitorias_jog1 <= 1):
    sjog1 = getpass.getpass(f"\n{jog1}, escolha entre, (0) = PEDRA,  (1) = PAPEL ou (2) = TESOURA: ").strip()
    while sjog1 not in ("0", "1", "2"):
        print(f"\n{jog1}, Se liga nas regras!!! DIGITE APENAS: (0) = PEDRA,  (1) = PAPEL ou (2) = TESOURA!!! \nVamos tentar de novo, OK...\n")
        sjog1 = getpass.getpass(f"\n{jog1}, escolha entre, (0) = PEDRA,  (1) = PAPEL ou (2) = TESOURA: ").strip()
        print("-=" * 40)
        sleep(1)
    sjog2 = getpass.getpass(f"\nSua vez {jog2}!!! escolha entre, (0) = PEDRA,  (1) = PAPEL ou (2) = TESOURA: \n").strip()
    while sjog2 not in ("0", "1", "2"):
        print(f"\n{jog2}, Se liga nas regras!!! DIGITE APENAS: (0) = PEDRA,  (1) = PAPEL ou (2) = TESOURA!!! \nVamos tentar de novo, OK...\n")
        sjog2 = getpass.getpass(f"{jog2}, escolha entre, (0) = PEDRA,  (1) = PAPEL ou (2) = TESOURA: \n").strip()
        print("-=" * 40)

    sleep(1)
    print("-=" * 40)
    print("\n\t\t\JO")
    sleep(1)
    print("\t\t\t\tKEN")
    sleep(1)
    print("\t\t\t\t\t\tPÔ!!!!!\n")
    print("-=" * 40)
    sleep(2)

    if sjog1 == sjog2:
        print(f"\nEntão... temos um empate {jog1} e {jog2} escolheram {opcoes[sjog1]} ")
        print(f"\nPlacar geral: {jog1} | {vitorias_jog1} x {vitorias_jog2} | {jog2}\n")
        print("-=" * 40)
    elif (sjog1 == "0" and sjog2 == "2") or (sjog1 == "1" and sjog2 == "0") or (sjog1 == "2" and sjog2 == "1"):
        vitorias_jog1 +=1
        print(f"\n{jog1} escolheu {opcoes[sjog1]} e {jog2} escolheu {opcoes[sjog2]}, logo {jog1} venceu este round!")
        print(f"\nPlacar geral: {jog1} | {vitorias_jog1} x {vitorias_jog2} | {jog2}\n")
        print("-=" * 40)
    elif(sjog2 == "0" and sjog1 == "2") or (sjog2 == "1" and sjog1 == "0") or (sjog2 == "2" and sjog1 == "1"):
        vitorias_jog2 +=1
        print(f"\n{jog1} escolheu {opcoes[sjog1]} e {jog2} escolheu {opcoes[sjog2]}, logo {jog2} venceu este round!")
        print(f"\nPlacar geral: {jog1} | {vitorias_jog1} x {vitorias_jog2} | {jog2}\n")
        print("-=" * 40)

if vitorias_jog1 > vitorias_jog2:
    sleep(1)
    print(f"\nParabéns {jog1} você foi o vencedor da melhor de 3!\n")
    print("-=" * 40)
else:
    sleep(1)
    print(f"\nParabéns {jog2} você foi o vencedor da melhor de 3!\n")
    print("-=" * 40)