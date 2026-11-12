""" Leia seis números inteiros. Ao final, mostre a soma de todos os números e quantos deles são maiores que zero.

Use um acumulador para a soma e um contador para os positivos. O zero participa da soma, mas não deve ser contado como positivo.

Teste com números positivos, negativos e zero na mesma execução. 
"""
numeros = 0
positivos = 0
for i in range(6):
    numero = int(input("Digite um número inteiro: "))
    numeros += numero
    if numero > 0:
        positivos += 1
    else:
        continue
print(f"Soma: {numeros}")    
print(f"Quantidade de positivos: {positivos}")    