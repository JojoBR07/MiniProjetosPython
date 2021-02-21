numero = int(input("Informe um numero positivo e menor que 11: "))

while numero > 11 or numero <0:
    numero = int(input("Numero invalido, informe outro positivo e menor que 11: "))

funcao = int(input("Escolha uma função: 1 = tabuada ou 2 = fatorial: "))

if funcao == 1:
    for i in range(1,(11)):
        print(numero," X ", i, " = ", numero*i)

elif funcao == 2:

    n = numero
    for i in range(1, (numero)):
        n = n * (numero - i)
    print(n)
