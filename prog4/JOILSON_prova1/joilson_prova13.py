nome = input("Informe o nome do produto: ")
codigo = int(input("Informe o código do produto: "))
valor = float(input("Informe o valor do produto: "))
desconto = int(input("Informe a porcentagem de desconto do produto: "))

desconto2 = valor*(desconto/100)
total = valor - desconto2

print("Nome do produto:",nome, "| Codigo","%04d" %codigo, "| Valor do Produto:$","%3.2f" %valor, "| Desconto:",desconto,"%","| Valor total: ","%3.2f"%total )
