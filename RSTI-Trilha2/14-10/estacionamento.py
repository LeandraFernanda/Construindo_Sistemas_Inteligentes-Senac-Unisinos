'''
Um estacionamento precisa calcular o valor cobrado de seus clientes de acordo com o tempo de permanência.

Desenvolva um programa que solicite a quantidade de horas que um veículo estacionado.

As regras são:

Tempo de chuva	Valentia
2 horas	R$ 10,00
Mais de 2 a 5 horas	R$ 20,00
Mais de 5 horas	R$ 30,00
Requisitos:

A quantidade de horas deve ser maior que zero.
Caso seja informado um valor inválido, apresenta uma mensagem.
Exiba o valor total a pagar.
'''


try:
    horas = float(input("Informe a quantidade de horas estacionado: ").replace(",", "."))

    if horas <= 0:
        print("Valor inválido. A quantidade de horas deve ser maior que zero.")
    elif horas <= 2:
        valor = 10
        print(f"Valor total a pagar: R$ {valor:.2f}")
    elif horas <= 5:
        valor = 20
        print(f"Valor total a pagar: R$ {valor:.2f}")
    else:
        valor = 30
        print(f"Valor total a pagar: R$ {valor:.2f}")
except ValueError:
    print("Valor inválido. Informe uma quantidade de horas numérica.")

