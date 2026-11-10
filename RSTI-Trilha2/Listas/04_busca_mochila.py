""" Use a lista ["corda", "água", "mapa", "água"]. Leia o nome de um item e informe se ele existe e quantas vezes aparece. Diferencie maiúsculas e minúsculas.
 """
mochila = ["corda", "água", "mapa", "água"]
print("Itens na mochila:", mochila)
item = input("Digite o nome do item: ")

if item in mochila:
    print(f"O item '{item}' existe na mochila.")
    print(f"Quantidade de vezes que aparece: {mochila.count(item)}")
else:
    print(f"O item '{item}' não existe na mochila.")