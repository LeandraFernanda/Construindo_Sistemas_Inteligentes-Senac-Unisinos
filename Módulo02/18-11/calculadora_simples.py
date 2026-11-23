""" Crie uma aplicação que receba dois valores numéricos e possua quatro botões, um para cada operação matemática: soma, subtração, multiplicação e divisão.

O resultado deverá ser apresentado na própria interface. Não se esqueça de validar os valores informados e impedir divisões por zero.

```text
+---------------------------------+
| Calculadora simples             |
+---------------------------------+
| Primeiro valor: [ 10          ] |
| Segundo valor:  [ 5           ] |
|                                 |
|    [ + ] [ - ] [ * ] [ / ]      |
|                                 |
|          Resultado: 15          |
+---------------------------------+
```
 
"""
import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora simples")
janela.geometry("400x300")
janela.resizable(False, False)

# Labels e campos de entrada
tk.Label(janela, text="Primeiro valor:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_valor1 = tk.Entry(janela)
entry_valor1.grid(row=0, column=1, padx=10, pady=5)
tk.Label(janela, text="Segundo valor:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_valor2 = tk.Entry(janela)
entry_valor2.grid(row=1, column=1, padx=10, pady=5) 

# Rótulo para exibir o resultado
rotulo_resultado = tk.Label(janela, text="Resultado: ", fg="blue")
rotulo_resultado.grid(row=4, columnspan=2, pady=10)

# Funções para operações matemáticas
def somar():
    try:
        valor1 = float(entry_valor1.get())
        valor2 = float(entry_valor2.get())
        resultado = valor1 + valor2
        rotulo_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        rotulo_resultado.config(text="Por favor, insira valores numéricos válidos.")

def subtrair():
    try:
        valor1 = float(entry_valor1.get())
        valor2 = float(entry_valor2.get())
        resultado = valor1 - valor2
        rotulo_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        rotulo_resultado.config(text="Por favor, insira valores numéricos válidos.")

def multiplicar():
    try:
        valor1 = float(entry_valor1.get())
        valor2 = float(entry_valor2.get())
        resultado = valor1 * valor2
        rotulo_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        rotulo_resultado.config(text="Por favor, insira valores numéricos válidos.")

def dividir():
    try:
        valor1 = float(entry_valor1.get())
        valor2 = float(entry_valor2.get())
        if valor2 == 0:
            rotulo_resultado.config(text="Erro: Divisão por zero não é permitida.")
        else:
            resultado = valor1 / valor2
            rotulo_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        rotulo_resultado.config(text="Por favor, insira valores numéricos válidos.")

# Botões para operações matemáticas
botao_somar = tk.Button(janela, text="+", command=somar)
botao_somar.grid(row=2, column=0, padx=10, pady=10)
botao_subtrair = tk.Button(janela, text="-", command=subtrair)
botao_subtrair.grid(row=2, column=1, padx=10, pady=10)
botao_multiplicar = tk.Button(janela, text="*", command=multiplicar)
botao_multiplicar.grid(row=3, column=0, padx=10, pady =10)
botao_dividir = tk.Button(janela, text="/", command=dividir)
botao_dividir.grid(row=3, column=1, padx=10, pady=10)


janela.mainloop()