import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("350x300")

rotulo = tk.Label()

# Primeiro número
tk.Label(janela, text="Primeiro número:").pack(pady=5)
entrada1 = tk.Entry(janela, width=20)
entrada1.pack()

# Segundo número
tk.Label(janela, text="Segundo número:").pack(pady=5)
entrada2 = tk.Entry(janela, width=20)
entrada2.pack()

# Onde vai aparecer o resultado
label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack(pady=15)

# Função que calcula
def calcular(operacao):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())

        if operacao == "+":
            resultado = n1 + n2
        elif operacao == "-":
            resultado = n1 - n2
        elif operacao == "*":
            resultado = n1 * n2
        elif operacao == "/":
            resultado = n1 / n2

        label_resultado.config(text=f"Resultado: {resultado}")
        print(f"{n1} {operacao} {n2} = {resultado}")

    except ValueError:
        label_resultado.config(text="Digite números válidos!")
    except ZeroDivisionError:
        label_resultado.config(text="Não pode dividir por zero!")

# Botões das operações
tk.Button(janela, text="+ Somar", width=15, command=lambda: calcular("+")).pack(pady=2)
tk.Button(janela, text="- Subtrair", width=15, command=lambda: calcular("-")).pack(pady=2)
tk.Button(janela, text="* Multiplicar", width=15, command=lambda: calcular("*")).pack(pady=2)
tk.Button(janela, text="/ Dividir", width=15, command=lambda: calcular("/")).pack(pady=2)

janela.mainloop()