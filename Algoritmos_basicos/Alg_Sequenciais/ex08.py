# Faça um algoritmo que leia o número de dias trabalhados por um funcionário 
# e o valor da sua diária e calcule o seu salário.

dias_trabalhados = int(input("Digite o numero de dias trabalhados: "))

valor_diaria = float(input("Digite o valor da diaria: "))

salario = dias_trabalhados * valor_diaria

print(f"O valor do seu salario e {salario}")