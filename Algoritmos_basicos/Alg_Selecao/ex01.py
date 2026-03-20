# Faça um algoritmo que leia dois números inteiros e mostre o maior deles.

num1 = int(input("Enter a number: "))

num2 = int(input("Enter a number: "))

if (num1 == num2):
    print("The numbers are equal")
elif (num1 > num2):
    print(f"The first number {num1} is bigger than the second {num2}")
else:
    print(f"The second number {num2} is bigger than the first {num1}")