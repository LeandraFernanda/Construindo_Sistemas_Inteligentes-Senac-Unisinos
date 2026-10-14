# Uma turma com 20 alunos fará um passeio. O ônibus custa R$ 600.00 para toda a turma. Cada ingresso custa R$ 15.00 e cada lanche custa R$ 10.00 por aluno.

# Crie variáveis para os dados e calcule, em variáveis separadas:

# o custo de todos os ingressos;
# o custo de todos os lanches;
# o custo total do passeio, incluindo o ônibus uma única vez;
# o valor que cada aluno deverá pagar, dividindo o custo total igualmente.
# Mostre um relatório com a quantidade de alunos e todos os custos. Depois altere a quantidade de alunos para 25 e execute novamente sem modificar as fórmulas.

# Para pensar: por que o custo total aumenta, mas o valor por aluno diminui?   

alunos = 20
custo_onibus = 600.00
custo_ingressos = alunos * 15.00  # Custo total dos ingressos
custo_lanches = alunos * 10.00  # Custo total dos lanches
custo_total = custo_onibus + custo_ingressos + custo_lanches  # Custo total do passeio
valor_por_aluno = custo_total / alunos  # Valor que cada aluno deverá pagar

print("Relatório do Passeio:")
print("Quantidade de alunos:", alunos)
print("Custo total dos ingressos: R$ {:.2f}".format(custo_ingressos))
print("Custo total dos lanches: R$ {:.2f}".format(custo_lanches))
print("Custo total do passeio: R$ {:.2f}".format(custo_total))
print("Valor por aluno: R$ {:.2f}".format(valor_por_aluno))
