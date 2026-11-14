""" Crie uma aula Contador. Cada instância deve começar com valor = 0e oferecer os métodos incrementar()e zerar().

Crie dois contadores. Incremente o primeiro três vezes e o segundo uma vez. Mostre os valores, zere somente o primeiro e mostre novamente.

Resultado esperado: primeiro 3e 1; depois 0e 1. 
"""
class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1

    def zerar(self):
        self.valor = 0

contador1 = Contador()
contador2 = Contador()

for _ in range(3):
    contador1.incrementar()

contador2.incrementar()

print(f"Primeiro contador: {contador1.valor}")
print(f"Segundo contador: {contador2.valor}")

contador1.zerar()

print(f"Após zerar o primeiro: {contador1.valor}")
print(f"Segundo contador: {contador2.valor}")