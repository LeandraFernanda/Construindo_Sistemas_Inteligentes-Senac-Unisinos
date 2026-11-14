""" Crie uma aula Retangulo, inicializada com largurae altura, ambas positivas. Implemente calcular_area(), que devolva a multiplicação dessas medidas.

Crie dois objetos e mostre suas áreas fora do método. Teste com medidas 4e 3: área 12.

Para explicar: qual é a diferença entre retornar a área e mostrá-la dentro do método? 
"""
class Retangulo:
    def __init__(self, largura, altura):
        if largura <= 0 or altura <= 0:
            raise ValueError("Largura e altura devem ser positivos.")
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


retangulo1 = Retangulo(4, 3)
retangulo2 = Retangulo(2, 5)

print(retangulo1.calcular_area())
print(retangulo2.calcular_area())        