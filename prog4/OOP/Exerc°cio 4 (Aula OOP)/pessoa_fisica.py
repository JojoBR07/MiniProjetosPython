from pessoa import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, CPF):
        super().__init__(nome, idade)
        self.CPF = CPF

    def getCPF(self):
        return self.CPF

    def setCPF(self, CPF):
        self.CPF = CPF