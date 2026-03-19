#Faça um algoritmo que leia a altura e o sexo de uma pessoa e mostre se ela está abaixo, 
# dentro ou acima do peso ideal, utilizando as fórmulas do exercício 3 da lista de algoritmos sequenciais.

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

IMC = weight / pow(height, 2)

print(f"Your IMC is {IMC}") 

if (IMC > 40):
    print("Obeso grau 3")
elif (35 < IMC < 39.9): 
    print("Obeso grau 2")
elif (30 < IMC < 34.9):
    print("Obeso grau 1")
elif (25 < IMC < 29.9):
    print("Sobrepeso")
elif (18.5 < IMC < 24.9):
    print("Peso normal")
else:
    print("Magro")