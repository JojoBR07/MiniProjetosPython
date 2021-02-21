senha = "o"

def password (senha):
    if len(senha) != 8:
        return "Senha não foi aceita! Senha deverá ter 8 digitos"
    elif senha.islower()==False:
        return "Senha não foi aceita! Letras Somente minúsculas"
    elif senha.isalpha():
        return "Senha não foi aceita! Ter letras e numeros"
    elif senha.isdigit():
        return "Senha não foi aceita! Ter letras e numeros"
    elif len(senha) == 8 and (senha.isalnum()==True) and (senha.islower()==True):
        print("Senha Válida")
        return "Senha Válida"
    else:
        return ""

while (senha != "fim"):
    Usuário = input("Digite seu Usuario: ")
    senha = input("Digite a senha: ")
    if senha == "fim":
        break
    retorno = password(senha)

    while (retorno!="Senha Válida"):
        print(retorno)
        senha = input("senha Inválida, digite novamente: ")
        retorno = password(senha)