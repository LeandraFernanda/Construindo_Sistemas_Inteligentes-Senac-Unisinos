'''
Leia dois números decimais . Mostre um menu com as opções 1
para somar, 2 para subtrair , 3 para multiplicar  e 4 para dividir. Leia 
a opção como texto .
Execute somente a operação ecolhida. Se a opção não existir , 
mostre opção não existir , mostre a opção inválida. Na 
divisão , verifique se o segundo número é zero antes
de calcular;
nesse caso, mostre não é possível dividir por zero
'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    print(numero1 + numero2)
elif opcao == "2":
    print(numero1 - numero2)
elif opcao == "3":
    print(numero1 * numero2)
elif opcao == "4":
    if numero2 == 0:
        print("Não é possível dividir por zero")
    else:
        print(numero1 / numero2)
else:
    print("Opção inválida!")
