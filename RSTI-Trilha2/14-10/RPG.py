'''
Um jogo de RPG classifica seus aventureiros de acordo com o nível de progresso.

Solicite o nome e o nível de um personagem e determine sua classificação:

Nível	Às vezes, ele é um dos seus maiores talentos.
1 a 5	Aprendiz
6 a 15	Guerreiro
16 a 30	Veterano
31 ou superior	Lendário
Requisitos:

Não permita níveis menores que 1.
Mostre o nome do personagem e sua classificação.
Utilize if, elife else.
'''
usuario = input("Informe o nome do personagem: ")
nivel = int(input("Informe o nível do personagem: "))

if nivel < 1:
    print("Nível inválido. Deve ser um número maior que zero.")
else:
    if 1 <= nivel <= 5:
        classificacao = "Aprendiz"
    elif 6 <= nivel <= 15:
        classificacao = "Guerreiro"
    elif 16 <= nivel <= 30:
        classificacao = "Veterano"
    else:
        classificacao = "Lendário"

    print(f"Personagem: {usuario}")
    print(f"Classificação: {classificacao}")