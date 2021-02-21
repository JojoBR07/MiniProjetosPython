#4.1
#Faça um programa que receba a distancia percorrida por um
#passageiro e calcule o valor da passagem, sendo que até 200 km é R$
#0,50 o quilometro , de 201 km até 400 km é R$ 0,45 e acima de 400
#km é de R$ 0,40 calcule e mostre o valor da passagem conforme
#tabela acima.

distancia = float(input("Informe a distância percorrida: "))

if distancia <= 200:
    valor=distancia*0.50
    print("R$ %3.2f" % valor)

elif distancia >= 200:
    if distancia <= 400:
        valor = distancia * 0.45
        print("R$ %3.2f" % valor)

elif distancia>400:
    valor = distancia * 0.40
    print("R$ %3.2f" %valor)

else:
    print("Sua distância é inválida, você informou um valor negativo.")