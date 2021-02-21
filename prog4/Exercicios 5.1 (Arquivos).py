arquivo=open("numeros.txt","w")
for linha in range(1,501):
    arquivo.write("%d\n" % linha)

arquivo=open('numeros.txt','r')
for linha in arquivo.readlines():
    print(linha)

arquivo.close()