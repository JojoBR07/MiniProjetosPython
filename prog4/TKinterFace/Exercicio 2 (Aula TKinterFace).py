import sqlite3
from tkinter import *

janela = Tk()
janela.title("Cadastra Alunos")
janela.geometry('600x500+200+200')

cursos = [" ", "Informatica", "Eletromecanica", "Quimica", "Edificações"]

var_consulta = 0;
var_curso = str(janela);
v1 = IntVar(janela)


def CriaTab():
    # Cria tabela
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    cursor.execute("\n"
                   "       create table alunos(\n"
                   "           id integer primary key autoincrement,\n"
                   "           nome text,\n"
                   "           cidade text,\n"
                   "           curso text);\n"
                   "       ")

    conexao.close()
    lbMens = Label(janela, text="Tabela Criada com Sucesso !!")
    lbMens.place(x=300, y=350)


def Consulta():
    conexao = sqlite3.connect("escola.db")
    banco = conexao.cursor()

    var_curso = cursos[var.get()]

    if v1.get() == 1:

        var_curso = cursos[var.get()]
        banco.execute("select nome, cidade, curso  from alunos where curso = '%s' " % var_curso)
    else:

        banco.execute("select *  from alunos order by nome")

    resultado = banco.fetchall()
    for registro in resultado:
        print(registro)
        edMostra.insert(END, registro)
        # lb.insert(END, i)
    banco.close()
    conexao.close()


def CadastraBD():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    var_nome = str(edNome.get())
    var_cidade = str(edCidade.get())
    var_curso = cursos[var.get()]

    flag = 0
    dados = [(var_nome, var_cidade, var_curso)]

    cursor.executemany('''insert into alunos (nome,cidade,curso) values(?, ?,?)''', dados)
    conexao.commit()
    cursor.close()
    conexao.close()


def sel():
    selection = cursos[var.get()]

    lbNomeCurso.config(text=selection)
    lbNomeCurso.place(x=150, y=100)


# .......
def sel2():
    var_consulta = v1.get()


# var_consulta= var.get()


btSalva = Button(janela, width=20, text="Salvar", command=CadastraBD)
btSalva.place(x=80, y=200)

btCria = Button(janela, width=20, text="Criar Tabela", command=CriaTab)
btCria.place(x=80, y=250)

btCons = Button(janela, width=20, text="Consulta Tabela", command=Consulta)
btCons.place(x=80, y=300)

lbMens = Label(janela, text="Mensagem")
lbMens.place(x=300, y=350)

#
lb = Label(janela, text="Nome")
lb.place(x=100, y=50)

edNome = Entry(janela, width=50, fg="blue")
edNome.place(x=150, y=50)

lbCidade = Label(janela, text="Cidade")
lbCidade.place(x=100, y=80)

edCidade = Entry(janela, width=30)
edCidade.place(x=150, y=80)

lbCurso = Label(janela, text="Curso")
lbCurso.place(x=100, y=100)
lbNomeCurso = Label(janela, text="Informatica")
lbNomeCurso.place(x=150, y=100)
opcao = int;
num = int;

edMostra = Listbox()

edMostra.config(width=50, height=30)
# height
edMostra.place(x=250, y=150)

var = IntVar()
R1 = Radiobutton(janela, text="Informatica", variable=var, value=1,command=sel).place(x=90, y=120)

R2 = Radiobutton(janela, text="Eletromecanica", variable=var, value=2,command=sel).place(x=190, y=120)

R3 = Radiobutton(janela, text="Quimica", variable=var, value=3,command=sel).place(x=300, y=120)

R4 = Radiobutton(janela, text="Edificações", variable=var, value=4, command=sel).place(x=400, y=120)

c1 = Checkbutton(text="Consulta Individual", var=v1, command=sel2).place(x=50, y=350)

janela.mainloop()