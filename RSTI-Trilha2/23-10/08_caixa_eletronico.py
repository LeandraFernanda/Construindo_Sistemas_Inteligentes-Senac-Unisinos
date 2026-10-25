'''
Desenvolva um caixa eletrônico simples com saldo inicial de R$ 500.00.

O programa deverá apresentar o seguinte menu:

=== CAIXA ELETRÔNICO ===
1 - Consultar saldo
2 - Depositar dinheiro
3 - Sacar dinheiro
0 - Sair
Regras:

O menu deverá continuar funcionando até que o usuário escolha sair.
Depósitos e saques devem possuir valores maiores que zero.
Não será permitido sacar mais dinheiro do que existe na conta.
O saldo deverá ser atualizado após depósitos e saques válidos.
Opções inválidas devem apresentar uma mensagem de erro.
Desafio adicional: conte quantos depósitos e saques foram realizados durante a execução.
'''

saldo = 1000.00
contagem_depositos = 0
contagem_saques = 0

while True:
    print("=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            contagem_depositos += 1
            print(f"Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
        else:
            print("Valor de depósito inválido. Deve ser maior que zero.")
    elif opcao == "3":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque > 0:
            if valor_saque <= saldo:
                saldo -= valor_saque
                contagem_saques += 1
                print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido. Deve ser maior que zero.")
    elif opcao == "0":
        print(f"Saindo do caixa eletrônico. Total de depósitos realizados: {contagem_depositos}, total de saques realizados: {contagem_saques}.")
        break
    else:
        print("Opção inválida!")