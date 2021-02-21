produtos={"Cachorro-Quente":15.50, "Refrigerante":8.00,"X Salada":18.00,"Torrada":9.50,"Batata frita":12.00}

print("Produtos:")
for i in produtos:
    print(i)

print("")
print("Preços:")
for i in produtos.values():
    print(i)

print("----------------------------------")

if "Torrada" in produtos:
    print("Produto torrada está na Lista")
else:
    print("Produto torrada não está na Lista")

print("----------------------------------")
print("Preço do X Salada:", produtos["X Salada"])

print("----------------------------------")
print("Chaves:",produtos.keys())

print("----------------------------------")
del produtos["Refrigerante"]
print("Item refrigerante removido: ", produtos)