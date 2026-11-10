""" Leia a quantidade de alunos. Se for menor ou igual a zero, informe que a quantidade é inválida. Para uma quantidade válida, leia e armazene as notas, solicitando novamente qualquer nota fora da faixa de 0 a 10.

Mostre todas as notas, a média, a maior nota, a menor nota e quantas atingiram pelo menos 7.

Teste com apenas um aluno, com notas repetidas e com uma nota inválida seguida de uma válida.  
"""
alunos = int(input("Digite a quantidade de alunos: "))
notas = []

if alunos <= 0:
    print("Quantidade de alunos inválida.")
else:
    for i in range(1, alunos + 1):
        nota = float(input(f"Digite a nota do aluno {i}: "))
        while nota < 0 or nota > 10:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
            nota = float(input(f"Digite a nota do aluno {i}: "))
        notas.append(nota)

    print("Notas dos alunos: ", notas)
    print("Média das notas: ", sum(notas) / len(notas))
    print("Maior nota: ", max(notas))
    print("Menor nota: ", min(notas))
    print("Quantidade de alunos que atingiram pelo menos 7: ", len([nota for nota in notas if nota >= 7]))

