# Faça um algoritmo que leia um número inteiro positivo e mostre todos os seus divisores.

num = int(input("Digite um número: "))

if num == '':
    print ("Digite um número")
else:
    for i in range (1,num):
        if num % i == 0:
            print (i)