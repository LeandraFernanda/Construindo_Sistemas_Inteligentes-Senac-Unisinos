'''
Um laboratório de tecnologia possui equipamentos que só podem ser utilizados por pessoas autorizadas.

Solicitar:

Idade.
Se uma pessoa é aluno matriculado ( simou nao).
Se possui autorização do professor ( simou nao).
Se o laboratório está disponível ( simou nao).
O acesso será permitido quando:

O laboratório está disponível.
A pessoa tem pelo menos 16 anos.
A pessoa para matriculada ou possui autorização do professor.
Requisitos: Utilize ande orapresente uma mensagem indicando se o acesso foi permitido ou negado.
'''

idade = int(input("Informe a idade: ")) 
aluno_matriculado = input("É aluno matriculado? (sim/nao): ").strip().lower()  # Normaliza a entrada para evitar problemas com maiúsculas/minúsculas e espaços.
autorizacao_professor = input("Possui autorização do professor? (sim/nao): ").strip().lower()  # Normaliza a entrada para evitar problemas com maiúsculas/minúsculas e espaços.
laboratorio_disponivel = input("O laboratório está disponível? (sim/nao): ").strip().lower()  # Normaliza a entrada para evitar problemas com maiúsculas/minúsculas e espaços.

if laboratorio_disponivel == "sim" and idade >= 16 and (aluno_matriculado == "sim" or autorizacao_professor == "sim"):
    print("Acesso permitido!")
else:
    print("Acesso negado!")

print("processo finalizado")  