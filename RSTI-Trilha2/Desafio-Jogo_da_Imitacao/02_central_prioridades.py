""" Missão 2 — Central de prioridades
Arquivo: 02_central_prioridades.py

A equipe dispõe de tempo limitado para analisar uma mensagem. As prioridades abaixo são regras fictícias para praticar decisões em Python.
"""

identificacao = input("Identificação da mensagem: ")
tempo_disponivel = float(input("Tempo disponível (em minutos): "))
tempo_necessario = float(input("Tempo necessário (em minutos): "))
risco_imediato = input("A mensagem indica risco imediato? (sim/nao): ").strip().lower()
pista_recorrente = input("A mensagem contém uma pista recorrente? (sim/nao): ").strip().lower()

if tempo_disponivel <= 0 or tempo_necessario <= 0:
    print("Tempo inválido")
elif risco_imediato not in ("sim", "nao") or pista_recorrente not in ("sim", "nao"):
    print("Resposta inválida")
else:
    if tempo_necessario > tempo_disponivel:
        resultado = "Solicitar apoio: tempo insuficiente"
    elif risco_imediato == "sim":
        resultado = "Prioridade máxima"
    elif pista_recorrente == "sim":
        resultado = "Prioridade alta"
    else:
        resultado = "Prioridade normal"

    print(f"Identificação da mensagem: {identificacao}")
    print(f"Resultado: {resultado}")

    if tempo_necessario <= tempo_disponivel:
        tempo_restante = tempo_disponivel - tempo_necessario
        print(f"Tempo restante: {tempo_restante} minutos")

# para comentar crtl + schift + A 
# format é usado para formatar a saída de texto, permitindo inserir variáveis dentro de uma string de forma legível e organizada. No código acima, ele é utilizado para exibir a identificação da mensagem, o resultado da análise e o tempo restante de forma clara e estruturada.
# def é definindo uma função em Python
# \n é usado para criar uma nova linha na saída de texto, permitindo que o texto seja exibido em linhas separadas para melhor legibilidade.
