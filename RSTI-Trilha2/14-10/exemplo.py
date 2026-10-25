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









# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade")

#     print("Você pode dirigir")
# else:
#     print("Você é menor de idade")
#     print("Você não pode dirigir") #o espaço seria a Identação do código, que é importante para o Python entender a hierarquia do código.

# media = float(input("Digite a media de 0 a 10:  "))

# if media >= 7:
#     print(f"Media: {media:2f}, Aprovado")
# elif media >= 5:
#     print(f"Media: {media:2f}, Recuperação")
# else:
#     print(f"Media: {media:2f}, Reprovado") windows + . = emojis
    



# idade = int(input("Idade:    😊 "))
# vagas = int(input("Vagas disponíveis: "))

# if idade >= 14 and vagas > 0:
#     print("Inscrição permitida. ")
# else:
#     print("Inscrição não permitida.")



# quantidade = int(input("Quantidade desejada:  "))
# estoque = 10

# if quantidade > 0:
#     if quantidade <= estoque: 
#         estoque = estoque - quantidade
#         print("Compra realizada com sucesso. Estoque atual: ", estoque)
#     else:
#         print("Quantidade inválida.")

# else: 
#     print("A quantidade deve ser maior que zero.")


nome = input("Nome do robô:  ")
energia = int(input("energia atual (0 a 100): "))
resposta = input("Está em manutenção? (S/N):    ")

print("======== Missão de verificação do robô ========")
print("Robô:", nome)


if energia >= 0 or energia > 100:
    print("Energia inválida. Digite um valor entre 0 e 100.")
elif resposta == "S" or resposta == "s":
    print("O robô está em manutenção. Não pode ser utilizado.") 
elif resposta == "N" or resposta == "n":
    if energia >= 50:
        print(f"O robô {nome} está pronto para uso.")
    else:
        print(f"Missão bloqueada: energia insuficiente. Nível atual: {energia}. ")    
else:
    em_manutencao = resposta == "S" or resposta == "s"

    if energia >= 50 and not em_manutencao:
        print(f"O robô {nome} está pronto para uso.")
    elif em_manutencao:
        print(f"MIssão bloqueada : robô em manutenção.")

    else:
        print(f"Missão bloqueada: energia insuficiente. Nível atual: {energia}. ")

print("Atendimento encerrado. Obrigado por utilizar o sistema de controle de robôs.")         

