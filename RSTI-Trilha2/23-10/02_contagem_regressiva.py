'''
Solicite um número inteiro positivo e faça uma contagem regressiva até zero.

Ao terminar, mostre Lançamento realizado!.
'''

numero = int(input("Digite um número inteiro positivo: "))  # Corrigido para converter a entrada em inteiro, pois input retorna uma string.
while numero < 1:  # Adicionado um loop para garantir que o número seja positivo.
    print("Número inválido. Por favor, digite um número inteiro positivo.")
    numero = int(input("Digite um número inteiro positivo: "))

for i in range(numero, -1, -1):  # Corrigido para usar range(numero, -1, -1) para incluir o número informado e contar regressivamente até zero.
    print(i)  # Corrigido para imprimir cada número em uma nova linha.
print("Lançamento realizado!")