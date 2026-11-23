""" Desenvolva uma interface gráfica para cadastrar personagens de um RPG. Cada personagem deverá possuir nome, classe, nível e quantidade de pontos de vida.

Ao clicar no botão "Cadastrar personagem", o programa deverá validar as informações, adicionar o personagem a uma lista e apresentar os personagens cadastrados na interface.

> [!TIP]
> Utilize os conhecimentos de Programação Orientada a Objetos para criar uma classe `Personagem` e instanciar um novo objeto a cada cadastro.
 
"""
from tkinter import *
from tkinter import messagebox

def cadastrar_personagem():
    nome = nome_entry.get()
    classe = classe_entry.get()
    nivel = nivel_entry.get()
    vida = vida_entry.get()

    if not nome or not classe or not nivel or not vida:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    messagebox.showinfo("Sucesso", f"Personagem '{nome}' ({classe}, nível {nivel}, {vida} PV) cadastrado!")

root = Tk()
root.title("Cadastro de Personagem RPG")

# Campos de entrada
Label(root, text="Nome:").grid(row=0, column=0, sticky=E)
nome_entry = Entry(root)
nome_entry.grid(row=0, column=1)

Label(root, text="Classe:").grid(row=1, column=0, sticky=E)
classe_entry = Entry(root)
classe_entry.grid(row=1, column=1)

Label(root, text="Nível:").grid(row=2, column=0, sticky=E)
nivel_entry = Entry(root)
nivel_entry.grid(row=2, column=1)

Label(root, text="Pontos de vida:").grid(row=3, column=0, sticky=E)
vida_entry = Entry(root)
vida_entry.grid(row=3, column=1)

# Botão de cadastro
btn_cadastrar = Button(root, text="Cadastrar personagem", command=cadastrar_personagem)
btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

