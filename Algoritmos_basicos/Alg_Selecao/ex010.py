#Faça um algoritmo que leia a idade de uma pessoa e mostre a sua classificação, de acordo com a seguinte tabela:
#até 9 anos: mirim
#10 a 13 anos: infantil
#14 a 17 anos: juvenil
#maiores de 18 anos: adulto

idade = int(input("Digite sua idade: "))

if idade <= 9:
    print("Mirim")
elif 10 <= idade <= 13:
    print("infantil")
elif 14 <= idade <= 17:
    print("juvenil")
else:
    print("adulto")