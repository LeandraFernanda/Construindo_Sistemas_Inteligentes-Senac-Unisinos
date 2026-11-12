""" Defina o código fictício "ROBO123". Dê ao usuário no máximo três tentativas para acertá-lo.

Mostre o número da tentativa antes de cada leitura. Se acertar, encerre o laço com break e informe o sucesso. Se errar todas, informe que as tentativas acabaram.

Teste um acerto na primeira tentativa, um acerto na terceira e três erros. 
"""
usuario = input("Digite o código do robô: ")
codigo = "ROBO123"
for codigo in range(1, 4):
    if usuario == codigo:
        print("Código correto! Acesso permitido.")
        break
    else:
        print(f"Tentativa {codigo}: Código incorreto. Tente novamente.")
        usuario = input("Digite o código do robô: ")
print("Fim das tentativas. Acesso negado.")