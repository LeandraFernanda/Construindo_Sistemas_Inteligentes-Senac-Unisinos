'''
Solicite quantos alunos existem em uma turma.

Em seguida, leia a nota de cada aluno e calcule a média geral.

A quantidade de alunos deve ser maior que zero.
'''

quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))
while quantidade_alunos <= 0:
    print("Quantidade inválida. Por favor, digite um número maior que zero.")
    quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))


