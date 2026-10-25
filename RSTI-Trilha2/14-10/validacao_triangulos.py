

# Receber os três lados
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

# 1. Validar se os lados formam um triângulo
if (a > 0 and b > 0 and c > 0 and
    a + b > c and
    a + c > b and
    b + c > a):

    # 2. Classificar o triângulo
    if a == b and b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")

else:
    print("Triângulo inválido")
