#3.8 –Faça um programa que receba um numero e mostre a tabuada ou fatorial,
#conforme opção. Se o numero
#for maior que 10, somente será possível calcular o fatorial.

numero = int(input("Informe um numero: "))

if numero<10:
    funcao = int(input("Escolha uma função: 1 = tabuada ou 2 = fatorial: "))
else:
    funcao=2

if funcao == 1:
    for i in range(1,(11)):
        print(numero," X ", i, " = ", numero*i)

elif funcao == 2:

    n = numero
    for i in range(1, (numero)):
        n = n * (numero - i)
    print(n)
else:
    print("Opção inválida")
