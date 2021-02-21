arquivo=open("numimpar.txt","r")
arquivo2=open("multipl3.txt","w")

for linha in arquivo.readlines():
    if int(linha) % 3 == 0:
        i = int(linha)
        print(linha)
        arquivo2.write("%d\n" % i)


arquivo.close()