#3.6 –Refaça o exercício 3.5, identificando o conceito aprovado
#(média superior a 6), exame(média entre 4 e 6)
#ou reprovado(média inferior a 4).

def media (x,y):
    x=(x+y)/2
    return x

x = int(input("Informe a primeira nota do Aluno: "))
y = int(input("Informe a segunda nota do Aluno: "))

media = media(x,y)

if media >= 6:
    print("Aprovado, PARABÉNS :)")
elif media >= 4 and media < 6:
    print("Você terá que fazer o exame :/")
else:
    print("Infelizmente você está reprovado :(")