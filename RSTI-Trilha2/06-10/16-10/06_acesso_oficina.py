'''
Leia a idade e pergunte se a pessoa possui inscrição (sim/não).
 Considere idade não negativa e uma das duas respostas indicadas
 A entrada só será permitida para quem tiver pelo menos 14 anos e inscrição confirmada
 Use and. Teste uma pessoa que atende aos dois critérios , outra que atende a apenas 
 um e outra que não atende a nenhum dos critérios.
'''

idade = int(input("Digite a idade: "))
inscricao = input("Possui inscrição? (sim/não): ")

if idade >= 14 and inscricao.lower() == "sim":
    print("Entrada permitida.")

elif idade < 14 and inscricao.lower() == "sim":
    print("Entrada não permitida: idade insuficiente.")

elif idade >= 14 and inscricao.lower() == "não":
    print("Entrada não permitida: inscrição não confirmada.")
else:
    print("Entrada não permitida: idade insuficiente e inscrição não confirmada.")

print("Fim do programa.")    