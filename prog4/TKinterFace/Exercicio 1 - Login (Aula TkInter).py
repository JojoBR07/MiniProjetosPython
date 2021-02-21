import sqlite3
from tkinter import *


def bt_click():

        senha = (ed2.get())
        user = (ed1.get())

        cursor.execute('''
        SELECT * FROM acesso WHERE usuario = ? and senha = ?
        ''', (user,senha))
        conexao.commit()

        if (cursor.fetchall()):
            lb3["text"]= "Acesso Permitido"
        else:
            lb3["text"] = "Acesso Negado"


# Criar tela de login
janela = Tk()
janela.title("Tela Login")
janela["background"] = "red"
janela.geometry("800x500+100+100")

# Iniciar conexão com o Banco de Dados
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()



lb = Label(janela,bg="red", text="Login de Usuário",font=("Verdana", 14))
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

bt = Button (janela, width=20, text= "Login", command=bt_click)
bt.place(x=280, y=220)



janela.mainloop()

conexao.commit()
cursor.close()
conexao.close()
