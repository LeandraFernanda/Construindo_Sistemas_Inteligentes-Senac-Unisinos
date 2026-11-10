"""  Comece com ["Ana", "Bruno", "Ana", "Carla"]. Leia um nome e remova apenas sua primeira ocorrência, se existir. Caso contrário, mostre uma mensagem. Ao final, apresente a lista e a quantidade restante.

Teste com Ana e com um nome ausente em execuções separadas. """
mochila = ["Ana", "Bruno", "Ana", "Carla"]
print("Itens na mochila:", mochila)
nome = input("Digite o nome do item a ser removido: ")

if nome in mochila:
    mochila.remove(nome)
    print(f"O item '{nome}' foi removido da mochila.")
else:
    print(f"O item '{nome}' não existe na mochila.")

print("Itens restantes na mochila:", mochila)
print("Quantidade de itens restantes:", len(mochila))