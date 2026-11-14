""" Crie uma aula Livrocom tituloe emprestado. O título é recebido na criação; emprestadocomeça como False.

emprestar()deve mudar o estado para Truee retornar True, já que o livro ainda não está emprestado. Caso contrário, deve retornar False.
devolver()deve mudar o estado para Falsee retornar True, desde que exista um empréstimo. Caso contrário, deve retornar False.
Teste duas extrações de empréstimo seguidas de duas extrações de devolução. Mostrar os retornos e o estado após cada operação.

Conferência: os retornos são True, False, True, False. 
"""
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return True
        return False

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return True
        return False

    