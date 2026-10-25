'''
Crie uma loja com atendimento de uma única compra por execução.

Leia o nome do aventureiro e sua quantidade de ouro, como número inteiro.
Se o ouro for negativo, mostre Quantidade de ouro inválida e não prossiga com a compra.
Caso contrário, mostre um menu: 1 para poção de vida (25 moedas), 2 para escudo (60 moedas) e 3 para espada (100 moedas).
Leia a opção como texto e verifique se ela existe.
Para uma opção válida, verifique se o ouro é suficiente. Se for, desconte o preço e mostre o item adquirido e o saldo restante. Caso contrário, informe quantas moedas faltam.
Se a opção não existir, mostre Item inválido.
O ouro só pode ser descontado quando a compra for confirmada. Teste uma compra com sobra de ouro, uma com o valor exato, outra com saldo insuficiente, uma opção inválida e um saldo inicial negativo.


'''

nome = input("Digite o nome do aventureiro: ")
ouro = int(input("Digite a quantidade de ouro: "))

if ouro < 0:
    print("Quantidade de ouro inválida")
else:
    print("Menu de itens:")
    print("1 - Poção de vida (25 moedas)")
    print("2 - Escudo (60 moedas)")
    print("3 - Espada (100 moedas)")
    opcao = input("Escolha um item: ")
print("Opção escolhida:", opcao)  # Adicionado para depuração, para verificar a entrada do usuário.