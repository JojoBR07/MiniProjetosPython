from tkinter import *
janela = Tk()
janela.title("Tela Inicial")

#Posicionamenrto da tela
#L=Largura A=Altura E=Distancia da Esqueda da tela T=Distancia do Topo da Tela
#LXA+E+T
janela.geometry('300x300+200+200')

#Usando Gerenciador PLACE
lb = Label(janela, text="Curso de Informática IFSUL !!")
lb.place(x=100, y=100)
Bt = Button (janela, width=20, text="Confirma")
Bt.place(x=100, y=200)

janela.mainloop()