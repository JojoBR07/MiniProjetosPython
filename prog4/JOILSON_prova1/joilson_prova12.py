L=[5,6,3,7,2,7,9,35,10,15,17,7]
print(L)
print("---------------------------------------------------------")

if 28 in L:
    print("Sim, existe o numero 28 na Lista")
else:
    print("Não, existe o numero 28 na Lista")

print("---------------------------------------------------------")

print("Soma da Lista: ", sum(L))
print("---------------------------------------------------------")

print("Menor valor da lista: ", min(L))
print("---------------------------------------------------------")

del L[9]
print("Numero 15 removido da lista: ",L)
print("---------------------------------------------------------")

print("Tamanho total da lista:",len(L))
print("---------------------------------------------------------")

L.sort()
print("Ordem crescente da Lista:", L)
print("---------------------------------------------------------")