""" Leia oito inteiros e armazene-os em uma lista. Percorra essa lista para criar outra contendo apenas os números pares. Mostre as duas listas. Preserve a ordem e os repetidos.

Lembre-se: numero % 2 == 0 identifica um par, incluindo zero e pares negativos. Teste também uma execução sem nenhum par. 
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)    
       
print("Números:", numeros)
print("Pares:", pares)

