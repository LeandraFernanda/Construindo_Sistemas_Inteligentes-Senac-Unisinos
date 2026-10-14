#  O programa abaixo deveria mostrar o nome de um curso, o valor da mensalidade e se a matrícula está ativa, mas contém erros:

# nome curso = "Python básico"
# mensalidade = 89,90
# matricula_ativa = true

# print("Curso:", nome_curso)
# print("Mensalidade:", Mensalidade)
# print("Matrícula ativa:", matricula_ativa)

# Reescreva o código corrigindo:

# o nome da variável que contém um espaço;
# a escrita do número decimal;
# a escrita do valor booleano;
# a diferença entre maiúsculas e minúsculas no nome da variável.
# Para cada correção, escreva um comentário explicando a regra da aula que foi aplicada. Ao final, mostre também type(mensalidade) para verificar se o valor é um float.



# Corrigindo o código:
nome_curso = "Python básico"  # Corrigido o nome da variável para não conter espaço, pois nomes de variáveis não podem ter espaços.
mensalidade = 89.90  # Corrigido o número decimal para usar ponto como separador decimal, pois em Python usamos ponto para decimais.
matricula_ativa = True  # Corrigido o valor booleano para começar com letra maiúscula, pois em Python os valores booleanos são True e False.
print(type(mensalidade))  # Verifica o tipo da variável mensalidade

print("Curso:", nome_curso)
print("Mensalidade:", mensalidade)  # Corrigido o nome da variável para começar com letra minúscula, pois Python é case-sensitive.
print("Matrícula ativa:", matricula_ativa)
