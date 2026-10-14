# Boletim de notas

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")

