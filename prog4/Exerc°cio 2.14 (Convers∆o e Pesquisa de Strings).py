#2.14
#Faça um programa que receba duas strings e crie uma terceira com
#Os caracteres comuns as duas.

primeira = input("Informe a primeira String: ")
segunda = input("Informe a segunda String: ")
terceira = ""

for letra in primeira:
    #Se a letra está na segunda String (comum a ambas)
    #Para evitar repetidas, nâo deve estar na terceira
    if letra in segunda and letra not in terceira:
        terceira+=letra

if terceira == "":
    print("Caracteres comuns não encontrados.")
else:
    print("Caracteres em comum: %s" %terceira)
