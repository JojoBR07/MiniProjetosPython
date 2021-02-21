arquivo=open("numpar.txt","r")

for linha in arquivo.readlines():
    if int(linha) % 4 == 0:
        print(linha)

arquivo.close()