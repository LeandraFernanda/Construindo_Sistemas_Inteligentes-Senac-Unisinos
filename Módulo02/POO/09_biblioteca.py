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
