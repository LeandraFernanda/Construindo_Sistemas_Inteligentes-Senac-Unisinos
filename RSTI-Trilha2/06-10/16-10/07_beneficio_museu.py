'''
Leia uma idade não negativa . Neste museu ficticio, pessoas com 
menos de 12 anos ou a partir de 60 anos tem entrada gratuita.
As demais pagam R$ 20,00.
Usar o (OR) e teste as idades 11, 12, 59 e 60.
'''

idade = int(input("Digite a idade: "))
if idade < 12 or idade >= 60:
    print("Entrada gratuita.")
else:
    print("Entrada paga: R$ 20,00.")


print("Fim do programa.")