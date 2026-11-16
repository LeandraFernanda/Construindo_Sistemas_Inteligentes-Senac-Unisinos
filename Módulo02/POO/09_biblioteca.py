""" Utilize a classe Livro do exercício 05 e uma lista com três livros de títulos diferentes. Construa um menu:
1 - Mostrar livros e disponibilidade
2 - Emprestar um livro
3 - Devolver um livro
0 - Sair
Nas opções 2 e 3, leia o título e procure o objeto com um for. Considere a correspondência exata entre os textos.

Se encontrar, chame o método adequado e apresente uma mensagem conforme seu retorno.
Se não encontrar, informe Livro não encontrado.
Trate opções desconhecidas com uma mensagem.
Repita o menu até escolher 0.
Teste: emprestar um livro disponível, tentar emprestá-lo novamente, devolvê-lo, tentar devolver um livro disponível e procurar um título inexistente.

As regras de empréstimo devem permanecer nos métodos. O menu fica responsável por receber entradas, localizar o objeto e mostrar os resultados.
"""
print("***********************Biblioteca************************")
class Livros:
    def __init__(self, titulo, disponivel=True):
        self.titulo = titulo
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            return False

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        else:
            return False 
livros = [
    Livros("Livro A", True),
    Livros("Livro B", True),
    Livros("Livro C", True)
]
print("Menu:")
while True:
    print("\n1 - Mostrar livros e disponibilidade")
    print("2 - Emprestar um livro")
    print("3 - Devolver um livro")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for livro in livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"Título: {livro.titulo}, Status: {status}")
    elif opcao == "2":
        titulo = input("Digite o título do livro que deseja emprestar: ")
        encontrado = False
        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True
                if livro.emprestar():
                    print(f"Livro '{titulo}' emprestado com sucesso.")
                else:
                    print(f"Livro '{titulo}' não está disponível para empréstimo.")
                break
        if not encontrado:
            print("Livro não encontrado.")
    elif opcao == "3":
        titulo = input("Digite o título do livro que deseja devolver: ")
        encontrado = False
        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True
                if livro.devolver():
                    print(f"Livro '{titulo}' devolvido com sucesso.")
                else:
                    print(f"Livro '{titulo}' já está disponível na biblioteca.")
                break
        if not encontrado:
            print("Livro não encontrado.")
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção desconhecida. Tente novamente.")

print("***********************Fim do Programa************************")        

