'''
Durante uma aventura, um personagem encontra um inimigo e precisa decidir se consegue derrotá-lo.

Solicitar:

Nome do personagem.
Vida atual.
Pontos de ataque.
Vida do inimigo.
Pontos de defesa do inimigo.
tipo o dano causado:

dano = ataque - defesa
Considere as seguintes regras:

Se a vida do personagem for menor ou igual a zero, ele não poderá atacar.
Se o dano for menor ou igual a zero, o ataque não causará dano.
Se o dano for maior ou igual à vida do inimigo, o inimigo será derrotado.
Caso contrário, o inimigo sobreviverá. Exiba a vida restante dele.
Desafio: Impedir que a vida restante do inimigo fique negativa.
'''

usuario = input("Informe o nome do personagem: ")
vida_personagem = int(input("Informe a vida atual do personagem: "))    

ataque_personagem = int(input("Informe os pontos de ataque do personagem: "))
vida_inimigo = int(input("Informe a vida do inimigo: "))
defesa_inimigo = int(input("Informe os pontos de defesa do inimigo: "))
