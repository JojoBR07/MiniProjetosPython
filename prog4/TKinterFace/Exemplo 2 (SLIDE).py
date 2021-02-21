import tkinter as tk
janela = tk.Tk()
janela.title("Tela Inicial")
# Muda a cor de fundo da Janela
#
janela["bg"] = "green"
janela["background"] = "green"

#Posicionamenrto da tela
#L=Largura A=Altura E=Distancia da borda Esquerda da tela T=Distancia do Topo da Tela
#LXA+E+T
janela.geometry("800x500+100+100")
janela.mainloop()