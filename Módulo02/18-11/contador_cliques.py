""" 
Desenvolva uma aplicação que possua um botão e um rótulo. A cada clique no botão, incremente um contador e atualize o rótulo apresentando a quantidade de cliques realizados.

```text
+----------------------------+
| Contador de cliques        |
+----------------------------+
|         Cliques: 0         |
|       [ Clique aqui ]      |
+----------------------------+
``` 
"""
import tkinter as tk

janela = tk.Tk()
janela.title("Contador de cliques")
janela.geometry("300x200")
janela.resizable(False, False)

contador = 0
rotulo = tk.Label(janela, text=f"Cliques: {contador}")
rotulo.pack(pady=20)

def incrementar_contador():
    global contador
    contador += 1
    rotulo.config(text=f"Cliques: {contador}")

botao = tk.Button(janela, text="Clique aqui", command=incrementar_contador)
botao.pack(pady=10)

janela.mainloop()