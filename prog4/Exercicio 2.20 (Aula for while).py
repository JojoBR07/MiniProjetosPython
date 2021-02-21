produtos={"Salgado":4.50, "Lanche":6.50, "Suco":3.00, "Refrigerante":3.50, "Doce":1.00}
'''
print("Produto: Salgado", "Preço: $", produtos["Salgado"])
print("Produto: Lanche", "Preço: $", produtos["Lanche"])
print("Produto: Suco", "Preço: $", produtos["Suco"])
print("Produto: Refrigerante", "Preço: $", produtos["Refrigerante"])
print("Produto: Doce", "Preço: $", produtos["Doce"])
'''
for i in produtos:
    print("Produto:", i, "|  Preço R$:", produtos[i])