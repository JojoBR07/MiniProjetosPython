#3.2- Crie uma função que receba como parâmetro uma lista , com
#valores de qualquer tipo .
#A função deve imprimir todos os elementos da lista numerando-os .

L = [5, 7, 2, 9, 4, 1, 3]

def numerar (lista):
    lista.sort()
    return lista


print(L)
print("-----------------------------------------------")

numerar(L)

print(L)