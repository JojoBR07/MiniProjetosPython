arquivo=open('lista.txt','r')
for linha in arquivo.readlines():
    n = linha[:linha.rfind(";")]
    nome= n[:n.rfind(";")]
    print(nome)
arquivo.close()