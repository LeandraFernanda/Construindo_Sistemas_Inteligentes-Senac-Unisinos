nome = "Atlas"
energia = 100
distanciaMetros = 0
missao_em_andamento = True

print("-----------------Meu Robô-----------------")
print("Nome do robô: ", nome)
print("Energia: ", energia)
print("Distância percorrida: ", distanciaMetros, " metros")
print("Missão em andamento: ", missao_em_andamento)
print("------------------------------------------")

print()
print(" 1 - O robo percorre 120 metros e consome20 pontos de energia")

distanciaMetros += 120
energia -= 20

print("Distância percorrida: ", distanciaMetros, " metros")
print("Energia: ", energia)
print("-------------------------------------------------")

print(" 2 - Coleta 3 amostras e consome 15 pontos de energia.")

amostras_coletadas = 3
energia -= 15
print()
print("--------------------------------------------------")


print(" 3 - Recarrega 10 pontos de energia.")
energia += 10
print("Energia: ", energia)
print()

print("------------------------------------------------------")

print(" 4 - Percorre mais 80 metros e consome 25 pontos de energia. ")
print()
distanciaMetros += 80
energia -= 25
print("Distância percorrida: ", distanciaMetros, " metros")
print("Energia: ", energia)
print()

print("------------------------------------------------------")

print(" 5 - Coleta mais 2 amostras e consome 10 pontos de energia.")

amostras_coletadas += 2
energia -= 10
print("Amostras coletadas: ", amostras_coletadas)
print("Energia: ", energia)
print()
print("------------------------------------------------------")
