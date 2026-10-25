'''
Uma aplicação possui um sistema simples de autenticação.

Consideram-se como credenciais cadastradas:

usuario_correto = "admin"senha_correta = "python123"
Solicite que uma pessoa informe seu usuário e sua senha.

O programa deverá apresentar uma das seguintes mensagens:

Acesso autorizado!— quando ambos estiverem corretos.
Senha incorreta!— quando o usuário estiver correto, mas a senha estiver errada.
Usuário não encontrado!— quando o usuário não existir.
Desafio: Utilize condições aninadas para verificar primeiro o usuário e depois a senha.
'''
usuario_correto = "admin"
senha_correta = "python123"

usuario = input("Digite o usuário: ")
if usuario == usuario_correto:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso autorizado!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não encontrado!")