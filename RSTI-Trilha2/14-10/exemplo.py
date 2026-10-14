# idade = int(input("Digite sua idade: "))
# print(f"Tipo da variavel 'idade' : {type(idade) }")
# print()
# print("No proximo aniversário voce terá",idade + 1,"anos")

# preco = float(input("Digite o preço do produto: "))
# quantidade = int(input("Quantidade:  "))

# total = preco * quantidade
# print("Total a pagar: R$", total)         


# teste = "SIM"

# print(teste)
# print()
# print(teste.lower())
# print(teste.capitalize())
# print(teste.upper())
# print(teste.swapcase())
# print(teste.islower())

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade")

    print("Você pode dirigir")
else:
    print("Você é menor de idade")
    print("Você não pode dirigir") #o espaço seria a Identação do código, que é importante para o Python entender a hierarquia do código.   
    
