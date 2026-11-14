""" Crie uma classe Turma, com nomee uma lista própria alunos, inicialmente vazia. Implemente matricular(nome_aluno)e quantidade_alunos(), que retorna o tamanho da lista.

Crie duas turmas. Matrícula duas pessoas na primeira e uma na segunda. Mostre o nome de cada turma, seus alunos e sua quantidade.

Nomes repetidos são permitidos neste exercício. Explique onde a lista deve ser criada para que uma turma não receba os alunos da outra. 
"""
class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, nome_aluno):
        self.alunos.append(nome_aluno)

    def quantidade_alunos(self):
        return len(self.alunos)

print("Turma 1:")
turma1 = Turma("Turma A")   
turma1.matricular("Alice")
turma1.matricular("Bob")    