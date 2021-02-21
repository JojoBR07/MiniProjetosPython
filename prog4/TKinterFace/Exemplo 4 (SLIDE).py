from tkinter import *

def bt_click():
    num1 = int(ed1.get())
    num2 = int (ed2.get())
    lb2["text"]= num1+num2

janela = Tk()
janela.title("Exemplo Recebe Dados")
janela.geometry('500x400+200+200')

ed1 = Entry(janela, width=20, fg="blue")
ed1.place(x=100, y=100)

ed2 = Entry(janela, width=20, fg="blue")
ed2.place(x=100, y=130)

bt = Button (janela, width=20, text= "Confirma", command=bt_click)
bt.place(x=80 , y=200)

lb2= Label(janela,width=30, fg="red", font=("Verdana", 14))
lb2.place(x=100, y=250)

def bt_click():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int (ed2.get())
        lb2["text"]= num1+num2
    else:
        lb2["text"] = "Valor informado não é numerico"

janela.mainloop()