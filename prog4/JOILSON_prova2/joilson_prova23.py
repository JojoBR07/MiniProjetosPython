arquivo=open("lista.txt","w")
arquivo2=open("lista.txt","r")

def gravar (x,y,z):
    arquivo = open("lista.txt", "a")
    arquivo.write("%s\n" % "{}; {}; {}".format(x, y, z))
    return ""

def mostra():
    arquivo = open('lista.txt', 'r')
    for linha in arquivo.readlines():
        n = linha[:linha.find(";")]
        nome = n[:n.find(";")]
        n = linha[:linha.rfind(";",2)]
        curso = n[:n.rfind(";",2)]
        print("Nome: ",nome, "Curso: ",curso)

for i in range(1,11):

    nome=input("Informe o seu nome: ")
    cidade=input("Informe sua cidade: ")
    curso=input("Informe o seu curso(Informática, Biologia, Química): ")

    if curso == "Informática" or curso == "Biologia" or curso == "Química":
        retorno = gravar(nome,cidade,curso)
    else:
        print("Curso inválido, operação não concluida.  :(")

print("Mostrar os Dados:")
mostra()
arquivo.close()
