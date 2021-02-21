arquivo = open("lista.txt","r")
p=0

for linha in arquivo.readlines():
    p = linha.find("G", p)
    if p == 0:
        i = (linha)
        print(i)

arquivo.close()