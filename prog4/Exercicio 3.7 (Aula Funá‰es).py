#3.7 – Escreva um programa que cria uma função para Receber e testar uma senha.
#Essa senha deverá ter letras e números com 6 digitos.
#O usuário terá no máximo 5 tentativas

def password (senha):

    if senha.isalpha():
        return ""

    elif senha.isdigit():
        return ""

    elif len(senha) == 6 and (senha.isalnum()==True):
        print("Senha Válida")
        return 0

    else:
        return ""


senha = input("Digite a senha: ")
retorno = password(senha)


while (retorno==""):
    senha = input("senha Inválida, digite novamente: ")
    retorno = password(senha)