#3.3- Crie uma função que receba como parâmetro uma lista
#com valores numéricos e retorne a média desses valores

L = [5, 5, 5, 5, 5, 5, 5]

def numerar (lista):
    media = (sum(lista)) / (len(lista))
    return media


print(L)
print("-----------------------------------------------")

media = numerar(L)

print(media)