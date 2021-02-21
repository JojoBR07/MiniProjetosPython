#17:
#Faça um programa que cliptografe uma frase. Para isso receba uma
#frase e substitua todas a letra “a” por “@” e a letra “e” por “%”
#Escreva a frase original e a cliptografada..

frase = input("Digite uma frase: ")
print(frase)

frase_criptografada = frase.replace('a','@')
print(frase_criptografada)

frase_criptografada = frase_criptografada.replace('e','%')
print(frase_criptografada)
