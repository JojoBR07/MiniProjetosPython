arquivo=open("numpar.txt","w")
arquivo2=open("numimpar.txt","w")

for linha in range(1,501):
    if linha % 2 == 0:
        arquivo.write("%d\n" % linha)
    else:
        arquivo2.write("%d\n" % linha)

arquivo.close()