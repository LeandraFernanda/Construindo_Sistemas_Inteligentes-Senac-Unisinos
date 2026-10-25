'''
Uma loja virtual deseja calcular o valor do frete com base na região do cliente e no valor da compra.

Solicite o valor da compra e a região de entrega:

Região	Frete
Sul	R$ 15,00
Sudeste	R$ 20,00
Centro-Oeste	R$ 25,00
Norte ou Nordeste	R$ 35,00
 extra:

Compras a partir de R$ 300,00 recebem frete grátis.
Compras com valor menor ou igual a zero são inválidas.
Regiões não reconhecidas devem apresentar Região inválida.
Mostre o valor da compra, o frete e o total.
Atenção: Mesmo que a compra tenha frete grátis, a região informada deverá ser válida.
'''
valor_compra = float(input("Digite o valor da compra: ").replace(",", "."))
if valor_compra <= 0:
    print("Valor de compra inválido. Deve ser maior que zero.") 

else:
    regiao = input("Digite a região de entrega (Sul, Sudeste, Centro-Oeste, Norte ou Nordeste): ").strip().lower()
    if regiao == "sul":
        frete = 15.00
    elif regiao == "sudeste":
        frete = 20.00
    elif regiao == "centro-oeste":
        frete = 25.00
    elif regiao in ["norte", "nordeste"]:
        frete = 35.00
    else:
        print("Região inválida.")
        frete = None

    if frete is not None:
        if valor_compra >= 300:
            frete = 0.00
            print("Frete grátis aplicado!")
        
        total = valor_compra + frete
        print(f"Valor da compra: R$ {valor_compra:.2f}")
        print(f"Valor do frete: R$ {frete:.2f}")
        print(f"Total a pagar: R$ {total:.2f}") 
        