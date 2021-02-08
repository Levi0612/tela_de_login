#!/venv/bin/python3
# --*-- coding: utf-8 --*--

import sqlite3
from tkinter import *

conexao = sqlite3.connect('banco.db')
conexao.cursor()


# Botao  Para Enviar os Dados
def clicar_entrar():
    login = entrar.get()
    senha = entrar2.get()

    try:
        c = conexao.cursor()
        c.execute("""CREATE TABLE usuarios (
                        email TEXT NOT NULL,
                        senha TEXT NOT NULL
                        );""")
        c.close()
    except:
        print('O Banco De Dados Já Existe')

    conexao.execute("INSERT INTO usuarios \
        (email,senha) VALUES ('" + login + "','" + senha + "')")

    conexao.commit()
    janela.destroy()
    conexao.close()


# Criar uma Janela
janela = Tk()

# Tamanho da janela
janela.geometry('250x150')

# janela.resizable(width=False, height=False)

# Titulo da janela
janela.title('login')

# Label Para Mostrar Onde Inserir o email
lb = Label(
    janela,
    width=0,
    text='Email',
)
lb.place(x=10, y=30)

# Entry Para Coletar login
entrar = Entry(janela, width=20)
entrar.place(x=70, y=50 - 20 + 0)

# Label Para Mostrar Onde Inserir o login
lb2 = Label(janela, width=0, text='Senha')
lb2.place(x=10, y=60)

# Entry Para Coletar senha
entrar2 = Entry(janela, width=20, show='*')
entrar2.place(x=70, y=50 + 10 + 0)

# Botão Para Envio Dos Dados
botao = Button(janela,
               width=10,
               text='Enviar',
               font='Arial',
               command=clicar_entrar)
botao.place(x=80, y=100)

# Manter a janela aberta
janela.mainloop()
