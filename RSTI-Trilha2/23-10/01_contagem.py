'''
Solicite um número inteiro positivo e apresente todos os números de 1 até o valor informado.

Exemplo:

Digite um número: 5

1
2
3
4
5
'''

numero = int(input("Digite um número inteiro positivo: "))  # Corrigido para converter a entrada em inteiro, pois input retorna uma string.
while numero < 1:  # Adicionado um loop para garantir que o número seja positivo.
    print("Número inválido. Por favor, digite um número inteiro positivo.")
    numero = int(input("Digite um número inteiro positivo: "))  

for i in range(1, numero + 1):  # Corrigido para usar range(1, numero + 1) para incluir o número informado.
    print(i)  # Corrigido para imprimir cada número em uma nova linha.        