""" Leia um número inteiro positivo e mostre os números de 1 até ele, incluindo o limite. Se a entrada for menor ou igual a zero, mostre uma mensagem de valor inválido.

Teste com 1, 5 e 0  
"""

numero = int(input("Digite um numero positivo: "))

if numero <= 0:
    print("Valor inválido")
else:
    for n in range(1, numero + 1):
        print(n)

