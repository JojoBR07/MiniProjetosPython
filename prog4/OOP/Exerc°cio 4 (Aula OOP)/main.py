from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

print("Cadastro de Pessoa Física")

Nome = input("Informe seu nome: ")
Idade = input("Informe sua idade: ")
cpf = input("Informe o CPF: ")

p1 = PessoaFisica(Nome, Idade, cpf)
print("Dados: ", "Nome:", p1.getNome(), "| Idade:", p1.getIdade(), "| CPF:", p1.getCPF())


print("Cadastro de Pessoa Juridica")

Nome = input("Informe seu nome: ")
Idade = input("Informe sua idade: ")
CNPJ = input("Informe o CNPJ: ")

p2 = PessoaJuridica(Nome, Idade, CNPJ)
print("Dados: ", "Nome: ", p2.getNome(), "Idade: ", p2.getIdade(), "CNPJ: ", p2.getCNPJ())


Idade = input("Informe uma nova idade para a Pessoa Física: ")
p1.setIdade(Idade)
print("Nova Idade: ", p1.getIdade())

CNPJ = input("Informe um novo CNPJ para a Pessoa Jurídica: ")
p2.setCNPJ(CNPJ)
print("Novo CNPJ: ", p2.getCNPJ())


