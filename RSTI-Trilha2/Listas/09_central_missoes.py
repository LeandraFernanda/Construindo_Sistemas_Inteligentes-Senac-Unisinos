"""  Desenvolva um menu para registrar as pontuações das missões de um robô:

1 - Registrar pontuação
2 - Mostrar relatório
3 - Desfazer o último registro
0 - Sair
Comece com uma lista vazia de pontuações.
Na opção 1, leia um inteiro de 0 a 100. Repita a leitura enquanto estiver fora da faixa e adicione apenas o valor válido.
Na opção 2, mostre as pontuações na ordem de registro, a quantidade, o total, a média e a maior pontuação. Mostre também quantas missões tiveram pelo menos 70 pontos.
Se a lista estiver vazia, o relatório deve informar que não há missões registradas, sem calcular média ou maior pontuação.
Na opção 3, remova e mostre a última pontuação com pop(). Se a lista estiver vazia, informe que não há registro para desfazer.
A opção 0 encerra o programa. Outras opções mostram uma mensagem de erro.
Teste de mesa: registre 80, 60 e 100. O relatório deve mostrar três missões, total 240, média 80.0, maior pontuação 100 e duas missões com pelo menos 70 pontos. Desfaça o último registro: restarão [80, 60], com média 70.0 e uma missão com pelo menos 70 pontos.

Desafio adicional: crie outra lista contendo somente as pontuações a partir de 70, sem modificar a lista original.
"""
pontuacoes = []

while True:
    print("\n=== Central de Missões ===")
    print("1 - Registrar pontuação")
    print("2 - Mostrar relatório")
    print("3 - Desfazer o último registro")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        pontuacao = int(input("Digite a pontuação da missão (0 a 100): "))

        while pontuacao < 0 or pontuacao > 100:
            print("Pontuação inválida. Digite um valor entre 0 e 100.")
            pontuacao = int(input("Digite a pontuação da missão (0 a 100): "))

        pontuacoes.append(pontuacao)
        print("Pontuação registrada com sucesso!")

    elif opcao == 2:
        if not pontuacoes:
            print("Não há missões registradas.")
        else:
            print("Pontuações:", pontuacoes)
            print("Quantidade de missões:", len(pontuacoes))
            print("Total:", sum(pontuacoes))
            print("Média:", sum(pontuacoes) / len(pontuacoes))
            print("Maior pontuação:", max(pontuacoes))

            acima_70 = 0
            for valor in pontuacoes:
                if valor >= 70:
                    acima_70 += 1

            print("Missões com pelo menos 70 pontos:", acima_70)

    elif opcao == 3:
        if not pontuacoes:
            print("Não há registro para desfazer.")
        else:
            removida = pontuacoes.pop()
            print(f"Última pontuação removida: {removida}")
            print("Lista atual:", pontuacoes)

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")

        pontuacoes_70 = [p for p in pontuacoes if p >= 70]
print("Pontuações maiores ou iguais a 70:", pontuacoes_70)


