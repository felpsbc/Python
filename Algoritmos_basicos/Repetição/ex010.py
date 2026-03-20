# Faça um algoritmo que leia vários números inteiros e mostre o maior deles. 
# A leitura deve ser interrompida quando for lido o valor zero.
num_maior = 0

while True:
    num = int(input("Digite um Número (0 para sair): "))
    
    if num == 0:
        break  
    
    if num > num_maior:
        num_maior = num 

print(f"O maior número digitado foi: {num_maior}")
