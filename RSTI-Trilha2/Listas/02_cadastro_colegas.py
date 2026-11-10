""" Leia quatro nomes e armazene-os em uma lista inicialmente vazia. Depois, mostre cada nome em uma linha, na ordem de cadastro. Nomes repetidos são permitidos. 
"""
nomes = []
for i in range(4):
    nome = input("Digite o nome do colega: ")
    nomes.append(nome)

for nome in nomes:
    print(nome)
    