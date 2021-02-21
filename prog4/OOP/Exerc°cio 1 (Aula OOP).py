#faça uma classe soma. Está classe terá 2 atributos v1 e v2
#o programa deverá declarar 2 objetos da classe some.
#O programa devrá mostrar na tela a soma dos 2 valores
#a classe deverá ter um método chamado "somar"

class Somar:
    def __init__(self,v1,v2):
        self.vlr1 = v1
        self.vlr2 = v2
    def soma(self):
        print(self.vlr1 + self.vlr2)

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

s1 = Somar(valor1,valor2)
s1.soma()
