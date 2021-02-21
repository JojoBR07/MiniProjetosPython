import sqlite3
from tkinter import *


janela = Tk()
janela.title("Biblioteca")
janela["background"] = "#ff9a75"
janela.geometry("800x500+100+100")

categoria = [" ", "Literário", "Técnico", "Periódico", "Didáticos"]
v1 = IntVar(janela)

def sel():
    selection = categoria[var.get()]
    lbNomeCurso.config(text=selection)
    lbNomeCurso.place(x=150, y=170)

def CriaTab():
    # Cria tabela
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute("\n"
                   "       create table livros(\n"
                   "           id integer primary key autoincrement,\n"
                   "           titulo text,\n"
                   "           autor text,\n"
                   "           ano text,\n"
                   "           editora text,\n"
                   "           categoria text);\n"
                   "       ")
    conexao.commit()
    cursor.close()
    conexao.close()

    lbMens = Label(janela, text="Tabela Criada com Sucesso !!",bg="#ff9a75")
    lbMens.place(x=80, y=450)

def Consulta():
    conexao = sqlite3.connect("biblioteca.db")
    banco = conexao.cursor()

    var_categoria = categoria[var.get()]

    if v1.get() == 1:

        var_categoria = categoria[var.get()]
        banco.execute("select titulo, autor,ano,editora,categoria  from livros where categoria = '%s' " % var_categoria)
    else:
        banco.execute("select titulo, autor,ano,editora,categoria  from livros order by titulo")

    resultado = banco.fetchall()
    for registro in resultado:
        print(registro)
        edMostra.insert(END, registro)
        # lb.insert(END, i)
        edMostra.insert(END,"-----------------------")
    banco.close()
    conexao.close()

def CadastraBD():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    titulo = str(ed_titulo.get())
    autor = str(ed_autor.get())
    ano = str(ed_ano.get())
    editora = str(ed_editora.get())
    var_categoria = categoria[var.get()]

    dados = [(titulo, autor, ano, editora, var_categoria)]

    cursor.executemany('''insert into livros (titulo,autor,ano,editora,categoria) values(?,?,?,?,?)''', dados)
    conexao.commit()
    cursor.close()
    conexao.close()

    lbMens = Label(janela, text="Livro cadastrado com Sucesso",bg="#ff9a75")
    lbMens.place(x=80, y=450)

def sel2():
    var_consulta = v1.get()



lb = Label(janela,bg="#ff9a75", text="Biblioteca",font=("Verdana", 14))
lb.place(x=200, y=0)

lb_titulo = Label(janela, text="Título:", bg="#ff9a75")
lb_titulo.place(x=100, y=50)
ed_titulo = Entry(janela, width=50)
ed_titulo.place(x=150, y=50)

lb_autor = Label(janela, text="Autor:", bg="#ff9a75")
lb_autor.place(x=100, y=80)
ed_autor = Entry(janela, width=30)
ed_autor.place(x=150, y=80)

lb_ano = Label(janela, text="Ano de Edição:", bg="#ff9a75")
lb_ano.place(x=60, y=110)
ed_ano = Entry(janela, width=20)
ed_ano.place(x=150, y=110)

lb_editora = Label(janela, text="Editora:", bg="#ff9a75")
lb_editora.place(x=100, y=140)
ed_editora = Entry(janela, width=50)
ed_editora.place(x=150, y=140)

lbCurso = Label(janela, text="Categoria:", bg="#ff9a75")
lbCurso.place(x=85, y=170)
lbNomeCurso = Label(janela, text="Literário", bg="#ff9a75")
lbNomeCurso.place(x=150, y=170)

var = IntVar()
R1 = Radiobutton(janela, text="Literário", variable=var, value=1,command=sel, bg="#ff9a75").place(x=100, y=200)
R2 = Radiobutton(janela, text="Técnico", variable=var, value=2,command=sel, bg="#ff9a75").place(x=190, y=200)
R3 = Radiobutton(janela, text="Periódico", variable=var, value=3,command=sel, bg="#ff9a75").place(x=300, y=200)
R4 = Radiobutton(janela, text="Didáticos", variable=var, value=4, command=sel, bg="#ff9a75").place(x=400, y=200)

c1 = Checkbutton(text="Consulta por categoria", var=v1, command=sel2, bg="#ff9a75").place(x=80, y=400)

edMostra = Listbox()
edMostra.config(width=40, height=30)
edMostra.place(x=250, y=250)

btSalva = Button(janela, width=20, text="Salvar", command=CadastraBD)
btSalva.place(x=80, y=250)

btCria = Button(janela, width=20, text="Criar Tabela", command=CriaTab)
btCria.place(x=80, y=300)

btCons = Button(janela, width=20, text="Consulta Tabela", command=Consulta)
btCons.place(x=80, y=350)

janela.mainloop()