def operacao (x,y):
    operation = int(input("Informe uma operação: 1=Soma, 2=Subtração, 3=Multiplicação, 4=Divisão: "))
    while (operation > 4 or operation < 1):
        operation = int(input("Informe Novamente: 1=Soma, 2=Subtração, 3=Multiplicação, 4=Divisão: "))
    if operation == 1:
        result = x+y
    elif operation == 2:
        result = x-y
    elif operation == 3:
        result = x*y
    else:
        result = x/y
    return result

val1 = 1
while val1 != 0:
    val1 = int(input("Informe um numero inteiro: "))
    if val1 != 0:
        val2 = int(input("Informe outro numero inteiro: "))

        resultado = operacao(val1,val2)
        print("Resultado = ",resultado)
