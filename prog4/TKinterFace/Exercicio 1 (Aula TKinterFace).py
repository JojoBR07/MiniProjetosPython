import sqlite3
from tkinter import *


def bt_click():

    senha = (ed2.get())
    user = (ed1.get())

    dados = [(user, senha)]

    if len(senha) != 8:
        lb3["text"] = "Senha não foi aceita! Senha deverá ter 8 digitos"
        return ""
    elif senha.islower()==False:
        lb3["text"] = "Senha não foi aceita! Letras Somente minúsculas"
        return ""
    elif senha.isalpha():
        lb3["text"] = "Senha não foi aceita! Ter letras e numeros"
        return ""
    elif senha.isdigit():
        lb3["text"] = "Senha não foi aceita! Ter letras e numeros"
        return ""
    elif len(senha) == 8 and (senha.isalnum()==True) and (senha.islower()==True):

        lb3["text"] = dados
        cursor.execute('''
        INSERT INTO acesso (usuario,senha)
        VALUES (?,?) ''', (user,senha))
        conexao.commit()

        lb3["text"]= "Cadastro criado com sucesso"
        return ""
    else:
        lb3["text"] = "Dados Inválido"
        return ""

# Criar tela de login
janela = Tk()
janela.title("Tela Login")
janela["background"] = "red"
janela.geometry("800x500+100+100")

# Iniciar conexão com o Banco de Dados
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

# Criar tabela acesso com usuario e senha
cursor.execute('''
CREATE TABLE IF NOT EXISTS acesso (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL
    );
''')

lb = Label(janela,bg="red", text="Cadastro de Usuário",font=("Verdana", 14))
lb.place(x=280, y=30)

ed1 = Entry(janela, width=20, fg="blue")
ed1.place(x=280, y=100)

ed2 = Entry(janela, width=20, fg="blue")
ed2.place(x=280, y=160)


lb1 = Label(janela, text="Usuário:",bg="red")
lb1.place(x=280, y=70)

lb2 = Label(janela, text="Senha:",bg="red")
lb2.place(x=280, y=130)

lb3 = Label(janela, text="",bg="red")
lb3.place(x=320, y=250)

bt = Button (janela, width=20, text= "Cadastrar", command=bt_click)
bt.place(x=280, y=220)


janela.mainloop()

conexao.commit()
cursor.close()
conexao.close()


