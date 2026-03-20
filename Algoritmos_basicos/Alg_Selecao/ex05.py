#Faça um algoritmo que leia um número inteiro 
# e mostre se ele é múltiplo de 3 e de 5 ao mesmo tempo.

X = int(input("Digite um numero: "))

if (X % 3 == 0 and X % 5 == 0):
    print("X e divisivel por 3 e por 5 ao mesmo tempo")
else: 
    print("ERRO")