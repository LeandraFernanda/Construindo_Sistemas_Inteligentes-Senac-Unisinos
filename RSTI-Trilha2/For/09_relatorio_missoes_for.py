""" Um robô pode realizar até cinco missões. Ele começa com 100 pontos de energia, e cada missão custa 25 pontos.

Utilize for para percorrer as missões de 1 até 5.
Antes de pedir o resultado da missão, verifique se existe energia suficiente. Se não houver, mostre Energia insuficiente e encerre o laço com break.
Para cada missão que puder ser realizada, solicite uma pontuação inteira entre 0 e 100. Utilize while para repetir a leitura enquanto a pontuação estiver fora da faixa.
Após receber uma pontuação válida, desconte a energia, acumule os pontos e conte a missão realizada.
Ao final, mostre a quantidade de missões realizadas, a pontuação total, a média de pontos por missão realizada e a energia restante. Só calcule a média se houver pelo menos uma missão realizada.
Teste de mesa: com pontuações 80, 60, 100 e 40, o robô deve completar quatro missões, somar 280 pontos, obter média 70.0 e terminar com energia 0. A quinta missão não deve solicitar pontuação.

Desafio adicional: altere a energia inicial para 20. O programa deve encerrar sem realizar missões e sem tentar dividir por zero. 
"""
print("***********************Missões do robô************************")
print("O robô começa com 100 pontos de energia, e cada missão custa 25 pontos.")
nome = input("Digite o nome do Robô:  ")
print("**************************************************************")
missao = input("Digite quantas missões o robô tem: ")
print("**************************************************************")
pontos = input("Digite quantos pontos o robô tem: ")
print("**************************************************************")

qtd = 0
missao = 0
for qtd in range(1, 6):
    energia = 100
    if energia < 25:
        print("Energia insuficiente")
        break
    else:
        while True:
            pontos = int(input(f"Digite a pontuação da missão {qtd} (0 a 100): "))
            if 0 <= pontos <= 100:
                break
            else:
                print("Pontuação inválida. Digite novamente.")
        energia -= 25
        missao += 1
        print(f"Missão {qtd} realizada com sucesso! Pontos: {pontos}, Energia restante: {energia}")
print("Encerrado")        


