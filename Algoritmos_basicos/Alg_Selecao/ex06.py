#Faça um algoritmo que leia dois números inteiros e mostre o resultado da multiplicação entre eles,
#  se ambos forem positivos; ou a soma, se pelo menos um deles for negativo.

num1 = int(input("Digite um numero: "))

num2 = int(input("Digite um numero: "))

if (num1 and num2 >= 0):
    print(f"A multiplicacao dos numeros e {num1 * num2}")
else:
    print(num1 + num2)
