'''
ler o preço do lanche e a quantidade comprada. calculeo total Considere 
preço e quantidade positivos se o total for a partir de 50 reais, aplique 
10% de desconto. caso contrario, mantenha o valor original.
mostre o total antes do desconto e o valor final .para calcular 10% de 
desconto, multiplique o total por 0.10 .teste totais abaixo de 50 , iguais
 a 50, a 50 e acima de 50.
'''

preco = float(input("Digite o preço do lanche: "))
quantidade = int(input("Digite a quantidade comprada: "))

total = preco * quantidade

if total >= 50:
    desconto = total * 0.10
    total_final = total - desconto
else:
    total_final = total

print(f"Total antes do desconto: R$ {total:.2f}")
print(f"Valor final: R$ {total_final:.2f}")

