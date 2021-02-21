produtos = {"Caderno":8.50,"Mochila":36.50,"Caneta":3.00,"Folha A4":9.50,"Lapiseira":12.00}
print(produtos)
produtos["Regua"]=8.80
print(produtos)
if "Regua" in produtos:
    print("True")
else:
    print("False")
print(produtos["Caneta"])
print(produtos.keys())
del(produtos["Caneta"])
print(produtos)