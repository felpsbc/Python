# Faça um algoritmo que leia três números reais e mostre-os em ordem crescente.\

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

if (num2 < num1 > num3 and num2 > num3):
    print(num3 , num2 , num1)

elif (num2 < num1 > num3 and num2 < num3):
    print(num2 , num3 , num1)

elif (num1 < num2 > num3 and num1 > num3):
    print(num3 , num1 , num2)

elif (num1 < num2 > num3 and num1 < num3):
    print(num1 , num3 , num2)
    
elif (num1 < num3 > num2 and num2 > num1):
    print(num1 , num2 , num3)

else:
    print(num2, num1 , num3)
