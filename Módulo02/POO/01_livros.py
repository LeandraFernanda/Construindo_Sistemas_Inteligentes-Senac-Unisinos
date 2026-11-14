""" Crie uma classe Livro, com os atributos titulo, autore paginas, recebidos em __init__.

Crie dois livros diferentes e apresente seus dados. Altere o número de páginas de apenas um deles e mostre os dois novamente.

Para explicar: quais são a classe, as instâncias e os atributos? A alteração afetou os dois livros? 
"""
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

titulo = "Senhor dos Anéis"
autor = "J.R.R. Tolkien"
paginas = 600

titulo2 = "Harry Potter"
autor2 = "J.K. Rowling"
paginas2 = 400

titulo3 = "Senhor dos Anéis 2"
autor3 = "J.R.R. Tolkien"
paginas3 = 650

#preciso exibir os livros para eu escolher os livros
print(f"Livro 1: {titulo} - Autor: {autor} - Páginas: {paginas}")
print(f"Livro 2: {titulo2} - Autor: {autor2} - Páginas: {paginas2}")
print(f"Livro 3: {titulo3} - Autor: {autor3} - Páginas: {paginas3}")
print("-----------------------------------")


livro1 = Livro(titulo, autor, paginas)
livro2 = Livro(titulo2, autor2, paginas2)