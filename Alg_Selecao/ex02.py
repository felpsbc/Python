# Faça um algoritmo que leia três números inteiros e mostre o menor deles.

num1 = int(input("Digite um numero: "))

num2 = int(input("Digite um numero: "))

num3 = int(input("Digite um numero: "))

if (num1 == num2 == num3 ):
    print("Os numeros sao iguais")
elif (num2 < num1 > num3):
    print(num1)
elif (num1 < num2 > num3):
    print(num2)
elif (num1 < num3 > num2):
    print(num3)
else: 
    print("ERRO")