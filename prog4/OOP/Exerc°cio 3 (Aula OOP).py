class person:
    def __init__(self,v1,v2,v3,v4):

        self.nome = v1
        self.rg = v2
        self.idade = int(v3)
        self.endereco = v4

    def listar(self):
        print ("")
        print("Nome: ",self.nome,
              "| RG: ",self.rg,
              "| Idade: ",self.idade,
              "| Endereço: ",self.endereco)
        print ("")

    def alterar(self):
        self.nome = (input('Digite seu nome: '))
        self.rg = (input('Digite seu RG: '))
        idade = int(input('Digite sua Idade: '))

        if idade >= self.idade:
            self.idade = idade
        else:
            print ("Idade Inválida")

        self.endereco = (input('Digite seu Endereço: '))

nome = (input('Digite seu nome: '))
rg = (input('Digite seu RG: '))
idade = int(input('Digite sua Idade: '))
endereco = (input('Digite seu Endereço: '))

s1 = person(nome,rg,idade,endereco)
print ("Os seguintes dados serão salvos:")
s1.listar()

print("------------------------------------------------------------------------------")

nome = (input('Digite seu nome: '))
rg = (input('Digite seu RG: '))
idade = int(input('Digite sua Idade: '))
endereco = (input('Digite seu Endereço: '))

s2 = person(nome,rg,idade,endereco)
print ("Os seguintes dados serão salvos:")
s2.listar()

print("------------------------------------------------------------------------------")

i = input("Deseja alterar os dados (Responda 1 para a pessoa 1 | Responda 2 para a pessoa 2 | Qualquer tecla para NÃO): ")
if i == "1":
    s1.alterar()
elif i == "2":
    s2.alterar()
else:
    print("Certo, seus dados serão salvos!")