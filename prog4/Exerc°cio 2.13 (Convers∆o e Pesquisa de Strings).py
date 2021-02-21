#2.13
#Faça um programa que receba duas strings.
#Verifique se a segunda aparece dentro da primeira e em qual
#posição.


val1 = input("Informe a primeira String: ")
val2 = input("Informe a segunda String: ")

val1.lower()
val2.lower()

if val2 in val1:
    print("A segunda frase está contida na primeira. ")

print("-------------------------------------------------------")

p=val1.find(val2)
if p>=0:
    print("Encontrado na Posição: %d" % p)
else:
    print("Não encontrou :(")