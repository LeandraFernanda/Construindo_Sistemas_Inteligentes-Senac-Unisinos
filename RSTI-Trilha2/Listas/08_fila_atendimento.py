""" Crie uma lista vazia e um menu com as opções:

1 - Adicionar pessoa ao final da fila
2 - Atender a primeira pessoa
3 - Mostrar a fila e sua quantidade de pessoas
0 - Sair
Utilize append() para adicionar e pop(0) para atender. Antes de atender, verifique se há alguém na fila. Opções desconhecidas devem apresentar uma mensagem de erro.

Teste atender com a fila vazia e adicionar Ana e Bruno para conferir a ordem dos atendimentos.  
"""
lista_fila = []
menu = """
1 - Adicionar pessoa ao final da fila
2 - Atender a primeira pessoa
3 - Mostrar a fila e sua quantidade de pessoas
0 - Sair
"""
while True:
    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pessoa = input("Digite o nome da pessoa a ser adicionada à fila: ")
        lista_fila.append(pessoa)
        print(f"{pessoa} foi adicionada à fila.")
    elif opcao == "2":
        if lista_fila:
            atendido = lista_fila.pop(0)
            print(f"{atendido} foi atendido.")
        else:
            print("A fila está vazia. Não há ninguém para atender.")
    elif opcao == "3":
        print("Fila atual: ", lista_fila)
        print("Quantidade de pessoas na fila: ", len(lista_fila))
    elif opcao == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
