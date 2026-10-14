# Controle de estoque da biblioteca
livros = {
    "Python para Iniciantes": 10,
    "Algoritmos e Estruturas de Dados": 5,
    "Programação Web com Python": 8,
    "Lógica de programação em Python": 7,
    "Inteligência Artificial com Python": 3,
    "Aprendendo Django": 4,
    "Flask para Desenvolvimento Web": 6,
    "Automação de Testes com Python": 2,
    "Python para Desenvolvimento Web": 4,
    "Python para Ciência de Dados": 3,

}

print("Estoque atual:")
for livro, quantidade in livros.items():
    print(f"- {livro}: {quantidade} unidades")

emprestimos = {}

while True:
    print("\nOpções:")
    print("1. Emprestar livro")
    print("2. Devolver livro")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livro = input("Qual livro você deseja emprestar? ")
        if livro in livros and livros[livro] > 0:
            livros[livro] -= 1
            emprestimos[livro] = emprestimos.get(livro, 0) + 1
            print(f"Você emprestou o livro '{livro}'.")
        else:
            print("Livro não disponível para empréstimo.")
    elif opcao == "2":
        livro = input("Qual livro você deseja devolver? ")
        if livro in emprestimos and emprestimos[livro] > 0:
            livros[livro] += 1
            emprestimos[livro] -= 1
            print(f"Você devolveu o livro '{livro}'.")
        else:
            print("Você não tem esse livro emprestado.")
    elif opcao == "3":
        break
    else:
        print("Opção inválida.")

print("\nEstoque final:")
for livro, quantidade in livros.items():
    print(f"- {livro}: {quantidade} unidades")

print("\nEmpréstimos atuais:")
for livro, quantidade in emprestimos.items():
    print(f"- {livro}: {quantidade} unidades")

