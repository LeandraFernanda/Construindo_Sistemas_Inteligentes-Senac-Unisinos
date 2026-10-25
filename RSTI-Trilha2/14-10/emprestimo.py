'''
Um banco deseja automatizar a análise inicial de empréstimos.

Solicite as seguintes informações:

Salário mensal do cliente.
Valor solicitado para empréstimo.
Quantidade de parcelas.
O empréstimo só poderá ser aprovado se todas as condições forem atendidas:

O salário deve ser de pelo menos R$ 2.000,00.
O valor solicitado não pode ultrapassar 10 vezes o salário.
O valor de cada parcela não pode ultrapassar 30% do salário.
A quantidade de parcelas deve estar entre 1 e 48.
Caso alguma condição não seja atendida, informe que o empréstimo foi recusado.

Desafio: Apresente o motivo da recusa.

Considere um empréstimo sem juros, apenas para fins de exercício.
'''
cliente_salario = float(input("Digite o salário mensal do cliente: ").replace(",", "."))
if cliente_salario < 2000:
    print("Empréstimo recusado: Salário insuficiente.")
else:
    cliente_emprestimo = float(input("Digite o valor solicitado para empréstimo: ").replace(",", "."))
    if cliente_emprestimo > 10 * cliente_salario:
        print("Empréstimo recusado: Valor solicitado ultrapassa o limite.")
    else:
        cliente_parcelas = int(input("Digite a quantidade de parcelas: "))
        if not (1 <= cliente_parcelas <= 48):
            print("Empréstimo recusado: Quantidade de parcelas inválida.")
        else:
            valor_parcela = cliente_emprestimo / cliente_parcelas
            if valor_parcela > 0.3 * cliente_salario:
                print("Empréstimo recusado: Valor da parcela ultrapassa o limite.")
            else:
                print("Empréstimo aprovado!")
print(f"Valor da parcela: R$ {valor_parcela:.2f} em {cliente_parcelas} parcelas.")
print(f"Valor total a ser pago: R$ {cliente_emprestimo:.2f}.")
print(f"Salário do cliente: R$ {cliente_salario:.2f}.")
print(f"Valor da parcela: R$ {valor_parcela:.2f}.")
print("Obrigado por utilizar nosso sistema de análise de empréstimos.")                