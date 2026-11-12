""" Leia um inteiro e apresente sua tabuada de multiplicação de 1 até 10, utilizando for. Cada linha deve mostrar os dois fatores e o resultado. 
"""
tabuada = int(input("Digite um número inteiro: "))

for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")
    