# Dividindo a conta
print("Bem-vindo ao divisor de conta!")
total = float(input("Qual o valor total da conta? "))
pessoas = int(input("Quantas pessoas vão dividir a conta? "))
valor_por_pessoa = total / pessoas
print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")
