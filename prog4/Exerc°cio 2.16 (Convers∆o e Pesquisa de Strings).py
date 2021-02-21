#2.16
#Faça um programa que receba uma senha.
#Essa senha deve conter apenas números ou apenas letras
#maiúsculas.
#Valide a senha recebida


password = input("Insira sua senha: ")

if password.isupper() and password.isalpha():
    print("Senha válida")
elif password.isdigit():
    print("Senha válida")
else:
    print("Senha inválida")

