# Faça um algoritmo que leia o salário de um funcionário e 
# calcule o seu novo salário com um aumento de 10% se o salário for menor que R$ 1000,00;
#  ou de 5% se o salário for maior ou igual a R$ 1000,00.

salario = float(input("digite seu salario: "))

if (salario >= 1000):
    salario += salario*0.05
    print(f"Seu novo salario com ajuste de 5% e {salario}")
else:
    salario += salario*0.1
    print(f"Seu novo salario com ajuste de 10% e {salario}")
