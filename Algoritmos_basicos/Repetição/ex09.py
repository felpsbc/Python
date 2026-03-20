# Faça um algoritmo que leia vários números inteiros e mostre a média aritmética entre eles. 
# A leitura deve ser interrompida quando for lido o valor zero.

contador = 0
soma = 0
while True:
    num = num = float(input(f"Insira o valor de um número para média Aritmética e digite 0 para interromper a leitura e fazer o cálculo : "))

    if num == 0:
        break
    soma += num
    contador += 1

resultado = soma/contador
print(f"O resultado da Média Aritmética é {resultado}")