import tkinter as tk

janela = tk.Tk()


janela.title("Sistema de Formulário")
janela.geometry("400x250")
#janela.resizable(False, False)
tk.Label(janela,
        text="Nome: ").pack(pady=5)
entrada_nome = tk.Entry(janela,
        width=40)
entrada_nome.pack()
#################################################################

tk.Label(janela,
        text="Endereço: " ).pack(pady=5)
entrada_endereco = tk.Entry(janela,
        width=40)
entrada_endereco.pack()
################################################################

tk.Label(janela,
         text="Telefone: ").pack(pady=5)
entrada_telefone = tk.Entry(janela,
        width=40)
entrada_telefone.pack()
####################################################################
def salvar():
    nome = entrada_nome.get()
    endereco = entrada_endereco.get()
    telefone = entrada_telefone.get()

    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Endereço: {endereco}\n")
        arquivo.write(f"Telefone: {telefone}\n")
        arquivo.write("\n")

    entrada_nome.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    resultado.config(text="Dados salvos com sucesso!")
botao = tk.Button(janela,
        text="Salvar",
        command=salvar)              

botao.pack(pady=20)
resultado = tk.Label(janela, text="")
resultado.pack(pady=5)
#####################################################################################
""" rotulo1 = tk.Label(janela, text="Digite seu e-mail: ")
rotulo1.pack(pady=10)
entrada1 = tk.Entry(janela, width=30)
entrada1.pack(pady=5)

######################################################################################
rotulo2 = tk.Label(janela, text="Digite sua idade: ")
rotulo2.pack(pady=10)
entrada2 = tk.Entry(janela, width=30)
entrada2.pack(pady=5)

#######################################################################################
resultado = tk.Label(janela, text="")


def cumprimentar():
    nome = entrada.get()
    email = entrada1.get()
    idade = entrada2.get()
    resultado.config(text=f"Olá, {nome}! E-mail: {email} - Idade: {idade}")
    resultado.pack(pady=5)


botao = tk.Button(
    janela,
    text="Confirmar",
    command=cumprimentar
)

botao.pack(pady=10) 
"""

janela.mainloop()