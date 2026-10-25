nome = input("Digite seu nome:  ")
cidade = input("Digite sua cidade:  ")
idade = int(input("Digite sua idade:  "))

'''
  mostra ficha e calcule quantos anos ela tera no proximo aniversário


'''

print("Ficha do Usuário:")
print(f"Nome: {nome}")
print(f"Cidade: {cidade}")
print(f"Idade: {idade}")

print(f"No próximo aniversário, {nome} terá {idade + 1} anos.")
