'''
Solicite cinco números inteiros e apresente a soma de todos eles.

Utilize um contador para controlar as repetições e um acumulador para guardar a soma.
'''

numeros = int(input("Digite cinco números inteiros:  "))
contador = 0
acumulador = 0


while contador < 5:
    acumulador += numeros
    contador += 1
    if contador < 5:
        numeros = int(input("Digite outro número inteiro:  "))

print("A soma dos cinco números é:  ", acumulador)
             