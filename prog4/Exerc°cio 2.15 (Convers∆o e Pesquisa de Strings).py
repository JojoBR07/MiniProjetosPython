#2.15
#Faça um programa que escreva a seguinte frase
#“Feirão de automóveis: Toda linha FIAT com desconto de 25 % nos
#modelos Siena, Idea e Uno 2,10! Promoção valida até Sexta feira”
#A Marca, o desconto , os modelos preço e o dia limite da promoção
#devem ser informado.
#Imprima a frase formatando a string


men=("Feirão de automoveis: Toda linha {0} com desconto de {1}% nos modelos {2}, {3} e {4}!"
     "Promoção válida até {5}" .format("Fiat", 15, "uno", "Siena", "Punto", "Sexta-Feira"))

print(men)