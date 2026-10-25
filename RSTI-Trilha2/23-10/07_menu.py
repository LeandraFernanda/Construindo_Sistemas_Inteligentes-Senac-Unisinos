'''
Crie um menu com as seguintes opções:

=== MENU ===
1 - Somar dois números
2 - Verificar maioridade
0 - Sair
O menu deverá continuar aparecendo até o usuário escolher a opção 0.

Utilize while True, condicionais e break.
'''

while True:
    print("=== MENU ===")
    print("1 - Somar dois números")
    print("2 - Verificar maioridade")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print(f"A soma é: {numero1 + numero2}")
    elif opcao == "2":
        idade = int(input("Digite a idade: "))
        if idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")
    elif opcao == "0":
        print("Saindo do menu...")
        break
    else:
        print("Opção inválida!")