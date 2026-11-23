""" Crie um formulário utilizando o gerenciador de layout `grid()`. O formulário deverá possuir campos para nome, idade e e-mail, além de um botão "Cadastrar".

Ao clicar no botão, verifique se todos os campos foram preenchidos e apresente as informações cadastradas em um rótulo na própria interface. 
"""
import tkinter as tk

janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("400x300")
janela.resizable(False, False)

# Labels e campos de entrada
tk.Label(janela, text="Nome:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Idade:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="E-mail:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_email = tk.Entry(janela)
entry_email.grid(row=2, column=1, padx=10, pady=5)

# Rótulo para exibir informações cadastradas
rotulo_informacoes = tk.Label(janela, text="", fg="blue")
rotulo_informacoes.grid(row=4, columnspan=2, pady=10)

# Botão de cadastro
def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()

    if nome and idade and email:
        rotulo_informacoes.config(text=f"Nome: {nome}\nIdade: {idade}\nE-mail: {email}")
    else:
        rotulo_informacoes.config(text="Por favor, preencha todos os campos.")

botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.grid(row=3, columnspan=2, pady=10)

janela.mainloop()