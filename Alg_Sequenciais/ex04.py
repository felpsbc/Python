#Faça um algoritmo que leia três números reais e mostre a média ponderada entre eles, 
# com pesos 2, 3 e 5, respectivamente.
Peso2 = 2 
Peso3 = 3
Peso5 = 5 

A = Peso2 *int(input("Enter a number: "))
B = Peso3 *int(input("Enter a number: "))
C = Peso5 *int(input("Enter a number: "))

somaPesos = Peso2 + Peso3 + Peso5

MedPon = A + B + C/ somaPesos

print(f"A Media ponderada e {MedPon}")