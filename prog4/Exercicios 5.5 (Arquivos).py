arquivo=open("lista.txt","w")

for i in range(1,11):
    nome=input("Informe o seu nome: ")
    cidade=input("Informe sua cidade: ")
    curso=input("Informe o seu curso: ")

    arquivo = open("lista.txt",'a')
    arquivo.write("%s\n" % "{}; {}; {}".format(nome,cidade,curso))

arquivo.close()