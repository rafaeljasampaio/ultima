import requests
from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Meu primeiro programa")

texto = Label(janela, text="Digite o 1º valor")
texto.grid(column=0, row=0, padx=10, pady=10)
texto2 = Label(janela, text="Digite o 2º valor")
texto2.grid(column=3, row=0, padx=10, pady=10)


#botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
#botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()
