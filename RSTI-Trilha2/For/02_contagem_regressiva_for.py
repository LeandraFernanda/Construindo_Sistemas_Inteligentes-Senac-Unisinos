""" Leia um número inteiro positivo e mostre os números de 1 até ele, incluindo o limite. Se a entrada for menor ou igual a zero, mostre uma mensagem de valor inválido.

Teste com 1, 5e 0 
"""


n = int(input("Digite um número inteiro positivo: "))


if n <= 0:
    print("Valor inválido! Digite um número maior que zero.")
else:
   
    for numero in range(1, n + 1):
        print(numero)
    print("Encerrado!")           