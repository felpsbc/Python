#Faça um algoritmo que leia o peso e a altura de uma pessoa e calcule o seu IMC 
#(Índice de Massa Corporal).

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