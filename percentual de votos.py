print("percentual de votos")
TOTAL_ELEITORES=int(input("Digite o número total de eleitores:"))
VOTOS_BRANCOS=int(input("Digite o número total de votos em branco:"))
VOTOS_NULOS=int(input("Digite o número total de votos nulos:"))
VOTOS_VALIDOS=int(input("Digite o número total de votos válidos:"))
PORCENTAGEM_VOTOS_BRANCOS=100*VOTOS_BRANCOS/TOTAL_ELEITORES
PORCENTAGEM_VOTOS_NULOS=100*VOTOS_NULOS/TOTAL_ELEITORES
PORCENTAGEM_VOTOS_VALIDOS=100- (PORCENTAGEM_VOTOS_NULOS+PORCENTAGEM_VOTOS_BRANCOS)
print("O total de eleitores é:", TOTAL_ELEITORES)
print("A porcentagem de votos em branco é:",PORCENTAGEM_VOTOS_BRANCOS, "%")
print("A porcentagem de votos em branco é:",PORCENTAGEM_VOTOS_NULOS, "%")
print("A porcentaegm de votos em branco é:",PORCENTAGEM_VOTOS_VALIDOS, "%")
