'''
Leia a temperatura e mostre apenas uma classificação: 
abaixo de 18: ambiente frio;
a partir de 18 e abaixo de 26: ambiente agradável;
a partir de 26: ambiente quente.
testar espcialmente os valores 18 e 26.
'''

temperatura = float(input("Digite a temperatura: "))

if temperatura < 18:
    print("O ambiente está frio.")
elif temperatura < 26:
    print("O ambiente está agradável.")
else:
    print("O ambiente está quente.")
    