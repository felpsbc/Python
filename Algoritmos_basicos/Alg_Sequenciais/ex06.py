#Faça um algoritmo que leia o salário de um funcionário 
# e calcule o seu novo salário com um aumento de 15%.

Salario = float(input("Qual seu salario? "))

Salario += 15*Salario/100 

print(f"Seu Salario com aumento e {Salario}")