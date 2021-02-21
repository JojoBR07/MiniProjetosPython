frase = "O pinto pia, a pipa pinga. Pinga a pipa e o pinto pia. Quanto mais o pinto pia mais a pipa pinga"
print(frase)
print("")

x = frase.count("pinto")
print("O pinto apareçe", x, "vezes na mensagem")

print("")
p=0
while(p>-1):
    p=frase.find("pinto",p)
    if p>=0:
        print("Posição: %d" % p)
        p+=1
print("")
print("Frase com galo: ",frase.replace('pinto','galo'))

p=[]
for i in frase.split(' '):
    i = i.capitalize()
    p.append(i)

print("Frase Maiuscula: ",' '.join(p))