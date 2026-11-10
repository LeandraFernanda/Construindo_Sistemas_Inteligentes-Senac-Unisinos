# Missão 1 — Cadastro de uma mensagem
# Arquivo: 01_cadastro_mensagem.py

# Antes de investigar uma mensagem, a equipe precisa organizar os dados disponíveis.

# Ôm pelo teclado:

# o nome ou apelido do analista;
# a identificação da mensagem, como texto, por exemplo MSG-007;
# uma quantidade de grupos de símbolos, como inteiros;
# o tempo estimado para analisar cada grupo, em minutos, como decimal.
# —

# A quantidade de grupos e o tempo por grupo devem ser maiores que zero.
# Se qualquer um desses valores for inválido, mostrem Dados inválidose não calculem o tempo total.
# Se os dados forem válidos, calcule o tempo total estimado: quantidade de grupos multiplicada pelo tempo por grupo.
# Apresentem uma ficha com o analista, a identidade, a quantidade de grupos e o tempo total em minutos.
# Se o total for menor ou igual a 60 minutos, mostrem Análise dentro do prazo; caso contrário, mostrem Reorganizar o trabalho.
# # Para explicar: por que a identificação é texto mesmo quando contém algarismos? Por que é adequado usar float()para o tempo em grupo?

nome = input("Nome do analista: ")
identificacao = input("Identificação da mensagem: ")

quantidade_grupos = int(input("Quantidade de grupos de símbolos: "))
tempo_por_grupo = float(input("Tempo estimado para analisar cada grupo (em minutos): "))

if quantidade_grupos <= 0 or tempo_por_grupo <= 0:
    print("Dados inválidos")
else:
    tempo_total = quantidade_grupos * tempo_por_grupo

    print("\n=== FICHA DE ANÁLISE ===")
    print("Analista:", nome)
    print("Identificação da mensagem:", identificacao)
    print("Quantidade de grupos:", quantidade_grupos)
    print("Tempo total estimado (em minutos):", tempo_total)

    if tempo_total <= 60:
        print("Análise dentro do prazo")
    else:
        print("Reorganizar o trabalho")