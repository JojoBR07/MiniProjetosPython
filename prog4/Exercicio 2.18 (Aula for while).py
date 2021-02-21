numero=int(input("Digite seu número:"))

while numero > 10:
    numero =input("Seu numero é maior que 11, digite novamente: ")

for i in range(1,11):
    resultado = int(i*numero)
    print(numero," x ", i, " = ", resultado)