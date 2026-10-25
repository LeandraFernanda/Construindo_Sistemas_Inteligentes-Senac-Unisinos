'''
Leia duas notas do mesmo peso. Se alguma nota estiver fora da faixa de 0 a 10
, mostre nota inválida e não calcule a média . Caso ambas sejam 
válidas, calcule e mostre a média e a situação: 
média a partir de 7: aprovado;
média a partir de 5 e abaixo de 7: recuperação;
média abaixo de 5: reprovado.
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Nota inválida. Por favor, digite notas entre 0 e 10.")
else:
    media = (nota1 + nota2) / 2
    print(f"A média é: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Em Recuperação")
    else:
        print("Situação: Reprovado")