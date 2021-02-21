from tkinter import *
janela=Tk()
cor = StringVar(janela)
cor.set("black")
l = Label(background=cor.get())
l.pack(fill='both',expand=True)
def pinta():
    l.configure(background=cor.get())
janela.title("Radiobutton Exemplo")
janela.geometry("300x300+600+200")
for txt,val in (("preto","black"), ("vermelho","red"), ("azul","blue"), ("verde","green")):
    Radiobutton(text=txt,value=val,variable=cor, command=pinta).pack(anchor=W)
mainloop()