#3.5 –Faça um programa que leia 2 notas de um aluno,
#calcule a média e imprima aprovado ou reprovado
#(para ser aprovado a média deve ser no mínimo 6)

def media (x,y):
    x=(x+y)/2
    return x

x = int(input("Informe a primeira nota do Aluno: "))
y = int(input("Informe a segunda nota do Aluno: "))

media = media(x,y)

if media >= 6:
    print("Aprovado, PARABÉNS")
else:
    print("Infelizmente você está reprovado")